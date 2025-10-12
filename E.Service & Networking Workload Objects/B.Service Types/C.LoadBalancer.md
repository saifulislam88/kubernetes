[**3.LoadBalancer**](#2-loadbalancer)\
### [3. LoadBalancer](https://github.com/saifulislam88/kubernetes/blob/main/A.Kubernetes-principle-concept/(A).Kubernetes%20Principle%20&%20Concept.md#3-loadbalancer)

**A LoadBalancer(Network LoadBalancer) service is the standard way to expose a service to the internet. The LoadBalancer service is the simplest and the fastest way to expose a service inside a Kubernetes cluster to the external world/outside or Internet. This external load balancer is associated with a specific IP address and routes external traffic to a Kubernetes service in your cluster.**

**The problem with this type of service** is that it is only available on the Cloud platform(AWS, GCP, Azure,others ) of some vendors and you should pay for it. On Cloud (AWS, GCP, Azure) will create Cloud Load Balancer service in the backend and generate a public IP address. 
                  
**But On Premises or So for local Kubernetes cluster NodePort is best option with external LoadBalancer (HaProxy, Nginx) that will give you a single public IP address that will forward all traffic to your NodePort service.**

- **Usage:** Exposes the service externally using a cloud provider’s load balancer and LoadBalancer type doesn’t support URL routing, SSL termination, etc.
- **Access:** External traffic can access the service via the load balancer’s IP.
- **Example:** Used in cloud environments (AWS, GCP, Azure) for production services.


**Deploying a web server in AWS Kubernetes (EKS) with a simple load balancer (without ingress) and multiple worker nodes.**

    
    ```plaintext
        +----------------------------+
        |          Internet          |
        +-------------+--------------+
                      |
                      v
        +----------------------------+
        |   AWS Load Balancer (ELB)  |  <------ External Public IP: 52.23.45.67 (Port 80)
        +-------------+--------------+
                      |
                      v
        +----------------------------+
        |        EKS Cluster         |
        | +------------------------+ |
        | |                        | |
        | |  Service (ELB)         | |
        | |  Cluster IP: 10.0.85.137 |
        | |  Ports: 80:31457/TCP   |  <------ Internal IP and Node Port within Kubernetes
        | |                        | |
        | +-----------+------------+ |
                      |
                      v
        | +------------------------+ |
        | |     Worker Node 1      | |
        | |  Private IP: 192.168.1.2 | 
        | | +--------------------+ | |
        | |    Web Server Pod      | |
        | |    Pod IP: 10.1.0.1    | |
        | |    Container Port: 80  | |
        | | +--------------------+ | |
        | +------------------------+ |
        | +------------------------+ |
        | |     Worker Node 2      | |
        | |  Private IP: 192.168.1.3 |
        | | +--------------------+ | |
        | |    Web Server Pod      | |
        | |    Pod IP: 10.1.0.2    | |
        | |    Container Port: 80  | |
        | | +--------------------+ | |
        | +------------------------+ |
        +----------------------------+
    
    
  **52.23.45.67:80 (ELB) -> 192.168.1.2:31457 or 192.168.1.3:31457 (NodePort) -> 10.0.85.137:80 (ClusterIP Service) -> 10.1.0.1:80 or 10.1.0.2:80 (Pods)**


 **web-server-deployment.yaml**
          
          apiVersion: apps/v1
      kind: Deployment
      metadata:
        name: web-server
      spec:
        replicas: 3
        selector:
          matchLabels:
            app: web-server
        template:
          metadata:
            labels:
              app: web-server
          spec:
            containers:
            - name: web-server
              image: nginx:latest
              ports:
              - containerPort: 80



**web-server-service.yaml**

        apiVersion: v1
        kind: Service
        metadata:
          name: web-server
        spec:
          type: LoadBalancer
          selector:
            app: web-server
          ports:
          - protocol: TCP
            port: 80
            targetPort: 80

