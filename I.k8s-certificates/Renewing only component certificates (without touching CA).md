## ✅ Renewing Only Component Certificates (without touching CA)

This guide helps you renew Kubernetes component certificates without regenerating CA certificates.

---

### 1️⃣ Backup /etc/kubernetes

```bash
sudo tar -czvf /root/kubernetes-backup-$(date +%F).tar.gz /etc/kubernetes
```

---

### 2️⃣ Check Certificate Expiration

```bash
sudo kubeadm certs check-expiration
```

**Example output:**

```
CERTIFICATE                EXPIRES                  RESIDUAL TIME   CERTIFICATE AUTHORITY   EXTERNALLY MANAGED
admin.conf                 Mar 12, 2026 05:32 UTC   5d              ca                      no
apiserver                  Mar 12, 2026 05:32 UTC   5d              ca                      no
apiserver-etcd-client      Mar 12, 2026 05:32 UTC   5d              etcd-ca                 no
apiserver-kubelet-client   Mar 12, 2026 05:32 UTC   5d              ca                      no
controller-manager.conf    Mar 12, 2026 05:32 UTC   5d              ca                      no
etcd-healthcheck-client    Mar 12, 2026 05:32 UTC   5d              etcd-ca                 no
etcd-peer                  Mar 12, 2026 05:32 UTC   5d              etcd-ca                 no
etcd-server                Mar 12, 2026 05:32 UTC   5d              etcd-ca                 no
front-proxy-client         Mar 12, 2026 05:32 UTC   5d              front-proxy-ca          no
scheduler.conf             Mar 12, 2026 05:32 UTC   5d              ca                      no
```

---

### 3️⃣ Renew All Component Certificates

- Uses existing CA.
- Generates new certs with a new expiry (default: 1 year).

```bash
sudo kubeadm certs renew all
```

---

### 4️⃣ Verify Renewed Certificates

```bash
sudo kubeadm certs check-expiration
```

---

### 5️⃣ Restart Relevant Components

**Get container IDs:**

```bash
sudo crictl ps | grep kube-apiserver
sudo crictl ps | grep kube-controller-manager
sudo crictl ps | grep kube-scheduler
sudo crictl ps | grep etcd
```

**Restart kubelet:**

```bash
sudo systemctl restart kubelet
```

---

**Alternatively, stop containers one by one:**

```bash
sudo crictl stop <kube-apiserver-ID>
sudo crictl stop <kube-controller-manager-ID>
sudo crictl stop <kube-scheduler-ID>
sudo crictl stop <etcd-ID>
```

---

### 6️⃣ Verify Containers Restarted

```bash
sudo crictl ps | grep kube-apiserver
sudo crictl ps | grep kube-controller-manager
sudo crictl ps | grep kube-scheduler
sudo crictl ps | grep etcd
```

---

### 7️⃣ Test Cluster Connectivity

```bash
kubectl get nodes --kubeconfig /etc/kubernetes/admin.conf
```

✅ If you see nodes listed without TLS errors, certificates were renewed successfully.

---

### 8️⃣ Update Kubeconfig on Admin Workstation (if applicable)

**Copy renewed kubeconfig:**

```bash
sudo cp /etc/kubernetes/admin.conf /home/saiful/admin.conf
sudo chown $(id -u):$(id -g) /home/saiful/admin.conf
```

**Transfer to workstation:**

From your workstation:

```bash
scp root@prod-k8-master-node:/home/saiful/admin.conf ~/.kube/config
```

### 🔁 If All Certs (Including CA) Expire

| Scenario                    | Impact                        |
| --------------------------- | ----------------------------- |
| Only component certs expire | API access issues, fixable    |
| CA certs expire             | Cluster breaks, kubelet fails |
| Both expire                 | Full outage, manual recovery  |

### Recovery Plan

- Restore backup of `/etc/kubernetes/pki`
- Restart `kubelet` and relevant static pods

---

### 🧠 Best Practices

- ✅ Rotate certs **before** expiry
- ✅ Keep regular backup of `/etc/kubernetes/pki`
- ✅ Monitor using cron or Prometheus alerts

