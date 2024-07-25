- [Q1?. Containers, and Kubernetes: Six Strategies for Application Deployment](https://github.com/saifulislam88/kubernetes/blob/main/kb8s-interview-questions.md#q1-containers-and-kubernetes-six-strategies-for-application-deployment)
- [Q2?. What is the most complex Kubernetes task in your organization? Often, it is about](https://github.com/saifulislam88/kubernetes/blob/main/kb8s-interview-questions.md#q2-what-is-the-most-complex-kubernetes-task-in-your-organization-often-it-is-about)
- [Q3?. Can we call a ReplicaSet a declarative object as well? If yes, what is the key difference between a Deployment and a ReplicaSet, and when should we use each?](https://github.com/saifulislam88/kubernetes/blob/main/kb8s-interview-questions.md#q3-can-we-call-a-replicaset-a-declarative-object-as-well-if-yes-what-is-the-key-difference-between-a-deployment-and-a-replicaset-and-when-should-we-use-each)
- [Q4?. Kubernetes Objects Comparison](https://github.com/saifulislam88/kubernetes/blob/main/kb8s-interview-questions.md#q4-kubernetes-objects-comparison)
- [Q5?. Kubernetes Oobjects vs Resources](https://github.com/saifulislam88/kubernetes/blob/main/kb8s-interview-questions.md#q5-kubernetes-objects-vs-resources)

- [Q6?.Kubernetes Ingress](https://github.com/saifulislam88/kubernetes/blob/main/kb8s-interview-questions.md#kubernetes-ingress)
- [Q7?.Docker Vs Podman Vs Containerd Vs CRI-O👇](https://www.linkedin.com/posts/mmumshad_kodekloud-devops-kubernetes-activity-7153377989160751105-viax?utm_source=share&utm_medium=member_desktop)
- 𝗞𝘂𝗯𝗲𝗿𝗻𝗲𝘁𝗲𝘀 𝗡𝗲𝘁𝘄𝗼𝗿𝗸𝗶𝗻𝗴: 𝗛𝗼𝘄 𝗱𝗼𝗲𝘀 𝗮 𝗣𝗼𝗱 𝗴𝗲𝘁 𝗶𝘁𝘀 𝗜𝗣 𝗔𝗱𝗱𝗿𝗲𝘀𝘀?
https://www.linkedin.com/posts/gunaseela_kubernetes-containerization-kuberenetsnetworking-activity-7209717060682072064-UJO9?utm_source=share&utm_medium=member_desktop


- Question 9: Describe the process of a blue-green deployment and its advantages...?

Answer: Blue-green deployment involves maintaining two identical environments; one (Blue) hosts the current production application, while the other (Green) holds the new version. Once the Green environment is tested and ready, traffic is switched from Blue to Green, minimizing downtime and allowing easy rollback. This method significantly reduces risk by providing a rapid rollback strategy if something goes wrong.



### **Q1?. Containers, and Kubernetes: Six Strategies for Application Deployment**

https://www.linkedin.com/pulse/containers-kubernetes-six-strategies-application-deployment-k-dd6ee/?trackingId=7bD5xsZQSqaRO60WflLajQ%3D%3D

### **Q2?. What is the most complex Kubernetes task in your organization? Often, it is about:**

1. Upgrading critical services with 0 downtime. (including K8s cluster)
2. Managing K8s across multiple clouds or a mix of on-premises and cloud.
3. Keeping track of the health, security and performance of a large scale cluster.
4. Private connection between multiple k8s clusters
5. Implementing DR & backups as well as multi cluster networking with service mesh. 
6. Rsync live copying of PVC data between two different cluster or two different provider EKS and AKS for instance

 I know complexity often arises from the combination of factors. What's the most complex Kubernetes task/tasks you have handled so far?

### **Q3?. Can we call a ReplicaSet a declarative object as well? If yes, what is the key difference between a Deployment and a ReplicaSet, and when should we use each?**

While both Deployments and ReplicaSets are declarative objects used to manage Pods in Kubernetes, Deployments provide a higher level of abstraction with additional features for managing application updates, rollbacks, and scaling. ReplicaSets are more basic and are usually managed by Deployments rather than being used directly. For most use cases, especially for stateless applications that require version control and updates, Deployments are the recommended choice.


**Comparison**

| Feature                | Deployment                                       | ReplicaSet                                       | Replication Controller                                   |
|------------------------|--------------------------------------------------|--------------------------------------------------|---------------------------------------------------------|
| **Primary Use**        | Manages ReplicaSets and provides declarative updates. | Ensures a specified number of pods are running.    | Ensures a specified number of pods are running (older method). |
| **Rolling Updates**    | Yes                                              | No                                               | No                                                      |
| **Rollbacks**          | Yes                                              | No                                               | No                                                      |
| **Declarative Updates**| Yes                                              | No                                               | No                                                      |
| **Self-healing**       | Yes                                              | Yes                                              | Yes                                                     |
| **Scaling**            | Yes                                              | Yes                                              | Yes                                                     |
| **Controller Management** | Manages ReplicaSets                              | Manages Pods                                      | Manages Pods                                             |
| **Preferred Usage**    | Recommended for managing stateless applications. | Used internally by Deployments, not typically used directly. | Legacy, use ReplicaSet or Deployment instead.            |



###  **Q4?. Kubernetes Objects Comparison

| Feature/Attribute          | Deployment                                     | ReplicaSet                                     | Replication Controller                            | Pod                                          | Service                                        | ConfigMap                                      | Secret                                         | PersistentVolume (PV)                          | PersistentVolumeClaim (PVC)                    | Ingress                                       |
|----------------------------|------------------------------------------------|------------------------------------------------|--------------------------------------------------|----------------------------------------------|------------------------------------------------|------------------------------------------------|------------------------------------------------|------------------------------------------------|------------------------------------------------|-----------------------------------------------|
| **Primary Use**            | Manages ReplicaSets and provides declarative updates. | Ensures a specified number of pods are running. | Ensures a specified number of pods are running (older method). | The smallest, most basic deployable object. | Exposes a set of Pods as a network service.     | Stores non-confidential configuration data.   | Stores confidential data (e.g., passwords).   | Abstracts storage for use by Kubernetes.      | Requests storage resources from PVs.          | Manages external access to services.           |
| **Rolling Updates**        | Yes                                            | No                                             | No                                               | No                                           | No                                             | No                                             | No                                             | No                                             | No                                             | No                                            |
| **Rollbacks**              | Yes                                            | No                                             | No                                               | No                                           | No                                             | No                                             | No                                             | No                                             | No                                             | No                                            |
| **Declarative Updates**    | Yes                                            | No                                             | No                                               | No                                           | No                                             | Yes                                            | Yes                                            | Yes                                            | Yes                                            | Yes                                           |
| **Self-healing**           | Yes                                            | Yes                                            | Yes                                              | Yes                                          | No                                             | No                                             | No                                             | No                                             | No                                             | No                                            |
| **Scaling**                | Yes                                            | Yes                                            | Yes                                              | No                                           | No                                             | No                                             | No                                             | No                                             | No                                             | No                                            |
| **Controller Management**  | Manages ReplicaSets                            | Manages Pods                                   | Manages Pods                                     | Runs containers.                            | Routes traffic to Pods.                       | Provides configuration to Pods.               | Provides secrets to Pods.                     | Provides storage resources.                   | Claims storage resources from PVs.            | Routes external traffic to services.          |
| **Preferred Usage**        | Recommended for managing stateless applications. | Used internally by Deployments, not typically used directly. | Legacy, use ReplicaSet or Deployment instead.    | Running single instances of applications.   | Abstracting access to Pods across nodes.      | Managing application configuration.           | Managing sensitive information.               | Provisioning and managing storage.            | Requesting and using storage in Pods.         | Managing HTTP and HTTPS traffic to services.  |
| **Supports Labels/Selectors** | Yes                                         | Yes                                            | Yes                                              | Yes                                          | Yes                                            | Yes                                            | Yes                                            | Yes                                            | Yes                                            | Yes                                           |
| **Supports Annotations**   | Yes                                            | Yes                                            | Yes                                              | Yes                                          | Yes                                            | Yes                                            | Yes                                            | Yes                                            | Yes                                            | Yes                                           |
| **Supports Namespaces**    | Yes                                            | Yes                                            | Yes                                              | Yes                                          | Yes                                            | Yes                                            | Yes                                            | Yes                                            | Yes                                            | Yes                                           |


### Q5?. Kubernetes Objects vs. Resources


**Think of Kubernetes objects as recipes.** They define what you want in your cluster, like how many pods to run (number of ingredients) and what image they should use (type of dish).

**Kubernetes resources are like the kitchen**. They provide the tools (commands) to interact with those recipes (objects). You can use these tools to create new recipes (deployments), check existing ones (pods), or adjust them (scaling replicas).

In short:

- Objects define what you want (recipes).
- Resources give you the tools to manage those things (kitchen).

**Examples:**

- Object: A deployment recipe specifying 3 pods running a specific image.
- Resource: The deployments command to create or scale that deployment.



**Here's a table summarizing the key differences:**
 
 | Feature   | Kubernetes Object      | Kubernetes Resource  |
 |-----------|------------------------|----------------------|
 | Definition| Persistent entity representing desired or actual state | API endpoint for interacting with objects |
 | Analogy   | Blueprint or configuration file | URL or access point for managing objects |
 | Examples  | Deployment, Pod, Service | pods, deployments, services |
 | Focus     | Definition of application state | Interaction with objects |



## Kubernetes Ingress

 **Is Ingress a load balancer?**

Ingress is not a load balancer. It contains all the routing rules, custom headers, and TLS configurations. The ingress controller acts as a load balancer.

**Why do I need an ingress controller?**

The ingress controller is responsible for the actual routing of external traffic to kubernetes service endpoints. Without an ingress controller, the routing rules added to the ingress will not work.

**What is the difference between ingress and Nginx?**

Ingress is a kubernetes object. Nginx is used as an ingress controller (Reverse proxy).

**Can we route traffic to multiple paths using ingress?**

Yes. With a single ingress definition, you can add multiple path-based routing configurations.

**Does ingress support TLS configuration?**

Yes. You can have TLS configurations in your ingress object definition. The TLS certification will be added as a Kubernetes secret and referred to in the ingress object.




