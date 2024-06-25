### Setup MetalLB for Ingress Controller on an On-Premises Kubernetes Cluster for a Single IP Based Load Balancer | Layer-2 Mode

![image](https://github.com/saifulislam88/kubernetes/assets/68442870/e4214f01-e365-484c-9a5a-ca5112c88314)

**MetalLB uses standard address discovery and routing protocols to advertise the external IP of a service on rest of your network. MetalLB can be configured to operate in `Layer-2 Mode` or `BGP Mode`.**
One of the toughest aspects of learning Kubernetes is wrapping your mind around how services and internal containers are exposed to the outside world. There are a number of ways to do this and each has pros and cons, but there are definitely ways that are recommended for production environments. Using a Kubernetes Loadbalancer is one of those. MetalLB is a very popular Kubernetes load balancer that many are using in their Kubernetes environments. Let’s take a look at the Kubernetes install MetalLB load balancer process and see what steps are involved to install the solution and test it out.

This tutorial guides you through the installation of the MetalLB load balancer on- premises Kubernetes cluster. **MetalLB provides a robust solution for LoadBalancer-type services in Kubernetes, offering a single IP address to route external requests to your applications.**


- [What is a Kubernetes Loadbalancer](https://github.com/saifulislam88/kubernetes/blob/main/G.k8s-configure-metalLB-on-premises/Setup-MetalLB-for-Nginx-Ingress-Loadbalancer-IP.md#what-is-a-kubernetes-loadbalancer)
- [MetalLB: What Is It](https://github.com/saifulislam88/kubernetes/blob/main/G.k8s-configure-metalLB-on-premises/Setup-MetalLB-for-Nginx-Ingress-Loadbalancer-IP.md#metallb-what-is-it)
- [MetalLB requirements](https://github.com/saifulislam88/kubernetes/blob/main/G.k8s-configure-metalLB-on-premises/Setup-MetalLB-for-Nginx-Ingress-Loadbalancer-IP.md#metallb-requirements)
- [Configuration MetalLB Loadbalancer](https://github.com/saifulislam88/kubernetes/blob/main/G.k8s-configure-metalLB-on-premises/Setup-MetalLB-for-Nginx-Ingress-Loadbalancer-IP.md#configuration-metallb-loadbalancer)
  - Step 1: [Enable strict ARP mode](https://github.com/saifulislam88/kubernetes/blob/main/G.k8s-configure-metalLB-on-premises/Setup-MetalLB-for-Nginx-Ingress-Loadbalancer-IP.md#--step-1-enable-strict-arp-mode)
  - Step 2: [MetalLB installation](https://github.com/saifulislam88/kubernetes/blob/main/G.k8s-configure-metalLB-on-premises/Setup-MetalLB-for-Nginx-Ingress-Loadbalancer-IP.md#--step-2-metallb-installation--metallb-crd--controller-using-the-official-manifest)
  - Step 3: [Create ConfigMap for IPAddressPools](https://github.com/saifulislam88/kubernetes/blob/main/G.k8s-configure-metalLB-on-premises/Setup-MetalLB-for-Nginx-Ingress-Loadbalancer-IP.md#--step-3-create-configmap-for-ipaddresspools)
  - Step 4: [Advertise the IP Address Pool](https://github.com/saifulislam88/kubernetes/blob/main/G.k8s-configure-metalLB-on-premises/Setup-MetalLB-for-Nginx-Ingress-Loadbalancer-IP.md#--step-4-advertise-the-ip-address-pool)

### What is a Kubernetes Loadbalancer?

A Kubernetes LoadBalancer directs traffic from an external load balancer to backend pods. In cloud environments like AWS, Azure, and GCP, the cloud provider handles the load balancing. Kubernetes itself does not have a built-in network load balancer for bare-metal clusters. For bare-metal, options are limited to NodePort and ExternalIPs for exposing services.

### MetalLB: What Is It?

MetalLB is an open-source solution that provides network load balancing for bare-metal Kubernetes clusters. **In short,it allows you to create Kubernetes services of type LoadBalancer.** It integrates seamlessly with standard networking environments and is widely used in production with great success. MetalLB offers a straightforward implementation designed to "just work."

![Pi7_Tool_342668049-b4013f92-13eb-4650-bf95-181782a4788b](https://github.com/saifulislam88/kubernetes/assets/68442870/be85c5e3-0e95-4ab9-af65-9309f41a009b)


### MetalLB requirements

- A Kubernetes cluster, running Kubernetes 1.13.0 or later
- No other network load-balancing functionality enabled
- A cluster network configuration that can coexist with MetalLB
- Some IPv4 addresses for MetalLB to hand out
- When using the BGP operating mode, you will need one or more routers capable of speaking BGP. When using the L2 operating mode, traffic on port 7946 (TCP & UDP, other ports can be configured) must be allowed between nodes, as required by members


### Configuration MetalLB Loadbalancer

If you’re using kube-proxy in `IPVS` mode, since Kubernetes `v1.14.2` you have to enable strict ARP mode. You can achieve this by editing `kube-proxy` config in current cluster and Set `ARP mode true`. Find out this KubeProxyConfiguratuon block and change only `strictARP: true`

#### - **Step 1: Enable strict ARP mode**

kubectl edit configmap -n kube-system kube-proxy
```sh
apiVersion: kubeproxy.config.k8s.io/v1alpha1
kind: KubeProxyConfiguration
mode: "ipvs"
ipvs:
  strictARP: true
```

#### - **Step 2: MetalLB installation** | MetalLB CRD & Controller using the [official](https://metallb.universe.tf/installation/) manifest


Now that you’re ready to install MetalLB, we’ll get right on it. Installing MetalLB is as easy as applying the `latest` manifest file.

```sh
export LATEST_VERSION=$(curl -s https://api.github.com/repos/metallb/metallb/releases/latest | grep \"tag_name\" | cut -d : -f 2,3 | tr -d \" | tr -d , | tr -d " ")
kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/$LATEST_VERSION/config/manifests/metallb-native.yaml
```

This will create a couple of resources in your cluster, in the metallb-system namespace. Some of the most noteworthy resources created by the manifest are the following;
  - A deployment called “controller”; this is the cluster-wide component that’s responsible for allocating IP addresses, configuring the load balancer, dynamically updating configurations and   
    performing health checks.
  - A daemonset called “speaker”; this component is deployed on each node and is responsible for ensuring that external traffic can reach the services within the Kubernetes cluster.
  - A couple of service accounts along with RBAC permissions which are necessary for the components to function.

You can verify the deployment of the components by executing the following command:

![image](https://github.com/saifulislam88/kubernetes/assets/68442870/1bb8db7f-89b3-4d60-bd5c-e6efcfd6d762)

#### - **Step 3: Create ConfigMap for IPAddressPools** 

Next you need to create `ConfigMap`, which includes an IP address range for the load balancer. The pool of IPs must be dedicated to MetalLB's use. You can't reuse for example the Kubernetes node IPs or IPs controlled by other services. You can, however, use private IP addresses from `node(master/worker)` network, for example `192.168.1.180-192.168.1.199`, but then you need to take care of the routing from the external network if you need external access. In this example, we don't need it.

Create a YAML file accordingly, and deploy it: kubectl apply -f metallb-l2-ipadd-pool.yaml

`vim metallb-l2-ipadd-pool.yaml`

```sh
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  name: first-pool
  namespace: metallb-system
spec:
  addresses:
  - 192.168.1.180-192.168.1.199
```
`kubectl apply -f metallb-l2-ipadd-pool.yaml`

#### - **Step 4: Advertise the IP Address Pool**

In the Kubernetes manifest below, I’ve configured an L2Advertisement for my `first-pool` pool which I created in the previous config manifest.

`vim metallb-pool-advertise.yaml`

```sh
apiVersion: metallb.io/v1beta1
kind: L2Advertisement
metadata:
  name: example
  namespace: metallb-system
spec:
  ipAddressPools:
  - first-pool
```
`kubectl apply -f metallb-pool-advertise.yaml`


- **🎉🙌 It is Big Congratulations 🎉🙌**
