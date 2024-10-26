https://devopscube.com/backup-etcd-restore-kubernetes/


The followings are effective and practical methods to restore etcd for multi-master Kubernetes clusters, and they cater to two main situations.
- etcd Restoration Methods for Multi-Master Kubernetes Clusters
 - Restore etcd Database to a Fresh Kubernetes Cluster and Join Additional Masters
 - Restore etcd Database to an Existing or Running Kubernetes Cluster
    - Restore to only one Master, remove others temporarily, then rejoin them
	  - Restore on All Master Nodes Simultaneously
