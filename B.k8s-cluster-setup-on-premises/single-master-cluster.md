## Kubernetes Cluster Setup on Ubuntu 24.04 (1 Master + 2 Workers)

This guide sets up a **Kubernetes cluster (latest stable v1.33)** with **1 control-plane (master)** and **2 worker nodes**.

---

## 🔹 1. Prerequisites

- 3 Ubuntu 24.04 servers:
  - **Master** (control plane)
  - **2 Workers**
- Minimum specs:
  - 2 CPUs
  - 2 GB RAM (4 GB recommended for master)
  - 20 GB Disk
- Root/sudo access
- Internet connectivity

---

## 🔹 2. Prepare All Nodes (Master + Workers)

Run on **all nodes**:

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Disable swap
sudo swapoff -a
sudo sed -i '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab

# Load kernel modules
cat <<EOF | sudo tee /etc/modules-load.d/k8s.conf
overlay
br_netfilter
EOF

sudo modprobe overlay
sudo modprobe br_netfilter

# Apply sysctl params
cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-iptables  = 1
net.bridge.bridge-nf-call-ip6tables = 1
net.ipv4.ip_forward                 = 1
EOF

sudo sysctl --system
```

---

## 🔹 3. Install Container Runtime (containerd)

```bash
# Install containerd
sudo apt install -y containerd

# Generate default config
sudo mkdir -p /etc/containerd
containerd config default | sudo tee /etc/containerd/config.toml

# Set systemd as cgroup driver
sudo sed -i 's/SystemdCgroup = false/SystemdCgroup = true/' /etc/containerd/config.toml

# Restart containerd
sudo systemctl restart containerd
sudo systemctl enable containerd
```

---

## 🔹 4. Install Kubernetes Components

Run on **all nodes**:

```bash
# Install dependencies
sudo apt-get install -y apt-transport-https ca-certificates curl gpg

# Add Kubernetes GPG key
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.33/deb/Release.key | \
  sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg

# Add Kubernetes repo
echo "deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.33/deb/ /" | \
  sudo tee /etc/apt/sources.list.d/kubernetes.list

# Install kubelet, kubeadm, kubectl
sudo apt update
sudo apt install -y kubelet kubeadm kubectl
sudo apt-mark hold kubelet kubeadm kubectl
```

---

## 🔹 5. Initialize Control Plane (Master Only)

```bash
sudo kubeadm init --pod-network-cidr=192.168.0.0/16
```

After successful init, set up kubectl:

```bash
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

⚠️ Copy the **`kubeadm join ...`** command displayed at the end.  
This will be used on the worker nodes.

---

## 🔹 6. Install Pod Network (CNI)

Example: **Calico**

```bash
kubectl apply -f https://raw.githubusercontent.com/projectcalico/calico/v3.27.3/manifests/calico.yaml
```

---

## 🔹 7. Join Worker Nodes

On **each worker**, run the `kubeadm join ...` command from step 5.

If lost, regenerate on master:

```bash
kubeadm token create --print-join-command
```

---

## 🔹 8. Verify Cluster

On **master**:

```bash
kubectl get nodes
```

✅ You should see `1 master` and `2 workers` in **Ready** state.

---

## ✅ Summary

- **All nodes**: system prep, containerd, kube tools  
- **Master**: `kubeadm init`, kubectl config, install Calico  
- **Workers**: `kubeadm join`  
- **Check**: `kubectl get nodes`
