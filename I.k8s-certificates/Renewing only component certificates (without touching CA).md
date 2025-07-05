
## Renewing only component certificates (without touching CA)

🚀
1️⃣ Back up /etc/kubernetes
sudo tar -czvf /root/kubernetes-backup-$(date +%F).tar.gz /etc/kubernetes

- **Check certificate expiration**
```sh
sudo kubeadm certs check-expiration
```

CERTIFICATE                EXPIRES                  RESIDUAL TIME   CERTIFICATE AUTHORITY   EXTERNALLY MANAGED\
admin.conf                 Mar 12, 2026 05:32 UTC   5d            ca                      no\
apiserver                  Mar 12, 2026 05:32 UTC   5d            ca                      no\
apiserver-etcd-client      Mar 12, 2026 05:32 UTC   5d            etcd-ca                 no\
apiserver-kubelet-client   Mar 12, 2026 05:32 UTC   5d            ca                      no\
controller-manager.conf    Mar 12, 2026 05:32 UTC   5d            ca                      no\
etcd-healthcheck-client    Mar 12, 2026 05:32 UTC   5d            etcd-ca                 no\
etcd-peer                  Mar 12, 2026 05:32 UTC   5d            etcd-ca                 no\
etcd-server                Mar 12, 2026 05:32 UTC   5d            etcd-ca                 no\
front-proxy-client         Mar 12, 2026 05:32 UTC   5d            front-proxy-ca          no\
scheduler.conf             Mar 12, 2026 05:32 UTC   5d            ca                      no

- **Renew only all component certificates**
  - Uses existing CA
  - Generates new certs with new expiry (default: 1 year)

```bash
sudo kubeadm certs renew all
```

- **Verify renewed certificates**

```sh 
sudo kubeadm certs check-expiration 
```

- **Restart Relevant Components**

For static pods (control plane) | Get container IDs

```bash
sudo crictl ps | grep kube-apiserver
sudo crictl ps | grep kube-controller-manager
sudo crictl ps | grep kube-scheduler
sudo crictl ps | grep etcd
```

```bash
sudo systemctl restart kubelet
```
---


Stop them one by one (example IDs shown—replace with your actual IDs)
sudo crictl stop <kube-apiserver-ID>
sudo crictl stop <kube-controller-manager-ID>
sudo crictl stop <kube-scheduler-ID>
sudo crictl stop <etcd-ID>


6️⃣ Verify containers restarted

sudo crictl ps | grep kube-apiserver
sudo crictl ps | grep kube-controller-manager
sudo crictl ps | grep kube-scheduler
sudo crictl ps | grep etcd


7️⃣ Test cluster connectivity

kubectl get nodes --kubeconfig /etc/kubernetes/admin.conf

✅ If you see nodes listed without TLS errors, certificates renewed successfully.

8️⃣ Update kubeconfig on admin workstation (if applicable)
Copy the renewed kubeconfig to your home directory
sudo cp /etc/kubernetes/admin.conf /home/mostafa/admin.conf
sudo chown $(id -u):$(id -g) /home/mostafa/admin.conf

Transfer to workstation
From your workstation:
scp root@prod-k8-master-node:/home/saiful/admin.conf ~/.kube/config









# ✅ Renewing Only Component Certificates (without touching CA)

This guide helps you renew Kubernetes component certificates without regenerating CA certificates.

---

## 🚀 1️⃣ Backup /etc/kubernetes

```bash
sudo tar -czvf /root/kubernetes-backup-$(date +%F).tar.gz /etc/kubernetes
```

---

## 2️⃣ Check Certificate Expiration

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

## 3️⃣ Renew All Component Certificates

- Uses existing CA.
- Generates new certs with a new expiry (default: 1 year).

```bash
sudo kubeadm certs renew all
```

---

## 4️⃣ Verify Renewed Certificates

```bash
sudo kubeadm certs check-expiration
```

---

## 5️⃣ Restart Relevant Components

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

## 6️⃣ Verify Containers Restarted

```bash
sudo crictl ps | grep kube-apiserver
sudo crictl ps | grep kube-controller-manager
sudo crictl ps | grep kube-scheduler
sudo crictl ps | grep etcd
```

---

## 7️⃣ Test Cluster Connectivity

```bash
kubectl get nodes --kubeconfig /etc/kubernetes/admin.conf
```

✅ If you see nodes listed without TLS errors, certificates were renewed successfully.

---

## 8️⃣ Update Kubeconfig on Admin Workstation (if applicable)

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

✅ **Done!**














#### 🛡 Renewing the CA Certificates (Advanced)

##### ⚠️ Warning:

Renewing the CA (`ca.crt`) will invalidate all existing component certs unless you use the **same key**.

##### 1. Backup first

```bash
cp -r /etc/kubernetes/pki /etc/kubernetes/pki-backup-$(date +%F)
```

##### 2. Renew CA

```bash
sudo kubeadm certs renew ca --use-api=false
```

Also for others:

```bash
sudo kubeadm certs renew etcd-ca --use-api=false
sudo kubeadm certs renew front-proxy-ca --use-api=false
```

##### 3. Optionally renew components to match new CA expiry

```bash
sudo kubeadm certs renew all
```

---

##### 🔁 If All Certs (Including CA) Expire

| Scenario                    | Impact                        |
| --------------------------- | ----------------------------- |
| Only component certs expire | API access issues, fixable    |
| CA certs expire             | Cluster breaks, kubelet fails |
| Both expire                 | Full outage, manual recovery  |

##### Recovery Plan

- Restore backup of `/etc/kubernetes/pki`
- Or: Recreate CA using OpenSSL + sign new certs manually
- Restart `kubelet` and relevant static pods

---

##### 🧠 Best Practices

- ✅ Rotate certs **before** expiry
- ✅ Keep regular backup of `/etc/kubernetes/pki`
- ✅ Monitor using cron or Prometheus alerts
- ⚠️ Avoid extending component certs to 10 years unless you have a specific reason

---
