
# Kubernetes Overview



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

![kubernestes-arch](https://github.com/saifulislam88/kubernetes/assets/68442870/ec3c0447-4819-4831-b0af-09a113f47114)



**Kubernetes follows a client-server architecture**. A Kubernetes cluster consists of at least **one master** (multi-master for high availability) and multiple compute nodes. 
The master is responsible  for exposing the application program interface (API), scheduling the deployments and managing the overall cluster. The master server consists of various components including
 
      ⮚ Kube-apiserver 
      ⮚ ETCD 
      ⮚ Kube-controller-manager
      ⮚ Kube-scheduler
      ⮚ DNS server for Kubernetes services.
      ⮚ Kubelet
      ⮚ Kube-proxy
      ⮚ Container Runtime(Docker,Podman)

**Worker Node** components include kubelet and kube-proxy on top of Docker. Each node runs a container runtime, like Docker, and an agent that communicates with the master (kubelet). Nodes (Worker Nodes) expose compute, networking and storage resources to applications. They can be virtual machines (VMs) running in a cloud or bare metal servers running within a data center.
