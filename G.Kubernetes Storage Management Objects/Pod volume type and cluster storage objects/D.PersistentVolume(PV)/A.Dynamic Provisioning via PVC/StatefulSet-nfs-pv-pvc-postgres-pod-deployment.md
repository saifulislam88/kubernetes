# Dynamic Provisioning with NFS in Kubernetes
## Step-by-step example with Stateful PostgreSQL (RWO), multiple replicas with RWX PVC, and shared NFS

This document provides a step-by-step guide to set up **dynamic provisioning with NFS**, configure **Stateful PostgreSQL** with **ReadWriteOnce (RWO)** PVC, and use **shared NFS** with multiple replicas (RWX).

## 1. **Overview**

We will configure the following:
- **Dynamic PVC provisioning** with NFS.
- **Stateful PostgreSQL DB** with `RWO` PVCs (only one replica can write at a time).
- **Three replicas** of a web app with **shared RWX storage** backed by NFS.
- Best practices and issues you may encounter along the way.

## 2. **Prerequisites**

- **Kubernetes cluster** running with `kubectl` access.
- **NFS server** setup and accessible by all nodes in the Kubernetes cluster. To configure an NFS server in ubuntu go to this [nfs-server install](https://github.com/saifulislam88/nfs-server). Just make sure you add this in your NFS exports file **```insecure,no_root_squash,rw,sync,no_subtree_check```**.
- [Install **`nfs-client`**](https://github.com/saifulislam88/nfs-server?tab=readme-ov-file#linux-client) to **`worker node`** where **nfs mounted** via kubernetes using this command `sudo apt install nfs-common -y`
- **NFS client provisioner** installed to dynamically provision volumes.

> To install the NFS client provisioner:

```bash
helm repo add nfs-subdir-external-provisioner https://kubernetes-sigs.github.io/nfs-subdir-external-provisioner/
helm repo update
helm install nfs-provisioner nfs-subdir-external-provisioner/nfs-subdir-external-provisioner   --set nfs.server=<NFS_SERVER_IP>   --set nfs.path=/srv/k8s-nfs   --set storageClass.name=nfs-client   --set storageClass.defaultClass=true
```

## 3. **Configuring Dynamic PVC Provisioning with NFS**

### 3.1 StorageClass for NFS Provisioning
Create the StorageClass to enable dynamic provisioning.

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: nfs-client
provisioner: k8s-sigs.io/nfs-subdir-external-provisioner
reclaimPolicy: Retain
volumeBindingMode: WaitForFirstConsumer
```
This **StorageClass** uses the **NFS Subdir External Provisioner**, and when a PVC is created using this class, it dynamically provisions an NFS-backed PV.

### 3.2 PVC for Stateful PostgreSQL (RWO)

We’ll configure a **StatefulSet** for PostgreSQL, which requires a **PersistentVolumeClaim (PVC)** that will bind to a dynamic PV created by the NFS provisioner. **RWO** ensures only one replica can write at a time.

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: postgres-pvc
  namespace: database
spec:
  accessModes: ["ReadWriteOnce"]
  resources:
    requests:
      storage: 20Gi
  storageClassName: nfs-client
```

### 3.3 StatefulSet for PostgreSQL

This StatefulSet will use the **PVC** created above and mount the dynamic NFS volume.

`echo -n 'my_secure_password' | base64`

```bash
kubectl create secret generic postgres-secret \
  --from-literal=password=bXlfc2VjdXJlX3Bhc3N3b3Jk \
  --namespace=database
```


```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: postgres
  namespace: database
spec:
  serviceName: postgres
  replicas: 1
  selector:
    matchLabels:
      app: postgres
  template:
    metadata:
      labels:
        app: postgres
    spec:
      containers:
        - name: postgres
          image: postgres:13-alpine
          env:
            - name: POSTGRES_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: postgres-secret
                  key: password
          volumeMounts:
            - name: postgres-data
              mountPath: /var/lib/postgresql/data
  volumeClaimTemplates:
    - metadata:
        name: postgres-data
      spec:
        accessModes: ["ReadWriteOnce"]
        resources:
          requests:
            storage: 20Gi
        storageClassName: nfs-client
```

> Ensure to create the `postgres-secret` with a `password` key to store the Postgres password.

### 3.4 Common Issues for Stateful PostgreSQL
- **Pod not starting due to incorrect PVC size**: Ensure the `PVC` is requesting the right size and matches the available PV.
- **Permission issues**: If the PVC is bound but the Pod fails to start, check the NFS server’s permissions.

## 4. **3 Replicas with 3 PVCs using RWX (ReadWriteMany)**

We will configure a deployment with **3 replicas** and **RWX PVC** to allow multiple replicas to read/write from the same NFS-backed volume.

### 4.1 PVC with RWX Access Mode

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: shared-pvc
  namespace: app
spec:
  accessModes: ["ReadWriteMany"]
  resources:
    requests:
      storage: 10Gi
  storageClassName: nfs-client
```
### 4.2 Deployment with 3 Replicas

In this example, the 3 replicas of the app will share the same NFS-backed PVC. The `RWX` access mode ensures all replicas can access the same data concurrently.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-app
  namespace: app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web-app
  template:
    metadata:
      labels:
        app: web-app
    spec:
      containers:
        - name: web-app
          image: busybox:latest
          command:
            - sh
            - -c
            - |
              while true; do
                echo "$(date)" > /data/timestamp.log;
                sleep 60;
              done
          volumeMounts:
            - name: shared-storage
              mountPath: /data
      volumes:
        - name: shared-storage
          persistentVolumeClaim:
            claimName: shared-pvc
```

### 4.3 Service to Expose Web App

```yaml
apiVersion: v1
kind: Service
metadata:
  name: web-app-svc
  namespace: app
spec:
  selector:
    app: web-app
  ports:
    - port: 80
      targetPort: 80
  type: ClusterIP
```

## 5. **Shared NFS with Multiple Replicas (for Web App)**

We will configure shared NFS storage for a web app that allows multiple replicas to **share data** across different nodes.

### 5.1 Shared NFS PVC

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: shared-nfs-pvc
  namespace: app
spec:
  accessModes: ["ReadWriteMany"]
  resources:
    requests:
      storage: 50Gi
  storageClassName: nfs-client
```
This PVC uses `nfs-client` StorageClass for shared NFS storage.

### 5.2 Deployment with Shared NFS PVC

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-app-shared
  namespace: app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web-app-shared
  template:
    metadata:
      labels:
        app: web-app-shared
    spec:
      containers:
        - name: web-app
          image: busybox:latest
          command:
            - sh
            - -c
            - |
              while true; do
                echo "$(date)" > /shared-data/timestamp.log;
                sleep 60;
              done
          volumeMounts:
            - name: shared-storage
              mountPath: /shared-data
      volumes:
        - name: shared-storage
          persistentVolumeClaim:
            claimName: shared-nfs-pvc
```

### 5.3 Exposing the Shared Web App via Service

```yaml
apiVersion: v1
kind: Service
metadata:
  name: web-app-shared-svc
  namespace: app
spec:
  selector:
    app: web-app-shared
  ports:
    - port: 80
      targetPort: 80
  type: ClusterIP
```

## 6. **Best Practices**

- Use **`WaitForFirstConsumer`** to ensure that the PV is only bound to the PVC when there is a consumer Pod. This ensures that Kubernetes schedules Pods on the correct node.
- Always set a **reclaim policy** to **Retain** for persistent data in production to avoid accidental data loss.
- For **shared access**, use **RWX (ReadWriteMany)** PVCs, but ensure that your NFS server can handle the load and that the file system is properly tuned for concurrent access.
- Ensure **correct node affinity** in the `StorageClass` if using node-local storage.

## 7. **Common Issues**

- **PVC Pending**: Ensure that the NFS server is reachable, and check that the storage class, access modes, and sizes match.
- **Permissions**: Ensure that the NFS server allows access from all nodes and that the Kubernetes nodes can mount the NFS share with proper permissions.
- **Performance**: Be aware that NFS, though widely used for RWX, might not be as performant as local disk solutions like Ceph or GlusterFS.

---

## 8. **Download Example MD File**

Download this guide as an example `.md` file:

[Dynamic Provisioning with NFS and PostgreSQL](sandbox:/mnt/data/k8s-storage-training/docs/dynamic-provisioning-nfs-pvc-postgres.md)
