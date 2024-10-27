
The followings are effective and practical methods to restore etcd for `multi-master` | `single-master` Kubernetes clusters, and they cater to two main situations.

- ETCD restoration methods for single-master Kubernetes clusters
- ETCD restoration methods for multi-master Kubernetes clusters
  - Restore ETCD database to a fresh Kubernetes cluster and then join additional masters
  - Restore ETCD database to an existing or running Kubernetes cluster
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
