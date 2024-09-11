![image](https://github.com/user-attachments/assets/70d9022f-7aa3-4a9a-93f1-e78b2c78bdb0)


**There are multiple ways to install the Ingress Controller:**

**Automatic with `Helm`**, using the project repository chart;\
**Manually with `kubectl apply`**, using YAML manifests;
<br>
<br>
<br>

### **Install NGINX Ingress Controller**

- Installing NGINX Ingress Controller Using `Helm`

```sh
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm repo update
kubectl create namespace ingress-nginx
helm install ingress-nginx ingress-nginx/ingress-nginx -n ingress-nginx
```

```sh
helm upgrade --install ingress-nginx ingress-nginx --repo https://kubernetes.github.io/ingress-nginx --namespace ingress-nginx --create-namespace
```


`kubectl get pods -n ingress-nginx`\

**Check the NGINX Ingress controller has been assigned a IP address from MetalLB or Cloud**\
`kubectl get svc -n ingress-nginx`

![image](https://github.com/user-attachments/assets/a09a9e82-f787-4e9f-ad63-a183cf6929ed)


**If unable to create ingress service with also 443, follow below to configure Ingress Controller to expose port 443**

```sh
helm install nginx-ingress ingress-nginx/ingress-nginx \
  --namespace ingress-nginx \
  --set controller.service.type=LoadBalancer \
  --set controller.service.ports.http=80 \
  --set controller.service.ports.https=443
```

`kubectl get pods -n ingress-nginx`\
`kubectl get svc -n ingress-nginx`


- Installing NGINX Ingress Controller Manually using `manifests`

```sh
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/cloud/deploy.yaml
kubectl get pods -n ingress-nginx
```
- Update the service type to LoadBalancer if necessary\
`kubectl edit svc ingress-nginx-controller -n ingress-nginx`

- **Checking ingress controller version**

```sh
kubectl -n ingress-nginx get pods
kubectl -n ingress-nginx logs ingress-nginx-controller-5bdc4f464b-q6mgv | grep "NGINX Ingress controller"
```
```sh
POD_NAMESPACE=ingress-nginx
POD_NAME=$(kubectl get pods -n $POD_NAMESPACE -l app.kubernetes.io/name=ingress-nginx --field-selector=status.phase=Running -o name)
kubectl exec $POD_NAME -n $POD_NAMESPACE -- /nginx-ingress-controller --version
```

