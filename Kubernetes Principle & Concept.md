# Kubernetes (K8s)
<a name="top"></a>
**Table of Contents**
- [Kubernetes Definition](https://github.com/saifulislam88/kubernetes/blob/main/Kubernetes%20Principle%20&%20Concept.md#kubernetes-definition)
- [Kubernetes Cluster Architecture](https://github.com/saifulislam88/kubernetes/blob/main/Kubernetes%20Principle%20&%20Concept.md#kubernetes-cluster-architecture)
- [Volume](https://github.com/saifulislam88/kubernetes/blob/main/Kubernetes%20Principle%20&%20Concept.md#types-of-volumes)


----
<img src="https://github.com/kubernetes/kubernetes/raw/master/logo/logo.png" width="100">

**Before we begin(Kubernetes), let's cover some basic ideas**

# Local Deployment (Own Computer/Laptop)

If you're new to web development, you've likely used a local server, such as 'localhost' or '127.0.0.1', to view your website or handle requests like GET HTTP.
In simple terms, you've worked on your own computer.
Setting up your app locally means you can view it on your own computer using a web address like http://localhost:3000/.
Your app's files are only on your computer. Nobody else can see them.


## Kubernetes Definition

Kubernetes, which translates from **Grek** to **"pilot"** or **"helmsman"**, is an open-source system for automating deployment, scaling, 
and managing containerized applications that which developed in Google lab to manage containerized applications in different 
kind of environments such as physical, virtual, and cloud infrastructure. **Kubernetes is an open source orchestration 
tool for managing clusters of containers.**

----

    ❖ Features of Kubernetes
    
    ⮚	Continues development, integration and deployment
    ⮚	Containerized infrastructure
    ⮚	Application-centric management
    ⮚	Auto-scalable infrastructure
[Back to Top](#top)
## Kubernetes Cluster Architecture

![kubernestes-arch](https://github.com/saifulislam88/kubernetes/assets/68442870/e47edbad-e743-493b-a0d8-a9a1f4561b3a)




**Kubernetes follows a client-server architecture**. A Kubernetes cluster consists of at least **one Master Node ** (multi-master for high availability) and multiple compute nodes. 
The master is responsible  for exposing the application program interface (API), scheduling the deployments and managing the overall cluster. The **Master Node** consists of various components including
 
      ⮚ Kube-apiserver 
      ⮚ ETCD 
      ⮚ Kube-controller-manager
      ⮚ Kube-scheduler
      ⮚ DNS server for Kubernetes services.
      ⮚ Kubelet
      ⮚ Kube-proxy
      ⮚ Container Runtime(Docker,Podman)

**Worker Node** components include
 
      ⮚ kubelet 
      ⮚ Kube-proxy
      ⮚ Each node runs a container runtime, 
like Docker, and an agent that communicates with the master (kubelet). Nodes (Worker Nodes) expose compute, networking and storage resources to applications. They can be virtual machines (VMs) running in a cloud or bare metal servers running within a data center.

So a Kubernetes cluster consists of **two types of nodes (minions)**:

      1. A Master node that coordinates the cluster.
      2. Nodes (called workers) where the application runs.

[Back to Top](#top)

## K8s Components Brief (Master & Worker)

- **Kube-APISERVER**

     ⮚ Acts as the front-end for the Kubernetes control plane **&** ⮚ Handles API requests and provides access to the cluster's state.
  
- **ETCD**

     ⮚ A consistent and highly-available key-value store **&** Stores all cluster data and configuration information.

- **Kube-Controller-Manager**

     ⮚ Runs various controllers to regulate the state of the cluster & Ensures the cluster's current state matches the desired state.

- **Kube-Scheduler**

     ⮚ Assigns tasks (pods) to worker nodes based on resource availability and constraints & Ensures efficient resource utilization.

- **DNS server for Kubernetes services**

     ⮚ Provides DNS resolution for Kubernetes services & Allows pods to communicate with each other using service names.

- **Kubelet** (both master and worker).

  ⮚  An agent that runs on each node  & Ensures containers are running in pods as expected.

- **Kube-Proxy** (both master and worker).

  ⮚ Maintains network rules on nodes & Enables communication between different Kubernetes services.

- **Container Runtime (Docker, Podman)** (both master and worker).

  ⮚  Software responsible for running containers & Supports containerized application execution.

[Back to Top](#top)



### Types of Volumes:

In Kubernetes, volumes serve as directories accessible to all pod containers, facilitating data sharing and persistence beyond container lifetimes. Let's delve into the types and best practices.
![image](https://github.com/saifulislam88/kubernetes/assets/68442870/801c8e39-be3d-44b7-8257-442d27944589)


📂 **EmptyDir**:
- Starts as an empty directory.
- Perfect for sharing files between containers in the same pod.
- Data lost when the pod is deleted.

📂 **HostPath**:
- Mounts a directory from the host node’s filesystem into the pod.
- Useful for accessing host files or directories.
- Data persists even if the pod is deleted.

📂 **Persistent Volume (PV)**:
- Cluster-wide resource.
- Stores data beyond a pod's lifetime.
- Requires provisioning by a storage resource.
- Provides an abstraction layer between storage and applications.

📂 **Storage Classes**:
- Defines properties for dynamically provisioned persistent volumes.
- Allows dynamic provisioning based on workload requirements.

📂 **Persistent Volume Claim (PVC)**:
- User or pod request for a specific amount of storage.
- Binds to a matching persistent volume.
- Adds a layer of abstraction between pods and storage infrastructure.

### Best Practices:

- Size PVs and PVCs according to data requirements.
- Use subpaths cautiously; document clearly.
- Implement monitoring, check logs for issues.
- Employ pod affinity rules for scheduling influence.

### Additional Considerations:

📂 **CSI (Container Storage Interface)**:
- Explore CSI (standardized interface for storage plugins) for interfacing with external storage systems.

📂 **Volume Snapshotting**:
- Investigate solutions for creating point-in-time copies of volumes.
- Useful for data protection and recovery.

📂 **Cross-Cluster Replication**:
- For multi-cluster deployments, replicate volumes across clusters, for data availability in case of cluster failures.

📂 **Caching Mechanisms**:
- Implement caching for enhanced data access, especially with large datasets.

In conclusion, Kubernetes volumes are integral to effective data management within a cluster. By adhering to best practices and considering additional aspects like monitoring, backup strategies, and dynamic provisioning, one can ensure the efficient and reliable use of volumes in a Kubernetes environment.

Streamline your CI/CD pipeline with Codegiant, the comprehensive DevSecOps platform designed to enhance your software development and deployment processes. With robust observability features, Codegiant simplifies Kubernetes monitoring, and offers an in-built Grafana dashboard for real-time insights. Say goodbye to managing multiple costly stacks and hello to improved efficiency, faster delivery, and reduced errors. Optimize your workflows and elevate your team's performance both mentally and financially with Codegiant.


[Back to Top](#top)












