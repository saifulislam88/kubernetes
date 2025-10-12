## ClusterIP Service (internal-only access)

[**1.ClusterIP**](#1-clusteripdefault)
### [1. ClusterIP(Default)]()

A ClusterIP is a virtual IP address assigned to a Kubernetes service, which is used for internal cluster communication.\
**ClusterIP is the default Kubernetes service. Your service will be exposed on a ClusterIP unless you manually define another type or type: `ClusterIP`**. **ClusterIP services are managed by the `Kubernetes API` Server and `kube-proxy`.**

If we deploy Kubernetes Cluster uisng `kubeadm`, ClusterIP default IP is **`10.96.0.0/12`**. If needed to change ClusterIP IP Block, this could be in a file such as `/etc/kubernetes/manifests/kube-apiserver.yaml` (if using kubeadm) or in a systemd service file.

- Internal communication within the cluster.
- Only accessible within the cluster (internal).
- It provides a stable, internal IP address for accessing the service within the cluster.
- Other services and pods within the same cluster can access this service.
- A backend service accessed only by other services within the cluster.


**Now create a service for pod to pod communication then we will deploy pod using `pod` | `deployment` | `statefulset` | `daemonset` objects.**

`vim my-app-svc.yaml`
  ```sh
      apiVersion: v1
      kind: Service
      metadata:
        name: my-service
      spec:
        selector:
          app: my-app
        ports:
          - protocol: TCP
            port: 80                     # Internal ClusterIP Port
            targetPort: 80               # Apps listen port on Pod/Container
   ```
`kubectl apply -f my-app-svc.yaml`\
`kubectl get svc` or `kubectl get service`


**Here deploying pods workload using `Deployment` objects**

`vim my-app-dep.yaml`

```sh

apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: my-app
  name: my-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: my-app
    spec:
      containers:
      - image: nginx
        name: nginx
```
`kubectl apply -f my-app-dep.yaml`\
`kubectl get pod`\
`curl http://ClusterIP`

![image](https://github.com/saifulislam88/kubernetes/assets/68442870/d5c7a15c-ba8a-4705-a5c2-425fa9b392ea)

We also can deploy pods & service using impertative command

`kubectl create deployment test --image=nginx`\
`kubectl expose deployment test --port=80 --target-port=80`\
`kubectl get svc test`

