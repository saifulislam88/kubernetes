
# Kubernetes Ingress Resource

## 🌐 What is an Ingress Resource?

**Ingress** is a **Kubernetes API resource** that manages **external HTTP/HTTPS access** to Services inside your cluster.  
It acts as a **Layer 7 (application-level) reverse proxy or load balancer**.

🧠 In short:  
> **Ingress = Entry point for web traffic into your cluster**

It lets you route external requests (e.g., `https://app.example.com`) to internal Services (`app-service` on port 8080).

---

## ⚙️ Basic Example

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: web-ingress
  namespace: prod
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx
  rules:
  - host: app.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: web-service
            port:
              number: 8080
```

### ✅ Explanation
- `host`: external domain name (`app.example.com`)
- `path`: URL path (`/`)
- `backend`: internal Service (`web-service`)
- `ingressClassName`: which Ingress Controller handles it (`nginx`)

---

## 🏭 Production / Realistic Example

A typical **multi-app production setup** might have:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: company-ingress
  namespace: prod
spec:
  ingressClassName: nginx
  rules:
  - host: api.company.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: backend-api
            port:
              number: 8080
  - host: portal.company.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: frontend-ui
            port:
              number: 80
  tls:
  - hosts:
    - api.company.com
    - portal.company.com
    secretName: company-tls-secret
```

### ✅ What Happens in Production
- Users hit `https://portal.company.com`
- Ingress routes traffic through the NGINX Ingress Controller → `frontend-ui` Service → Pods
- TLS termination happens at the Ingress layer using `company-tls-secret`

---

## ⚠️ Common Real-World Issues

| Issue | Cause / Explanation |
|--------|----------------------|
| **404 Not Found** | Path or Service name mismatch in Ingress |
| **No external access** | Ingress Controller not installed (e.g., NGINX, Traefik) |
| **SSL errors** | Wrong or missing TLS secret |
| **Loopback / timeout** | Backend Service not reachable (wrong port or selector) |
| **Ingress not created** | `ingressClassName` missing or doesn’t match controller |
| **Multiple Ingresses conflicting** | Duplicate hosts in same namespace or cluster |

---

## ✅ Quick Summary

| Concept | Description |
|----------|--------------|
| **Kind** | `Ingress` |
| **API Version** | `networking.k8s.io/v1` |
| **Purpose** | Expose HTTP/HTTPS routes externally |
| **Requires** | Ingress Controller (e.g., NGINX, Traefik, HAProxy) |
| **Layer** | L7 (Application Layer) |
| **Used For** | Routing multiple apps/domains under one Load Balancer |

---

## 🔗 Traffic Flow Overview

```
[ External User ]
       │
       ▼
Ingress (Layer 7 Routing)
       │
       ▼
Service (Layer 4 Load Balancing)
       │
       ▼
Pod (Container Application)
```

---

**In Summary:**  
Ingress is a powerful Kubernetes resource that provides a centralized way to expose, route, and secure HTTP/HTTPS traffic for multiple applications using a single load balancer.

