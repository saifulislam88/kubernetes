B.k8s-simple-nginx-web-with-nginx-ingress-controller

### **Prerequisites:**

- **MetalLB**: Provides LoadBalancer services in a bare-metal cluster by assigning IPs from a specified range.
**1.** 🧩Ensure [MetalLB installation](https://github.com/saifulislam88/kubernetes/blob/main/G.k8s-configure-metalLB-on-premises/Setup-MetalLB-for-Nginx-Ingress-Loadbalancer-IP.md) if your cluster is running in a **bare-metal environment**, to provide a LoadBalancer IP.

- **NGINX Ingress Controller:** Manages external access to services in a Kubernetes cluster, typically via HTTP/HTTPS.
**2.** 🧩Ensure that [NGINX Ingress Controller installation](https://github.com/saifulislam88/kubernetes/blob/main/H.k8s-ingress-controller-resource-routing-lb-ssl-nginx-haproxy-traefik/A.k8s-Ingress-controller-installation.md#install-nginx-ingress-controller) in your cluster (via `Helm` or`manually`as outlined previously).











