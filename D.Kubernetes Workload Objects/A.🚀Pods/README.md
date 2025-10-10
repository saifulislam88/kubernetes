## 🚀Pods
<img width="1659" height="548" alt="image" src="https://github.com/user-attachments/assets/45f52824-e20b-4aee-9673-c625ebe2c9ec" />

Pods are the smallest deployable units of Kubernetes Cluster that you can create and manage. Kubernetes pods have a defined lifecycle.

### **Pods in a Kubernetes cluster are used in two main ways:**
   **1**. Pods that run a `single container`.\
   **2**. Pods that run `multiple containers` that need to work together.

So We can create pods in Kubernetes Cluster in two method which already we know. Lets see example:
  
**1.📌Creating a pod using `Imperative way`**\
**`kubectl run nginx-01 --image=nginx`**

**2.📌Creating a pod using `Declarative way`**\
**`kubectl create ns ops`**\
**`kubectl run nginx-01 --image=nginx --namespace=ops -o yaml --dry-run=client > nginx-01.yaml`**

**`vim nginx-01.yaml`**

```sh
apiVersion: v1
kind: Pod
metadata:
  name: nginx-01
  namespace: dev
spec:
  containers:
  - name: nginx
    image: nginx
```
**`kubectl apply -f nginx-01.yaml`**\
**`kubectl get pods -n ops`**

**Get List of Containers in a specific Pod**     
`kubectl get pod <pod-name> -o jsonpath='{.spec.containers[*].name}' | tr ' ' '\n'; echo`  
<br>

- ### 📌Static Pods

**Static Pods** are managed directly by the `Kubelet` on a specific node, without the **intervention** of the Kubernetes API Server. These pods are defined by YAML files placed in a directory on the node (typically `/etc/kubernetes/manifests`), and the `Kubelet` continuously watches and manages them.

**Static Pods on Master Nodes:** Used for critical control plane components, such as:
- **kube-apiserver:** Handles cluster communication.
- **kube-controller-manager:** Runs controller processes.
- **kube-scheduler:** Schedules pods on nodes.
- **etcd:** Stores all cluster data.
These pods are directly managed by the `Kubelet` on the `master node` and are essential for the functioning of the Kubernetes control plane.

`vim /etc/kubernetes/manifests/static-nginx.yaml`

```sh
apiVersion: v1
kind: Pod
metadata:
  name: static-nginx
  labels:
    app: nginx
spec:
  containers:
  - name: nginx
    image: nginx:latest
    ports:
    - containerPort: 80
```
