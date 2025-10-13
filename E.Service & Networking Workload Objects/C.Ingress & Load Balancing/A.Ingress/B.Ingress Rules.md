
## 🌐 Kubernetes Ingress Rules

Ingress rules define how incoming HTTP/HTTPS traffic is routed to internal Services within a Kubernetes cluster.  
They are part of the **Ingress resource specification**.

---

## 🧩 1️⃣ What Is an Ingress Rule?
Each **Ingress rule** tells Kubernetes which host (domain) and path (URL) should forward traffic to a specific Service and port.

```yaml
rules:
- host: <domain-name>
  http:
    paths:
    - path: <url-path>
      pathType: <Exact | Prefix | ImplementationSpecific>
      backend:
        service:
          name: <service-name>
          port:
            number: <service-port>
```

---

## ⚙️ 2️⃣ Basic Ingress Rule Example
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: basic-ingress
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
            name: app-service
            port:
              number: 80
```

**Explanation:**  
Requests to `http://app.example.com/*` → routed to Service **app-service** on port **80**.

---

## 🧭 3️⃣ Path Matching (pathType)

| Path Type | Behavior | Example |
|------------|-----------|----------|
| Exact | Matches the path exactly | `/login` → only `/login` |
| Prefix | Matches all paths with the given prefix | `/api` → `/api`, `/api/v1`, `/api/v2/...` |
| ImplementationSpecific | Depends on the Ingress Controller (not recommended) | Controller-defined behavior |

🔹 **Recommendation:** Use `Prefix` or `Exact`.

---

## 🏭 4️⃣ Multiple Rule Example (Production Scenario)
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: multi-app-ingress
  namespace: prod
spec:
  ingressClassName: nginx
  rules:
  - host: portal.company.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: frontend-service
            port:
              number: 80
  - host: api.company.com
    http:
      paths:
      - path: /v1/
        pathType: Prefix
        backend:
          service:
            name: backend-service
            port:
              number: 8080
  tls:
  - hosts:
    - portal.company.com
    - api.company.com
    secretName: company-tls
```

**In Production:**  
- `https://portal.company.com` → frontend-service:80  
- `https://api.company.com/v1/` → backend-service:8080  
TLS uses **company-tls** for HTTPS.

---

## ⚙️ 5️⃣ Advanced Example (Multiple Paths Under Same Host)
```yaml
rules:
- host: app.example.com
  http:
    paths:
    - path: /api/
      pathType: Prefix
      backend:
        service:
          name: api-service
          port:
            number: 8080
    - path: /web/
      pathType: Prefix
      backend:
        service:
          name: web-service
          port:
            number: 80
```

**Behavior:**  
- `/api/...` → api-service  
- `/web/...` → web-service

---

## ⚠️ 6️⃣ Common Issues with Ingress Rules

| Problem | Likely Cause |
|----------|---------------|
| 404 Not Found | Path or Service name mismatch |
| default backend - 404 | No rule matches the request |
| TLS not working | Wrong or missing secretName |
| Wrong Service target | Incorrect port number or service selector |
| Rule ignored | Missing ingressClassName or Ingress Controller not deployed |

---

## ✅ 7️⃣ Summary

| Concept | Description |
|----------|--------------|
| Ingress Rule | Defines routing logic for external HTTP/HTTPS requests |
| Host | Domain name to match (e.g., `api.example.com`) |
| Path | URL path to route within that host |
| Backend | Target Service and port |
| PathType | Match type: Exact, Prefix, or ImplementationSpecific |
| TLS | Optional, for HTTPS traffic |

---

## 🔗 Ingress Rule Flow

```
[ Client Request: https://api.example.com/v1/users ]
         │
         ▼
Ingress Controller
    (NGINX / Traefik)
         │
         ▼
Ingress Rule → Service (backend-service:8080)
         │
         ▼
Pods (running your app)
```

---
**Author:** Progoti Systems  
**File:** `k8s_ingress_rules.md`
