
# Kubernetes Overview

## Table of Contents
- [Kubernetes Definition](#Kubernetes Definition)
- [Kubernetes Cluster Architecture](#Kubernetes Cluster Architecture)


----
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

## Components Brief (Master & Worker)

- **Kube-APISERVER**
  - Acts as the front-end for the Kubernetes control plane.
  - Handles API requests and provides access to the cluster's state.
  
- **ETCD**
  - A consistent and highly-available key-value store.
  - Stores all cluster data and configuration information.

- **Kube-Controller-Manager**
  - Runs various controllers to regulate the state of the cluster.
  - Ensures the cluster's current state matches the desired state.

- **Kube-Scheduler**
  - Assigns tasks (pods) to worker nodes based on resource availability and constraints.
  - Ensures efficient resource utilization.

- **DNS server for Kubernetes services**
  - Provides DNS resolution for Kubernetes services.
  - Allows pods to communicate with each other using service names.

- **Kubelet** (both master and worker).
  - An agent that runs on each node 
  - Ensures containers are running in pods as expected.

- **Kube-Proxy** (both master and worker).
  - Maintains network rules on nodes.
  - Enables communication between different Kubernetes services.

- **Container Runtime (Docker, Podman)** (both master and worker).
  - Software responsible for running containers.
  - Supports containerized application execution.

