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

