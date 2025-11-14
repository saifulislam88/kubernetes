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

### storageClassName
