# Kubernetes (K8s)
<a name="top"></a>
**Table of Contents**
- [Prerequisite Concepts](https://github.com/saifulislam88/kubernetes/blob/main/(A).Kubernetes%20Principle%20%26%20Concept.md#before-we-beginning-kubernetes-lets-cover-some-basic-ideas)
- [Kubernetes Definition](https://github.com/saifulislam88/kubernetes/blob/main/(A).Kubernetes%20Principle%20%26%20Concept.md#kubernetes-definition)
- [Kubernetes Cluster Architecture](https://github.com/saifulislam88/kubernetes/blob/main/(A).Kubernetes%20Principle%20&%20Concept.md#kubernetes-cluster-architecture)
- [Kubernetes Components](https://github.com/saifulislam88/kubernetes/blob/main/(A).Kubernetes%20Principle%20&%20Concept.md#k8s-components-brief-master--worker)
- [Kubernetes Native Objects](https://github.com/saifulislam88/kubernetes/blob/main/(A).Kubernetes%20Principle%20&%20Concept.md#kubernetes-native-objects)
  - [Part 01](https://github.com/saifulislam88/kubernetes/blob/main/(A).Kubernetes%20Principle%20&%20Concept.md#part-01)
  - [Part 02](https://github.com/saifulislam88/kubernetes/blob/main/(A).Kubernetes%20Principle%20&%20Concept.md#part-02)
  - [Objects organized in categories](https://github.com/saifulislam88/kubernetes/blob/main/(A).Kubernetes%20Principle%20&%20Concept.md#the-following-table-shows-the-important-native-kubernetes-object-types-organized-in-categories)
- [Volume](https://github.com/saifulislam88/kubernetes/blob/main/(A).Kubernetes%20Principle%20&%20Concept.md#types-of-volumes)


----
<img src="https://github.com/kubernetes/kubernetes/raw/master/logo/logo.png" width="100">

## Before we beginning Kubernetes, let's cover some basic ideas

   **1.Local Deployment (Own Computer/Laptop)**

   If you're new to web development, you've likely used a local server, such as **'localhost' or '127.0.0.1'**, to view your website or handle requests like GET HTTP.
   In simple terms, you've worked on your own computer.
   Setting up your app locally means you can view it on your own computer using a web address like **http://localhost:3000/**.
   Your app's files are only on your computer. Nobody else can see them.

  **2.On-prem (VM or Phisycal Server)**

  When you use on-prem (short for on-premises), you're putting your application on a physical server.
  This means people from outside your company can access your app. But if lots of people try to use it at once, your server might struggle.
  To handle more users, you might need to add extra servers. This is called "horizontal scaling."
  Or you might need to upgrade your server's power, like adding more memory. That's called "vertical scaling."

  **3.Cloud Deployment**
  
  In the last two scenarios, when you needed to handle more requests, you had to manually increase your server's capacity or add more servers. However, there's a simpler option called cloud deployment.
  With cloud deployment, you place your application on servers owned by another company, such as Amazon Web Services (AWS). These companies handle tasks like making your servers bigger or adding more 
  if necessary. Similar to using your own servers, your application is accessible to anyone, not just individuals within your organization.
  
  Companies like AWS are commonly referred to as "public cloud vendors." Think of it as renting an apartment in a large building. You have your own space, but there are other tenants sharing the building with you, each with their own separate apartments. In addition to public cloud offerings, these vendors also provide private servers known as VPCs (virtual private clouds). Within a VPC, 
  certain resources are reserved exclusively for your use, 
  ensuring they remain readily available whenever you require them. Therefore, you have two primary deployment options: public cloud deployments and private cloud deployments. With this understanding 
  of deployment methods, let's now explore Kubernetes.


## Kubernetes Definition

Kubernetes, which translates from **Grek** to **"pilot"** or **"helmsman"**, is an open-source system for automating deployment, scaling, 
and managing containerized applications that which developed in Google lab to manage containerized applications in different 
kind of environments such as physical, virtual, and cloud infrastructure. 

**Kubernetes (K8s) is usually defined as a container orchestration service. Kubernetes is an open source orchestration 
 tool for managing clusters of containers. So Kubernetes is simply a tool to manage containers.**
  **Now, what are containers???**


----

    ❖ Features of Kubernetes
    
    ⮚	Continues development, integration and deployment
    ⮚	Containerized infrastructure
    ⮚	Application-centric management
    ⮚	Auto-scalable infrastructure
[Back to Top](#top)


**Containers**

Let's revisit the different ways of deploying applications we talked about—**locally, On-prem, and in the cloud.**
Imagine a friend, like another developer, wants to work with your code. They'd need to get their own "copy" of it.
They'd go to a platform like GitHub and download your project files. Then, they'd install any extra tools needed to run your code smoothly.
But sometimes, their computer might have different settings that make it hard for your code to work right.
That's where containers come in handy. They wrap up your code with all the settings and tools it needs to run, no matter where it's put.
**Containers are like pre-packaged sets of tools and code. You just plug them in, and they start working without any fuss. |OR| Containers are predefined configurations and dependencies, along with the code files that make it possible for the code to run seamlessly.**
And that's where Kubernetes steps in. It helps manage these containers, making sure they have enough resources and spreading out the work evenly.


## Kubernetes Cluster Architecture

![kubernestes-arch](https://github.com/saifulislam88/kubernetes/assets/68442870/e47edbad-e743-493b-a0d8-a9a1f4561b3a)


**There are two main components in K8s**. So a Kubernetes cluster consists of **two types of nodes (minions)**:

      1. A Master node that coordinates the cluster.
      2. Nodes (called workers) where the application runs.

**Kubernetes follows a client-server architecture**. A Kubernetes cluster consists of at least **one Master Node ** (multi-master for high availability) and multiple Worker nodes. 
The master is responsible  for exposing the application program interface (API), scheduling the deployments and managing the overall cluster. 

The **Master Node** consists of various components including
 
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



[Back to Top](#top)

## K8s Components Brief (Master & Worker)

  **1.Kube-APISERVER**

         ⮚ Acts as the front-end for the Kubernetes control plane.
         ⮚ Handles API requests and provides access to the cluster's state.
  
  **2.ETCD**

         ⮚ A consistent and highly-available key-value store.
         ⮚ Stores all cluster data and configuration information.

  **3.Kube-Controller-Manager**

         ⮚ Runs various controllers to regulate the state of the cluster.
         ⮚ Ensures the cluster's current state matches the desired state.

  **4.Kube-Scheduler**

         ⮚ Assigns tasks (pods) to worker nodes based on resource availability and constraints.
         ⮚ Ensures efficient resource utilization.

 **5.CoreDNS**

         ⮚ Provides DNS resolution for Kubernetes services.
         ⮚ Allows pods to communicate with each other using service names.

 **6.Kubelet** (Both Master and Worker)

         ⮚  An agent that runs on each node  & Ensures containers are running in pods as expected.

 **7.Kube-Proxy** (Both Master and Worker)

        ⮚ Maintains network rules on nodes & Enables communication between different Kubernetes services.

 **8.Container Runtime (Docker,Podman,Containerd,CRI-O)** (Both Master and Worker).

        ⮚  Software responsible for running containers & Supports containerized application execution.

[Back to Top](#top)



## Kubernetes Native Objects

### Part 01
Here is a short explanation with real-world examples 👇

- 𝗣𝗼𝗱: Deployment Unit - Running a single-instance, e.g., Nginx web server

- 𝗦𝗲𝗿𝘃𝗶𝗰𝗲: Networking - Exposing a set of pods to other pods within the cluster. e.g., Exposing a set of Redis server pods.

- 𝗩𝗼𝗹𝘂𝗺𝗲: Storage - Storing database files for a MySQL server running in a pod.

- 𝗡𝗮𝗺𝗲𝘀𝗽𝗮𝗰𝗲: Workload Isolation - Segregating apps/teams/projects in a dedicated/shared cluster. e.g., Different namespaces for apps or stages like development, testing, and production.

- 𝗥𝗲𝗽𝗹𝗶𝗰𝗮𝗦𝗲𝘁: Replication - Running five replicas of a web server application. e.g. Nginx server with multiple replicas for load balancing.

- 𝗗𝗲𝗽𝗹𝗼𝘆𝗺𝗲𝗻𝘁: Management - Uses Replicaset + Rolling out a new version of a web server application. e.g. Upgrading from Nginx version 1.19 to 1.20.

- 𝗦𝘁𝗮𝘁𝗲𝗳𝘂𝗹𝗦𝗲𝘁: State Management - Scaling a distributed database like Cassandra. e.g. Cassandra cluster with multiple nodes.

- 𝗗𝗮𝗲𝗺𝗼𝗻𝗦𝗲𝘁: Node Operation - Running a log collection daemon on every node. e.g. Fluentd or Filebeat for log collection.

- 𝗝𝗼𝗯: Task Execution - Processing a large compute job using several workers. e.g. A data processing job using Apache Spark.

- 𝗖𝗿𝗼𝗻𝗝𝗼𝗯: Scheduled Tasks - Running a batch job at specific times. e.g. A nightly backup job.

- 𝗦𝗲𝗰𝗿𝗲𝘁: Sensitive Data - Storing the password for a database. e.g. MongoDB password.

- 𝗖𝗼𝗻𝗳𝗶𝗴𝗠𝗮𝗽: Configuration - Storing the configuration for a web server. e.g. Nginx configuration file.

- 𝗜𝗻𝗴𝗿𝗲𝘀𝘀: External Access - Exposing a web application to the internet. e.g. A web application running on Apache.

- 𝗡𝗲𝘁𝘄𝗼𝗿𝗸𝗣𝗼𝗹𝗶𝗰𝘆: Network Rules - Defining how pods communicate with each other. e.g. Allowing traffic from a specific IP range or bewtween namespace ot pods with specific labels.

- 𝗛𝗼𝗿𝗶𝘇𝗼𝗻𝘁𝗮𝗹 𝗣𝗼𝗱 𝗔𝘂𝘁𝗼𝘀𝗰𝗮𝗹𝗲𝗿 (𝗛𝗣𝗔): Scalability - Automatically scaling a web server application based on CPU usage. e.g. An auto-scaling Nginx deployment.

- 𝗣𝗲𝗿𝘀𝗶𝘀𝘁𝗲𝗻𝘁𝗩𝗼𝗹𝘂𝗺𝗲 (𝗣𝗩): Persistent Storage - Providing a file system for a MongoDB database pod.

- 𝗣𝗲𝗿𝘀𝗶𝘀𝘁𝗲𝗻𝘁𝗩𝗼𝗹𝘂𝗺𝗲𝗖𝗹𝗮𝗶𝗺 (𝗣𝗩𝗖): Storage Request - Requesting storage for a PostgreSQL database pod.

- 𝗘𝗻𝗱𝗽𝗼𝗶𝗻𝘁𝘀𝗹𝗶𝗰𝗲𝘀: Network endpoint Points - Storing IP addresses for a service. e.g., IP addresses of pods running an Nginx server.

- 𝗦𝗲𝗿𝘃𝗶𝗰𝗲𝗔𝗰𝗰𝗼𝘂𝗻𝘁: Authentication - Giving a pod the necessary permissions to interact with the Kubernetes API.

- 𝗥𝗼𝗹𝗲/𝗖𝗹𝘂𝘀𝘁𝗲𝗿𝗥𝗼𝗹𝗲: Authorization - Granting read access to pods in a specific namespace.

![image](https://github.com/saifulislam88/kubernetes/assets/68442870/334db1f0-3240-4e5e-b058-a2d908a1cb9e)


[Back to Top](#top)

### Part 02

Here is a short explanation with real-world examples 👇

- 𝗥𝗼𝗹𝗲𝘀: Namespace Scopped Permissions, E.g., a developer/service account has a role that allows updates to pods in the development namespace.

- 𝗖𝗹𝘂𝘀𝘁𝗲𝗿𝗥𝗼𝗹𝗲𝘀: Clusterwide-permissions. E.g., a cluster administrator/service account has a ClusterRole that allows node maintenance tasks such as rebooting or upgrading nodes.

- 𝗣𝗿𝗶𝗼𝗿𝗶𝘁𝘆𝗖𝗹𝗮𝘀𝘀: Pod Prioritization. E.g., a payment processing Pod has a PriorityClass that ensures it gets scheduled before less critical workloads.

- 𝗣𝗼𝗱𝗗𝗶𝘀𝗿𝘂𝗽𝘁𝗶𝗼𝗻𝗕𝘂𝗱𝗴𝗲𝘁𝘀: Availability - A PodDisruptionBudget ensures at least three are always running for a service with five replicas. E.g., an API service with a PodDisruptionBudget to maintain availability during voluntary disruptions.

- 𝗟𝗶𝗺𝗶𝘁𝗥𝗮𝗻𝗴𝗲𝘀: Resource Constraints - Eg: A policy set to restrict each container in a specific namespace to a maximum of 2 CPU cores and 2GB of memory.

- 𝗥𝗲𝘀𝗼𝘂𝗿𝗰𝗲𝗤𝘂𝗼𝘁𝗮: Usage Limits. E.g., A ResourceQuota that limits the "dev" namespace to a maximum of 10 GB of memory and 4 vCPUs.

- 𝗦𝘁𝗼𝗿𝗮𝗴𝗲𝗖𝗹𝗮𝘀𝘀𝗲𝘀: Storage-provisioning - Eg: Configuring fast-storage volumes with SSDs for databases and slow-storage volumes with HDDs for log processing. When creating PVs, storage class has to be mentioned if required.

- 𝗥𝘂𝗻𝘁𝗶𝗺𝗲𝗖𝗹𝗮𝘀𝘀: Contianer Runtime-specification: Eg: A Pod specification that requires a gVisor as the container runtime.

- 𝗖𝘂𝘀𝘁𝗼𝗺𝗥𝗲𝘀𝗼𝘂𝗿𝗰𝗲𝗗𝗲𝗳𝗶𝗻𝗶𝘁𝗶𝗼𝗻𝘀: Extendability. E.g., a CRD to manage a new type of resource, such as a MongoDB instance, managed by a MongoDB Operator.

![image](https://github.com/saifulislam88/kubernetes/assets/68442870/42b7edd0-dd4c-4356-b1f6-50ec946d9107)

[Back to Top](#top)

### **The following table shows the important native Kubernetes object types organized in categories.**


| Category                     | Kubernetes Objects                                                                                   |
|------------------------------|------------------------------------------------------------------------------------------------------|
| **Workload**                 | 1. Pods                                                                                              |
|                              | 2. ReplicaSets                                                                                       |
|                              | 3. Deployments                                                                                       |
|                              | 4. StatefulSets                                                                                      |
|                              | 5. DaemonSets                                                                                        |
|                              | 6. Jobs                                                                                              |
|                              | 7. CronJobs                                                                                          |
|                              | 8. Horizontal Pod Autoscaler                                                                         |
|                              | 9. Vertical Pod Autoscaler                                                                           |
| **Service & Networking**     | 1. Services                                                                                          |
|                              | 2. Ingress                                                                                           |
|                              | 3. IngressClasses                                                                                    |
|                              | 4. Network Policies                                                                                  |
|                              | 5. Endpoints                                                                                         |
|                              | 6. EndpointSlices                                                                                    |
| **Storage**                  | 1. PersistentVolumes                                                                                 |
|                              | 2. PersistentVolumeClaims                                                                            |
|                              | 3. StorageClasses                                                                                    |
|**Configuration & Management**| 1. ConfigMaps                                                                                       |
|                              | 2. Namespaces                                                                                        |
|                              | 3. ResourceQuotas                                                                                    |
|                              | 4. LimitRanges                                                                                       |
|                              | 5. Pod Disruption Budgets (PDB)                                                                      |
|                              | 6. Pod Priority and Preemption                                                                       |
| **Security**                 | 1. Secrets                                                                                           |
|                              | 2. ServiceAccounts (sa)                                                                              |
|                              | 3. Roles                                                                                            |
|                              | 4. RoleBindings                                                                                      |
|                              | 5. ClusterRoles                                                                                      |
|                              | 6. ClusterRoleBindings                                                                               |
| **Metadata**                 | 1. Labels and Selectors                                                                              |
|                              | 2. Annotations                                                                                       |
|                              | 3. Finalizers                                                                                        |


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












