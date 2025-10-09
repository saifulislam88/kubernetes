
### [Ingress Controller](#ingressresource)

```sh

                                                     +--------------------------+
                                                     |    External Clients      |
                                                     |  https://example.com/api |
                                                     +--------------------------+
                                                     DNS resolves example.com to a public IP — the Ingress Controller service IP.
                                                     Request hits the NodePort/LoadBalancer Service → forwarded to the Ingress Controller Pod.

                                                                 |
                                                                 v
                                                     +---------------------------+
                                                     | Ingress Controller Service|  (Type: LoadBalancer(Cloud) or NodePort(bare-Metal))
                                                     | (e.g., ingress-nginx svc) |  (Role: Exposes the Ingress Controller pod to external clients on ports 80/443)
                                                     +---------------------------+
                                                                 |
                                                                 v
                                                     +---------------------------+
                                                     | Ingress Controller Pod    |  (Pod- e.g., ingress-nginx contoller, haproxy-ingress)
                                                     | (e.g., nginx-controller)  |  Function: Reads Ingress rules → configures internal reverse proxy → handles external requests.
                                                     +---------------------------+            - Watches Ingress resources 
                                                                                              - Applies rules to reverse proxy config
                                                                                              - Handles actual L7 (HTTP/S) traffic 
                                                                                              - Matches hostname and path against Ingress rules.
                                                                                              - Forwards request to the matching K8s Service, which routes to Pods.
                                                      
                                                                 |
                                                                 v
                  +-----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
                  |                                                                                               |                                                                                                     |
       +------------------------+                                                       +--------------------------------------------------+                                                         +----------------------------------------+                                                                    
       | Ingress Resource (CRD) |                                                       |    ConfigMap/Annotations                         |                                                         |          TLS Secrets(opt)              |
       |      (Rules)           |                                                       |          (Settings)                              |                                                         | - Tuning controller behavior           |
       +------------------------+                                                       +--------------------------------------------------+                                                         | - SSL, headers, timeouts, rewrites     |                                               
What it is: A Kubernetes object (kind: Ingress) that defines routing rules.             Purpose: Fine-tune behavior of the controller (timeouts, header rewrites, SSL settings, etc.).               +----------------------------------------+
Example: Match example.com/path1 and route to service-a; match /path2 → service-b.      Source: ConfigMap is loaded at pod startup; annotations are read from each Ingress object.

 
                                         |
                                         v
                            +-----------------------------+     
                            |  Internal K8s Service       |
                            |  Routes to target Pods      |
                            |  - Type: ClusterIP          |
                            |  - e.g., svc: my-app        |
                            +-----------------------------+
 What they are: Normal Kubernetes ClusterIP services (e.g., svc: my-app-service) that point to pods.
                                         |
                                         v
                            +-----------------------------+
                            |      Application Pod        |
                            |  (e.g., my-app-xxx-xxxx)    |
                            +-----------------------------+




```


**An Ingress Controller is a software program of Ingress that runs inside your Kubernetes cluster and implements the Ingress API. It reads Ingress objects and takes actions to properly route incoming requests.** Essentially, the Ingress Controller is responsible for making Ingress resources functional. So It acts as an interpreter for Ingress resources, translating the traffic rules defined in the Ingress objects into configurations for your load balancer or edge router.

**Examples of Ingress Controllers**\
There are many available Ingress controllers, all of which have different features.

   - **AKS Application Gateway Ingress Controller** is an ingress controller that configures the Azure Application Gateway.
   - **GKE Ingress Controller** for Google Cloud
   - **AWS Application Load Balancer Ingress Controller**
   - **HAProxy Ingress** is an ingress controller for HAProxy.
   - **Istio Ingress** is an Istio based ingress controller.
   - **The NGINX Ingress** Controller for Kubernetes works with the NGINX webserver (as a proxy).
   - **The Traefik Kubernetes** Ingress provider is an ingress controller for the Traefik proxy.

     
NGINX/Traefik, and HAProxy Ingress Controller is a Kubernetes-native load balancer and reverse proxy that manages inbound traffic to the services within a Kubernetes cluster. It is used to expose HTTP and HTTPS services externally and route traffic based on URL paths, hostnames, etc.

   - Ingress resources define the desired traffic routing. Ingress Controllers implement those desired routes by interacting with your load balancer or edge router.
   - We create an Ingress resource and deploy an Ingress Controller to manage it.

<img src="https://github.com/saifulislam88/kubernetes/assets/68442870/87a65cc5-2dc6-4add-b8f6-cd7e5c28d967" alt="Kubernetes Ingress" width="400"/>

- **Relationship Between Ingress and Ingress Controller**
  - **Ingress:** Defines the rules for routing external traffic to services within the cluster. It is a declarative specification of how traffic should be handled.
  - **Ingress Controller:** The operational component that watches for Ingress resources, interprets their rules, and configures the necessary infrastructure to enforce them. It acts on the   
      instructions provided by Ingress resources.

- **How They Work Together**

  - **Define Ingress Resources:** You create Ingress resources to specify how incoming traffic should be routed to services within your Kubernetes cluster.
  - **Ingress Controller Watches for Ingress Resources:** The Ingress Controller constantly monitors the Kubernetes API server for changes to Ingress resources.
    Configure Load Balancer/Proxy: Upon detecting changes, the Ingress Controller updates the configuration of the underlying load balancer or proxy (e.g., NGINX, HAProxy, Traefik) to reflect the   
    specified routing rules.
  - **Traffic Routing:** Incoming traffic is then routed according to the rules defined in the Ingress resources and enforced by the Ingress Controller.

  - <img src="https://github.com/saifulislam88/kubernetes/assets/68442870/02919b8b-624e-40fe-9bac-6e023441cfa9" alt="Kubernetes Ingress" width="400"/>


  https://nidhiashtikar.medium.com/kubernetes-ingress-d71127920357
