- **PersistentVolume (PV)** – the actual storage in the cluster  

- Cluster-level storage object.
- Points to real storage (NFS, disk, LUN, cloud).
- Created manually (static) or by StorageClass (dynamic).


  - `accessModes` – how it can be mounted:
    - `ReadWriteOnce (RWO)` – one node can write  
    - `ReadWriteMany (RWX)` – many nodes can read/write  
    - `ReadOnlyMany (ROX)` – many nodes, read-only (rare)


  - `persistentVolumeReclaimPolicy` – what happens to the data when the PVC is deleted?
    - `Retain` – **keep the data**, admin cleans manually  
    - `Delete` – **delete the actual storage**  
    - `Recycle` – deprecated (don’t use in new setups)

  - `volumeMode`
    - `Filesystem` – normal filesystem (most common)  
    - `Block` – raw block device


### PVC (PersistentVolumeClaim)

App’s request: “I need X GiB with mode Y.”
Bound 1:1 to a PV.
Pod uses PVC as a volume.


### StorageClass (SC) – "How to create PVs on demand"
A recipe/template to create new disks automatically when PVCs ask for them.

**Without StorageClass, an admin must:**\
1. Create PVs manually.\
2. Then apps bind to those PVs.
With StorageClass and a provisioner/CSI driver, PVs can be created automatically when a PVC is created.


Template that describes how to create PVs automatically.
PVC references it with storageClassName.
Can be set as default for easy use.
