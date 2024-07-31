# Kubernetes (K8s)
<a name="top"></a>
**Table of Contents**
- [Prerequisite Concepts](https://github.com/saifulislam88/kubernetes/blob/main/A.Kubernetes-principle-concept/(A).Kubernetes%20Principle%20%26%20Concept.md#before-we-beginning-kubernetes-lets-cover-some-basic-ideas)
- [Kubernetes Definition](https://github.com/saifulislam88/kubernetes/blob/main/A.Kubernetes-principle-concept/(A).Kubernetes%20Principle%20%26%20Concept.md#kubernetes-definition)
- [Kubernetes Cluster Architecture](https://github.com/saifulislam88/kubernetes/blob/main/A.Kubernetes-principle-concept/(A).Kubernetes%20Principle%20&%20Concept.md#kubernetes-cluster-architecture)
   - [Nodes Component Overview & Roles in a Kubernetes Cluster](#Nodes-Component-Overview--Roles-in-a-Kubernetes-Cluster)
     - [Master Node](#master-nodecontrol-plane)
       - [kube-apiserver](#kube-apiserver)
       - [kube-scheduler](#kube-scheduler)
       - [kube-controller-manager](#kube-controller-manager)
       - [etcd](#etcd)
       - [kubelet](#kubelet)
       - [kube-proxy](#kube-proxy)
       - [container runtime interface(CRI)](#Container-Runtime-InterfaceCRI)
       - [coredns](#coredns)
     - [Worker Node](#worker-nodedata-plane)
       - [kubelet](#kubelet)
       - [kube-proxy](#kube-proxy)
       - [Container Runtime Interface(CRI)](#Container-Runtime-Interface-CRI)
       - [coredns](#coredns)
- [Kubernetes Native Objects]()
  - [Kubernetes Workload Objects]()
      - [Pods](#pods)
      - [ReplicaSets](#ReplicaSets)
      - [Deployments](Deployments)
      - [StatefulSets](StatefulSets)
      - [DaemonSets](DaemonSets)
      - [Jobs]()
      - [CronJobs]()
      - [Horizontal Pod Autoscaler[
      - [Vertical Pod Autoscaler[
  - [Kubernetes Service & Networking Objects](https://github.com/saifulislam88/kubernetes/blob/main/A.Kubernetes-principle-concept/(A).Kubernetes%20Principle%20&%20Concept.md#kubernetes-services-type)
      - [ClusterIP](https://github.com/saifulislam88/kubernetes/blob/main/A.Kubernetes-principle-concept/(A).Kubernetes%20Principle%20&%20Concept.md#1-clusteripdefault)
      - [NodePort](https://github.com/saifulislam88/kubernetes/blob/main/A.Kubernetes-principle-concept/(A).Kubernetes%20Principle%20&%20Concept.md#2-nodeport)
      - [LoadBalancer](https://github.com/saifulislam88/kubernetes/blob/main/A.Kubernetes-principle-concept/(A).Kubernetes%20Principle%20&%20Concept.md#3-loadbalancer)
      - [Headless]
      - [ExternalName](https://github.com/saifulislam88/kubernetes/blob/main/A.Kubernetes-principle-concept/(A).Kubernetes%20Principle%20&%20Concept.md#4-externalname)
    - [Kubernetes Resources](https://github.com/saifulislam88/kubernetes/blob/main/A.Kubernetes-principle-concept/(A).Kubernetes%20Principle%20&%20Concept.md#kubernetes-resources)
      - [Kubernetes Ingress](https://github.com/saifulislam88/kubernetes/blob/main/A.Kubernetes-principle-concept/(A).Kubernetes%20Principle%20&%20Concept.md#ingress)
        - [Ingress Controlller](https://github.com/saifulislam88/kubernetes/blob/main/A.Kubernetes-principle-concept/(A).Kubernetes%20Principle%20&%20Concept.md#ingress-controller)
          - [MetalLB | BareMetal LB](https://github.com/saifulislam88/kubernetes/blob/main/A.Kubernetes-principle-concept/(A).Kubernetes%20Principle%20%26%20Concept.md#metallb--baremetal-lb)
  - [Kubernetes Scheduling]()
       - Manual Scheduling
       - Labeling and Node Selector
       - Node Affinity | Anti-Affinity
       - Taints and Tolerations
       - Resource Management
  - [Kubernetes Configuration & Management Objects]
      - ConfigMaps
      - Namespaces
      - ResourceQuotas
      - LimitRanges
      - Pod Disruption Budgets (PDB)
      - Pod Priority and Preemption
  - [Kubernetes Storage Management Objects]
      - Persistent Volumes (PV) & Persistent Volume Claims (PVC)
      - [Storage Classes/Type](https://github.com/saifulislam88/kubernetes/blob/main/A.Kubernetes-principle-concept/(A).Kubernetes%20Principle%20&%20Concept.md#types-of-volumes)
      - Access Modes for Volumes
  - [Kubernetes Security Objects]
      - Secrets
      - ServiceAccounts (sa)
      - Roles
      - RoleBindings
      - ClusterRoles
      - ClusterRoleBindings
  - [Kubernetes Metadata Objects]

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


  ❖ Features of Kubernetes
    
- Continues development, integration and deployment
- Containerized infrastructure
- Application-centric management
- Auto-scalable infrastructure


![image](https://github.com/saifulislam88/kubernetes/assets/68442870/27c2d490-3410-42ce-8a46-28e8de6b661f)


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

**Kubernetes follows a client-server architecture**. A Kubernetes cluster consists of at least **one Master Node** & **one Worker Node**(Multi-Master & Worker for high availability)

**There are two main components in K8s**. So a Kubernetes cluster consists of **two types of nodes (minions)**:

      1. Master Node that coordinates the cluster.
      2. Worker Node where the application runs.

### Master Node(Control-Plane)

**The master is responsible  for exposing the application program interface (API), scheduling the deployments and managing the overall cluster.** The **Master Node** consists of various components including..
 
   - [kube-apiserver](#kube-apiserver)
   - [kube-scheduler](#kube-scheduler)
   - [kube-controller-manager](#kube-controller-manager)
   - [etcd](#etcd)
   - [kubelet](#kubelet)
   - [kube-proxy](#kube-proxy)
   - [container runtime interface(CRI)](#container-runtime-interfaceCRI)
   - [coredns](#coredns)

### Worker Node(Data-Plane)

**The Worker Nodes where the application runs and expose compute, networking and storage resources to applications.** They can be **virtual machines (VMs)** running in a `Cloud`, `On-Premises VE` or `Bare Metal` servers running within a data center. The **Worker Node** consists of various components including..

   - [kubelet](#kubelet)
   - [kube-proxy](#kube-proxy)
   - [container runtime interface(CRI)](#container-runtime-interfaceCRI)
   - [coredns](#coredns)

[Back to Top](#top)


## Nodes Component Overview & Roles in a Kubernetes Cluster

We will talk about building a Kubernetes cluster in the following articles. **In Kubernetes, a master node is identified primarily by the presence of the following components**: `kube-apiserver`, `kube-scheduler` `kube-controller-manager`, `etcd` and **Conversely, a worker node is primarily characterized by the presence of**: `kubelet`, `kube-proxy`, `Container Runtime Interface (CRI)`. **However**, master nodes also include components traditionally associated with worker nodes, such as `kubelet`, `kube-proxy`, and `CRI`. This is because control plane components (`kube-apiserver`, `kube-scheduler`, `kube-controller-manager`, `etcd`) run as Pods not daemon on the master node. To manage and maintain these Pods, the master node requires `kubelet`, `kube-proxy`, and `CRI`. **Thus, in practice, a master node performs functions similar to a worker node** by handling containerized workloads and maintaining Pod health, effectively blurring the distinction between master and worker nodes.

### kube-apiserver

API server is the central management component of the Kubernetes control plane that receives all REST requests for modifications (to pods, services, replication sets/controllers and others), serving as frontend to the cluster. Also, this is the only component that communicates with the etcd cluster, making sure data is stored in etcd and is in agreement with the service details of the deployed pods.

   - The central control point for the entire cluster.
   - Handles RESTful API requests to perform CRUD operations on resources (pods, services, etc.).
   - The component that exposes the API server.

### kube-scheduler

Scheduler is responsible for tracking utilization of working load on cluster nodes. Scheduler watches when a new Pod is created, this component assigns it to a node for execution based on resource requirements, policies, and ‘affinity’ specifications regarding geolocation and interference with other workloads.

   - Watches newly created Pods and assigns them to a worker node based on resource availability and constraints(like taints, tolerations, labels, and node affinity)
   - Ensures efficient resource utilization.


### kube-controller-manager

  - The component that is responsible for controller processes. 
  - Runs various controllers to regulate the state of the cluster.
  - Ensures the cluster's current state matches the desired state.

Kubernetes runs a group of controllers (`Node Controller`, `Replication Controller`, `Endpoints Controller`, `Namespace Controller`, and `Service Account Controller`) in the background that handle routine tasks in the cluster. Like node-controller which is controlling if nodes are down or like endpoint-controller that creates the endpoints objects.


### etcd

A simple, high availability and distributed key value storage which is used to store the Kubernetes cluster data (such as number of pods, their state, namespace, etc), API objects and service discovery details. 
**It is only accessible from the API server for security reasons.** etcd enables notifications to the cluster about configuration changes with the help of watchers. Notifications are API requests on each etcd cluster node to trigger the update of information in the node’s storage.

 - Key-value store used as Kubernetes' backing store for all cluster data.
 - Stores configuration data, state, and metadata.

   
### kubelet

This component communicates with the control plane. **So Kubelet is an agent application that runs on each node in the cluster.** It takes a set of specifications, PodSpecs, and ensures containers are working as well as listening to new commands from the kube-apiserver(master node).

**Once the scheduler assigns a pod to a node, the kubelet on that node is responsible for**\
 - Primary "node agent" that runs on each node.
 - Downloading the pod's container images.
 - Ensures that containers are running in a pod as expected.
 - Monitoring the health of the pod and its containers.
 - Takes a set of PodSpecs and ensures that the described containers are running and healthy.
 - Reporting the status back to the control plane.




### kube-proxy

 - The `kube-proxy` handles network communications inside or outside of your cluster.
 - Maintains network rules on nodes & Enables communication between different Kubernetes services like pods, services, and the external network.
 - Network proxy that runs on each node.

### container runtime interface(CRI)

- Software responsible for running containers & Supports containerized application execution. **Examples** include `Docker`, `containerd`, and `CRI-O`.
- Interacts with `kubelet` to manage `container lifecycle`.

### coredns

- Provides DNS resolution for Kubernetes services.
- Helps internal communication within the cluster by resolving service names to IP addresses.

[Back to Top](#top)



## Kubernetes Native Objects

In this article, we will explore Kubernetes objects together. Assuming you have created your Kubernetes cluster using one of the provided methods such as [Minikube](https://minikube.sigs.k8s.io/docs/start/?arch=%2Flinux%2Fx86-64%2Fstable%2Fbinary+download), [Kind](https://kind.sigs.k8s.io/docs/user/quick-start/#installation), or [Kubeadm](https://github.com/saifulislam88/kubernetes/blob/main/B.k8s-cluster-setup-on-premises/A.Kubernetes-cluster-setup-on-Ubuntu-22.04.md), we can now dive into the world of Kubernetes objects.


<div style="display: flex; justify-content: space-between;">
  <img src="https://github.com/saifulislam88/kubernetes/assets/68442870/334db1f0-3240-4e5e-b058-a2d908a1cb9e" alt="Image 1" style="width: 48%; height: 600px;">
  <img src="https://github.com/saifulislam88/kubernetes/assets/68442870/42b7edd0-dd4c-4356-b1f6-50ec946d9107" alt="Image 2" style="width: 48%; height: 600px;">
</div>


Kubernetes objects are persistent entities in the Kubernetes system. Kubernetes uses these entities to represent the state of your cluster. Some of the Kubernetes Objects are Pods, Depoyments, Namespaces, StatefulSets, Services, etc.

**There are two ways to create a Kubernetes object via `kubectl`: `Imperative` or `declarative`.**

Let’s see both of them in action by creating a simple nginx pod.

### **Imperative Way**

To run a single pod with nginx image which is called nginx:\
**`kubectl run nginx-01 --image=nginx`** This command will start a pod called `nginx` which uses the image `nginx`.\
Let’s check if it has been created by using:\
**`kubectl get pods`**


### **Declarative Way**

To create the same pod in a declarative way, we need to create a `YAML` file.**The YAML file in Kubernetes for any resource must have 3 key values**: **`apiVersion`, `kind`, `metadata`.** And depending on the resource you might have a **`spec`, `data`,** etc.

**`apiVersion`:** Which version of the Kubernetes API you’re using to create this object\
**`kind:`** What kind of object that you want to create\
**`metadata`:** Data that helps uniquely identify the object, including a name string, UID, and an optional namespace\
**`spec`:** What state that you desire for the object

So the YAML file ( let’s call nginx-02.yaml) for creating the same pod would be like this:

```sh
apiVersion: v1
kind: Pod
metadata:
  name: nginx-02
spec:
  containers:
  - name: nginx          
    image: nginx
```
Pod uses apiVersion v1 ( which is the correct API version for creating a pod), kind is Pod, in the metadata section we define the name of the `pod`, `namespace`, `labels`, etc. And under `spec`, we define the containers inside the pod.

To create this object we can use the **`apply` or `create`** command:\
**`kubectl apply -f nginx-02.yaml`** or **`kubectl create -f nginx-02.yaml`**

Note the difference between **`create`** and **`apply`** commands. **`create`** can only be used for creating a resource from scratch while **`apply`** can be used to create an object from scratch and also update a change to it. The **`-f`** basically means file.


### **Namespaces**

Kubernetes supports multiple virtual clusters backed by the same physical cluster. These virtual clusters are called **`namespaces`**. It is mainly used for Workload Isolation - Segregating apps/teams/projects in a dedicated/shared cluster. e.g., Different namespaces for apps or stages like development, testing, and production.


For checking the existing namespaces:\
**`kubectl get namespaces`** or **`kubectl get ns`**

Let’s start by creating namespaces.\
**`kubectl create namespace namespace1`**   **[Imperative Way]**

Or **[Declarative Way]**

```sh
apiVersion: v1
kind: Namespace
metadata:
  name: namespace2
```
**`kubectl apply -f namespace2.yaml`**

**Here's some suitable command for managing `namesapce` object**

**`kubectl run nginx --image=nginx --namespace=namespace1`**\
**`kubectl get pods`**\
**`kubectl get namespaces`**\
**`kubectl get pods -n namespace1`  or `kubectl get pods --namespace=namespace1`**\
**`kubectl get pods --all-namespaces`**\
**`kubectl get pods --all-namespaces -o wide`**\
**`kubectl get namespace --no-headers | wc -l`**\
**`kubectl config set-context --current --namespace=namespace1`**\
**`kubectl delete namespace namespace1`**



### [Kubernetes Workload Objects]()

**A workload is an application running on Kubernetes.**

## 🚀Pods

Pods are the smallest deployable units of Kubernetes Cluster that you can create and manage. Kubernetes pods have a defined lifecycle.\
   - ### **Pods in a Kubernetes cluster are used in two main ways:**
   **1**. Pods that run a single container.\
   **2**. Pods that run multiple containers that need to work together.

   - ### **Creating a pod using `Imperative way`**
**`kubectl run nginx-01 --image=nginx`**

   - ### **Creating a pod using `Declarative way`**
**`kubectl create ns ops`**\
**`kubectl run nginx-01 --image=nginx --namespace=ops -o yaml --dry-run=client > nginx-01.yaml`**\
**`vim nginx-01.yaml`**
```sh
apiVersion: v1
kind: Pod
metadata:
  name: nginx-01
  namespace: dev
spec:
  containers:
  - name: nginx
    image: nginx
```
**`kubectl apply -f nginx-01.yaml`**\
**`kubectl get pods -n ops`**
`kubectl get pod <pod-name> -o jsonpath='{.spec.containers[*].name}' | tr ' ' '\n'; echo`  [**Get List of Containers in a Pod**]     
  
## 🚀ReplicaSets

**A ReplicaSet is used for making sure that the designated number of pods is up and running.** It is convenient to use when we are supposed to run multiple pods at a given time. ReplicaSet requires labels to understand which pods to run, a number of replicas that are supposed to run at a given time, and a template of the pod that it needs to create.

**`kubectl create rs nginx --image=nginx --replicas=3 --dry-run=client -o yaml > nginx-replicaset.yaml`**

```sh
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: nginx-08
  labels:
    app: nginx
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
        image: nginx
```

Please note that it is not using **apiVersion “v1”** but “**apps/v1**”. We define a label in replica set metadata and use it as a selector under spec. With Replicas ( spec.replicas) we defined the number of replicas that should be up and running. And on the template ( spec.template), we put the information about the pod that we want to be created.

**`kubectl apply -f nginx-replicaset.yaml`**\
**`kubectl get pods`**

Please observe that it takes the name of the replica set and attaches a random value next to it as a pod name ( i.e nginx-cn5wq). Let’s see the replica set in action by forcefully deleting a pod.

**`kubectl delete pod <pod-name>`**\
**`kubectl get pods`**\
**`kubectl get replicasets`**


## 🚀Deployments
## 🚀StatefulSets
## 🚀DaemonSets

#### Key Differences Between Pod, ReplicaSet, Deployment, StatefulSet, and DaemonSet

| **Aspect**     | **Pod** | **ReplicaSet** | **Deployment** | **StatefulSet** | **DaemonSet** |
|----------------|---------|----------------|----------------|-----------------|---------------|
| **Definition** | The smallest and most basic deployable object in Kubernetes. Represents a single instance of a running process in a cluster. | A controller that ensures a specified number of Pod replicas are running at any given time. | A higher-level controller that provides declarative updates to applications and manages ReplicaSets. | A controller that manages the deployment and scaling of a set of Pods, and provides guarantees about the ordering and uniqueness of these Pods. | A controller that ensures a copy of a Pod is running on all (or some) nodes in the cluster. |
| **Components** | - Can contain one or more containers.<br>- All containers in a Pod share the same network namespace, IP address, and storage. | - Contains a Pod template that defines the Pods to be created.<br>- Manages the lifecycle of these Pods. | - Contains a Pod template and a ReplicaSet template.<br>- Manages the lifecycle of ReplicaSets and their Pods. | - Contains a Pod template.<br>- Provides unique identities to Pods and ensures ordered deployment and scaling. | - Contains a Pod template.<br>- Ensures a copy of the Pod runs on all (or selected) nodes. |
| **Use Case**   | Suitable for running a single instance of an application or a single container. Rarely used directly in production. | Ensures the desired number of Pod replicas are running to provide high availability and load balancing. | Facilitates rolling updates, rollbacks, and versioning of applications. Ideal for managing stateless applications. | Suitable for stateful applications that require stable network identities and persistent storage. | Suitable for running system-level or cluster-wide services such as monitoring or logging agents on every node. |
| **Management** | - Pods are ephemeral; once a Pod is deleted, it cannot be restored.<br>- Pods are managed by higher-level controllers such as ReplicaSets or Deployments. | - Automatically replaces Pods if they are deleted or fail.<br>- Not commonly used directly; typically managed by Deployments. | - Allows for declarative updates to Pods and ReplicaSets.<br>- Automatically manages rollouts and rollbacks, ensuring zero downtime. | - Provides guarantees about the ordering and uniqueness of Pods.<br>- Manages the lifecycle of Pods with persistent identifiers and storage. | - Ensures that a Pod is running on all (or selected) nodes.<br>- Automatically adds Pods to new nodes when they are added to the cluster. |
| **Summary**    | Basic units of work in Kubernetes, representing a single instance of a running process. | Ensures a specified number of Pod replicas are running for high availability and fault tolerance. | Provides declarative updates and lifecycle management for applications, making it easier to handle updates, rollbacks, and scaling. | Manages stateful applications that require unique Pod identities and stable storage. | Ensures a Pod is running on all nodes, typically used for system-level services. |


  
  #### - Jobs
  #### - CronJobs
  #### - Horizontal Pod Autoscaler
  #### - Vertical Pod Autoscaler



𝗦𝗲𝗿𝘃𝗶𝗰𝗲

Networking - Exposing a set of pods to other pods within the cluster. e.g., Exposing a set of Redis server pods.

- #### 𝗩𝗼𝗹𝘂𝗺𝗲: Storage - Storing database files for a MySQL server running in a pod.

𝗥𝗲𝗽𝗹𝗶𝗰𝗮𝗦𝗲𝘁: Replication - Running five replicas of a web server application. e.g. Nginx server with multiple replicas for load balancing.

𝗗𝗲𝗽𝗹𝗼𝘆𝗺𝗲𝗻𝘁: Management - Uses Replicaset + Rolling out a new version of a web server application. e.g. Upgrading from Nginx version 1.19 to 1.20.

𝗦𝘁𝗮𝘁𝗲𝗳𝘂𝗹𝗦𝗲𝘁: State Management - Scaling a distributed database like Cassandra. e.g. Cassandra cluster with multiple nodes.

𝗗𝗮𝗲𝗺𝗼𝗻𝗦𝗲𝘁: Node Operation - Running a log collection daemon on every node. e.g. Fluentd or Filebeat for log collection.

𝗝𝗼𝗯: Task Execution - Processing a large compute job using several workers. e.g. A data processing job using Apache Spark.

#### - 𝗖𝗿𝗼𝗻𝗝𝗼𝗯: Scheduled Tasks - Running a batch job at specific times. e.g. A nightly backup job.

#### - 𝗦𝗲𝗰𝗿𝗲𝘁: Sensitive Data - Storing the password for a database. e.g. MongoDB password.

#### - 𝗖𝗼𝗻𝗳𝗶𝗴𝗠𝗮𝗽: Configuration - Storing the configuration for a web server. e.g. Nginx configuration file.

#### - 𝗜𝗻𝗴𝗿𝗲𝘀𝘀: External Access - Exposing a web application to the internet. e.g. A web application running on Apache.

#### - 𝗡𝗲𝘁𝘄𝗼𝗿𝗸𝗣𝗼𝗹𝗶𝗰𝘆: Network Rules - Defining how pods communicate with each other. e.g. Allowing traffic from a specific IP range or bewtween namespace ot pods with specific labels.

#### - 𝗛𝗼𝗿𝗶𝘇𝗼𝗻𝘁𝗮𝗹 𝗣𝗼𝗱 𝗔𝘂𝘁𝗼𝘀𝗰𝗮𝗹𝗲𝗿 (𝗛𝗣𝗔): Scalability - Automatically scaling a web server application based on CPU usage. e.g. An auto-scaling Nginx deployment.

#### - 𝗣𝗲𝗿𝘀𝗶𝘀𝘁𝗲𝗻𝘁𝗩𝗼𝗹𝘂𝗺𝗲 (𝗣𝗩): Persistent Storage - Providing a file system for a MongoDB database pod.

#### - 𝗣𝗲𝗿𝘀𝗶𝘀𝘁𝗲𝗻𝘁𝗩𝗼𝗹𝘂𝗺𝗲𝗖𝗹𝗮𝗶𝗺 (𝗣𝗩𝗖): Storage Request - Requesting storage for a PostgreSQL database pod.

#### - 𝗘𝗻𝗱𝗽𝗼𝗶𝗻𝘁𝘀𝗹𝗶𝗰𝗲𝘀: Network endpoint Points - Storing IP addresses for a service. e.g., IP addresses of pods running an Nginx server.

#### - 𝗦𝗲𝗿𝘃𝗶𝗰𝗲𝗔𝗰𝗰𝗼𝘂𝗻𝘁: Authentication - Giving a pod the necessary permissions to interact with the Kubernetes API.

#### - 𝗥𝗼𝗹𝗲/𝗖𝗹𝘂𝘀𝘁𝗲𝗿𝗥𝗼𝗹𝗲: Authorization - Granting read access to pods in a specific namespace.

[Back to Top](#top)

#### - 𝗥𝗼𝗹𝗲𝘀: Namespace Scopped Permissions, E.g., a developer/service account has a role that allows updates to pods in the development namespace.

#### - 𝗖𝗹𝘂𝘀𝘁𝗲𝗿𝗥𝗼𝗹𝗲𝘀: Clusterwide-permissions. E.g., a cluster administrator/service account has a ClusterRole that allows node maintenance tasks such as rebooting or upgrading nodes.

#### - 𝗣𝗿𝗶𝗼𝗿𝗶𝘁𝘆𝗖𝗹𝗮𝘀𝘀: Pod Prioritization. E.g., a payment processing Pod has a PriorityClass that ensures it gets scheduled before less critical workloads.

#### - 𝗣𝗼𝗱𝗗𝗶𝘀𝗿𝘂𝗽𝘁𝗶𝗼𝗻𝗕𝘂𝗱𝗴𝗲𝘁𝘀: Availability - A PodDisruptionBudget ensures at least three are always running for a service with five replicas. E.g., an API service with a PodDisruptionBudget to maintain availability during voluntary disruptions.

#### - 𝗟𝗶𝗺𝗶𝘁𝗥𝗮𝗻𝗴𝗲𝘀: Resource Constraints - Eg: A policy set to restrict each container in a specific namespace to a maximum of 2 CPU cores and 2GB of memory.

#### - 𝗥𝗲𝘀𝗼𝘂𝗿𝗰𝗲𝗤𝘂𝗼𝘁𝗮: Usage Limits. E.g., A ResourceQuota that limits the "dev" namespace to a maximum of 10 GB of memory and 4 vCPUs.

#### - 𝗦𝘁𝗼𝗿𝗮𝗴𝗲𝗖𝗹𝗮𝘀𝘀𝗲𝘀: Storage-provisioning - Eg: Configuring fast-storage volumes with SSDs for databases and slow-storage volumes with HDDs for log processing. When creating PVs, storage class has to be mentioned if required.

#### - 𝗥𝘂𝗻𝘁𝗶𝗺𝗲𝗖𝗹𝗮𝘀𝘀: Contianer Runtime-specification: Eg: A Pod specification that requires a gVisor as the container runtime.

#### - 𝗖𝘂𝘀𝘁𝗼𝗺𝗥𝗲𝘀𝗼𝘂𝗿𝗰𝗲𝗗𝗲𝗳𝗶𝗻𝗶𝘁𝗶𝗼𝗻𝘀: Extendability. E.g., a CRD to manage a new type of resource, such as a MongoDB instance, managed by a MongoDB Operator.


[Back to Top](#top)


## [Kubernetes Services Type]((https://github.com/saifulislam88/kubernetes/blob/main/A.Kubernetes-principle-concept/(A).Kubernetes%20Principle%20&%20Concept.md#kubernetes-services-type))

A service is an abstract mechanism for exposing pods on a network. Kubernetes workloads aren’t network-visible by default. You make containers available to the local or outside world by creating a service. Service resources route traffic into the containers within pods. Kubernetes supports several ways of getting external traffic into your cluster. 

**Why use a Service?**

Suppose you decide to create an HTTP server cluster to manage request coming from thousands of browsers, you create a deployment file where you specify to run an Nginx application in 3 copies on 3 Pods. These Pods are accessible via the node IP. If a Pod on a node goes down and recreated on another node its IP change and the question is: how can I reference that Pod?
To make Pods accessible from external, Kubernetes uses a Service as a level of abstraction. A Service, basically, lives between clients and Pods and when an HTTP request arrives, it forwards the request to the right Pod.

Service get a stable IP address that can use to contact Pods. A client sends a request to the stable IP address, and the request is routed to one of the Pods in the Service.
A Service identifies its member Pods with a selector. For a Pod to be a member of the Service, the Pod must have all of the labels specified in the selector. A label is an arbitrary key/value pair that is attached to an object.

The following Service manifest has a selector that specifies two labels. The selector field says any Pod that has both the app: metrics label and the department: engineering label is a member of this
 
  Service.
  apiVersion: v1
  kind: Service
  metadata:
    name: my-service
  spec:
    selector:
      app: metrics
      department: engineering
    ports:
    ...


[**1.ClusterIP,**](https://github.com/saifulislam88/kubernetes/blob/main/A.Kubernetes-principle-concept/(A).Kubernetes%20Principle%20&%20Concept.md#1-clusteripdefault)
 
[**2.NodePort,**](https://github.com/saifulislam88/kubernetes/blob/main/A.Kubernetes-principle-concept/(A).Kubernetes%20Principle%20&%20Concept.md#2-nodeport)

[**3.LoadBalancer,**](https://github.com/saifulislam88/kubernetes/blob/main/A.Kubernetes-principle-concept/(A).Kubernetes%20Principle%20&%20Concept.md#2-loadbalancer)
 
[**4.ExternalName,**](https://github.com/saifulislam88/kubernetes/blob/main/A.Kubernetes-principle-concept/(A).Kubernetes%20Principle%20&%20Concept.md#4-externalname)
 
**5.Headless**


### [1. ClusterIP(Default)](https://github.com/saifulislam88/kubernetes/blob/main/A.Kubernetes-principle-concept/(A).Kubernetes%20Principle%20&%20Concept.md#1-clusteripdefault)

**ClusterIP is the default Kubernetes service. Your service will be exposed on a ClusterIP unless you manually define another type or type: ClusterIP**

- **Usage:** Internal communication within the cluster.
- **Access:** Other services and pods within the same cluster can access this service.
- **Example:** A backend service accessed only by other services within the cluster.

  
      apiVersion: v1
      kind: Service
      metadata:
        name: my-service
      spec:
        selector:
          app: my-app
        ports:
          - protocol: TCP
            port: 80                     [Internal ClusterIP Port]
            targetPort: 80               [Apps listen port on Pod/Container]
      

![image](https://github.com/saifulislam88/kubernetes/assets/68442870/d5c7a15c-ba8a-4705-a5c2-425fa9b392ea)



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


### [4. ExternalName](https://github.com/saifulislam88/kubernetes/blob/main/A.Kubernetes-principle-concept/(A).Kubernetes%20Principle%20&%20Concept.md#4-externalname)

For any pod to access an application outside of the Kubernetes cluster like the external DB server, we use the ExternalName service type. Unlike in the previous examples, instead of an endpoint object, the service will simply redirect to a CNAME of the external server.

```sh
apiVersion: v1
  kind: Service
  metadata:
    name: redis-service
  spec:
    type: ExternalName
    externalName: my.redis-service.example.com
```


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## [Kubernetes Resources](https://github.com/saifulislam88/kubernetes/blob/main/A.Kubernetes-principle-concept/(A).Kubernetes%20Principle%20&%20Concept.md#kubernetes-resources)

Services are five widely used resources that all have a role in routing traffic. Each one lets you expose services with a unique set of features and trade-offs.

**In Kubernetes, everything is accessed through APIs.** To create different types of objects like pods, namespaces, and configmaps, the Kubernetes API server provides API endpoints. These object-specific endpoints are called **API resources or simply resources**. For example, the API endpoint used to create a pod is referred to as a Pod resource. In simpler terms, a resource is a specific API URL used to access an object, and you can interact with these objects using HTTP methods like GET, POST, and DELETE.


### [Ingress](https://github.com/saifulislam88/kubernetes/blob/main/A.Kubernetes-principle-concept/(A).Kubernetes%20Principle%20&%20Concept.md#ingress)
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


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### [Ingress Controller](https://github.com/saifulislam88/kubernetes/blob/main/A.Kubernetes-principle-concept/(A).Kubernetes%20Principle%20&%20Concept.md#ingressresource)




**An Ingress Controller is a software program of Ingress that runs inside your Kubernetes cluster and implements the Ingress API. It reads Ingress objects and takes actions to properly route incoming requests.** Essentially, the Ingress Controller is responsible for making Ingress resources functional. So It acts as an interpreter for Ingress resources, translating the traffic rules defined in the Ingress objects into configurations for your load balancer or edge router.

  
   - **NGINX, Traefik, and HAProxy are common Ingress controllers.**
     
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




### MetalLB | BareMetal LB
https://www.adaltas.com/en/2022/09/08/kubernetes-metallb-nginx/

## Kubernetes Scheduling

**Kubernetes scheduling is the process and key responsible for deciding which pods are assigned to the matched nodes in a cluster. This feature is also used to prevent pods from being scheduled on the master node, ensuring the master node remains free from taking on workloads.** So it aims to schedule the pod to a correct and available node. While the scheduler decides which node a pod should run on (it only decides and does not put the pod on that node), **the kubelet on the assigned node retrieves the pod definition from the API and starts the pod by creating the necessary resources and containers.** The scheduler evaluates the resource requirements of each pod (such as CPU and memory) and **considers constraint rules like** **`taints`, `tolerations`, `labels`, and `node affinity`** to determine the best node for the pod. 
**It chooses the optimal node based on Kubernetes’ scheduling principles and rules.**

- Manual Scheduling
- Labeling
- Node Selector
- Node Affinity | Anti-Affinity
- Taints and Tolerations

### Manual Scheduling
### Labeling
### Node Selector
### Node Affinity | Anti-Affinity
### Taints and Tolerations
### Taints/Toleration and Node Affinity




"Taints and Tolerations", the main goal of this feature was to prevent unwanted pods from being scheduled on some particular nodes. Kubernetes also used this feature to prevent pods from being scheduled on the master node and to ensure the master node was free from taking on workloads. Taints are generally applied on nodes to prevent unwanted scheduling, tolerations are applied on pods to allow them to be scheduled on nodes that have taints




### Resource Management








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












