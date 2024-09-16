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
- [Kubernetes Native Objects](#kubernetes-native-objects)
  - [Kubernetes Workload Objects](#Kubernetes-Workload-Objects)
      - [Pods](#pods)
      - [ReplicaSets](#ReplicaSets)
      - [Deployments](#Deployments)
      - [StatefulSets](#StatefulSets)
      - [DaemonSets](#DaemonSets)
      - [Jobs]()
      - [CronJobs]()
      - [Horizontal Pod Autoscaler[
      - [Vertical Pod Autoscaler[
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
- [Kubernetes Scheduling](#Kubernetes-Scheduling)
  - [Manual Scheduling](#Manual-Scheduling)
    - [nodeName](#nodename)
    - [nodeSelector](#nodeSelector--label)
  - [Automatic Scheduling](#Automatic-Scheduling)
    - [Taints and Tolerations](#taints-and-tolerations)
      - [Taints](#Taints)
      - [Tolerations](#Tolerations)
      - [Taints and Tolerations Use Cases](#taints-and-tolerations-use-cases)
      - [The Three Taints Effects Implementation and Tolerations Managing](#the-three-taints-effects-implementation-and-tolerations-managing)
         - [1.NoSchedule](#1-noschedule)
         - [2.PreferNoSchedule](#2-prefernoschedule)
         - [3.NoExecute](#3-noexecute)
      - [Some important built in taints-based-on-three-effects](#some-important-built-in-taints-based-on-three-effects)
         - [Node Role Taints](#1-node-role-taints)
         - [Node Condition Taints](#2-node-condition-taints)
         - [Node Lifecycle Taints](#3-node-lifecycle-taints)
         - [Importance-of-built-in-taints](#importance-of-built-in-taints---these-built-in-taints-ensure)
      - [Node Affinity/Anti-Affinity and Pod Affinity/Anti-Affinity](#node-affinityanti-affinity-and-pod-affinityanti-affinity)
         - [Node Affinity](#Node-Affinity)
         - [Node Anti-Affinity](#node-anti-affinity)
         - [POD Affinity](#pod-affinity)
         - [POD Anti-Affinity](#pod-anti-affinity)
  - [Kubernetes Configuration & Management Objects]
      - ConfigMaps
      - Namespaces
      - ResourceQuotas
      - LimitRanges
      - Pod Disruption Budgets (PDB)
      - Pod Priority and Preemption
  - [Kubernetes Storage Management Objects]
      - Persistent Volumes (PV) & Persistent Volume Claims (PVC)
      - [Storage Classes/Type](#types-of-volumes)
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

## Deploy Highly Available Kubernetes Cluster using [Kubeadm](https://github.com/saifulislam88/kubernetes/blob/main/B.k8s-cluster-setup-on-premises/A.Kubernetes-cluster-setup-on-Ubuntu-22.04.md)

## [Kubernetes Native Objects](#Kubernetes-Native-Objects)

Kubernetes objects are persistent entities in the Kubernetes system that represent the state of your cluster. These objects are the fundamental components that describe what resources are present, what applications are running, and how they behave. They are essential because they allow you to define the desired state of your applications and infrastructure in a declarative manner. By managing Kubernetes objects, you can control everything from workloads to networking, storage, and security within your cluster.

Kubernetes objects are the core building blocks that define and control the state of your Kubernetes cluster. Here are crucial Kubernetes Native Head Objects:


- [Kubernetes Workload Objects](#kubernetes-workload-objects)
- [Kubernetes Service & Networking Objects](#kubernetes-service--networking-objects)
- [Kubernetes Scheduling](#Kubernetes-Scheduling)
- [Kubernetes Configuration & Management Objects](#Kubernetes-Configuration--Management-Objects)
- [Kubernetes Storage Management Objects](#Kubernetes-Storage-Management-Objects)
- [Kubernetes Security Objects](#Kubernetes-Security-Objects)
- [Kubernetes Metadata Objects](#Kubernetes-Metadata-Objects)



In this article, we will explore Kubernetes objects together. Assuming you have created your Kubernetes cluster using one of the provided methods such as
 
[Minikube](https://minikube.sigs.k8s.io/docs/start/?arch=%2Flinux%2Fx86-64%2Fstable%2Fbinary+download),\
[Kind](https://kind.sigs.k8s.io/docs/user/quick-start/#installation), or\
[Kubeadm](https://github.com/saifulislam88/kubernetes/blob/main/B.k8s-cluster-setup-on-premises/A.Kubernetes-cluster-setup-on-Ubuntu-22.04.md)

**So now we will dive into the world of Kubernetes objects.**

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

Pods are the smallest deployable units of Kubernetes Cluster that you can create and manage. Kubernetes pods have a defined lifecycle.

**Pods in a Kubernetes cluster are used in two main ways:**
   **1**. Pods that run a `single container`.\
   **2**. Pods that run `multiple containers` that need to work together.

So We can create pods in Kubernetes Cluster in two method which already we know. Lets see example:
  
**1.📌Creating a pod using `Imperative way`**\
**`kubectl run nginx-01 --image=nginx`**

**2.📌Creating a pod using `Declarative way`**\
**`kubectl create ns ops`**\
**`kubectl run nginx-01 --image=nginx --namespace=ops -o yaml --dry-run=client > nginx-01.yaml`**

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

**Get List of Containers in a specific Pod**     
`kubectl get pod <pod-name> -o jsonpath='{.spec.containers[*].name}' | tr ' ' '\n'; echo`  
<br>


## 🚀ReplicaSets

**A ReplicaSet is used for making sure that the designated number of pods is up and running.** It is convenient to use when we are supposed to run multiple pods at a given time. ReplicaSet requires labels to understand which pods to run, a number of replicas that are supposed to run at a given time, and a template of the pod that it needs to create.

**`kubectl create rs nginx --image=nginx --replicas=3 --dry-run=client -o yaml > nginx-replicaset.yaml`**


vim nginx-replicaset.yaml`


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

A Deployment provides declarative updates for Pods and ReplicaSets.

You describe a desired state in a Deployment, and the Deployment Controller changes the actual state to the desired state at a controlled rate. You can define Deployments to create new ReplicaSets, or to remove existing Deployments and adopt all their resources with new Deployments.

**Table of Contents**
- [Creating a Deployment](#creating-a-deployment)
- [Updating nginx-deployment deployment](#updating-nginx-deployment-deployment)
- [Rolling Back a Deploymen](#rolling-back-a-deploymen)
- [Checking Rollout History of a Deployment](#checking-rollout-history-of-a-deployment)
- [Rolling Back to a Previous Revision](#rolling-back-to-a-previous-revision)
- [Scaling a Deployment](#scaling-a-deployment)
- [Deployment Strategy](#deployment-strategy)
  - [Recreate Deployment](#recreate-deployment)
  - [Rolling Update Deployment](#rolling-update-deployment)


## Creating a Deployment
To create a Deployment imperatively (using imperative commands) for nginx.\
`kubectl create deployment nginx-deployment --image=nginx:1.14.2 --replicas=3`

Optionally, you can generate the Deployment manifest.\
`kubectl run nginx-deployment --image=nginx:1.14.2 --replicas=3 --dry-run=client -o yaml >> nginx-deployment.yaml`


## Updating nginx-deployment deployment
Let's update the nginx Pods to use the nginx:1.16.1 image instead of the nginx:1.14.2 image.\
`kubectl set image deployment/nginx-deployment nginx=nginx:1.16.1`

Alternatively, you can edit the Deployment and change.\
`kubectl edit deployment/nginx-deployment`

To see the rollout status, run.\
`kubectl rollout status deployment/nginx-deployment`


## Rolling Back a Deploymen
Suppose that you made a typo while updating the Deployment, by putting the image name as nginx:1.161 instead of nginx:1.16.1.\
`kubectl set image deployment/nginx-deployment nginx=nginx:1.161`

The rollout gets stuck. You can verify it by checking the rollout status.\
`kubectl rollout status deployment/nginx-deployment`

Describe Deployment.\
`kubectl describe deployment nginx-deployment`


## Checking Rollout History of a Deployment

Use --record while creating the deployment so that it will start recroding the deployment.\
`kubectl create -f deploy.yaml --record=true`

First, check the revisions of this Deployment.\
`kubectl rollout history deployment/nginx-deployment`

To see the details of each revision, run.\
`kubectl rollout history deployment/nginx-deployment --revision=2`

How to check k8s deploy history.\
`kubectl rollout history deployment/erpbe-pod  --revision=1  -o yaml`

## Rolling Back to a Previous Revision 

Now you've decided to undo the current rollout and rollback to the previous revision.\
`kubectl rollout undo deployment/nginx-deployment`

Alternatively, you can rollback to a specific revision by specifying it with --to-revision.\
`kubectl rollout undo deployment/nginx-deployment --to-revision=2`

Check if the rollback was successful and the Deployment is running as expected, run.\
`kubectl get deployment nginx-deployment`

Get the description of the Deployment.\
`kubectl describe deployment nginx-deployment`


## Scaling a Deployment
You can scale a Deployment by using the following command.
`kubectl scale deployment/nginx-deployment --replicas=10`


Assuming horizontal Pod autoscaling is enabled in your cluster, you can set up an autoscaler for your Deployment and choose the minimum and maximum number of Pods you want to run based on the CPU utilization of your existing Pods.\
`kubectl autoscale deployment/nginx-deployment --min=10 --max=15 --cpu-percent=80`

## Deployment Strategy

### Recreate Deployment
All existing Pods are killed before new ones are created when .spec.strategy.type==Recreate.

### Rolling Update Deployment
The Deployment updates Pods in a rolling update fashion when .spec.strategy.type==RollingUpdate. You can specify maxUnavailable and maxSurge to control the rolling update process.

`maxUnavailable` is an optional field that specifies the maximum number of Pods that can be unavailable during the update process.

`maxSurge` is a parameter used in Kubernetes Deployments to control the number of additional Pods that can be created above the desired number of Pods during a rolling update.


When the maxUnavailable and maxSurge parameters are not explicitly specified in a Deployment manifest, Kubernetes uses default values for these parameters.

**By default**

maxUnavailable is set to 25% of the total number of Pods.
maxSurge is set to 25% of the total number of Pods.
These defaults ensure a balanced rolling update process where at least 75% of the desired Pods are available (ensuring high availability) and allows for up to a 25% increase in the total number of Pods during the update process.

If you don't specify maxUnavailable and maxSurge, Kubernetes will apply these default values to your Deployment. However, it's always good practice to explicitly define these parameters to match your specific requirements and ensure predictable behavior during updates.





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

[**1.ClusterIP**](#1-clusteripdefault)\
[**2.NodePort**](#2-nodeport)\
[**3.LoadBalancer**](#2-loadbalancer)\
[**4.ExternalName**](#4-externalname)\
[**5.Headless**]()


### [1. ClusterIP(Default)]()

A ClusterIP is a virtual IP address assigned to a Kubernetes service, which is used for internal cluster communication.\
**ClusterIP is the default Kubernetes service. Your service will be exposed on a ClusterIP unless you manually define another type or type: `ClusterIP`**. **ClusterIP services are managed by the `Kubernetes API` Server and `kube-proxy`.**

If we deploy Kubernetes Cluster uisng `kubeadm`, ClusterIP default IP is **`10.96.0.0/12`**. If needed to change ClusterIP IP Block, this could be in a file such as `/etc/kubernetes/manifests/kube-apiserver.yaml` (if using kubeadm) or in a systemd service file.

- Internal communication within the cluster.
- Only accessible within the cluster (internal).
- It provides a stable, internal IP address for accessing the service within the cluster.
- Other services and pods within the same cluster can access this service.
- A backend service accessed only by other services within the cluster.


**Now create a service for pod to pod communication then we will deploy pod using `pod` | `deployment` | `statefulset` | `daemonset` objects.**

`vim my-app-svc.yaml`
  ```sh
      apiVersion: v1
      kind: Service
      metadata:
        name: my-service
      spec:
        selector:
          app: my-app
        ports:
          - protocol: TCP
            port: 80                     # Internal ClusterIP Port
            targetPort: 80               # Apps listen port on Pod/Container
   ```
`kubectl apply -f my-app-svc.yaml`\
`kubectl get svc` or `kubectl get service`


**Here deploying pods workload using `Deployment` objects**

`vim my-app-dep.yaml`

```sh

apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: my-app
  name: my-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: my-app
    spec:
      containers:
      - image: nginx
        name: nginx
```
`kubectl apply -f my-app-dep.yaml`\
`kubectl get pod`\
`curl http://ClusterIP`

![image](https://github.com/saifulislam88/kubernetes/assets/68442870/d5c7a15c-ba8a-4705-a5c2-425fa9b392ea)

We also can deploy pods & service using impertative command

`kubectl create deployment test --image=nginx`\
`kubectl expose deployment test --port=80 --target-port=80`\
`kubectl get svc test`

------------------------------------------------------------------------------------------------------------------------------------------------------------------

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

[Here is details](#kubernetes-resources)


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### [Ingress Controller](#ingressresource)




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

### MetalLB | BareMetal LB
https://www.adaltas.com/en/2022/09/08/kubernetes-metallb-nginx/



--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## 🚀Kubernetes Scheduling
**The Kubernetes scheduler is responsible for selecting the best node for a pod based on available resources, constraints, and preferences.** This feature is also used to prevent pods from being scheduled on the master node, ensuring the master node remains free from taking on workloads.** So it aims to schedule the pod to a correct and available node. While the scheduler decides which node a pod should run on (it only decides and does not put the pod on that node), **the kubelet on the assigned node retrieves the pod definition from the API and starts the pod by creating the necessary resources and containers.** The scheduler evaluates the resource requirements of each pod (such as CPU and memory) and **considers constraint rules like** **`taints`, `tolerations`, `labels`, and `node affinity`** to determine the best node for the pod. 
**It chooses the optimal node based on Kubernetes’ scheduling principles and rules.**

- [Manual Scheduling](#Manual-Scheduling)
   - [nodeName](#nodename)
   - [nodeSelector](#nodeSelector--label)
- [Automatic Scheduling](#Automatic-Scheduling)
   - [Taints and Tolerations](#taints-and-tolerations)
      - [Taints](#Taints)
      - [Tolerations](#Tolerations)
      - [Taints and Tolerations Use Cases](#taints-and-tolerations-use-cases)
      - [The Three Taints Effects Implementation and Tolerations Managing](#the-three-taints-effects-implementation-and-tolerations-managing)
         - [1.NoSchedule](#1-noschedule)
         - [2.PreferNoSchedule](#2-prefernoschedule)
         - [3.NoExecute](#3-noexecute)
      - [Some important built in taints-based-on-three-effects](#some-important-built-in-taints-based-on-three-effects)
         - [Node Role Taints](#1-node-role-taints)
         - [Node Condition Taints](#2-node-condition-taints)
         - [Node Lifecycle Taints](#3-node-lifecycle-taints)
         - [Importance-of-built-in-taints](#importance-of-built-in-taints---these-built-in-taints-ensure)
      - [Node Affinity/Anti-Affinity and Pod Affinity/Anti-Affinity](#node-affinityanti-affinity-and-pod-affinityanti-affinity)
         - [Node Affinity](#Node-Affinity)
         - [Node Anti-Affinity](#node-anti-affinity)
         - [POD Affinity](#pod-affinity)
         - [POD Anti-Affinity](#pod-anti-affinity)


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### 🚀Manual Scheduling
```````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
If a node has a **taint** and you try to manually schedule a pod on that node without adding the corresponding **toleration** to the pod, the pod will not be scheduled successfully.
Manual scheduling does not override taints. You still need to ensure the pod has the necessary tolerations if the node has taints. **Node affinity** rules are not strictly enforced during manual scheduling. If you manually schedule a pod to a node, Kubernetes will place the pod on that node even if it does not meet the node affinity rules specified in the pod spec.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### 🔥nodeName

We can manually schedule our pods on the whichever node we want. Let us have a look at all how it really happens. Every POD has a field called **`nodeName`** that by default is not set and kube-scheduler sets it on its own. So if one needs to manually schedule a pod, then they just need to set the **`nodeName**` **property in the pod definition file under the spec section.**

**Note:** Above method only works when pod is still not created. If the pod is created and already running, then this method won’t work.


For instance, let’s create our beloved nginx pod once again by assigning a node name this time.\
**`kubectl run manual-scheduling-nodeName-pod --image=nginx -o yaml --dry-run=client > manual-scheduling-nodeName-pod.yaml`**\
**`vim manual-schedule-pod.yaml`**
```sh
apiVersion: v1
kind: Pod
metadata:
  name: manual-scheduling-nodeName-pod
spec:      
  containers:
  - name: nginx          
    image: nginx
  nodeName: node-02    # Specify the exact node name here
```
**`kubectl apply -f manual-scheduling-nodeName-pod.yaml`**\
**`kubectl get pods -o wide`**

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### 🔥nodeSelector | label

`nodeSelector` is that the simplest recommendation for hard scheduling a pod on a specific `node using node label`. If you want to run your pods on a specific set of nodes, use `nodeSelector` to ensure that happens. You can define the `nodeSelector` field as a set of key-value pairs in `PodSpec`

- **🌟Display Labels of a Node**\
`kubectl get node kb8-worker-1 --show-labels | awk '{print $NF}' | sed 's/,/\n/g' | sed 's/^/Labels:         /'`
- **🌟Label a Node** | `kubectl label nodes <node-name> <key>=<value>`\
`kubectl label nodes node-01 disktype=ssd`
- **🌟Get Nodes with Specific Labels** | `kubectl get nodes -l <key>=<value>`\
`kubectl get nodes -l disktype=ssd`   
- **🌟Get Detailed Information about a Node**\
`kubectl describe node kb8-worker-1`
- **🌟Remove a Label from a Node**\
`kubectl label nodes node-01 disktype=ssd-`
- **🌟Pod scheduling using `nodeSelector`**\
**`kubectl run manual-scheduling-nodeSelector-pod --image=nginx -o yaml --dry-run=client > manual-scheduling-nodeSelector-pod.yaml`**

**`vim manual-scheduling-nodeSelector-pod`**
```sh
apiVersion: v1
kind: Pod
metadata:
  name: manual-scheduling-nodeSelector-pod
  labels:
    env: prod
spec:
  containers:
  - name: nginx
    image: nginx
    imagePullPolicy: IfNotPresent
  nodeSelector:
    disktype: ssd  # Specify the exact node label here for nodeSelector
```
**`kubectl apply -f manual-scheduling-nodeSelector-pod.yaml`**\
**`kubectl get pods -o wide`**


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## 🚀Automatic Scheduling

### 🔥Taints and Tolerations
"Taints and Tolerations", the main goal of this feature was to prevent unwanted pods from being scheduled on some particular nodes. Kubernetes also used this feature to prevent pods from being scheduled on the master node and to ensure the master node was free from taking on workloads. Taints are generally applied on nodes to prevent unwanted scheduling, tolerations are applied on pods to allow them to be scheduled on nodes that have taints

### 🔥Taints
**Taints** are applied to nodes to indicate that certain pods should avoid or be evicted from those nodes unless the pods have the matching **tolerations.**

The kubectl taint command with the required taint allows us to add taints to nodes. The general syntax for the command is:\
**`kubectl taint nodes <node name> <taint key>=<taint value>:<taint effect>`**

So when a taint to be applied, it consists of a **`key`**,**`value`**, and an **`effect`**

**Key:** A label that identifies the taint (e.g., **special-node**).\
**Value:** Additional information or context (e.g., **backend**).\
**Effect:** Specifies the action (e.g., **`NoSchedule`**, **`PreferNoSchedule`**, or **`NoExecute`**).

**`Key`**, **`Value`**, and **`Effect`**: These three elements define the characteristic and behavior of a **taint**. The **key and value** are arbitrary strings that you assign, **while the effect determines what happens to pods that do not tolerate the taint:**

### 🔥Tolerations
A toleration is essentially the counter to a taint, allowing a pod to “ignore” taints applied to a node. A toleration is defined in the pod specification and must match the key, value, and effect of the taint it intends to tolerate.

**🎯A toleration has three main components:**

- **Key:** Identifies the taint the toleration refers to.
- **Operator:** Defines the relationship between the key and value; common operators are ✅**`Equal`** and ✅**`Exists`**.
- **Value:** The value associated with the key (used with Equal operator).
- **Effect:** Specifies the taint effect to tolerate (**`NoSchedule`**, **`PreferNoSchedule`**, **`NoExecute`**).


**🎯Tolerations are specified in PodSpec in the following formats depending on the operator.**

**🧩Equal Operator**
```sh
tolerations:
- key: "<taint key>"
  operator: "Equal"
  value: "<taint value>"
  effect: "<taint effect>"
```
**🧩Exists Operator**
```sh
tolerations:
- key: "<taint key>"
  operator: "Exists"
  effect: "<taint effect>"
```
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### 🔥Taints and Tolerations Use Cases

- **Specifying nodes with special hardware :** Often, pod workloads must run on nodes with specialized hardware such as non-x86 processors, optimized memory/storage, or resources like GPUs.
- **Creating dedicated nodes**
- **Reserving Nodes for System Daemons**
- **Isolating Faulty Nodes**
- **Node Decommissioning or Maintenance**
- **Ensuring High Availability**
- **Preventing Resource Starvation**

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### 🔥The three taints effects implementation and tolerations managing

- 🌟**Viewing Taints on Nodes**\
`kubectl describe node worker-ndoe1`

- 🌟**Removing a Taint from a Node**\
**`kubectl taint nodes <node-name> <key>:<effect>-`**
`kubectl taint nodes node1 dedicated=database:NoSchedule-`

- 🌟**To remove all taints**\
`kubectl patch node <node-name> -p '{"spec":{"taints":[]}}'`

- 🌟**To see which nodes have taints:**\
`kubectl get nodes -o jsonpath='{.items[*].metadata.name}{"\n"}{.items[*].spec.taints}'`

- 🌟**Find already tainted by the Kubernetes default installation**\
`kubectl get nodes -o=custom-columns=NodeName:.metadata.name,TaintKey:.spec.taints[*].key,TaintValue:.spec.taints[*].value,TaintEffect:.spec.taints[*].effect`

- 🌟**Drain the Node: To safely evict pods from the node (e.g., for node shutdown), you might follow up with**\
`kubectl drain worker-node-2 --ignore-daemonsets --delete-emptydir-data`

- 🌟**Marks worker-node-2 as unschedulable to prevent new pods from being assigned, useful for maintenance, updates, or troubleshooting while keeping existing pods running.**\
`kubectl cordon worker-node-2`

- 🌟**This will make worker-node-2 schedulable again, ready to accept new pods.**\
`kubectl uncordon worker-node-2`

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### 🔥1. NoSchedule
The pod will not get scheduled to the node without a matching toleration for the tainted nodes.

- 📌**Adding a Taint to a Node**\
`kubectl taint nodes worker-node1 dedicated=backend:NoSchedule`\
`kubectl taint nodes worker-node2 env=prod:NoSchedule`
`kubectl taint nodes worker-node3 gpu=true:NoSchedule`


📌**Adding Tolerations to Pods**| `NoSchedule` Effect ** 

🧩**A. Equal Operator**\
`vim toleration-NoSchedule-equal-pod`
```sh
apiVersion: v1
kind: Pod
metadata:
  name: toleration-NoSchedule-equal-pod
spec:
  containers:
  - name: nginx
    image: nginx
  tolerations:
  - key: "dedicated"
    operator: "Equal"
    value: "backend"
    effect: "NoSchedule"
```
`kubectl apply -f toleration-NoSchedule-equal-pod.yaml`


🧩**B. Exists Operator**\
`vim toleration-NoSchedule-exists-pod`
```sh
apiVersion: v1
kind: Pod
metadata:
  name: toleration-NoSchedule-exists-pod
spec:
  containers:
  - name: nginx
    image: nginx
tolerations:
- key: "env"
  operator: "Exists"
  effect: "NoSchedule"
```
`kubectl apply -f toleration-NoSchedule-exists-pod.yaml`
`kubectl get pod -o wide`

![image](https://github.com/user-attachments/assets/f8c0cf5e-ab0d-4f58-904b-fff0e998dc70)


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### 🔥2. PreferNoSchedule
This softer version of `NoSchedule` attempts to avoid placing non-tolerant pods on the node but does not strictly enforce it, allowing for scheduling flexibility under constrained resources.

The `PreferNoSchedule` taint is a soft rule, meaning it prefers not to schedule general workloads on these nodes but does not strictly prevent it. The scheduler uses this flexibility to make the best use of available resources based on current demand, availability, and overall cluster health.

In real-world scenarios, general workloads will be scheduled on nodes tainted with PreferNoSchedule when there are specific conditions within the cluster, typically when:\
**1.Resource Exhaustion on Other Nodes**\
**2.High Availability and Redundancy**\
**3.Node Maintenance or Downtime**\
**4.Cluster Autoscaling Delays**\
**4.Soft Reservation for Specific Workloads**

- 📌**Adding a `Taint` to a Node**\
`kubectl taint nodes worker-node-1 special-purpose=true:NoSchedule`\
`kubectl taint nodes worker-node-1 redundant=true:PreferNoSchedule`\
`kubectl taint nodes worker-node-3 temporary-use=true:PreferNoSchedule`\
`kubectl taint nodes worker-node-4 reserved-for-special=true:PreferNoSchedule`

📌**Adding `Tolerations` to Pods**| `PreferNoSchedule` Effect ** 

**🧩Resource Exhaustion on Other Nodes**
```sh
apiVersion: v1
kind: Pod
metadata:
  name: general-workload-pod
  labels:
    app: general-app
spec:
  containers:
    - name: general-app
      image: nginx
      ports:
        - containerPort: 80
```
`kubectl apply -f general-workload-pod.yaml`


**🧩High Availability and Redundancy**
```sh
apiVersion: apps/v1
kind: Deployment
metadata:
  name: high-availability-app
spec:
  replicas: 5
  selector:
    matchLabels:
      app: ha-app
  template:
    metadata:
      labels:
        app: ha-app
    spec:
      containers:
        - name: ha-app
          image: nginx
          ports:
            - containerPort: 80
```
`kubectl apply -f high-availability-app.yaml`

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### 🔥3. NoExecute
This will immediately evict all(running,stop,others) if the pods don’t have tolerations for the tainted nodes.It's crucial for maintaining node conditions like dedicated hardware usage or regulatory compliance.

📌**Adding `Tolerations` to Pods**| `NoExecute` Effect ** 
`kubectl taint nodes node1 dedicated=database:NoExecute`\
`kubectl taint nodes node2 maintenance=true:NoExecute`


📌**Adding Tolerations to Pods**| `NoExecute` Effect ** 

🧩**A. Equal Operator**\
`vim toleration-NoExecute-equal-pod`
```sh
apiVersion: v1
kind: Pod
metadata:
  name: toleration-NoExecute-equal-pod
spec:
  containers:
  - name: nginx
    image: nginx
  tolerations:
  - key: "dedicated"
    operator: "Equal"
    value: "database"
    effect: "NoExecute"
```
`kubectl apply -f toleration-NoExecute-equal-pod.yaml`


🧩**B. Exists Operator**\
`vim toleration-NoExecute-exists-pod`
```sh
apiVersion: v1
kind: Pod
metadata:
  name: toleration-NoExecute-exists-pod
spec:
  containers:
  - name: nginx
    image: nginx
tolerations:
- key: "maintenance"
  operator: "Exists"
  effect: "NoExecute"
```
`kubectl apply -f toleration-NoExecute-exists-pod.yaml`
`kubectl get pod -o wide`

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### 🔥Some important Built-in Taints based on three effects

Kubernetes comes with several built-in taints that are automatically applied to nodes based on certain conditions or roles to help manage pod scheduling and node health. These taints play a critical role in maintaining the stability, performance, and availability of the cluster by guiding the scheduler on where pods should or shouldn't run. Here are some key built-in taints and their roles:

#### 🧩1. Node Role Taints

- 📌**Taint:** `node-role.kubernetes.io/control-plane:NoSchedule` or `node-role.kubernetes.io/master:NoSchedule`\
  🌟**Role:** Applied to control plane nodes (formerly known as master nodes) to prevent user workloads from being scheduled on them. This ensures that control plane components have dedicated resources and aren't disrupted by other workloads.

- 📌**Taint:** `node-role.kubernetes.io/control-plane:NoExecute` or `node-role.kubernetes.io/master:NoExecute`\
  🌟**Role:** Similar to `NoSchedule`, but also evicts any non-tolerant pods already running on the control plane nodes.

#### 🧩2. Node Condition Taints

These taints are automatically added by the kubelet or node controller based on the health of the node:

📌**Taint:** `node.kubernetes.io/not-ready:NoExecute`\
🌟**Role:** Indicates that the node is not ready (e.g., due to network partition, disk pressure). Pods without a matching toleration will be evicted from the node.

📌**Taint:** `node.kubernetes.io/unreachable:NoExecute`\
🌟**Role:** Indicates that the node is unreachable from the API server (e.g., network failure). Similar to `not-ready`, it evicts non-tolerant pods.

📌**Taint:** `node.kubernetes.io/memory-pressure:NoSchedule`\
🌟**Role:** Applied when a node is under memory pressure. Prevents scheduling new pods that do not have a toleration for this condition.

📌**Taint:** `node.kubernetes.io/disk-pressure:NoSchedule`\
🌟**Role:** Applied when a node is experiencing disk pressure (e.g., low disk space). Prevents new non-tolerant pods from being scheduled on the node.

📌**Taint:** `node.kubernetes.io/unschedulable:NoSchedule`\
🌟**Role:** Applied to nodes marked as unschedulable (e.g., through `kubectl cordon`). This taint prevents any new pods from being scheduled on the node until it is marked as schedulable again.

📌**Taint:** `node.kubernetes.io/network-unavailable:NoSchedule`\
🌟**Role:** Applied when a node's network is unavailable. Prevents pods that do not tolerate this taint from being scheduled on the node.

📌**Taint:** `node.kubernetes.io/pid-pressure:NoSchedule`\
🌟**Role:** Applied when the node is under PID pressure, which means the system is running low on process IDs. This prevents new pods from being scheduled if they do not have a matching toleration.

#### 🧩3. Node Lifecycle Taints

📌**Taint:** `node.kubernetes.io/taint-effect:NoSchedule`\
🌟**Role:** These are used to influence the scheduling based on specific effects or operational considerations, such as retiring a node from the cluster or handling certain lifecycle states.

#### 🧩Importance of Built-In Taints - These built-in taints ensure:

- **Node Health Management:** Nodes in poor health (e.g., unreachable, under memory pressure) do not accept new workloads, and existing non-tolerant workloads are evicted to maintain application stability.
- **Role Separation:** Ensures that control plane nodes are not burdened with user workloads, preserving their capacity for critical cluster management functions.
- **Operational Stability:** Automatically reacts to infrastructure changes (e.g., maintenance, scaling) by controlling where pods are placed or removed based on node conditions.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### 🚀Node Affinity/Anti-Affinity and Pod Affinity/Anti-Affinity

In Kubernetes, `Node Affinity`, `Anti-Affinity`, `Pod Affinity`, and `Anti-Affinity` are **scheduling constraints** that dictate where pods should or shouldn’t be placed in relation to nodes and other pods. These mechanisms help in optimizing resource usage, increasing availability, reducing failure risks, and ensuring proper workload isolation.

#### **📌Key Scheduling Concepts(Re-BrainStroming)**
- **NodeName:** A simple, direct way to schedule a pod onto a specific node by specifying the node’s name.
- **Node Selector:** Used to assign pods to nodes with specific labels. It's a basic form of node selection.
- **Taints and Tolerations:** Taints applied to nodes prevent pods from being scheduled on them unless the pods have a matching toleration.

#### **📌Affinity Types**
- **Hard Affinity** (`requiredDuringSchedulingIgnoredDuringExecution`):the pod will only be scheduled on nodes that meet the affinity rule.
- **Soft Affinity** (`preferredDuringSchedulingIgnoredDuringExecution`): the scheduler prefers to schedule the pod on matching nodes but can still place it on other nodes if necessary.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### 🔥Node Affinity
**`Node Affinity` is a more flexible and expressive version of** **`nodeSelector`**. It allows pods to be scheduled onto specific nodes based on **`labels`** and the conditions defined by the administrator. It is used when workloads require specific types of nodes or hardware.

You must apply node labels first on the node (e.g.,`disktype=ssd`, `region=us-west`, etc.). Then, you can use either nodeSelector or Node Affinity to schedule the pod on the node(s) with the matching label.

#### **📌noSelector Commands** | Before Affinity applying have to need adding labels
`kubectl get nodes -l disktype=ssd`              # Get Nodes with Specific Labels - kubectl get nodes -l <key>=<value>\
`kubectl describe node kb8-worker-1`\            
`kubectl label nodes node-01 disktype=ssd`       # Label a Node - kubectl label nodes <node-name> <key>=<value>\
`kubectl label nodes node-02 zone=bd-west`       # Label a Node - kubectl label nodes <node-name> <key>=<value>\
`kubectl label nodes node-01 disktype=ssd-`      # Remove a Label from a Node - kubectl label nodes -\
`kubectl run manual-scheduling-nodeSelector-pod --image=nginx -o yaml --dry-run=client > manual-scheduling-nodeSelector-pod.yaml`  # A Pod config file with a nodeSelector section

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#### **🔥Why Use Node Affinity if nodeSelector Exists?**
`nodeSelector` provides basic scheduling capabilities, but **`Node Affinity`** offers more **flexibility** and **advanced control** over where pods are scheduled. Here's why `nodeAffinity` is needed despite having `nodeSelector`:

- #### **📌1.Soft Constraints (Preferred Scheduling)**
With nodeSelector, scheduling is a hard constraint—pods will only run on nodes that match the label, otherwise, they won’t run. nodeAffinity allows for soft constraints using preferredDuringSchedulingIgnoredDuringExecution

```sh
apiVersion: v1
kind: Pod
metadata:
  name: affinity-pod-preferred
spec:
  containers:
    - name: nginx
      image: nginx
  affinity:
    nodeAffinity:
      # Soft constraint: Prefer nodes with label zone=us-west
      preferredDuringSchedulingIgnoredDuringExecution:
        - weight: 1
          preference:
            matchExpressions:
              - key: zone
                operator: In
                values:
                  - bd-west

```

- #### **📌2.Advanced Operators and Expressions:**

`nodeSelector` can only perform exact matches with a key-value pair. `nodeAffinity` supports advanced operators like `In`, `NotIn`, `Exists`, and `DoesNotExist` for more complex matching logic.

**Use Case:** You want a pod to be scheduled on nodes that have a disktype that’s either `ssd` or `nvme`, but **Avoid** any node labeled with `disktype=hdd`.

```sh
apiVersion: v1
kind: Pod
metadata:
  name: affinity-pod-required
spec:
  containers:
  - name: nginx
    image: nginx
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: disktype
            operator: In
            values:
            - ssd
            - nvme
          - key: disktype
            operator: NotIn
            values:
            - hdd
```

- #### **📌3.Hard and Soft Constraints Together:**
With **Node Affinity**, you can combine both **hard** and **soft** constraints in a single policy. This allows you to define strict rules that must be followed, along with preferences that can guide Kubernetes to choose certain nodes if available.

**Use Case:** You want to force the pod to run on nodes with `disktype=ssd`, but if possible, prefer nodes in the `us-west` zone.

```sh
apiVersion: v1
kind: Pod
metadata:
  name: affinity-pod-required-
spec:
  containers:
    - name: nginx
      image: nginx
  affinity:
    nodeAffinity:
      # Hard constraint: Only schedule on nodes with label disktype=ssd
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
            - key: disktype
              operator: In
              values:
                - ssd
      # Soft constraint: Prefer nodes with label zone=us-west
      preferredDuringSchedulingIgnoredDuringExecution:
      - weight: 1
        preference:
          matchExpressions:
            - key: zone
              operator: In
              values:
                - us-west
```

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### 🔥Node Anti-Affinity
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### 🔥Pod Affinity
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### 🔥Pod Anti-Affinity











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












