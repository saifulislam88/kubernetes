### How to Install, Deploy, and Test on-premises Multi Master Kubernetes (k8s) Cluster with HaProxy on Ubuntu 22.04


- What is Kubernetes Cluster
- [Pre-requisites](https://github.com/saifulislam88/kubernetes/blob/main/B.k8s-cluster-setup-on-premises/A.Kubernetes-cluster-setup-on-Ubuntu-22.04.md#--pre-requisites)
- Configurations Steps
  - Hardware/VM Rediness with OS
  - Setting up Static IPV4 on all nodes
  - Disabling swap & Setting up hostnames
  - Installing Kubernetes components on all nodes
    - Configure modules
    - Configure POD networking 
    - Install containerd (Master & Worker Node)
    - Modify containerd configuration (Master & Worker Node)
    - Install Kubernetes Management Tools (Master & Worker Node)
  - 
  - Configure Kuberctl on Only All Master Nodes

  ### - Pre-requisites

     ##### - Standard


| Component             | VM Requirements         | RAM    | vCPU | Storage |
|-----------------------|-------------------------|--------|------|---------|
| HaProxy               | 1 VM                    | 2GB    | 2    | 20GB    |
| Master/Controller Node| 2 VMs                   | 4GB    | 4    | 50GB    |
| Worker Node           | 1 or more VMs           | 4GB    | 4    | 50GB    |
| Operating System      | Ubuntu 22.04 LTS        | -      | -    | -       |
| Pod Network Block     |                         | -      | -    | -       |


     ##### - Minimal

      - At least 2 nodes.
      - 2 vCPUs.
      - At least 4GB of RAM.
      - At least 20GB of disk space.
      - A reliable internet connection.
