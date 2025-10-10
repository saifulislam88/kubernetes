## Multi Container Pod
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
