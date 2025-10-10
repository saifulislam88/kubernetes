## 🚀Pods

Pods are the smallest deployable units of Kubernetes Cluster that you can create and manage. Kubernetes pods have a defined lifecycle.

## Key Points about Pods

- **Atomic Unit**: A Pod encapsulates one or more application containers, storage resources, a unique network IP, and configuration options. It's the basic building block of Kubernetes applications.
- **Containers**: Pods can contain one or more containers, which are managed as a single entity within the Pod. These containers share the same network namespace, allowing them to communicate with each other using localhost.
- **Networking**: Each Pod in Kubernetes is assigned a unique IP address, which allows communication between Pods and external clients or other Pods within the same cluster.
- **Storage**: Pods can define volumes that are mounted into their containers, allowing them to share data between containers or persist data beyond the lifetime of the Pod.
- **Lifecycle**: Pods have a lifecycle managed by the Kubernetes control plane. They can be created, updated, and terminated based on deployment configurations, scaling requirements, or failures.
- **Atomicity and Scalability**: Pods are atomic units that can be replicated and scaled horizontally. You can create multiple replicas of a Pod to handle increased load or ensure high availability.


<img width="1659" height="548" alt="image" src="https://github.com/user-attachments/assets/45f52824-e20b-4aee-9673-c625ebe2c9ec" />

### **Pods in a Kubernetes cluster are used in two main ways:**
   **1**. Pods that run a `Single container`.\
   **2**. Pods that run `Multi-containers` that need to work together.

So We can create pods in Kubernetes Cluster in two method which already we know Like as `Imperative Approach` & `Declarative Approach`. Lets see example:
  
- [Single container](https://github.com/saifulislam88/kubernetes/blob/main/D.Kubernetes%20Workload%20Objects/A.%F0%9F%9A%80Pods/A.Single-Container.md)
- [Multi-Containers](https://github.com/saifulislam88/kubernetes/blob/main/D.Kubernetes%20Workload%20Objects/A.%F0%9F%9A%80Pods/B.Multi-Containers.md)
