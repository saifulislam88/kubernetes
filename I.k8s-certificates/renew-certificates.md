
---

#### ✅ Renewing Certificates Safely

##### 1. Renew All Component Certificates

```bash
sudo kubeadm certs renew all
```

- Uses existing CA
- Generates new certs with new expiry (default: 1 year)

##### 2. Restart Relevant Components

```bash
sudo systemctl restart kubelet
```

For static pods (control plane):

```bash
docker ps | grep kube-apiserver
# or
crictl ps | grep kube
```

Restart those containers if needed.

---

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
