![image](https://github.com/user-attachments/assets/70d9022f-7aa3-4a9a-93f1-e78b2c78bdb0)


**There are multiple ways to install the Ingress Controller:**

**Automatic with `Helm`**, using the project repository chart;\
**Manually with `kubectl apply`**, using YAML manifests;


**Install NGINX Ingress Controller**

- Installing NGINX Ingress Controller Using `Helm`

```sh
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm repo update
kubectl create namespace ingress-nginx
helm install ingress-nginx ingress-nginx/ingress-nginx -n ingress-nginx
```
`kubectl get pods -n ingress-nginx`\
`kubectl get svc -n ingress-nginx`



**Installing NGINX Ingress Controller Manually**

- Deploy NGINX Ingress Controller `manifests`

```sh
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/cloud/deploy.yaml
kubectl get pods -n ingress-nginx
```
- Update the service type to LoadBalancer if necessary
`kubectl edit svc ingress-nginx-controller -n ingress-nginx`


