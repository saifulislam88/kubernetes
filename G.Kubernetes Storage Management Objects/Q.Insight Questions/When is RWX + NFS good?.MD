RWX NFS is great for things like:

- A web app deployment with 3 replicas sharing:
  - `/var/www/uploads`
  - `/shared-assets`

- CI agents dumping logs into a shared directory

- Any app where multiple pods legitimately share files and the app is designed for that.

## Example (for non-DB use):
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: shared-files-pvc
spec:
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: 20Gi
  storageClassName: nfs-rwx


- ✅ Kubernetes + NFS RWX can serve 3 pods across nodes.
- ❌ Using one shared RWX NFS volume for 3 Postgres pods is not safe → Postgres is not a shared-disk cluster DB.

### For Postgres:

- Use RWO and one PVC per pod (your `volumeClaimTemplates` pattern is good).
- Add replication at the database level, not by sharing one RWX volume.
