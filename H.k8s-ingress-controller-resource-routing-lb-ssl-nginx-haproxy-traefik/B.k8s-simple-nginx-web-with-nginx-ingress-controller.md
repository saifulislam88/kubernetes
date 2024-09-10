## Simple two nginx web servers deploy with nginx-ingress-controller

<img src="https://github.com/saifulislam88/docker/assets/68442870/09012688-7671-4f50-8208-dedad3b66353" alt="Signature" width="400"/>

&nbsp;&nbsp;**Copyright** © 2024 Md. Saiful Islam(**mSI**). All Rights Reserved | **Internet & ChatBot**<br>
<br>

- [Prerequisites](#Prerequisites)
- [Make a project directory](#make-a-project-directory)
- [Deployment, Service, and ConfigMap for `nginx1`](#deployment-service-and-configmap-for-nginx1)
- [Deployment, Service, and ConfigMap for `nginx2`](#deployment-service-and-configmap-for-nginx2)
- [Create an IngressClass for NGINX](#create-an-ingressclass-for-nginx)
- [Ingress Resource to Route Traffic](#ingress-resource-to-route-traffic)
- [Ingress Common Issues and Solutions](#ingress-common-issues-and-solutions)

### **🚀Prerequisites**


- **Kubernetes Cluster:** Ensure you have a running [Kubernetes cluster]
- **kubectl:** Install kubectl and configure it to interact with your cluster.
- **Helm:** Install [Helm](https://github.com/saifulislam88/kubernetes/blob/main/L.k8s-helm-helmcharts/helm-Kubernetes-package-manager.md) if you are deploying the NGINX Ingress Controller via Helm.
- **MetalLB**: Provides LoadBalancer services in a bare-metal cluster by assigning IPs from a specified range.🧩Ensure [MetalLB installation](https://github.com/saifulislam88/kubernetes/blob/main/G.k8s-configure-metalLB-on-premises/Setup-MetalLB-for-Nginx-Ingress-Loadbalancer-IP.md) if your cluster is running in a **bare-metal environment**, to provide a LoadBalancer IP.
- **NGINX Ingress Controller:** Manages external access to services in a Kubernetes cluster, typically via HTTP/HTTPS. 🧩Ensure that [NGINX Ingress Controller installation](https://github.com/saifulislam88/kubernetes/blob/main/H.k8s-ingress-controller-resource-routing-lb-ssl-nginx-haproxy-traefik/A.k8s-Ingress-controller-installation.md#install-nginx-ingress-controller) in your cluster (via `Helm` or`manually`as outlined previously).
- Follow the below setup steps for better understanding and [download manifests](https://github.com/msidka/k8s-simple-nginx-web-with-nginx-ingress-controller-manifests)


### 🚀Make a project directory
git clone https://github.com/msidka/k8s-simple-nginx-web-with-nginx-ingress-controller-manifests.git


### 🚀Deployment, Service, and ConfigMap for `nginx1`

**1. 🎯Deployment for Nginx-1**

`vim nginx1-deployment.yaml`

```sh
# nginx1-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx1-deployment
  namespace: ingress-nginx
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nginx1
  template:
    metadata:
      labels:
        app: nginx1
    spec:
      containers:
      - name: nginx1
        image: nginx:1.21.6
        volumeMounts:
        - name: nginx1-html
          mountPath: /usr/share/nginx/html
        ports:
        - containerPort: 80
      volumes:
      - name: nginx1-html
        configMap:
          name: nginx1-html-config

```

**2. 🎯Service for Nginx-1**

`vim nginx1-service.yaml`

```sh
# nginx1-service.yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx1-service
  namespace: ingress-nginx
spec:
  selector:
    app: nginx1
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
  type: ClusterIP
```

**3. 🎯ConfigMap for nginx1 Content**

`vim nginx1-configmap.yaml`

```sh
# nginx1-configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: nginx1-html-config
  namespace: ingress-nginx
data:
  index.html: |
    <html>
    <body>
    <h1>Welcome to NGINX 1 Server</h1>
    <p>This is the content served by nginx1.</p>
    </body>
    </html>
```

### 🚀Deployment, Service, and ConfigMap for `nginx2`

**4. 🎯Deployment for Nginx-2**

`vim nginx2-deployment.yaml`

```sh
# nginx2-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx2-deployment
  namespace: ingress-nginx
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nginx2
  template:
    metadata:
      labels:
        app: nginx2
    spec:
      containers:
      - name: nginx2
        image: nginx:1.21.6
        volumeMounts:
        - name: nginx2-html
          mountPath: /usr/share/nginx/html
        ports:
        - containerPort: 80
      volumes:
      - name: nginx2-html
        configMap:
          name: nginx2-html-config

```

**5. 🎯Service for Nginx-2**

`vim nginx2-service.yaml`

```sh
# nginx2-service.yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx2-service
  namespace: ingress-nginx
spec:
  selector:
    app: nginx2
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
  type: ClusterIP
```

**6. 🎯ConfigMap for nginx2 Content**

`vim nginx2-configmap.yaml`

```sh
# nginx2-configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: nginx2-html-config
  namespace: ingress-nginx
data:
  index.html: |
    <html>
    <body>
    <h1>Welcome to NGINX 2 Server</h1>
    <p>This is the content served by nginx2.</p>
    </body>
    </html>
```

### 🚀Create an IngressClass for NGINX

**7. 🎯If an IngressClass does not exist for the NGINX Ingress Controller, create one:**

`kubectl get ingress -n ingress-nginx`\
`kubectl get ingressclass`
![image](https://github.com/user-attachments/assets/1d08278e-1e81-47af-b803-b8e8c169593b)


`vim nginx-ingress-class.yaml`

```sh
# nginx-ingress-class.yaml
apiVersion: networking.k8s.io/v1
kind: IngressClass
metadata:
  name: nginx
  annotations:
    ingressclass.kubernetes.io/is-default-class: "true"  # Set as default, optional
spec:
  controller: k8s.io/ingress-nginx
```

### 🚀Ingress Resource to Route Traffic

**8.A. 🎯Ingress Resource Configuration for `80/http` port | single hostname**\
This Ingress resource will route traffic based on paths `/nginx1` and `/nginx2`:

vim `nginx-ingress_http.yaml`

```sh
# nginx-ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: nginx-ingress
  namespace: ingress-nginx
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx  # Reference the correct IngressClass here
  rules:
  - host: app.saiful.com      # Replace with your domain, or use without host to match all
    http:
      paths:
      - path: /nginx1
        pathType: Prefix
        backend:
          service:
            name: nginx1-service
            port:
              number: 80
      - path: /nginx2
        pathType: Prefix
        backend:
          service:
            name: nginx2-service
            port:
              number: 80
```

🎯**8.B. Ingress Resource Configuration for `443/https` port | `multiple hostname` | `80/http redirect to https`**\


- [Creating Self-Signed SSL Certificates Using OpenSSL or Purchase CA-signed](https://github.com/saifulislam88/kubernetes/blob/main/H.k8s-ingress-controller-resource-routing-lb-ssl-nginx-haproxy-traefik/k8s-ingress-tls-ssl-configuration.md#--creating-self-signed-ssl-certificates-using-openssl)

- [Create Kubernetes TLS Secret](https://github.com/saifulislam88/kubernetes/blob/main/H.k8s-ingress-controller-resource-routing-lb-ssl-nginx-haproxy-traefik/k8s-ingress-tls-ssl-configuration.md#--create-kubernetes-tls-secret)

**`kubectl apply -f saiful-hello-app-tls.yaml`**


**Update the nginx-ingress.yaml manifest for `https/tls`**\
`vim  nginx-ingress_https.yaml`

```sh
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: nginx-ingress
  namespace: ingress-nginx
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
    nginx.ingress.kubernetes.io/ssl-redirect: "true"       # Redirect HTTP to HTTPS
    nginx.ingress.kubernetes.io/force-ssl-redirect: "true" # Force SSL redirect
spec:
  ingressClassName: nginx
  tls:
  - hosts:
    - app1.saiful.com
    - app2.saiful.com
    secretName: saiful-hello-app-tls  # Kubernetes Secret containing the SSL certificate and key
  rules:
  - host: app1.saiful.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: nginx1-service
            port:
              number: 80
  - host: app2.saiful.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: nginx2-service
            port:
              number: 80
```

**9. 🎯Apply Configurations**

```sh
kubectl apply -f nginx1-configmap.yaml
kubectl apply -f nginx1-deployment.yaml
kubectl apply -f nginx1-service.yaml
```

```sh
kubectl apply -f nginx2-configmap.yaml
kubectl apply -f nginx2-deployment.yaml
kubectl apply -f nginx2-service.yaml
```

```sh
kubectl apply -f nginx-ingress-class.yaml
kubectl apply -f saiful-hello-app-tls.yaml
```
`kubectl apply -f nginx-ingress_http.yaml`\
**|OR|**\
`kubectl apply -f nginx-ingress_https.yaml`


**9. 🎯Testing the Setup**

**`http`**\
`Access http://app.saiful.com/nginx1 to reach the nginx1 server.`\
`Access http://app.saiful.com/nginx2 to reach the nginx2 server.`

`curl -H "Host: app.saiful.com" http://<external-ip>/nginx1`\
`curl -H "Host: app.saiful.com" http://<external-ip>/nginx2`

**`https`**\
`Access https://app1.saiful.com to reach the nginx1 server.`\
`Access https://app2.saiful.com to reach the nginx2 server.`

`curl -H "Host: app1.saiful.com" https://<external-ip>`\
`curl -H "Host: app2.saiful.com" https://<external-ip>2`


**10. 🎯Explanation**

**Deployment:** Manages the NGINX pods in a replicated fashion.\
**Service:** Exposes the NGINX pods internally within the cluster on port 80.\
**Ingress:** Routes external traffic from http://example.com to the NGINX service. The Ingress controller (NGINX Ingress) handles this routing and load balances traffic to the NGINX pods.


### 🚀Ingress Common Issues and Solutions

**404 Errors:** Ensure the paths in the Ingress resource are correct and match the backend services.\
**IngressClass Issues:** If you encounter validation errors for the IngressClass, ensure it exists and matches the Ingress resource's specification.\
**Service Endpoints Missing:** Ensure the NGINX pods are running and ready. Use kubectl describe on the service and deployment to debug readiness issues.


**11. 🎯Troubleshooting**

**Check ingress**\
`kubectl get ingress -n ingress-nginx`\
`kubectl get ingressclass`

**Check NGINX Pods and Services**\
`kubectl get pods -n ingress-nginx`\
`kubectl get svc -n ingress-nginx`

**Inspect the Ingress Resource**\
`kubectl describe ingress nginx-ingress -n ingress-nginx`

**Check Ingress Controller Logs**\
`kubectl logs -l app.kubernetes.io/name=ingress-nginx -n ingress-nginx`

**Verify Ingress Rules**\
kubectl get ingress nginx-ingress -n ingress-nginx -o yaml

**Debugging Services and Pods**\
`kubectl get endpoints -n ingress-nginx`\
`kubectl describe svc nginx1-service -n ingress-nginx`

**Verify the TLS Secret**\
`kubectl get secret -n ingress-nginx`\
`kubectl get secret saiful-hello-app-tls -o yaml`\
`kubectl get secret saiful-hello-app-tls -o jsonpath='{.data.tls\.crt}' | base64 --decode`\
`kubectl get secret saiful-hello-app-tls -o jsonpath='{.data.tls\.key}' | base64 --decode`

**Recreate the TLS Secret (If Necessary)**\
`kubectl delete secret saiful-hello-app-tls`

curl -v https://nginx1.example.com\
curl -v https://nginx2.example.com\
