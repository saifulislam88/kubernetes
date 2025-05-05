### 🔐 Kubernetes Certificate Expiry & Renewal Strategy

This knowledgebase covers how Kubernetes handles TLS certificates, the implications of expiry, and the complete renewal and recovery process for CA and component certificates.

---

#### 📌 Certificate Types in Kubernetes

| Certificate                    | Purpose                                  | Signed By   | Default Validity |
| ------------------------------ | ---------------------------------------- | ----------- | ---------------- |
| `ca.crt`                       | Cluster Certificate Authority            | Self-signed | 10 years         |
| `apiserver.crt`                | TLS cert for Kubernetes API Server       | `ca`        | 1 year           |
| `etcd-ca.crt`                  | CA for etcd-related certificates         | Self-signed | 10 years         |
| `front-proxy-ca.crt`           | CA for front proxy communication         | Self-signed | 10 years         |
| `apiserver-kubelet-client.crt` | Used by apiserver to connect to kubelets | `ca`        | 1 year           |

---

#### ⏰ How to Check Expiration

```bash
kubeadm certs check-expiration
```

Shows expiration of all certs and residual time remaining.

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

