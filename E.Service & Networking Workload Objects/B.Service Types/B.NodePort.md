`NodePort` exposes a Service on a **static port** (e.g., `30080`)  
on **every Node’s IP** in the cluster.

That means traffic can enter through **any Node’s IP:NodePort** and reach the Service.

- **Usage:** Exposes the service on each node’s IP at a static port (30000-32767).
- **Access:** External traffic can access the service using <NodeIP>:<NodePort>.
- **Example:** Useful for development, testing, or small-scale environments

## 🧠 How It Works

- The Service is still backed by a **ClusterIP** internally.  
- `kube-proxy` maps external traffic from the Node’s port (e.g., `:30080`)  
  to one of the Pods behind the Service.  
- It performs **basic load balancing** across backend Pods.

---

## ✅ Use Case

- Simple external exposure (without external LoadBalancer)  
- Useful in **development / testing** environments

---

## 🧩 Example — Deployment + NodePort Service

### `deployment.yaml`
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
      - name: web
        image: nginx:latest
        ports:
        - containerPort: 8080
```

### `service-nodeport.yaml`
```yaml
apiVersion: v1
kind: Service
metadata:
  name: web-service
spec:
  type: NodePort
  selector:
    app: web
  ports:
  - port: 80
    targetPort: 8080
    nodePort: 30080
```

✅ Apply both:
```bash
kubectl apply -f deployment.yaml
kubectl apply -f service-nodeport.yaml
```

Access the application via:
```
http://<Node-IP>:30080
```

---

## 📦 Load Balancing Role

✅ Acts as a **cluster-wide Layer 4 load balancer (TCP/UDP)**  
🌍 Exposes Service externally on every Node’s IP  
⚠️ Lacks advanced routing, SSL termination, or path-based rules (unlike Ingress)

---

## 🧭 Summary

| Feature | Description |
|----------|-------------|
| **Type** | NodePort |
| **Layer** | L4 (TCP/UDP) |
| **Access** | External via Node IP + Port |
| **Load Balancing** | Basic round-robin to backend Pods |
| **Best For** | Testing or internal environments without cloud LB |


![image](https://github.com/saifulislam88/kubernetes/assets/68442870/45ff2e4f-666d-4226-b335-6f52577e7175)
