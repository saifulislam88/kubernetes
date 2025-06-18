Each Ingress Controller usually watches Ingress resources tagged with its ingressClassName.

Example:

```sh
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: example-ingress
spec:
  ingressClassName: nginx      # can be haproxy, traefik, etc.

```

The controller filters only those Ingresses that match its class name.
