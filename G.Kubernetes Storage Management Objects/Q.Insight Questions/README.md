## No volume specified

**No volume specified** → Pod writes to **ephemeral container layer** (lost on reschedule).
By default, a Pod does **not** get an `emptyDir`.
If you don’t declare any volumes, your containers write to their **own writable image layer** (overlayfs). That layer is:

- **Ephemeral:** lost on any container restart, Pod delete, or reschedule.  
- **Accounted as `ephemeral-storage`:** can trigger eviction if it grows too much.  
- **Per-container:** not shared between containers in the same Pod.

---

## What `emptyDir` actually is

`emptyDir` only exists **if you specify it** in the Pod spec. It’s:

- **Ephemeral but Pod-scoped:** survives container restarts inside the same Pod, but is deleted when the **Pod** is deleted or moves to another node.  
- **Shared across containers** in the same Pod.  
- Can be backed by **node disk** (default) or **memory** (`medium: Memory`).

**Example:**

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: demo-emptydir
spec:
  containers:
    - name: app
      image: busybox
      command: ["sh","-c","echo hello > /work/hello.txt && sleep 3600"]
      volumeMounts:
        - name: work
          mountPath: /work
  volumes:
    - name: work
      emptyDir: {}          # or: { medium: Memory }
```

---

## Auto-mounted projected volume (not `emptyDir`)

There is an automatic volume you’ll often see, but it’s **not** `emptyDir`—it’s a **projected** service-account token at:

```
/var/run/secrets/kubernetes.io/serviceaccount
```

It is **read-only** and **not for app data**.

## **Dynamic PVC** → install a provisioner + StorageClass, then just create a **PVC** (no PV YAML).
## **Static PVC** → create **PV** first, then **PVC** binds to it (useful for restores / pre-existing data).
