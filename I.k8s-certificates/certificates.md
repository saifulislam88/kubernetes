### 🔐 Kubernetes Certificate Expiry & Renewal Strategy

This knowledgebase covers how Kubernetes handles TLS certificates, the implications of expiry, and the complete renewal and recovery process for CA and component certificates.

---

#### 📌 Certificate Types in Kubernetes

| Certificate                    | Purpose                                             | Signed By        | Default Validity |
| ------------------------------ | --------------------------------------------------- | ---------------- | ---------------- |
| `ca.crt`                       | Cluster Certificate Authority                       | Self-signed      | 10 years         |
| `etcd-ca.crt`                  | CA for etcd-related certificates                    | Self-signed      | 10 years         |
| `front-proxy-ca.crt`           | CA for front proxy communication                    | Self-signed      | 10 years         |
| `apiserver.crt`                | TLS certificate for Kubernetes API Server           | `ca`             | 1 year           |
| `apiserver-kubelet-client.crt` | Used by API server to authenticate against kubelets | `ca`             | 1 year           |
| `apiserver-etcd-client.crt`    | Used by API server to connect securely to etcd      | `etcd-ca`        | 1 year           |
| `front-proxy-client.crt`       | Used by API server to communicate with front-proxy  | `front-proxy-ca` | 1 year           |
| `etcd-server.crt`              | TLS for etcd server itself                          | `etcd-ca`        | 1 year           |
| `etcd-peer.crt`                | etcd peer-to-peer communication                     | `etcd-ca`        | 1 year           |
| `etcd-healthcheck-client.crt`  | etcd health check client certificate                | `etcd-ca`        | 1 year           |
| `admin.conf`                   | kubeconfig for admin user                           | `ca`             | 1 year           |
| `controller-manager.conf`      | kubeconfig for controller manager                   | `ca`             | 1 year           |
| `scheduler.conf`               | kubeconfig for scheduler                            | `ca`             | 1 year           |

#### 🎯 Logical Categories of Kubernetes Certificates

This document summarizes the main Kubernetes certificates, their categories, and how they depend on each other.

---

#### 🟢 1️⃣ Cluster CA Certificates

These are **root certificates** that sign other certificates in the cluster.

##### ✅ Cluster CA
- **File:** `ca.crt`
- **Signs:**
  - `apiserver.crt`
  - `apiserver-kubelet-client.crt`
  - `admin.conf`
  - `controller-manager.conf`
  - `scheduler.conf`

---

##### ✅ etcd CA
- **File:** `etcd-ca.crt`
- **Signs:**
  - `etcd-server.crt`
  - `etcd-peer.crt`
  - `etcd-healthcheck-client.crt`
  - `apiserver-etcd-client.crt`

---

##### ✅ Front-Proxy CA
- **File:** `front-proxy-ca.crt`
- **Signs:**
  - `front-proxy-client.crt`

> 📝 These 3 CAs are **independent roots**, each responsible for a different part of the system.

---

#### 🟡 2️⃣ API Server Certificates

Used for securing API server traffic.

- `apiserver.crt` – serves HTTPS for API server
- `apiserver-kubelet-client.crt` – used by API server to authenticate to kubelet
- `apiserver-etcd-client.crt` – used by API server to authenticate to etcd

**Dependencies:**
- `apiserver.crt` depends on `ca.crt`
- `apiserver-kubelet-client.crt` depends on `ca.crt`
- `apiserver-etcd-client.crt` depends on `etcd-ca.crt`

---

#### 🟣 3️⃣ etcd Certificates

Used internally by etcd cluster nodes.

- `etcd-server.crt`
- `etcd-peer.crt`
- `etcd-healthcheck-client.crt`

**Dependency:**
- All signed by `etcd-ca.crt`

---

#### 🔵 4️⃣ Client Kubeconfigs

Certificates embedded in kubeconfigs for admins and controllers.

- `admin.conf`
- `controller-manager.conf`
- `scheduler.conf`

**Dependency:**
- All signed by `ca.crt`

---

#### 🟠 5️⃣ Front Proxy Certificates

Used by the API aggregation layer.

- `front-proxy-client.crt`

**Dependency:**
- Signed by `front-proxy-ca.crt`


---

#### ⏰ How to check certificates expiration

```bash
kubeadm certs check-expiration
```

Shows expiration of all certs and residual time remaining.

```sh
root@prod-k8-master-node:~# kubeadm certs check-expiration
[check-expiration] Reading configuration from the cluster...
[check-expiration] FYI: You can look at this config file with 'kubectl -n kube-system get cm kubeadm-config -o yaml'

CERTIFICATE                EXPIRES                  RESIDUAL TIME   CERTIFICATE AUTHORITY   EXTERNALLY MANAGED
admin.conf                 Jul 15, 2025 10:47 UTC   23d             ca                      no
apiserver                  Jul 15, 2025 10:47 UTC   23d             ca                      no
apiserver-etcd-client      Jul 15, 2025 10:47 UTC   23d             etcd-ca                 no
apiserver-kubelet-client   Jul 15, 2025 10:47 UTC   23d             ca                      no
controller-manager.conf    Jul 15, 2025 10:47 UTC   23d             ca                      no
etcd-healthcheck-client    Jul 15, 2025 10:47 UTC   23d             etcd-ca                 no
etcd-peer                  Jul 15, 2025 10:47 UTC   23d             etcd-ca                 no
etcd-server                Jul 15, 2025 10:47 UTC   23d             etcd-ca                 no
front-proxy-client         Jul 15, 2025 10:47 UTC   23d             front-proxy-ca          no
scheduler.conf             Jul 15, 2025 10:47 UTC   23d             ca                      no

CERTIFICATE AUTHORITY   EXPIRES                  RESIDUAL TIME   EXTERNALLY MANAGED
ca                      Jul 13, 2034 10:47 UTC   9y              no
etcd-ca                 Jul 13, 2034 10:47 UTC   9y              no
front-proxy-ca          Jul 13, 2034 10:47 UTC   9y              no
```




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

