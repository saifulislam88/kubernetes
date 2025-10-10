### 📌Static Pods

**Static Pods** are managed directly by the `Kubelet` on a specific node, without the **intervention** of the Kubernetes API Server. These pods are defined by YAML files placed in a directory on the node (typically `/etc/kubernetes/manifests`), and the `Kubelet` continuously watches and manages them.

**Static Pods on Master Nodes:** Used for critical control plane components, such as:
- **kube-apiserver:** Handles cluster communication.
- **kube-controller-manager:** Runs controller processes.
- **kube-scheduler:** Schedules pods on nodes.
- **etcd:** Stores all cluster data.
These pods are directly managed by the `Kubelet` on the `master node` and are essential for the functioning of the Kubernetes control plane.

`vim /etc/kubernetes/manifests/static-keycloak-pod-svc.yaml`

```sh
apiVersion: v1
kind: Pod
metadata:
  name: static-keycloak
  #namespace: test1
  labels:
    app: keycloak
spec:
  containers:
  - name: keycloak
    image: quay.io/keycloak/keycloak:24.0.3
    args: ["start-dev"]
    ports:
    - containerPort: 8080
---
apiVersion: v1
kind: Service
metadata:
  name: keycloak-svc
  namespace: test1
spec:
  selector:
    app: keycloak
  ports:
  - port: 8080
    targetPort: 8080
  type: ClusterIP
```
`kubectl get endpoints keycloak-svc`
