
### 🎯 Kubernetes CA Certificate Renewal Guide

This guide explains **two approaches to renewing Kubernetes CA certificates**:

1️⃣ Renewing with the **same private key** (safe, minimal impact)  
2️⃣ Renewing with a **new private key** (full CA rotation)

---

#### ✅ 1️⃣ Renew Each CA Certificate Using the Same Private Key

This approach **extends the CA certificate expiry** without changing the private key.  
**All existing component certificates remain trusted.**

##### 🚀 Steps

1. **Backup existing PKI**

```bash
sudo cp -r /etc/kubernetes/pki /etc/kubernetes/pki-backup-$(date +%F)
```

2. **Renew Cluster CA Certificate**

```bash
sudo kubeadm certs renew ca --use-api=false
```

3. **Renew etcd CA Certificate**

```bash
sudo kubeadm certs renew etcd-ca --use-api=false
```

4. **Renew Front-Proxy CA Certificate**

```bash
sudo kubeadm certs renew front-proxy-ca --use-api=false
```

5. **Verify the renewed certificates**

```bash
sudo kubeadm certs check-expiration
```

✅ **No immediate re-issuance of component certificates is required.**\
✅ **No downtime required.**

---

#### 🛡️ 2️⃣ Renew Each CA Certificate Creating a New Private Key (Full Rotation)

This approach **generates a completely new private key** for each CA.  
**All component certificates must be re-issued** because they are no longer trusted by the new CA.

⚠️ **Important: This process causes API downtime during rotation.**\
⚠️ **This is the disruptive scenario.**

- Downtime: Yes, there will be a short interruption.
- All old certificates become invalid.
- You must regenerate all component certs and kubeconfigs.
- API server and kubelet connections are interrupted while restarting.
- Clients using old admin.conf cannot connect until they get updated kubeconfig.



##### 🚀 Steps

1. **Backup existing PKI**

```bash
sudo cp -r /etc/kubernetes/pki /etc/kubernetes/pki-backup-$(date +%F)
```

2. **Generate New Cluster CA Private Key and Certificate**

```bash
openssl genrsa -out /etc/kubernetes/pki/ca.key 2048

openssl req -x509 -new -nodes -key /etc/kubernetes/pki/ca.key   -subj "/CN=kubernetes"   -days 3650   -out /etc/kubernetes/pki/ca.crt
```

3. **Generate New etcd CA Private Key and Certificate**

```bash
openssl genrsa -out /etc/kubernetes/pki/etcd/ca.key 2048

openssl req -x509 -new -nodes -key /etc/kubernetes/pki/etcd/ca.key   -subj "/CN=etcd-ca"   -days 3650   -out /etc/kubernetes/pki/etcd/ca.crt
```

4. **Generate New Front-Proxy CA Private Key and Certificate**

```bash
openssl genrsa -out /etc/kubernetes/pki/front-proxy-ca.key 2048

openssl req -x509 -new -nodes -key /etc/kubernetes/pki/front-proxy-ca.key   -subj "/CN=front-proxy-ca"   -days 3650   -out /etc/kubernetes/pki/front-proxy-ca.crt
```

5. **Renew All Component Certificates (to trust the new CA)**

```bash
sudo kubeadm certs renew all
```

6. **Regenerate Kubeconfigs**

```bash
sudo kubeadm init phase kubeconfig admin
sudo kubeadm init phase kubeconfig controller-manager
sudo kubeadm init phase kubeconfig scheduler
```

7. **Restart Kubelet and Control Plane Pods**

```bash
sudo systemctl restart kubelet
```

or stop static pods manually:

```bash
sudo crictl ps | grep kube
sudo crictl stop <container-id>
```

8. **Verify Cluster Health**

```bash
kubectl get nodes --kubeconfig /etc/kubernetes/admin.conf
```

✅ **Update kubeconfig on all admin workstations.**

✅ **Confirm nodes and pods are visible without TLS errors.**

---


