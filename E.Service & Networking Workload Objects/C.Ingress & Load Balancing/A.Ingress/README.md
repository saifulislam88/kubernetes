
## [Kubernetes Resources](#kubernetes-resources)

Services are five widely used resources that all have a role in routing traffic. Each one lets you expose services with a unique set of features and trade-offs.

**In Kubernetes, everything is accessed through APIs.** To create different types of objects like pods, namespaces, and configmaps, the Kubernetes API server provides API endpoints. These object-specific endpoints are called **API resources or simply resources**. For example, the API endpoint used to create a pod is referred to as a Pod resource. In simpler terms, a resource is a specific API URL used to access an object, and you can interact with these objects using HTTP methods like GET, POST, and DELETE.


### [Ingress](d#ingress)
An Ingress is a Kubernetes resource that defines how external traffic should be routed to services within your cluster.
Ingress is actually NOT a type of service. Instead, it sits in front of multiple services and act as a “smart router” or entrypoint into your cluster. So Ingress is an API object in Kubernetes that manages external access to services within a cluster, typically HTTP and HTTPS. It provides a single point of entry for routing and load balancing requests to various services based on defined rules.

**It acts like a traffic rule specifying:**
  - **Hostnames:** Which domain names or subdomains should trigger the rule.
  - **Paths:** Which URL paths should be mapped to specific services.
  - **Backend Services:** Which services within the cluster should handle the traffic for each path.

**Key Features of Ingress:**
  - Load Balancing: Distributes incoming traffic across multiple services.
  - Name-Based Virtual Hosting: Routes traffic based on the host header.
  - URL Routing: Directs traffic based on the request URL.
  - SSL Termination: Handles SSL/TLS encryption and decryption.

**So Ingress means the traffic that enters the cluster and egress is the traffic that exits the cluster.**

**Example:** Consider a scenario where you have multiple services (e.g., web app, API, admin interface) running in a Kubernetes cluster. Instead of creating a separate LoadBalancer for each service, you can define an Ingress resource to manage all incoming traffic. The Ingress rules will route requests to the appropriate service based on the request's URL path or host.

```sh
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: test-ingress
      namespace: dev
    spec:
      rules:
      - host: test.apps.example.com
        http:
          paths:
          - backend:
              serviceName: hello-service
              servicePort: 80
```

![image](https://github.com/user-attachments/assets/00fe0120-0d6f-4363-88fd-939c3f98d179)
