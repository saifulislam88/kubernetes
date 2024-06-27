### Highly Available Kubernetes Cluster using kubeadm
  #### - Deploy and Test on-premises Multi Master Kubernetes (k8s) Cluster with HaProxy on Ubuntu 22.04
https://github.com/justmeandopensource/kubernetes/tree/master/kubeadm-ha-keepalived-haproxy/external-keepalived-haproxy


- What is Kubernetes Cluster
- [Pre-requisites](https://github.com/saifulislam88/kubernetes/blob/main/B.k8s-cluster-setup-on-premises/A.Kubernetes-cluster-setup-on-Ubuntu-22.04.md#--pre-requisites)
- Configuration and Installation Steps
  - Step 1: Hardware/VM Rediness with OS
  - Step 2: Update hostfile `/etc/hosts`(all nodes)
  - Step 1: Update & install ntp client(all nodes)
  - Step 1: Setting up Static IPV4 on all nodes
  - Step 1: Disabling swap & Setting up hostnames
  - Step 1: Installing Kubernetes components on all nodes
    - A. Configure modules
    - B. Configure POD networking 
    - C. Install containerd (Master & Worker Node)
    - D. Modify containerd configuration (Master & Worker Node)
    - E. Install Kubernetes Management Tools (Master & Worker Node)
  - 
  - Configure Kuberctl on Only All Master Nodes
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

 - downlaod the hostfile update script 
```sh
curl -O https://github.com/saifulislam88/ubuntu-essentials-package-installing-manager/blob/main/hostconfig.sh
chmod +x hostconfig.sh
```

 - Run the `./hostconfig.sh` script or add manually `/etc/hosts`

```sh
172.16.16.51   lb1.saiful.com        kb8ln1
172.16.16.52   lb2.saiful.com        kb8ln2
172.16.16.101  kmaster1.saiful.com   kb8mn1
172.16.16.102  kmaster2.saiful.com   kb8mn2
172.16.16.120  kworker1.saiful.com   kb8wn1
172.16.16.121  kworker2.saiful.com   kb8wn2

```
### Update & install ntp client(all nodes)

```sh
sudo apt-get update -y
curl -O https://github.com/saifulislam88/ubuntu-essentials-package-installing-manager/blob/main/install-chrony-server-OR-client-acting.sh
chmod +x install-chrony-server-OR-client-acting.sh
./install-chrony-server-OR-client-acting.sh

```




