
## Kubernetes Resources Overview

In Kubernetes, a **resource** is any API object managed by the control plane — things like **Pod**, **Service**, **Deployment**, **ConfigMap**, etc.

You can verify all available resources in your cluster using the command:

```bash
kubectl api-resources
```

### Example Output

Among the listed items, you’ll find both **Endpoints** and **Ingress**, which are Kubernetes resources:

```
NAME         SHORTNAMES   APIVERSION                  NAMESPACED   KIND
endpoints    ep           v1                          true         Endpoints
ingresses    ing          networking.k8s.io/v1        true         Ingress
```

- **Endpoints (ep)**: Represent the actual Pod IPs associated with a Service.
- **Ingress (ing)**: Manages HTTP/HTTPS access to Services from outside the cluster.

These are both API-managed objects, which means they are **resources** in Kubernetes.
