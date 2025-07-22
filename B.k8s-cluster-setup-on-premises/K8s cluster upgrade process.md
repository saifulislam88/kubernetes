
### 🚀 Kubernetes Cluster Upgrade: Downtime & Procedure

Upgrading a Kubernetes cluster is a critical operation that can be done with zero or minimal downtime — especially if you plan carefully.

---

### ✅ 1. Will There Be Downtime?

| Component       | Impact                                                             |
|----------------|---------------------------------------------------------------------|
| Control Plane   | 🔸 Minor control-plane downtime (API server restarts for seconds)   |
| Worker Nodes    | 🔸 No pod kill if drained properly                                  |
| App Pods        | ✅ Keep running if designed properly (stateless, readiness probes)  |

> 🎯 Application traffic remains unaffected if apps don’t rely directly on the API server.

---

### 🛠️ Upgrade Procedure with Minimal Downtime

📌 Assume you're using `kubeadm`. Here's a safe rolling strategy:

---

#### 🔹 Step 1: Back Up

- Backup etcd (if self-hosted)

```bash
ETCDCTL_API=3 etcdctl snapshot save snapshot.db
```

- Backup `/etc/kubernetes/` and `/var/lib/etcd/` (control plane only)

---

#### 🔹 Step 2: Upgrade Control Plane Node(s)

```bash
apt-mark unhold kubeadm && apt-get install -y kubeadm=1.X.Y-00
kubeadm upgrade plan
kubeadm upgrade apply v1.X.Y
```

Then upgrade kubelet and kubectl, and restart kubelet:

```bash
apt-get install -y kubelet=1.X.Y-00 kubectl=1.X.Y-00
systemctl restart kubelet
```

✅ Result: API server restarts briefly (~5s), pods keep running.

---

#### 🔹 Step 3: Upgrade Worker Nodes (One by One)

Drain the node:

```bash
kubectl drain <node-name> --ignore-daemonsets --delete-emptydir-data
```

Upgrade kubeadm/kubelet/kubectl:

```bash
apt-get install -y kubeadm=1.X.Y-00
kubeadm upgrade node
apt-get install -y kubelet=1.X.Y-00 kubectl=1.X.Y-00
systemctl restart kubelet
```

Uncordon the node:

```bash
kubectl uncordon <node-name>
```

✅ Pods will reschedule only if needed. No forced downtime.

---

#### 🔹 Step 4: Verify Cluster

```bash
kubectl get nodes
kubectl get pods --all-namespaces
```

---

## ✅ Tips to Avoid Downtime

- Use **PodDisruptionBudgets (PDBs)** to control app disruption  
- Use **readiness probes** to delay traffic during rollout  
- Don’t run critical apps on control plane nodes  
- Use **multiple replicas** of workloads for resilience
