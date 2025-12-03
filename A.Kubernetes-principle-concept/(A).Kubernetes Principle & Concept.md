# Kubernetes (K8s)

<img src="https://github.com/saifulislam88/docker/assets/68442870/09012688-7671-4f50-8208-dedad3b66353" alt="Signature" width="400"/>

&nbsp;&nbsp;**Copyright** © 2024 Md. Saiful Islam(**mSI**). All Rights Reserved | **Internet & ChatBot**<br>
<br>
<a name="top"></a>
**Table of Contents**
- [Prerequisite Concepts](#Containers)
   - [Containers](#Containers)
   - [Container Orchestration](#Container-Orchestration)
   - [List of Container Orchestration Tools](#list-of-container-orchestration-tools)
- [Kubernetes](#kubernetes)
   - [Definition](#Definition)
   - [Features of Kubernetes | Why Use Kubernetes Among These Options](#features-of-kubernetes--why-use-kubernetes-among-these-options-)
   - [Kubernetes Deployment Platform](#kubernetes-deployment-platform)
   - [Key steps in working with Kubernetes | Cluster Creation to App Management](#key-steps-in-working-with-kubernetes--cluster-creation-to-app-management)
   - [Kubernetes Learning Path](#kubernetes-learning-path)
- [Kubernetes Cluster Architecture](#kubernetes-cluster-architecture)
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
- [Deploy Highly Available Kubernetes Cluster using Kubeadm](#deploy-highly-available-kubernetes-cluster-using-kubeadm)
  - [Kubeadm](https://github.com/saifulislam88/kubernetes/blob/main/B.k8s-cluster-setup-on-premises/A.Kubernetes-cluster-setup-on-Ubuntu-22.04.md)
- Kubernetes Manifest/Yaml
   - Structure of a Kubernetes Manifest
   - Example Structure
   - Detailed Breakdown of the Metadata Section
   - Different types of Manifests
- [Kubernetes Native Objects](#kubernetes-native-objects)

  - [Kubernetes Service & Networking Objects](#kubernetes-service--networking-objects)
    - [Kubernetes Services Type](#kubernetes-services-type)
      - [ClusterIP](#1-clusteripdefault)
      - [NodePort](#2-nodeport)
      - [LoadBalancer](#3-loadbalancer)
      - [Headless]()
      - [ExternalName](#4-externalname)
      - [Endpoint(ep) | Pod IP - is not a service ](#endpointep--pod-ip---is-not-a-service)
      - [Ingress - is not a service](#ingress---is-not-a-service)
    - [Kubernetes Resources](#kubernetes-resources)
      - [Kubernetes Ingress](#ingress)
        - [Ingress Controlller](#ingress-controller)
          - [MetalLB | BareMetal LB](#metallb--baremetal-lb)
    - NetworkPolicy


----
<img src="https://github.com/kubernetes/kubernetes/raw/master/logo/logo.png" width="100">


## **Containers**

Let's visit the different ways of deploying applications we talked below about—[**locally, On-prem, and in the cloud.**](#kubernetes-deployment-platform)\
Imagine a friend, like another developer, wants to work with your code. They'd need to get their own "copy" of it.They'd go to a platform like GitHub and download your project files. Then, they'd install any extra tools needed to run your code smoothly. But sometimes, their computer might have different settings that make it hard for your code to work right. That's where containers come in handy. They wrap up your code with all the settings and tools it needs to run, no matter where it's put.\
**Containers are like pre-packaged sets of tools and code. You just plug them in, and they start working without any fuss. |OR| Containers are predefined configurations and dependencies, along with the code files that make it possible for the code to run seamlessly.**


## Container Orchestration

Container orchestration is the automated process of managing, scheduling, scaling, and maintaining containers in a clustered environment.This helps in efficiently managing complex applications with multiple components and microservices.

### **List of Container Orchestration Tools**
There are several alternatives to Kubernetes for container orchestration, each with its own unique features and use cases.

**1.Kubernetes**\
**2.Docker Swarm**\
**3.Apache Mesos**\
**4.Nomad**\
**5.OpenShift**\
**6.Rancher**\
**7.Amazon EKS (Elastic Kubernetes Service)**\
**8.Google Kubernetes Engine (GKE)**\
**9.Azure Kubernetes Service (AKS)**

# Kubernetes

## Definition

Kubernetes, which translates from **Grek** to **"pilot"** or **"helmsman"**, is an open-source system for automating deployment, scaling, 
and managing containerized applications that which developed in Google lab to manage containerized applications in different 
kind of environments such as physical, virtual, and cloud infrastructure. 

**Kubernetes (K8s) is usually defined as a container orchestration service. Kubernetes is an open source orchestration tool for managing clusters of containers. So Kubernetes is simply a tool to manage containers.**\
**`Now, what are containers`???**


### **Features of Kubernetes** | Why Use Kubernetes Among These Options ?
    
- Scalability and Flexibility
- High Availibilty(HA)
- Auto-scalable infrastructure
- Self-HealingService Discovery and Load Balancing
- Declarative Configuration and Automation
- Rolling Updates and Rollbacks
- Application-centric management
- Extensibility and Ecosystem
- Continues development, integration and deployment
- Multi-Cloud and Hybrid Cloud Support


## Kubernetes Deployment Platform

**1.Local Deployment (Own Computer/Laptop)**

If you're new to web development, you've likely used a local server, such as **'localhost' or '127.0.0.1'**, to view your website or handle requests like GET HTTP. In simple terms, you've worked on your own computer. Setting up your app locally means you can view it on your own computer using a web address like **http://localhost:3000/**. Your app's files are only on your computer. Nobody else can see them.

**2.On-prem (VM or Phisycal Server)**

When you use on-prem (short for on-premises), you're putting your application on a physical server. This means people from outside your company can access your app. But if lots of people try to use it at once, your server might struggle. To handle more users, you might need to add extra servers. This is called "horizontal scaling."Or" you might need to upgrade your server's power, like adding more memory. That's called "vertical scaling."

**3.Cloud Deployment**
  
In the last two scenarios, when you needed to handle more requests, you had to manually increase your server's capacity or add more servers. However, there's a simpler option called cloud deployment.
With cloud deployment, you place your application on servers owned by another company, such as Amazon Web Services (AWS). These companies handle tasks like making your servers bigger or adding more 
if necessary. Similar to using your own servers, your application is accessible to anyone, not just individuals within your organization.
  
Companies like AWS are commonly referred to as "public cloud vendors." Think of it as renting an apartment in a large building. You have your own space, but there are other tenants sharing the building with you, each with their own separate apartments. In addition to public cloud offerings, these vendors also provide private servers known as VPCs (virtual private clouds). Within a VPC, certain resources are reserved exclusively for your use, 
ensuring they remain readily available whenever you require them. Therefore, you have two primary deployment options: public cloud deployments and private cloud deployments. With this understanding of deployment methods, let's now explore Kubernetes.

## Key steps in working with Kubernetes | Cluster Creation to App Management

- Initialize Your Kubernetes Cluster
- Deploy Your First Application
- Inspect and Interact with Your App
- Expose Your Application to the World
- Scale Your Application
- Update and Manage Application Versions

![image](https://github.com/saifulislam88/kubernetes/assets/68442870/27c2d490-3410-42ce-8a46-28e8de6b661f)

## Kubernetes Learning Path

- Kubernetes Basics - The foundation of Kubernetes knowledge.
- Hosting Applications on Kubernetes - Moving to practical application hosting.
- Focus on One Type of Application - Concentrating on specific types of applications.
- Application Types:
**Stateless Apps:** Simple applications without state.\
**Stateful Apps:** Applications that maintain state, such as databases.\
**Caching Services:** Memory-based caching systems.\
**Queuing Services:** Message queuing systems.\
**Database Clusters:** Stateful systems with specific needs.\
**Storage Solutions:** External storage like NFS.
- Understand Specific Requirements & Design Patterns- Delving into the nuances of each application type.
- Master Observability - Focus on monitoring, logging, and tracing to gain deep insights into your applications and infrastructure.
- Incremental Learning Approach
- Gradually learning each type without feeling overwhelmed.


[Back to Top](#top)


## Kubernetes Cluster Architecture

![kubernestes-arch](https://github.com/saifulislam88/kubernetes/assets/68442870/e47edbad-e743-493b-a0d8-a9a1f4561b3a)

**Kubernetes follows a client-server architecture**. A Kubernetes cluster consists of at least **one Master Node** & **one Worker Node**(Multi-Master & Worker for high availability)

**There are two main components in K8s**. So a Kubernetes cluster consists of **two types of nodes (minions)**:

      1. Master Node that coordinates the cluster.
      2. Worker Node where the application runs.

### Master Node(Control-Plane)

**The master is responsible  for exposing the application program interface (API), scheduling the deployments and managing the overall cluster.** The **Master Node** consists of various components including..

 - Master four Core Components — that's why these are called master/control plane node in Kubernetes
   - [kube-apiserver](#kube-apiserver)
   - [kube-scheduler](#kube-scheduler)
   - [kube-controller-manager](#kube-controller-manager)
   - [etcd](#etcd)
 - Master Pods managing Components — that's why these are called worker/master nodes components in Kubernetes
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

We will talk about building a Kubernetes cluster in the following articles. **In Kubernetes, a master node is identified primarily by the presence of the following components**: `kube-apiserver`, `kube-scheduler` `kube-controller-manager`, `etcd` and **Conversely, a worker node is primarily characterized by the presence of**: `kubelet`, `kube-proxy`, `Container Runtime Interface (CRI)`. **However**, master nodes also include components traditionally associated with worker nodes, such as `kubelet`, `kube-proxy`, and `CRI`. This is because control plane components (`kube-apiserver`, `kube-scheduler`, `kube-controller-manager`, `etcd`) run as [Static Pods]()not daemon on the master node. To manage and maintain these Pods, the master node requires `kubelet`, `kube-proxy`, and `CRI`. **Thus, in practice, a master node performs functions similar to a worker node** by handling containerized workloads and maintaining Pod health, effectively blurring the distinction between master and worker nodes.

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

## Deploy Highly Available Kubernetes Cluster using [Kubeadm](https://github.com/saifulislam88/kubernetes/blob/main/B.k8s-cluster-setup-on-premises/A.Kubernetes-cluster-setup-on-Ubuntu-22.04.md)



















#### Key Differences Between Pod, ReplicaSet, Deployment, StatefulSet, and DaemonSet

| **Aspect**     | **Pod** | **ReplicaSet** | **Deployment** | **StatefulSet** | **DaemonSet** |
|----------------|---------|----------------|----------------|-----------------|---------------|
| **Definition** | The smallest and most basic deployable object in Kubernetes. Represents a single instance of a running process in a cluster. | A controller that ensures a specified number of Pod replicas are running at any given time. | A higher-level controller that provides declarative updates to applications and manages ReplicaSets. | A controller that manages the deployment and scaling of a set of Pods, and provides guarantees about the ordering and uniqueness of these Pods. | A controller that ensures a copy of a Pod is running on all (or some) nodes in the cluster. |
| **Components** | - Can contain one or more containers.<br>- All containers in a Pod share the same network namespace, IP address, and storage. | - Contains a Pod template that defines the Pods to be created.<br>- Manages the lifecycle of these Pods. | - Contains a Pod template and a ReplicaSet template.<br>- Manages the lifecycle of ReplicaSets and their Pods. | - Contains a Pod template.<br>- Provides unique identities to Pods and ensures ordered deployment and scaling. | - Contains a Pod template.<br>- Ensures a copy of the Pod runs on all (or selected) nodes. |
| **Use Case**   | Suitable for running a single instance of an application or a single container. Rarely used directly in production. | Ensures the desired number of Pod replicas are running to provide high availability and load balancing. | Facilitates rolling updates, rollbacks, and versioning of applications. Ideal for managing stateless applications. | Suitable for stateful applications that require stable network identities and persistent storage. | Suitable for running system-level or cluster-wide services such as monitoring or logging agents on every node. |
| **Management** | - Pods are ephemeral; once a Pod is deleted, it cannot be restored.<br>- Pods are managed by higher-level controllers such as ReplicaSets or Deployments. | - Automatically replaces Pods if they are deleted or fail.<br>- Not commonly used directly; typically managed by Deployments. | - Allows for declarative updates to Pods and ReplicaSets.<br>- Automatically manages rollouts and rollbacks, ensuring zero downtime. | - Provides guarantees about the ordering and uniqueness of Pods.<br>- Manages the lifecycle of Pods with persistent identifiers and storage. | - Ensures that a Pod is running on all (or selected) nodes.<br>- Automatically adds Pods to new nodes when they are added to the cluster. |
| **Summary**    | Basic units of work in Kubernetes, representing a single instance of a running process. | Ensures a specified number of Pod replicas are running for high availability and fault tolerance. | Provides declarative updates and lifecycle management for applications, making it easier to handle updates, rollbacks, and scaling. | Manages stateful applications that require unique Pod identities and stable storage. | Ensures a Pod is running on all nodes, typically used for system-level services. |


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

## [Kubernetes Service & Networking Objects](#kubernetes-service--networking-objects)


A service is an abstract mechanism for exposing pods on a network. Kubernetes workloads aren’t network-visible by default. You make containers available to the local or outside world by creating a service. Service resources route traffic into the containers within pods. Kubernetes supports several ways of getting external traffic into your cluster. 

**Why use a Service?**

Suppose you decide to create an HTTP server cluster to manage request coming from thousands of browsers, you create a deployment file where you specify to run an Nginx application in 3 copies on 3 Pods. These Pods are accessible via the node IP. If a Pod on a node goes down and recreated on another node its IP change and the question is: how can I reference that Pod?
To make Pods accessible from external, Kubernetes uses a Service as a level of abstraction. A Service, basically, lives between clients and Pods and when an HTTP request arrives, it forwards the request to the right Pod.

Service get a stable IP address that can use to contact Pods. A client sends a request to the stable IP address, and the request is routed to one of the Pods in the Service.
A Service identifies its member Pods with a selector. For a Pod to be a member of the Service, the Pod must have all of the labels specified in the selector. A label is an arbitrary key/value pair that is attached to an object.

The following Service manifest has a selector that specifies two labels. The selector field says any Pod that has both the app: metrics label and the department: engineering label is a member of this
 
```sh
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
```
## [Kubernetes Services Type](#kubernetes-services-type)





[**5.Headless**]()



------------------------------------------------------------------------------------------------------------------------------------------------------------------


### [Endpoint(ep) | Pod IP - is not a service](#endpointep--pod-ip---is-not-a-service)

**Endpoints are not services;** they are objects that store the actual IP addresses of the pods that match a service selector, used internally by services to direct traffic to the correct pods.

`kubectl get endpoints`\
`kubectl get pods -o wide`\
`kubectl describe endpoints <endpoint-name>`\
`kubectl get endpoints <service-name>`\
`kubectl get endpoints <service-name> -o wide`\
`kubectl get endpoints <service-name> -o yaml`\
`kubectl get endpoints <service-name> -o json`

### [Ingress - is not a service](#ingress---is-not-a-service)

**Ingress is not a service;** it is a resource that manages external access to services, typically HTTP, and can provide `Load balancing`, `SSL termination`, and `Name-based virtual hosting`,`Path-based`,`URL Routing`.

`kubectl apply -f ingress.yaml`\
`kubectl get ingress`\
`kubectl describe ingress <ingress-name>`\
`kubectl delete ingress <ingress-name>`\
`kubectl get pods -n <ingress-namespace> -l app.kubernetes.io/name=ingress-nginx`\
`kubectl logs <ingress-controller-pod> -n <ingress-namespace>`\
`kubectl get svc -n <ingress-namespace>`\
`curl -H "Host: <your-hostname>" http://<ingress-ip>`




