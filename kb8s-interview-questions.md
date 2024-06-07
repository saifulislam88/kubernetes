#### **Q1?. Containers, and Kubernetes: Six Strategies for Application Deployment**

https://www.linkedin.com/pulse/containers-kubernetes-six-strategies-application-deployment-k-dd6ee/?trackingId=7bD5xsZQSqaRO60WflLajQ%3D%3D

**Q2?. What is the most complex Kubernetes task in your organization? Often, it is about:**

1. Upgrading critical services with 0 downtime. (including K8s cluster)
2. Managing K8s across multiple clouds or a mix of on-premises and cloud.
3. Keeping track of the health, security and performance of a large scale cluster.
4. Private connection between multiple k8s clusters
5. Implementing DR & backups as well as multi cluster networking with service mesh. 
6. Rsync live copying of PVC data between two different cluster or two different provider EKS and AKS for instance

 I know complexity often arises from the combination of factors. What's the most complex Kubernetes task/tasks you have handled so far?

**Q3?. Can we call a ReplicaSet a declarative object as well? If yes, what is the key difference between a Deployment and a ReplicaSet, and when should we use each?**

While both Deployments and ReplicaSets are declarative objects used to manage Pods in Kubernetes, Deployments provide a higher level of abstraction with additional features for managing application updates, rollbacks, and scaling. ReplicaSets are more basic and are usually managed by Deployments rather than being used directly. For most use cases, especially for stateless applications that require version control and updates, Deployments are the recommended choice.


# Comparison

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



# Kubernetes Objects Comparison

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

### Example Usage
```yaml
# Deployment Example
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
