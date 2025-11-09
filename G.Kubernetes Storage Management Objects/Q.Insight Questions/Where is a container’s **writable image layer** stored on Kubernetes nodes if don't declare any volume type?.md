### Where is a container’s **writable image layer** stored on Kubernetes nodes if don't declare any volume type?

> Is there one universal filesystem path for a container’s writable layer on Kubernetes nodes?  
> **Answer:** **No.** It depends on the **container runtime** (containerd, Docker, CRI-O) and its configuration.

---

## Q1) What are the **typical default storage locations** by runtime?

**A)** Here are the common defaults you’ll see in the field. (They can be changed by daemon config.)

### containerd (most common in modern k8s)
- Writable *upperdir* snapshots:
  ```
  /var/lib/containerd/io.containerd.snapshotter.v1.overlayfs/snapshots/<SNAP_ID>/
  ```
  (You’ll see subdirs like `fs/` and `work/`.)
- The container’s assembled rootfs (what the container actually sees) is usually bind-mounted at:
  ```
  /run/containerd/io.containerd.runtime.v2.task/k8s.io/<CONTAINER_ID>/rootfs
  ```

### Docker (legacy / dockershim days)
- Overlay2 paths:
  - **Writable layer (upperdir):**
    ```
    /var/lib/docker/overlay2/<ID>/diff
    ```
  - **Merged view (container’s rootfs):**
    ```
    /var/lib/docker/overlay2/<ID>/merged
    ```

### CRI-O
- Overlay paths:
  - **Writable layer (upperdir):**
    ```
    /var/lib/containers/storage/overlay/<ID>/diff
    ```
  - **Merged view:**
    ```
    /var/lib/containers/storage/overlay/<ID>/merged
    ```

> **Note:** These are defaults; operators can relocate storage via runtime configuration.

---

## Q2) How do you **discover the exact path** on a specific node?

**A)** Use whatever tooling matches your runtime. Examples:

### With `crictl` (works for containerd/CRI-O)
```bash
# 1) find the container ID for your Pod
crictl ps -a | grep <pod-name>

# 2) inspect to see the rootfs mount path (often under /run/containerd/.../rootfs)
crictl inspect <CONTAINER_ID> | jq -r '.info.runtimeSpec.root.path'
```

### With containerd’s `ctr`
```bash
# list containers in the k8s namespace
ctr -n k8s.io c ls

# get info (look for snapshot key / rootfs info)
ctr -n k8s.io c info <CONTAINER_ID>

# then check the corresponding snapshot directory
ls -l /var/lib/containerd/io.containerd.snapshotter.v1.overlayfs/snapshots/
```

### With Docker (legacy)
```bash
docker ps | grep <pod-name>
docker inspect <CONTAINER_ID>   | jq -r '.[0].GraphDriver.Data.UpperDir, .[0].GraphDriver.Data.MergedDir'
```

---

## Q3) How is this different from **kubelet Pod volumes** (emptyDir, PVC, etc.)?

**A)** Those are mounted under kubelet’s Pod volume tree, e.g.:
```
/var/lib/kubelet/pods/<POD-UID>/volumes/...
```
That path hosts things like **`emptyDir`**, **`configMap`**, **`secret`**, and **PVC** mounts.  
It is **not** the same as the **container image’s writable overlay layer** described above.

---

## Q4) TL;DR summary for interviews

- There’s **no single** Kubernetes path for the writable layer; it’s **runtime-specific**.  
- **containerd:** look under  
  `/var/lib/containerd/.../snapshots/<ID>/` and `/run/containerd/.../rootfs`.  
- **Docker:** `/var/lib/docker/overlay2/<ID>/(diff|merged)`.  
- **CRI-O:** `/var/lib/containers/storage/overlay/<ID>/(diff|merged)`.  
- To be precise, **inspect** the container using `crictl inspect`, `ctr`, or `docker inspect` and follow the paths shown.

---

## Q5) Why does this matter in production? (bonus)

- Troubleshooting **disk pressure** / **evictions** (ephemeral-storage usage).  
- Forensics on what was written to the writable layer vs. a mounted volume.  
- Validating that app data is in **PVCs** (persistent) rather than the ephemeral image layer.
