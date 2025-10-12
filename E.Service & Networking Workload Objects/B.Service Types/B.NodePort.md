
[**2.NodePort**](#2-nodeport)\
### [2. NodePort](https://github.com/saifulislam88/kubernetes/blob/main/A.Kubernetes-principle-concept/(A).Kubernetes%20Principle%20&%20Concept.md#2-nodeport)

**The NodePort service serves as the external entry point for incoming requests for your app.**

- **Usage:** Exposes the service on each node’s IP at a static port (30000-32767).
- **Access:** External traffic can access the service using <NodeIP>:<NodePort>.
- **Example:** Useful for development, testing, or small-scale environments

        apiVersion: v1
      kind: Service
      metadata:
        name: my-service
      spec:
        type: NodePort
        selector:
          app: my-app
        ports:
          - protocol: TCP
            port: 8080                     [Internal ClusterIP Port]
            targetPort: 80                 [Apps listen port on Pod/Container]
            nodePort: 30080                [NodePort] Ex; http://nodeIP:30080 ->8080 ->80

![image](https://github.com/saifulislam88/kubernetes/assets/68442870/45ff2e4f-666d-4226-b335-6f52577e7175)
