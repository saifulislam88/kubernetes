## Setup MetalLB for Ingress Controller on an On-Premises Kubernetes Cluster for a Single IP Based Load Balancer


One of the toughest aspects of learning Kubernetes is wrapping your mind around how services and internal containers are exposed to the outside world. There are a number of ways to do this and each has pros and cons, but there are definitely ways that are recommended for production environments. Using a Kubernetes Loadbalancer is one of those. MetalLB is a very popular Kubernetes load balancer that many are using in their Kubernetes environments. Let’s take a look at the Kubernetes install MetalLB load balancer process and see what steps are involved to install the solution and test it out.

This tutorial guides you through the installation of the MetalLB load balancer on- premises Kubernetes cluster. **MetalLB provides a robust solution for LoadBalancer-type services in Kubernetes, offering a single IP address to route external requests to your applications.**

### What is a Kubernetes Loadbalancer?

A Kubernetes LoadBalancer directs traffic from an external load balancer to backend pods. In cloud environments like AWS, Azure, and GCP, the cloud provider handles the load balancing. Kubernetes itself does not have a built-in network load balancer for bare-metal clusters. For bare-metal, options are limited to NodePort and ExternalIPs for exposing services.

### etalLB: What Is It?

MetalLB is an open-source solution that provides network load balancing for bare-metal Kubernetes clusters. **In short,it allows you to create Kubernetes services of type LoadBalancer.** It integrates seamlessly with standard networking environments and is widely used in production with great success. MetalLB offers a straightforward implementation designed to "just work."

![image](https://github.com/saifulislam88/kubernetes/assets/68442870/b4013f92-13eb-4650-bf95-181782a4788b)






### MetalLB requirements

- A Kubernetes cluster, running Kubernetes 1.13.0 or later
- No other network load-balancing functionality enabled
- A cluster network configuration that can coexist with MetalLB
- Some IPv4 addresses for MetalLB to hand out
- When using the BGP operating mode, you will need one or more routers capable of speaking BGP. When using the L2 operating mode, traffic on port 7946 (TCP & UDP, other ports can be configured) must be allowed between nodes, as required by members


### Install MetalLB Loadbalancer

If you’re using kube-proxy in `IPVS` mode, since Kubernetes `v1.14.2` you have to enable strict ARP mode. You can achieve this by editing `kube-proxy` config in current cluster and Set `ARP mode true`. Find out this KubeProxyConfiguratuon block and change only `strictARP: true`

- **Steps 1: Enable strict ARP mode**

kubectl edit configmap -n kube-system kube-proxy
```sh
apiVersion: kubeproxy.config.k8s.io/v1alpha1
kind: KubeProxyConfiguration
mode: "ipvs"
ipvs:
  strictARP: true
```


