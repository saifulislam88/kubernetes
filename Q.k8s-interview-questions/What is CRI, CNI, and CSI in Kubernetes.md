
## What is CRI, CNI, and CSI in Kubernetes?

In Kubernetes, **CRI**, **CNI**, and **CSI** are interfaces that enable pluggable architecture for container runtime, networking, and storage:

---

### 1. CRI – Container Runtime Interface

- **Purpose**: Allows Kubernetes to use different container runtimes (like containerd, CRI-O, Docker via shim).  
- **Role**: Connects the `kubelet` to the underlying container runtime.  
- **Examples**:
  - containerd  
  - CRI-O  
  - Docker (deprecated in K8s 1.20+ via dockershim)

---

### 2. CNI – Container Network Interface

- **Purpose**: Manages network connectivity for pods.  
- **Role**: Provides IP addressing and routing so that pods can communicate with each other and with external services.  
- **Examples**:
  - Calico  
  - Flannel  
  - Cilium  
  - Weave Net

---

### 3. CSI – Container Storage Interface

- **Purpose**: Allows Kubernetes to use various storage systems (block or file storage).  
- **Role**: Standardizes how storage volumes are provisioned, attached, and mounted.  
- **Examples**:
  - Rook (Ceph)  
  - OpenEBS  
  - Amazon EBS CSI Driver  
  - NFS CSI Driver

---

### Summary Table

| Interface | Purpose                      | Connected Component       | Examples                     |
|-----------|------------------------------|----------------------------|------------------------------|
| CRI       | Container runtime integration| kubelet ↔ containerd       | containerd, CRI-O            |
| CNI       | Pod networking               | kubelet ↔ network plugin   | Calico, Flannel              |
| CSI       | Persistent storage           | kubelet ↔ storage plugin   | Rook, OpenEBS, AWS EBS       |
