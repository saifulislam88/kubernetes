
# ✅ Using Init Containers for One-Time Tasks in Kubernetes

An **Init Container** runs before your main application container starts — perfect for tasks like:

- Database migrations (e.g., `flyway`, `alembic`, custom scripts)
- Pre-configuration
- Downloading secrets or configs

---

## 🔧 How It Works:

- Kubernetes runs the Init Container(s) **first**
- They **must complete successfully**
- Then, Kubernetes **starts your app container**

---

## 🧱 Example YAML

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-with-migration
spec:
  initContainers:
  - name: migrate-db
    image: mycompany/db-migrator
    command: ["sh", "-c", "python migrate.py"]

  containers:
  - name: myapp
    image: mycompany/myapp
    ports:
    - containerPort: 8080
```

> 🔁 If the Init Container fails, the pod will retry it — and your main app won’t start until the migration finishes successfully.
