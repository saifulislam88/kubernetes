## Single-Container

**1.📌Creating a pod using `Imperative way`**\
**`kubectl run nginx-01 --image=nginx`**

**2.📌Creating a pod using `Declarative way`**\
**`kubectl create ns ops`**\
**`kubectl run nginx-01 --image=nginx --namespace=ops -o yaml --dry-run=client > nginx-01.yaml`**
`kubectl run nginx-01 --image=nginx --namespace=ops -o yaml > test.yaml`

### Help Tips : kubectl run --help

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
