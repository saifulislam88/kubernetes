# ⚖️ Kubernetes Service Types and Their Load Balancer Roles

| Service Type | LB Role | Access Scope | Layer | Use Case |
|---------------|----------|--------------|--------|-----------|
| **ClusterIP** | Internal load balancing among Pods | In-cluster only | L4 (TCP/UDP) | Microservice communication |
| **NodePort** | Basic external load balancing via Node IPs | External (Node IP + Port) | L4 (TCP/UDP) | Testing, limited exposure |
| **LoadBalancer** | Cloud LB forwarding to NodePort/ClusterIP | External (public IP) | L4 (TCP/UDP) | Production, cloud-native |
| **Ingress** | HTTP/HTTPS load balancing & routing | External (domain-based) | L7 (HTTP/HTTPS) | Web/API traffic routing |

---

## 💡 Final Takeaway

✅ **ClusterIP** → Internal load balancing (service-to-service).  

✅ **NodePort** → External entry point + basic LB (for testing or custom setups).  

✅ **LoadBalancer** → External cloud-managed LB.  

✅ **Ingress** → Advanced HTTP/HTTPS routing and TLS management.
