### Highly Available Kubernetes Cluster using [Kubeadm](https://github.com/saifulislam88/kubernetes/blob/main/B.k8s-cluster-setup-on-premises/A.Kubernetes-cluster-setup-on-Ubuntu-22.04.md)
**Deploy and Test on-premises Multi Master Kubernetes (k8s) Cluster with HaProxy on Ubuntu 22.04**


<img width="636" alt="stacketcd" src="https://github.com/saifulislam88/kubernetes/assets/68442870/89d9f8c5-0ef6-4680-90ce-cf72551e44e2">


- [What is Kubernetes Cluster](https://github.com/saifulislam88/kubernetes/blob/main/B.k8s-cluster-setup-on-premises/A.Kubernetes-cluster-setup-on-Ubuntu-22.04.md#what-is-kubernetes-cluster)
- [Pre-requisites](https://github.com/saifulislam88/kubernetes/blob/main/B.k8s-cluster-setup-on-premises/A.Kubernetes-cluster-setup-on-Ubuntu-22.04.md#--pre-requisites--environment)
- [Configuration and Installation Steps](https://github.com/saifulislam88/kubernetes/blob/main/B.k8s-cluster-setup-on-premises/A.Kubernetes-cluster-setup-on-Ubuntu-22.04.md#configuration-and-installation-steps)
  - Step 1: [Hardware/VM Rediness with OS](https://github.com/saifulislam88/kubernetes/blob/main/B.k8s-cluster-setup-on-premises/A.Kubernetes-cluster-setup-on-Ubuntu-22.04.md#step-1-hardwarevm-rediness-with-os)
  - Step 2: [Update hostfile `/etc/hosts`and hostname (all nodes)](https://github.com/saifulislam88/kubernetes/blob/main/B.k8s-cluster-setup-on-premises/A.Kubernetes-cluster-setup-on-Ubuntu-22.04.md#step-2-update-hostfile-etchostsall-nodes)
  - Step 3: [Update & install ntp client(all nodes)](https://github.com/saifulislam88/kubernetes/blob/main/B.k8s-cluster-setup-on-premises/A.Kubernetes-cluster-setup-on-Ubuntu-22.04.md#step-3-update--install-ntp-clientall-nodes)
  - Step 4: [Disable UFW Firewall (all nodes)](https://github.com/saifulislam88/kubernetes/blob/main/B.k8s-cluster-setup-on-premises/A.Kubernetes-cluster-setup-on-Ubuntu-22.04.md#step-4-disable-ufw-firewall-all-nodes)
  - Step 5: [Set up loadbalancer & Keepalived Services (loadbalancer1 & loadbalancer2)](https://github.com/saifulislam88/kubernetes/blob/main/B.k8s-cluster-setup-on-premises/A.Kubernetes-cluster-setup-on-Ubuntu-22.04.md#step-5-set-up-loadbalancer-loadbalancer1--loadbalancer2)
  - Step 6: [Installing Kubernetes Components on (All Master & Worker nodes)](https://github.com/saifulislam88/kubernetes/blob/main/B.k8s-cluster-setup-on-premises/A.Kubernetes-cluster-setup-on-Ubuntu-22.04.md#step-6-installing-kubernetes-components-on-all-master--worker-nodes)
    - A. [Disabling Swap and (All Master & Worker nodes)](https://github.com/saifulislam88/kubernetes/blob/main/B.k8s-cluster-setup-on-premises/A.Kubernetes-cluster-setup-on-Ubuntu-22.04.md#--a-disabling-swap-and-all-master--worker-nodes)
    - B. [Enable and load kernel modules (All Master & Worker Node)](https://github.com/saifulislam88/kubernetes/blob/main/B.k8s-cluster-setup-on-premises/A.Kubernetes-cluster-setup-on-Ubuntu-22.04.md#--a-disabling-swap-and-all-master--worker-nodes)
    - C. [Configure Kernel setting (All Master & Worker Node)](https://github.com/saifulislam88/kubernetes/blob/main/B.k8s-cluster-setup-on-premises/A.Kubernetes-cluster-setup-on-Ubuntu-22.04.md#--c-configure-kernel-setting-all-master--worker-node)
    - D. [Install containerd (All Master & Worker Node)](https://github.com/saifulislam88/kubernetes/blob/main/B.k8s-cluster-setup-on-premises/A.Kubernetes-cluster-setup-on-Ubuntu-22.04.md#--d-install-containerd-all-master--worker-node)
    - E. [Install Kubernetes Management Tools (All Master & Worker Node)](https://github.com/saifulislam88/kubernetes/blob/main/B.k8s-cluster-setup-on-premises/A.Kubernetes-cluster-setup-on-Ubuntu-22.04.md#--e-install-kubernetes-management-tools-all-master--worker-node)
    - F. [Reboot all (All Master & Worker Nodes)](https://github.com/saifulislam88/kubernetes/blob/main/B.k8s-cluster-setup-on-premises/A.Kubernetes-cluster-setup-on-Ubuntu-22.04.md#--f-reboot-all-master--worker-nodes)
  - Step 7: [Initialise the machine as a master node](https://github.com/saifulislam88/kubernetes/blob/main/B.k8s-cluster-setup-on-premises/A.Kubernetes-cluster-setup-on-Ubuntu-22.04.md#step-7-initialise-the-machine-as-a-master-node)
  - Step 8: [Configure Kuberctl (Only All Master Nodes)](https://github.com/saifulislam88/kubernetes/blob/main/B.k8s-cluster-setup-on-premises/A.Kubernetes-cluster-setup-on-Ubuntu-22.04.md#step-8-configure-kuberctl-only-all-master-nodes)
  - Step 9: [Configure Calico POD overlay networking(Only Primary Master Node)](https://github.com/saifulislam88/kubernetes/blob/main/B.k8s-cluster-setup-on-premises/A.Kubernetes-cluster-setup-on-Ubuntu-22.04.md#step-9-configure-calico-pod-overlay-networkingonly-primary-master-node)
  - Step 10: [Verifying the cluster (All command will execute from Master)](https://github.com/saifulislam88/kubernetes/blob/main/B.k8s-cluster-setup-on-premises/A.Kubernetes-cluster-setup-on-Ubuntu-22.04.md#step-10-verifying-the-cluster-all-command-will-execute-from-master)
     
### What is Kubernetes Cluster

**A Kubernetes (K8s) cluster is a group of master nodes, or worker machines, that run containerized applications**. So a cluster contains a control plane and one or more compute machines, or nodes. The control plane is responsible for maintaining the desired state of the cluster, such as which applications are running and which container images they use. Nodes actually run the applications and workloads.


Kubernetes it’s a scalable orchestration technology, it can start from single node installation, up to the huge HA clusters, based on hundreds nodes inside. Most of the popular cloud providers, represent the different kind of Kubernetes implementations, so you can start using it very fast and easy in there. But there is a lot of situations and lot of companies that can’t use clouds for their needs, but they wanna get all benefits from the modern technologies of using containers also. And there bare metal Kubernetes installation comes on the scene. 

**In this example, we’ll create a highly available (HA) Kubernetes cluster with a multi-master topology.**
We know that there are different methods for deploying Kubernetes clusters. From the methods listed below, we have deployed a Kubernetes cluster using the [Kubeadm](https://github.com/saifulislam88/kubernetes/blob/main/B.k8s-cluster-setup-on-premises/A.Kubernetes-cluster-setup-on-Ubuntu-22.04.md) method.

**The methods are:**

[Kubeadm](https://github.com/saifulislam88/kubernetes/blob/main/B.k8s-cluster-setup-on-premises/A.Kubernetes-cluster-setup-on-Ubuntu-22.04.md)\
[Minikube](https://minikube.sigs.k8s.io/docs/start/?arch=%2Flinux%2Fx86-64%2Fstable%2Fbinary+download)\
[Kind](https://kind.sigs.k8s.io/docs/user/quick-start/#installation)\
**K3s**\
**Managed Kubernetes Services - GKE | EKS | AKS**\
**Kops**\
**MicroK8s**\
**RKE (Rancher Kubernetes Engine)**\
**OpenShift**


### Pre-requisites | Environment

- Standard

|      Role       |         FQDN              |       IP       |     OS       |  RAM   | vCPU | Storage |
|-----------------|---------------------------|----------------|--------------|--------|------|----------
| Load Balancer   | lb1.saiful.com            | 172.16.16.51   | Ubuntu 22.04 |  2G    |  2   |  10G    |
| Load Balancer   | lb2.saiful.com            | 172.16.16.52   | Ubuntu 22.04 |  2G    |  2   |  10G    |
| Master          | kmaster1.saiful.com       | 172.16.16.101  | Ubuntu 22.04 |  4G    |  3   |  20G    |
| Master          | kmaster2.saiful.com       | 172.16.16.102  | Ubuntu 22.04 |  4G    |  3   |  20G    |
| Worker          | kworker1.saiful.com       | 172.16.16.120  | Ubuntu 22.04 |  4G    |  3   |  20G    |
| Worker          | kworker2.saiful.com       | 172.16.16.121  | Ubuntu 22.04 |  4G    |  3   |  20G    |

- Minimal
  - At least 2 nodes(master,worker)
  - 2 vCPUs.
  - At least 4GB of RAM.
  - At least 20GB of disk space.
  - A reliable internet connection.


### Configuration and Installation Steps


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

### Step 3: Update & install ntp client(all nodes)

```sh
sudo apt-get update -y
wget https://raw.githubusercontent.com/saifulislam88/ubuntu-essentials-package-installing-manager/main/install-chrony-server-OR-client-acting.sh
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

- Configure `/etc/haproxy/haproxy.cfg` Haproxy on both LB(LB1 & LB2)

```sh
global
  maxconn 50000
  log /dev/log local0
  user haproxy
  group haproxy

defaults
  log global
  timeout connect 10s
  timeout client 30s
  timeout server 30s

frontend kubernetes-frontend
  bind *:6443
  mode tcp
  option tcplog
  default_backend kubernetes-backend

backend kubernetes-backend
  option httpchk GET /healthz
  http-check expect status 200
  mode tcp
  option check-ssl
  balance roundrobin
  server kmaster1 172.16.4.101:6443 check fall 3 rise 2
  server kmaster2 172.16.4.102:6443 check fall 3 rise 2

```
```sh
haproxy -c -f /etc/haproxy/haproxy.cfg
systemctl restart haproxy
systemctl enable haproxy
```

### Step 6: Installing Kubernetes Components on (All Master & Worker nodes)

#### - A. Disabling Swap and (All Master & Worker nodes)

```sh
swapoff -a; sed -i '/swap/d' /etc/fstab
```
#### - B. Enable and load kernel modules (All Master & Worker Node)

```sh
cat >> /etc/modules-load.d/containerd.conf <<EOF
overlay
br_netfilter
EOF

modprobe overlay
modprobe br_netfilter
```

#### - C. Configure Kernel setting (All Master & Worker Node)

Set up system `Kernel settings & parameters` these are related to `Networking(CNI)` and the `Container Runtime Interface (CRI)`.
```sh
cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-iptables  = 1
net.bridge.bridge-nf-call-ip6tables = 1
net.ipv4.ip_forward                 = 1
EOF
```
`sysctl --system`

#### - D. Install containerd (All Master & Worker Node)

Install the container runtime (containerd) for managing containers.

```sh
sudo apt-get update
apt install -y apt-transport-https
sudo apt-get install -y containerd
```
```sh
#Modify containerd configuration

sudo mkdir -p /etc/containerd
sudo containerd config default | sudo tee /etc/containerd/config.toml
sudo sed -i 's/SystemdCgroup \= false/SystemdCgroup \= true/g' /etc/containerd/config.toml

```
`cat /etc/containerd/config.toml`

```sh
sudo systemctl restart containerd.service
sudo systemctl enable containerd.service
sudo systemctl status containerd
```

#### - E. [Install Kubernetes Management Tools](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/#install-using-native-package-management) (All Master & Worker Node)

```sh
sudo apt-get update
sudo apt-get install -y ca-certificates curl
sudo apt-get install -y apt-transport-https ca-certificates curl
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.29/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.29/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
```

```sh
sudo apt-get update
sudo apt-get install -y kubelet kubeadm kubectl
sudo apt-mark hold kubelet kubeadm kubectl
```
**`systemctl status kubelet`**

⚠️(`:warning:`) When you check the **`kubelet`** service status using **`systemctl status kubelet`** on both the master and worker nodes, you may see that it is in an **"activating"** state like below screenshot. This is not an issue. When the **kubeadm** service is initiated on the **master node**, it will automatically start the **kubelet** service. After all **worker nodes** have joined the **master**, the **kubelet** service on those nodes will also become **active automatically.**

![image](https://github.com/user-attachments/assets/d05c14eb-6d0d-4a9c-833b-9674a240bccb)


#### - F. Reboot (All Master & Worker Nodes)

```sh
init 6
```


### Step 7: Initialise the machine as a master node:

Initialization the Kubernetes Cluster on any one of the Kubernetes master node where `172.16.4.100` is master servers VIP and `192.168.0.0/16` is Pod CIDR.If want to change this cidr,you have to udpate [CNI network configuration operator file]()

- **Execute the following command where the culster will be `multi-master` with `Loadbalancers & VIP`**

```sh
sudo kubeadm init --control-plane-endpoint="172.16.4.100:6443" --apiserver-advertise-address=172.16.4.101 --pod-network-cidr=172.16.0.0/16 --cri-socket /run/containerd/containerd.sock --ignore-preflight-errors Swap
```

- ⚠️(`:warning:`) where the culster will be `single master` it will be applicable for that time ONLY.

```sh
# `172.16.4.101` primary master ip
sudo kubeadm init --apiserver-advertise-address=172.16.4.101 --pod-network-cidr=192.168.0.0/16 --cri-socket /run/containerd/containerd.sock --ignore-preflight-errors Swap
```
**`systemctl status kubelet`** 

- **Save the join command printed in the output after the above command and copy the commands to join other master nodes and worker nodes.**

  - For **For master nodes**

```sh
kubeadm join 172.16.4.100:6443 --token mamz03.e9q8n66cuoui8ua6 \
        --discovery-token-ca-cert-hash sha256:3ffe97a8644080a85efed10ac77ba4bcd2bcbf25a402bec8995ec5d458ff2374 \
        --control-plane
```

  - For **worker nodes**

```sh
kubeadm join 172.16.4.100:6443 --token mamz03.e9q8n66cuoui8ua6 \
        --discovery-token-ca-cert-hash sha256:3ffe97a8644080a85efed10ac77ba4bcd2bcbf25a402bec8995ec5d458ff2374
```
**`systemctl status kubelet`** 


- **You can print join token and construct manually**

`kubeadm token list`\
`kubeadm token create --print-join-command`\
`kubeadm token list`\
`openssl x509 -pubkey -in /etc/kubernetes/pki/ca.crt | openssl rsa -pubin -outform der 2>/dev/null | openssl dgst -sha256 -hex | sed 's/^.* //'`

  - **Manual construct for joining for Worker**
kubeadm join <control-plane-endpoint>:6443 --token <token> \
    --discovery-token-ca-cert-hash sha256:<ca-cert-hash>


  - **Manual construct for joining for Master**
kubeadm join <control-plane-endpoint>:6443 --token <token> \
        --discovery-token-ca-cert-hash sha256:<ca-cert-hash> \
        --control-plan



### Step 8: Configure Kuberctl (Only All Master Nodes)

- **Master Node (Primary)**
```sh
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

**⚠️ Alternatively, if you are the root user, you can also run the following command instead of the above:**

```sh
export KUBECONFIG=/etc/kubernetes/admin.conf
```
`kubectl get nodes`

**Expected Output:**
![image](https://github.com/saifulislam88/kubernetes/assets/68442870/d94b5f81-4eb8-42df-a60c-c52bca215270)



- **Execute on the other Master Nodes (ssh root login first)**

mkdir -p $HOME/.kube
scp root@kmaster1.saiful.com:/etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

### Step 9: Configure Calico POD overlay networking(Only Primary Master Node)

Calico is 𝗖𝗡𝗜 - 𝗖𝗼𝗻𝘁𝗮𝗶𝗻𝗲𝗿 𝗡𝗲𝘁𝘄𝗼𝗿𝗸 𝗜𝗻𝘁𝗲𝗿𝗳𝗮𝗰𝗲 plugin that is responsible for inserting a network interface into the container network namespace
**In this step**, we'll install Calico, a powerful networking solution, to facilitate on-premises deployments in your Kubernetes cluster.

- **Install the operator on your cluster networking.**

`kubectl create -f https://raw.githubusercontent.com/projectcalico/calico/v3.24.1/manifests/tigera-operator.yaml`

- **Download the custom resources necessary to configure Calico**

curl https://raw.githubusercontent.com/projectcalico/calico/v3.24.1/manifests/custom-resources.yaml -O

- **Customize the downloaded custom-resources.yaml manifest for adding your planning cidr networking block where my network is `cidr: 192.168.0.0/16` and install**

`vim custom-resources.yaml`

![image](https://github.com/saifulislam88/kubernetes/assets/68442870/c8af802d-b909-4935-a3c1-a0516c8bbf26)

`kubectl create -f custom-resources.yaml`

### Step 10: Verifying the cluster (All command will execute from Master)

`kubectl get nodes`

**Expected Output:**

![image](https://github.com/saifulislam88/kubernetes/assets/68442870/19e0f3d5-3c1d-4f94-94f7-aa9d05f8397a)

- **Get Cluster Info**

`kubectl cluster-info`
`kubectl get cs`

- **Check that all the pods deployed correctly**

`kubectl get pods -n kube-system`

- **Get APi resources list and sort name**

`kubectl api-resources`

- **Dump current cluster state to stdout**

`kubectl cluster-info dump`

- **Verify the etcd Cluster Members**

`apt  install etcd-client -y`

```sh
ETCDCTL_API=3 etcdctl member list --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/peer.crt \
  --key=/etc/kubernetes/pki/etcd/peer.key
```
