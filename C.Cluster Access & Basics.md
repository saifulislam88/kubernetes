- Understand the cluster, nodes, and control plane
- kubectl CLI overview
- Namespaces, contexts, and kubeconfig
- Inspecting cluster components:
```sh
kubectl get nodes
kubectl get pods -A
kubectl get ns
kubectl get pods -A -o wide
kubectl describe node <node-name>
kubectl get pod -n test
kubectl create namespace test
kubectl config set-context --current --namespace=test
``
