## Deploying a MariaDB Cluster on Kubernetes using StatefulSet

## Introduction
The objective of this project was to deploy a highly available MariaDB cluster on Kubernetes using StatefulSets. The deployment ensures data synchronization across multiple database instances and provides automatic failover to maintain availability. The project also incorporated an **NFS** storage class for persistent data storage. Here is the project diagram. 

![image](https://github.com/user-attachments/assets/8c5a5bda-34e7-4899-bf51-2ff0e12527f3)

## Project Scope
1. **Set Up Kubernetes Cluster**: Ensure a running Kubernetes cluster. In my case I have used an on-premise 3 node kubernetes cluster with kubernetes version 1.30. This project assumes you already have a running kubernetes cluster.\
2. **MariaDB Configuration**: Use ConfigMap for MariaDB settings.\
3. **Persistent Storage**: Use NFS for persistent volume claims. Here I have used an **NFS** server for persistent storage and used an `Storage Class` named `nfs-client` to automate the pv provisioning. To configure an NFS server in ubuntu go to this [nfs-server install](https://github.com/saifulislam88/nfs-server). Just make sure you add this in your NFS exports file ```insecure,no_root_squash,rw,sync,no_subtree_check```.\
4. Install `nfs-client` to **`worker node`** where **nfs mounted** via kubernetes using this command `sudo apt-get install nfs-common -y`
5.To use NFS as your storage class in kubernetes follow this [nfs-subdir-external-provisioner](https://github.com/kubernetes-sigs/nfs-subdir-external-provisioner).\
6. **Service Configuration**: Set up headless service and load balancer for client access and failover.\
7. **StatefulSet Deployment**: Deploy MariaDB using StatefulSet to ensure ordered and unique pod management.

## Project Implementation

### Step 1: Set Up Kubernetes Cluster
A Kubernetes cluster was set up using kubeadm on ubuntu 20.04. For production, cloud providers like GKE, EKS, or AKS can be used.

### Step 2: Create a ConfigMap and secret for MariaDB Configuration
A ConfigMap and secret were created to configure the MariaDB instances with necessary settings for the Cluster.

Modify the these values in the ``mariadb-sercret.yaml`` file with your custome values

```yaml
  MYSQL_DATABASE:
  MYSQL_PASSWORD:
  MYSQL_ROOT_PASSWORD:
  MYSQL_USER:
```
This ConfigMap and Secret were applied to the Kubernetes cluster:

```kubectl apply -f mariadb-configmap.yaml```

```kubectl apply -f mariadb-secret.yaml```

### Step 3: Create a Headless Service for StatefulSet
A headless service was created to manage the MariaDB StatefulSet:

This service was applied to the cluster:
```kubectl apply -f mariadb-headless-service.yaml```

### Step 4: Create a Persistent Volume Claim Template with NFS StorageClass
A Persistent Volume Claim (PVC) was created with the NFS storage class to ensure persistent data storage:

This PVC was applied to the cluster:
```kubectl apply -f mariadb-pvc.yaml```

### Step 5: Create the StatefulSet for MariaDB
A StatefulSet was configured and deployed for MariaDB, using the NFS storage class for persistent storage:

This StatefulSet was applied to the cluster:
```kubectl apply -f mariadb-statefulset.yaml```

### Step 6: Deploy the LoadBalancer Service for the StatefulSet

To access the MariaDB cluster, a LoadBalancer service was created and applied: ```kubectl apply -f mariadb-loadbalancer.yaml```

### Step 7: Verify the Deployment
The status of the StatefulSet, pods, and services was checked: 
```
kubectl get statefulset
kubectl get pods
kubectl get svc
```
### Step 8: Connect to the cluster

To connect to the cluster you can use ``Mysql Workbench``
Open the app use the LoadBalancer IP in the host section. Type the ``MYSQL_USER`` and ``MYSQL_PASSWORD`` that you've configured in the secret to access the database. 

For Local K8s cluster you won't get any LB IP untill you configure metallb in your cluster. To configure metallb follow these links below.

1. [Metallb installation in kubernetes | Saiful's Blog](https://github.com/saifulislam88/kubernetes/blob/main/G.k8s-configure-metalLB-on-premises/Setup-MetalLB-for-Nginx-Ingress-Loadbalancer-IP.md)


