### 📌Static Pods

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
