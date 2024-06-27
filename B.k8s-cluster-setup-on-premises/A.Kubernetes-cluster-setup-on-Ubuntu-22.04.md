### Highly Available Kubernetes Cluster using kubeadm
  #### - Deploy and Test on-premises Multi Master Kubernetes (k8s) Cluster with HaProxy on Ubuntu 22.04

<img width="636" alt="stacketcd" src="https://github.com/saifulislam88/kubernetes/assets/68442870/89d9f8c5-0ef6-4680-90ce-cf72551e44e2">


https://github.com/justmeandopensource/kubernetes/tree/master/kubeadm-ha-keepalived-haproxy/external-keepalived-haproxy


- What is Kubernetes Cluster
- [Pre-requisites](https://github.com/saifulislam88/kubernetes/blob/main/B.k8s-cluster-setup-on-premises/A.Kubernetes-cluster-setup-on-Ubuntu-22.04.md#--pre-requisites)
- Configuration and Installation Steps
  - Step 1: Hardware/VM Rediness with OS
  - Step 2: Update hostfile `/etc/hosts`and hostname (all nodes)
  - Step 3: Update & install ntp client(all nodes)
  - Step 4: Disable UFW Firewall (all nodes)
  - Step 5: Set up loadbalancer & Keepalived Services (loadbalancer1 & loadbalancer2)
  - Step 5: Disabling Swap and (All Master & Worker nodes)
  - Step 1: Installing Kubernetes Components on (All Master & Worker nodes)
    - A. Configure modules (Master & Worker Node)
    - B. Configure Networking (Master & Worker Node)
    - C. Install containerd (Master & Worker Node)
    - D. Modify containerd configuration (Master & Worker Node)
    - E. Install Kubernetes Management Tools (Master & Worker Node)
    - F. Reboot all (Master & Worker Nodes)
  - Step 10: Configure Kuberctl (Only All Master Nodes)
  - Step 11: Configure Calico POD overlay networking(Only Primary Master Node)
  - Step 12: Print Join token for other Master nodes joining to the Cluster (Primary Master Node).
     - Join Other master node to the Cluster (Slave Master nodes)
  - Step 12: Print Join token for worker nodes joining to the Cluster (Primary Master Node).
     - Join worker Node to the Cluster (All Worker Nodes)
     - Get Cluster Info (Master Node)
  - 
### - What is Kubernetes Cluster

### - Pre-requisites | Environment

##### - Standard

|      Role       |         FQDN              |       IP       |     OS       |  RAM   | vCPU | Storage |
|-----------------|---------------------------|----------------|--------------|--------|------|----------
| Load Balancer   | lb1.saiful.com            | 172.16.16.51   | Ubuntu 22.04 |  2G    |  2   |  10G    |
| Load Balancer   | lb2.saiful.com            | 172.16.16.52   | Ubuntu 22.04 |  2G    |  2   |  10G    |
| Master          | kmaster1.saiful.com       | 172.16.16.101  | Ubuntu 22.04 |  4G    |  3   |  20G    |
| Master          | kmaster2.saiful.com       | 172.16.16.102  | Ubuntu 22.04 |  4G    |  3   |  20G    |
| Worker          | kworker1.saiful.com       | 172.16.16.120  | Ubuntu 22.04 |  4G    |  3   |  20G    |
| Worker          | kworker2.saiful.com       | 172.16.16.121  | Ubuntu 22.04 |  4G    |  3   |  20G    |

##### - Minimal
  - At least 2 nodes(master,worker)
  - 2 vCPUs.
  - At least 4GB of RAM.
  - At least 20GB of disk space.
  - A reliable internet connection.


### Step 1: Hardware/VM Rediness with OS

- VMs Creation and IP/network configuration each node from node network `172.16.16.0/24`
- Password for the root account on all these virtual machines: `t0mc@t`
- Perform all commands as root user unless otherwise specified.
- Virtual IP managed by Keepalived on the load balancer nodes.
  - Virtual IP: `172.16.16.100`
- Pod Network CIDR: `192.168.0.0/16`
  

### Step 2: Update hostfile `/etc/hosts`(all nodes)

 - Downlaod the hostfile and hostname updating script 
```sh
curl -O https://github.com/saifulislam88/ubuntu-essentials-package-installing-manager/blob/main/hostconfig.sh
chmod +x hostconfig.sh
```

 - Run the `./hostconfig.sh` script or add manually `/etc/hosts`

```sh
172.16.16.51   klb1.saiful.com       kb8ln1
172.16.16.52   klb2.saiful.com       kb8ln2
172.16.16.101  kmaster1.saiful.com   kb8mn1
172.16.16.102  kmaster2.saiful.com   kb8mn2
172.16.16.120  kworker1.saiful.com   kb8wn1
172.16.16.121  kworker2.saiful.com   kb8wn2

```
 - 

### Step 3: Update & install ntp client(all nodes)

```sh
sudo apt-get update -y
curl -O https://github.com/saifulislam88/ubuntu-essentials-package-installing-manager/blob/main/install-chrony-server-OR-client-acting.sh
chmod +x install-chrony-server-OR-client-acting.sh
./install-chrony-server-OR-client-acting.sh

```
### Step 4: Disable UFW Firewall (all nodes)
```sh
systemctl disable --now ufw
```
### Step 5: Set up loadbalancer (loadbalancer1 & loadbalancer2)

- Install Keepalived & Haproxy(lb1 & lb2)
```sh
apt update && apt install -y keepalived haproxy
```

- create the health check script `/etc/keepalived/check_apiserver.sh`(On both LB nodes )

```sh

cat >> /etc/keepalived/check_apiserver.sh <<EOF
#!/bin/sh

errorExit() {
  echo "*** $@" 1>&2
  exit 1
}

curl --silent --max-time 2 --insecure https://localhost:6443/ -o /dev/null || errorExit "Error GET https://localhost:6443/"
if ip addr | grep -q 172.16.16.100; then
  curl --silent --max-time 2 --insecure https://172.16.16.100:6443/ -o /dev/null || errorExit "Error GET https://172.16.16.100:6443/"
fi
EOF

chmod +x /etc/keepalived/check_apiserver.sh

```

- Create keepalived config `/etc/keepalived/keepalived.conf` on (LB1)

```sh
cat >> /etc/keepalived/keepalived.conf <<EOF
vrrp_script check_apiserver {
  script "/etc/keepalived/check_apiserver.sh"
  interval 3
  timeout 10
  fall 5
  rise 2
  weight -2
}

vrrp_instance VI_1 {
    state MASTER
    interface eth1
    virtual_router_id 1
    priority 150
    advert_int 5
    authentication {
        auth_type PASS
        auth_pass NoPass@Mr.MSI
    }
    virtual_ipaddress {
        172.16.16.100
    }
    track_script {
        check_apiserver
    }
}
EOF

#Keepalived Daemon Management
systemctl enable --now keepalived
systemctl restart keepalived
systemctl status keepalived

```

- Create keepalived config `/etc/keepalived/keepalived.conf` on (LB2)

```sh
cat >> /etc/keepalived/keepalived.conf <<EOF
vrrp_script check_apiserver {
  script "/etc/keepalived/check_apiserver.sh"
  interval 3
  timeout 10
  fall 5
  rise 2
  weight -2
}

vrrp_instance VI_1 {
    state <span style="color:yellow;">BACKUP</span>
    interface eth1
    virtual_router_id 1
    priority 100
    advert_int 5
    authentication {
        auth_type PASS
        auth_pass NoPass@Mr.MSI
    }
    virtual_ipaddress {
        172.16.16.100
    }
    track_script {
        check_apiserver
    }
}
EOF

#Keepalived Daemon Management
systemctl enable --now keepalived
systemctl restart keepalived
systemctl status keepalived
```







### Step 11: Configure Calico POD overlay networking(Only Primary Master Node)

Calico is 𝗖𝗡𝗜 - 𝗖𝗼𝗻𝘁𝗮𝗶𝗻𝗲𝗿 𝗡𝗲𝘁𝘄𝗼𝗿𝗸 𝗜𝗻𝘁𝗲𝗿𝗳𝗮𝗰𝗲 plugin that is responsible for inserting a network interface into the container network namespace
