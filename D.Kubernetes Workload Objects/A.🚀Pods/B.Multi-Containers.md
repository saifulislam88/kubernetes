## Multi Container Pod
```
vim multi-containers.yaml
```

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: multi-container-pod
spec:
  containers:
    - name: nginx-container
      image: nginx:latest
      ports:
        - containerPort: 80
      volumeMounts:
        - name: shared-data
          mountPath: /usr/share/nginx/html   # Nginx serves this path
    - name: busybox-container
      image: busybox:latest
      command: ["sh", "-c", "echo 'Hello from Busybox' > /usr/share/nginx/html/index.html; sleep 3600"]
      volumeMounts:
        - name: shared-data
          mountPath: /usr/share/nginx/html   # Must match Nginx mount
  volumes:
    - name: shared-data
      emptyDir: {}
```

This output confirms that your pod multi-container-pod has two containers.\
`kubectl get pod multi-container-pod -o jsonpath='{.spec.containers[*].name}'; echo`

Check logs of each container.
```
kubectl logs multi-container-pod -c nginx-container
kubectl logs multi-container-pod -c busybox-container
```
Exec into each container.
```
kubectl exec -it multi-container-pod -c nginx-container -- /bin/bash
kubectl exec -it multi-container-pod -c busybox-container -- /bin/bash
```

Verify shared volume content.
```
kubectl exec -it multi-container-pod -c nginx-container -- ls /usr/share/nginx/html
kubectl exec -it multi-container-pod -c busybox-container -- cat /usr/share/nginx/html/index.html
```




Run with Labels, Example tier

```
kubectl run redis -l tier=db --image=redis:alpine  || kubectl run redis --image=redis:alpine --labels tier=db
kubectl get pods --show-labels
```

Use "kubectl describe" for related events and troubleshooting

```
kubectl get nodes
kubectl get pods --all-namespaces
kubectl get pods -o wide --all-namespaces
kubectl get pods -o wide
kubectl describe pods <podid>
```

Start a busybox pod and keep it in the foreground, don't restart it if it exits.

```
kubectl run -i -t busybox --image=busybox --restart=Never
```














