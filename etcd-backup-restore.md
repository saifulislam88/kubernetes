
The followings are effective and practical methods to restore etcd for `multi-master` | `single-master` Kubernetes clusters, and they cater to two main situations.

- A. ETCD restoration methods for single-master Kubernetes clusters
- B. ETCD restoration methods for multi-master Kubernetes clusters
  - B.1. Restore ETCD database to a fresh Kubernetes cluster and then join additional masters
  - B.2. Restore ETCD database to an existing or running Kubernetes cluster
     - Restore to only one master, remove others temporarily before restoring, then rejoin them
     - Restore on all master nodes simultaneously

### `Step:1` - Install etcdctl client in all master nodes

```sh
apt install etcd-client
```

### `Step:2` - Investigation etcd command | Before backup

#### To find etcd member list**
  
```sh
ETCDCTL_API=3 etcdctl member list --endpoints=https://localhost:2379 --cacert=/etc/kubernetes/pki/etcd/ca.crt --cert=/etc/kubernetes/pki/etcd/peer.crt --key=/etc/kubernetes/pki/etcd/peer.key
```

#### To check the status of the etcd health**

- **`Single Master`**

```sh
ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379 --cacert=/etc/kubernetes/pki/etcd/ca.crt --cert=/etc/kubernetes/pki/etcd/server.crt --key=/etc/kubernetes/pki/etcd/server.key endpoint health
```

- **Multi-Master Masters**(`Change IPs according to your masters`)

```sh
ETCDCTL_API=3 etcdctl --endpoints=https://192.168.4.140:2379 --endpoints=https://192.168.4.168:2379 --endpoints=https://192.168.4.138:2379 --cacert=/etc/kubernetes/pki/etcd/ca.crt --cert=/etc/kubernetes/pki/etcd/peer.crt --key=/etc/kubernetes/pki/etcd/peer.key endpoint health
```


####  To check the status of the etcd cluster endpoints | Show details about DB Size,Leader | Multi-Masters(Change IPs)

```sh
sudo ETCDCTL_API=3 etcdctl --endpoints=https://192.168.4.138:2379 --endpoints=https://192.168.4.140:2379 --endpoints=https://192.168.4.168:2379 --cacert=/etc/kubernetes/pki/etcd/ca.crt --cert=/etc/kubernetes/pki/etcd/peer.crt --key=/etc/kubernetes/pki/etcd/peer.key endpoint status --write-out=table
```

## Backup etcd snapshot
### `Step:3` - Taking an etcd backup snapshot
We can take backup using two methods command likes `option:1` & `option:2` where 1 is more easy.

### **Option 1(`Good`):** 
- Before starting, set up these environment variables to simplify commands to all master nodes

```sh
export ETCDCTL_API=3
export ETCD_CERT_PATH="/etc/kubernetes/pki/etcd"
export ETCDCTL_CACERT="${ETCD_CERT_PATH}/ca.crt"
export ETCDCTL_CERT="${ETCD_CERT_PATH}/server.crt"
export ETCDCTL_KEY="${ETCD_CERT_PATH}/server.key"
export ETCDCTL_ENDPOINTS="https://127.0.0.1:2379
```

- To take a backup, run the following command on any master node:

```sh
etcdctl snapshot save /backup/etcd-snapshot.db --cacert="${ETCDCTL_CACERT}" --cert="${ETCDCTL_CERT}" --key="${ETCDCTL_KEY}" --endpoints="${ETCDCTL_ENDPOINTS}"
```

### **Option 2(`Complex`):** 
- To take a backup, run the following command on any master node:

```sh
ETCDCTL_API=3 etcdctl --endpoints=https://[127.0.0.1]:2379 --cacert=/etc/kubernetes/pki/etcd/ca.crt --cert=/etc/kubernetes/pki/etcd/server.crt --key=/etc/kubernetes/pki/etcd/server.key snapshot save /backup/etcd-snapshot.db
```

### `Step:4` - verify the snapshot using the following command

`ETCDCTL_API=3 etcdctl --write-out=table snapshot status /backup/etcd-snapshot.db`


## Restoring etcd backup

### Restore etcd backup for single-master Kubernetes clusters

- Before restoring etcd, Ensure that all static pods (`kube-apiserver`, `control-plane`, `etcd`, `scheduler`) are not in the running state on all control plane nodes.

   ```sh
   mv /etc/kubernetes/manifests /etc/kubernetes/manifests-bak
   kubectl get po -n kube-system
   ```

- **To remove all ETCD data**
  Run the commands below on all control plane nodes. Ensure that the /var/lib/etcd directory is empty after running these commands.

  ```sh
  mv /var/lib/etcd /var/lib/bak-etcd
  ```
  
- Restore ETCD Snapshot to a new folder
  Here is the command to restore etcd and `--data-dir /var/lib/etcd-new`specific data directory for the restore.

  ```sh
  ETCDCTL_API=3 etcdctl --data-dir /var/lib/etcd-new snapshot restore /backup/etcd-snapshot.db
  ```

- **Modify/Updating /etc/kubernetes/manifests-bak/etcd.yaml for ETCD Data Directory**

  The following steps modify **`/etc/kubernetes/manifests-bak/etcd.yaml`** to use a new data directory path, `/var/lib/etcd-new`, for etcd. Here is below existing/original path `/var/lib/etcd` which need to be update according to new backup restore location.

  ```sh
  - --data-dir=/var/lib/etcd
  
  volumeMounts:
      - mountPath: /var/lib/etcd
        name: etcd-data
  
  volumes:
    - hostPath:
        path: /var/lib/etcd
        type: DirectoryOrCreate
      name: etcd-data
  ```

    **After dpdating paths in` etcd.yaml` for `var/lib/etcd-new`**

  `sudo vi /etc/kubernetes/manifests-bak/etcd.yaml`

  ```sh
  - --data-dir=**`/var/lib/etcd-new`** # Update the `data-dir` path: Change this line
  
  volumeMounts:                        # Update `volumeMounts` path: Change this section:
   - mountPath: **`/var/lib/etcd-new`**
     name: etcd-data
     
  volumes:
   - hostPath:                        # Update `hostPath` under volumes: Change this section:
       path: **`/var/lib/etcd-new`**
       type: DirectoryOrCreate
     name: etcd-data
  ```

- Move the backup directory

  
- Restart the system services.
  
```sh
systemctl daemon-reload
systemctl restart containerd
systemctl restart kubelet
```
