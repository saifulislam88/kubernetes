## 🚀Kubernetes Scheduling
**The Kubernetes scheduler is responsible for selecting the best node for a pod based on available resources, constraints, and preferences.** This feature is also used to prevent pods from being scheduled on the master node, ensuring the master node remains free from taking on workloads.** So it aims to schedule the pod to a correct and available node. While the scheduler decides which node a pod should run on (it only decides and does not put the pod on that node), **the kubelet on the assigned node retrieves the pod definition from the API and starts the pod by creating the necessary resources and containers.** The scheduler evaluates the resource requirements of each pod (such as CPU and memory) and **considers constraint rules like** **`taints`, `tolerations`, `labels`, and `node affinity`** to determine the best node for the pod. 
**It chooses the optimal node based on Kubernetes’ scheduling principles and rules.**

**💡Node Selection:** Chooses the best node for each pod based on resources and constraints.\
**💡Resource Management:** Ensures nodes have enough CPU and memory for pods.\
**💡Constraint Handling:** Considers rules like taints and labels for scheduling.\
**💡Master Node Management:** Keeps master nodes free from pods.\
**💡Optimal Scheduling:** Aims to place pods efficiently and effectively.

- [Manual Scheduling](#Manual-Scheduling)
   - [nodeName](#nodename)
   - [nodeSelector](#nodeSelector--label)
- [Automatic Scheduling](#Automatic-Scheduling)
   - [Taints-and Tolerations](#1taints-and-tolerations)
      - [Taints](#1ataints)
       - [To set taints | Useful-commands](#to-set-taints-on-nodes--useful-commands)
      - [Tolerations](#1btolerations)
       - [Taints and Tolerations Use Cases](#to-set-taints-on-nodes--useful-commands)
      - [Example of Tolerations on Taint Nodes](#example-of-tolerations-on-taint-nodes)
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
```                                                                                                                                     ```
If a node has a **taint** and you try to manually schedule a pod on that node without adding the corresponding **toleration** to the pod, the pod will not be scheduled successfully.
Manual scheduling does not override taints. You still need to ensure the pod has the necessary tolerations if the node has taints. **Node affinity** rules are not strictly enforced during manual scheduling. If you manually schedule a pod to a node, Kubernetes will place the pod on that node even if it does not meet the node affinity rules specified in the pod spec.


### 🔥nodeName
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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


### 🔥nodeSelector | label
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
`kubectl label nodes node-01 disktype-`
- **🌟Pod scheduling using `nodeSelector`**\
**`kubectl run manual-scheduling-nodeSelector-pod --image=nginx -o yaml --dry-run=client > manual-scheduling-nodeSelector-pod.yaml`**

**`vim manual-scheduling-nodeSelector-pod`**
```sh
apiVersion: v1
kind: Pod
metadata:
  name: manualScheduling
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

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🚀Automatic Scheduling
```                                                                                                                                     ```
<p align="justify">

**Automatic scheduling** refers to Kubernetes' ability to place pods on nodes based on available `resources` and `scheduling policies` without manual intervention. Kubernetes uses its built-in scheduler to decide where to place pods based on factors such as resource requests, constraints, and other scheduling rules.

  - [Taints-and Tolerations](#1taints-and-tolerations)
      - [Taints](#1ataints)
       - [To set taints | Useful-commands](#to-set-taints-on-nodes--useful-commands)
      - [Tolerations](#1btolerations)
      - [Taints and Tolerations Use Cases](#to-set-taints-on-nodes--useful-commands)
      - [Example of Tolerations on Taint Nodes](#example-of-tolerations-on-taint-nodes)
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

### 🔥1.Taints and Tolerations

🔭"**`Taints and Tolerations`**", the main goal of this feature was to prevent `unwanted pods from being scheduled on some particular nodes`. Kubernetes also used this feature to prevent pods from being scheduled on the master node and to ensure the master node was free from taking on workloads. Taints are generally applied on nodes to prevent unwanted scheduling, tolerations are applied on pods to allow them to be scheduled on nodes that have taints

</p>

### **Features of `Taints & Tolerations`**
   - **Specifying nodes with special hardware**
   - **Creating dedicated nodes**
   - **Reserving Nodes for System Daemons**
   - **Isolating Faulty Nodes**
   - **Node Decommissioning or Maintenance**
   - **Ensuring High Availability**
   - **Preventing Resource Starvation**

![image](https://github.com/user-attachments/assets/f68e2560-58a5-4360-962a-eca63516b069)


### 🔥1.A.Taints
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**Taints** are applied to nodes to indicate that certain pods should avoid or be evicted from those nodes unless the pods have the matching **tolerations.** So when a taint to be applied in a node, each taint consists of three parts **🟢`key`**,**🟢`value`**, and an **🟢`effect`**

- **1.Key:** A label that identifies the taint (e.g., **special-node**).
- **2.Value:** Additional information or context (e.g., **backend**).
- **3.Effect:** There are 3 types of effect in in taints
   - **1.[`NoSchedule`](#1-noschedule)**: The pod will not get scheduled to the node without a matching `toleration` for the tainted nodes.\
&nbsp;&nbsp;&nbsp;&nbsp; **`kubectl taint node worker-node1 dedicated=backend:NoSchedule`**
   - **2.[`PreferNoSchedule`](#2-prefernoschedule)**: This softer version of NoSchedule attempts to avoid placing non-tolerant pods on the node but does not strictly enforce it.\
&nbsp;&nbsp;&nbsp;&nbsp; **`kubectl taint node worker-node2 backup=true:PreferNoSchedule`**
   - **3.[`NoExecute`](#3-noexecute)**: Evicts existing pods that do not tolerate the taint.\
     &nbsp;&nbsp;&nbsp;&nbsp; **`kubectl taint node worker-node3 maintenance=database:NoExecute`**

**`Key`**, **`Value`**, and **`Effect`**: These three elements define the characteristic and behavior of a **taint**. The **key and value** are arbitrary strings that represent your node’s attributes or goals, **while the effect determines the action taken on pods that do not tolerate the taint**

#### 🔴`To set taints on nodes` | `Useful Commands`
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
- 🌟**Viewing Taints on Nodes**\
`kubectl describe node worker-ndoe

- 🌟**To see which nodes have taints:**\
`kubectl get nodes -o jsonpath='{.items[*].metadata.name}{"\n"}{.items[*].spec.taints}'`

- 🌟**Find already tainted by the Kubernetes default installation**\
`kubectl get nodes -o=custom-columns=NodeName:.metadata.name,TaintKey:.spec.taints[*].key,TaintValue:.spec.taints[*].value,TaintEffect:.spec.taints[*].effect`

- 🌟**To add taints to a node**\
`kubectl taint nodes <node name> <taint key>=<taint value>:<taint effect>`

- 🌟**Removing a Taint from a Node** | `kubectl taint nodes <node-name> <key>:<effect>-`\
`kubectl taint nodes node1 dedicated=database:NoSchedule-`

- 🌟**To remove all taints**\
`kubectl patch node <node-name> -p '{"spec":{"taints":[]}}'`

- 🌟**Drain the Node: To safely evict pods from the node (e.g., for node shutdown), you might follow up with**\
`kubectl drain worker-node-2 --ignore-daemonsets --delete-emptydir-data`

- 🌟**Marks worker-node-2 as unschedulable to prevent new pods from being assigned, useful for maintenance, updates, or troubleshooting while keeping existing pods running.**\
`kubectl cordon worker-node-2`

- 🌟**This will make worker-node-2 schedulable again, ready to accept new pods.**\
`kubectl uncordon worker-node-2`


### 🔥1.B.Tolerations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
A toleration is essentially the counter to a taint, allowing a pod to “ignore” taints applied to a node. A toleration is defined in the pod specification and must match the key, value, and effect of the taint it intends to tolerate.

**🔴Tolerations has 4 main components:**

- **1.Key:** Identifies the taint the toleration refers to.
- **2.Operator:** Defines the relationship between the key and value; common operators are ✅**`Equal`** and ✅**`Exists`**.
   - **🧩Equal Operator** : Equal Operator (==): Matches a specific key-value pair. It's used when you want to tolerate a taint that has both a specific key and value.
```sh
tolerations:
- key: "<taint key>"
  operator: "Equal"
  value: "<taint value>"
  effect: "<taint effect>"
```
   - **🧩Exists Operator** : Matches any taint key regardless of the value. It's used when you want to tolerate a taint based only on its key, without checking the value.
```sh
tolerations:
- key: "<taint key>"
  operator: "Exists"
  effect: "<taint effect>"
```
- **3.Value:** The value associated with the key (used with Equal operator).
- **4.Effect:** Specifies the taint effect to tolerate (**`NoSchedule`**, **`PreferNoSchedule`**, **`NoExecute`**).


## 🚀Example of Tolerations on Taint Nodes

### 🔥1. NoSchedule
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**The pod will not get scheduled to the node without a matching toleration for the tainted nodes.**

- 📌**Adding a Taint to a Node**\
`kubectl taint nodes worker-node1 dedicated=backend:NoSchedule`

- 🟢**Adding Tolerations**| `NoSchedule` Effect ** | 🧩`Equal` Operator

```sh
vim toleration-noschedule-equal-pod.yaml
```
```sh
apiVersion: v1
kind: Pod
metadata:
  name: toleration-noschedule-equal-pod
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
```sh
kubectl apply -f toleration-noschedule-equal-pod.yaml
kubectl get pod -o wide
```

- 🟢**Adding Tolerations**| `NoSchedule` Effect | 🧩`Exists` Operator

```sh
vim toleration-noschedule-exists-pod.yaml
```
```sh
apiVersion: v1
kind: Pod
metadata:
  name: toleration-noschedule-exists-pod
spec:
  containers:
  - name: nginx
    image: nginx
tolerations:
- key: "env"
  operator: "Exists"
  effect: "NoSchedule"
```
```sh
kubectl apply -f toleration-noschedule-exists-pod.yaml
kubectl get pod -o wide
```

![image](https://github.com/user-attachments/assets/f8c0cf5e-ab0d-4f58-904b-fff0e998dc70)


### 🔥2. PreferNoSchedule
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**This softer version of `NoSchedule` attempts to avoid placing non-tolerant pods on the node but does not strictly enforce it, allowing for scheduling flexibility under constrained resources.**

The `PreferNoSchedule` taint is a soft rule, meaning it prefers not to schedule general workloads on these nodes but does not strictly prevent it. The scheduler uses this flexibility to make the best use of available resources based on current demand, availability, and overall cluster health. In real-world scenarios, general workloads will be scheduled on nodes tainted with `PreferNoSchedule` when there are specific conditions within the cluster, typically when

**1.Resource Exhaustion on Other Nodes**\
**2.High Availability and Redundancy**\
**3.Node Maintenance or Downtime**\
**4.Cluster Autoscaling Delays**\
**4.Soft Reservation for Specific Workloads**

- 📌**Adding a `Taint` to a Node**\
`kubectl taint nodes worker-node-1 dedicated=backend:NoSchedule`\
`kubectl taint nodes worker-node-2 backup=true:PreferNoSchedule`\


- 🟢**Without Adding `Tolerations` & `Operators`** | `PreferNoSchedule` Effect 

```sh
vim without-adding-tolerations-operators-general-workload-pod.yaml
```
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
```sh
kubectl apply -f without-adding-tolerations-operators-general-workload-pod.yaml
kubectl get pod -o wide
```

- 🟢**Adding Tolerations**| `PreferNoSchedule` Effect | 🧩`Equal` Operator

```sh
vim toleration-prefernoschedule-equal-pod.yaml
```
```sh
apiVersion: v1
kind: Pod
metadata:
  name: toleration-prefernoschedule-equal-pod
spec:
  containers:
  - name: nginx
    image: nginx
  tolerations:
  - key: "backup"
    operator: "Equal"
    value: "true"
    effect: "PreferNoSchedule"
```
```sh
kubectl apply -f toleration-prefernoschedule-equal-pod.yaml
kubectl get pod -o wide
```

- 🟢**Adding Tolerations**| `PreferNoSchedule` Effect | 🧩`Exists` Operator

```sh
vim toleration-prefernoschedule-exists-pod.yaml
```
```sh
apiVersion: v1
kind: Pod
metadata:
  name: toleration-prefernoschedule-exists-pod
spec:
  containers:
  - name: nginx
    image: nginx
tolerations:
- key: "backup"
  operator: "Exists"
  effect: "PreferNoSchedule"
```
```sh
kubectl apply -f toleration-prefernoschedule-exists-pod.yaml
kubectl get pod -o wide
```


### 🔥3. NoExecute
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
This will immediately evict all(running,stop,others) if the pods don’t have tolerations for the tainted nodes.It's crucial for maintaining node conditions like dedicated hardware usage or regulatory compliance.

- 📌**Adding a `Taint` to a Node**\
 `kubectl taint nodes node2 maintenance=database:NoExecute`


- 🟢**Adding Tolerations**| `NoExecute` Effect ** | 🧩`Equal` Operator

```sh
vim toleration-noexecute-equal-pod.yaml
```
```sh
apiVersion: v1
kind: Pod
metadata:
  name: toleration-noexecute-equal-pod
spec:
  containers:
  - name: nginx
    image: nginx
  tolerations:
  - key: "maintenance"
    operator: "Equal"
    value: "database"
    effect: "NoExecute"
```
```sh
kubectl apply -f toleration-noexecute-equal-pod.yaml
kubectl get pod -o wide
```


- 🟢**Adding Tolerations**| `NoExecute` Effect ** | 🧩`Exists` Operator

```sh
vim toleration-NoExecute-exists-pod.yaml
```
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
```sh
kubectl apply -f toleration-noexecute-exists-pod.yaml
kubectl get pod -o wide
```

### 🔥Some important Built-in Taints based on three effects
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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



### 🚀Node Affinity/Anti-Affinity and Pod Affinity/Anti-Affinity
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
In Kubernetes, `Node Affinity`, `Node Anti-Affinity`, `Pod Affinity`, and `pod Anti-Affinity` are **scheduling constraints** that dictate where pods should or shouldn’t be placed in relation to nodes and other pods. These mechanisms help in **optimizing** `resource usage`, `increasing availability`, `reducing failure risks`, and `ensuring proper workload isolation`.

#### **📌K8s Scheduling key Concepts(Re-BrainStroming)**
- **NodeName:** A simple, direct way to schedule a pod onto a specific node by specifying the node’s name.
- **Node Selector:** Used to assign pods to nodes with specific labels. It's a basic form of node selection.
- **Taints and Tolerations:** Taints applied to nodes prevent pods from being scheduled on them unless the pods have a matching toleration.

#### **📌Affinityand Anti-Affinity Types**
- **Hard Affinity** (`requiredDuringSchedulingIgnoredDuringExecution`): The pod will only be scheduled on nodes that meet the affinity rule.
- **Soft Affinity** (`preferredDuringSchedulingIgnoredDuringExecution`): The scheduler prefers to schedule the pod on matching nodes but can still place it on other nodes if necessary.


### 🔥Node Affinity
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**`Node Affinity` is a more flexible and expressive version of** **`nodeSelector`**. It allows pods to be scheduled onto specific nodes based on **`labels`** and the conditions defined by the administrator. It is used when workloads require specific types of nodes or hardware.\
You must apply node `labels` first on the node (e.g.,`disktype=ssd`, `region=hdd`, etc.). Then, you can use either `nodeSelector` or `Node Affinity` to schedule the pod on the node(s) with the matching label.

**`nodeSelector`** can only perform exact matches with a key-value pair. `Node Affinity` supports advanced operators like `In`, `NotIn`, `Exists`, and `DoesNotExist` for more complex matching logic.


#### **Q❓Why use Node Affinity if `nodeSelector` already exists?**

`nodeSelector` provides basic scheduling capabilities, but **`Node Affinity`** offers more **flexibility** and **advanced control** over where pods are scheduled. Here's why `nodeAffinity` is needed despite having `nodeSelector`:


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### 📌Node Affinity | Prerequisite
Before we start, we must need to `labeling` your nodes to use `Node Affinity` or `nodeSelector`

- **🌟Display Exiting Labels of a Node**\
```sh
kubectl get node <🔥node_name> --show-labels | awk '{print $NF}' | sed 's/,/\n/g' | sed 's/^/Labels:         /'
```
- **🟢Labeling Nodes ** | `kubectl label nodes <node-name> <key>=<value>`
```sh
kubectl label nodes <🔥node_name_1> disktype=ssd
```
```sh
kubectl label nodes <🔥node_name_2> disktype=hdd
```
- **🔴Remove a Label from a Node**
```sh
kubectl label nodes <🔥node_name> disktype-
```
- **🌟Find Nodes Name using Label** | `kubectl get nodes -l <key>=<value>`
```sh
kubectl get nodes -l disktype=ssd
```
- **🌟Get Detailed Information about a Node**
```sh
kubectl describe node <🔥node_name>
```

 #### 📌Example:`1` | `Hard` Node-Affinity | In and NotIn Operators

This is an example of`required node affinity` (**hard constraint**) where the pod must be scheduled on nodes that match the given labels:
```sh
vim hard-affinity-pod-in-notin.yaml
```
```sh
apiVersion: v1
kind: Pod
metadata:
  name: hard-affinity-pod-in-notin
spec:
  containers:
  - name: nginx
    image: nginx
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:  # Hard affinity (required)
        nodeSelectorTerms:
        - matchExpressions:
          - key: disktype
            operator: In
            values:
            - ssd  # Only schedule on nodes with label disktype=ssd
          - key: region
            operator: NotIn
            values:
            - hdd  # Do not schedule on nodes in hdd
```
```sh
kubectl apply -f hard-affinity-pod-in-notin.yaml
```

**In this example:**\
Pods will only be scheduled on nodes with the label **disktype=ssd**.\
Pods will **not** be scheduled on nodes labeled **region=hdd**.\






- #### **📌3.Hard and Soft Constraints Together:** | In and In
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
With **Node Affinity**, you can combine both **hard** and **soft** constraints in a single policy. This allows you to define strict rules that must be followed, along with preferences that can guide Kubernetes to choose certain nodes if available.

**Use Case:** You want to force the pod to run on nodes with `disktype=ssd`, but if possible, prefer nodes in the `hdd` disktype.

```sh
apiVersion: v1
kind: Pod
metadata:
  name: storage-preferred-pod
spec:
  containers:
  - name: my-container
    image: nginx
  affinity:
    nodeAffinity:
      preferredDuringSchedulingIgnoredDuringExecution:
      - weight: 1
        preference:
          matchExpressions:
          - key: disktype
            operator: In
            values:
            - ssd   # Prefer SSD nodes
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: disktype
            operator: In
            values:
            - ssd
            - hdd  # If SSD is not available, allow scheduling on HDD
```






- #### **📌2.Soft Affinity (Preferred Scheduling)** - 
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**Node Affinity** allows for soft constraints or Affinity using `preferredDuringSchedulingIgnoredDuringExecution`

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
      # Soft constraint: Prefer nodes with label zone=hdd
      preferredDuringSchedulingIgnoredDuringExecution:
        - weight: 1
          preference:
            matchExpressions:
              - key: zone
                operator: In
                values:
                  - hdd
```

- #### **📌2.Advanced Operators and Expressions:**
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


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



--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### 🔥Node Anti-Affinity
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Node Anti-Affinity ensures that pods are not scheduled on certain nodes based on labels. Let’s set this up so that a pod is not scheduled on nodes labeled `disktype=hdd`.

```sh
apiVersion: v1
kind: Pod
metadata:
  name: ssd-only-pod
spec:
  containers:
  - name: my-container
    image: nginx
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: disktype
            operator: NotIn
            values:
            - hdd  # Do not schedule on HDD nodes
```
```sh
kubectl apply -f ssd-only-pod.yaml
```
```sh
kubectl get pods -o wide
```






### 🔥Pod Affinity
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**PodAffinity** allows you to schedule a pod **closer** to other pods (in the same topology or zone) based on labels.

**Pod Affinity Example:**
Let’s assume you have a group of front-end pods labeled `app=frontend` on certain nodes, and you want to ensure a new `backend` pod is scheduled **on the same node** as a `front-end` pod for low-latency communication.

**Label a Frontend Pod:**

```sh
apiVersion: v1
kind: Pod
metadata:
  name: frontend-pod
  labels:
    app: frontend
spec:
  containers:
  - name: frontend-container
    image: nginx
```
```sh
kubectl apply -f frontend-pod.yaml
```
```sh
kubectl get pods -o wide
```

```sh
apiVersion: v1
kind: Pod
metadata:
  name: backend-pod
spec:
  containers:
  - name: backend-container
    image: my-backend-image
  affinity:
    podAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
      - labelSelector:
          matchExpressions:
          - key: app
            operator: In
            values:
            - frontend  # Ensure backend is placed where frontend pods are running
        topologyKey: kubernetes.io/hostname  # Ensure it is on the same node as frontend pods
```






### 🔥Pod Anti-Affinity


```sh

apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp-deployment
  labels:
    app: myapp
spec:
  replicas: 3  # Number of replicas
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: myapp-container
        image: nginx
      affinity:
        podAntiAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
          - labelSelector:
              matchExpressions:
              - key: app
                operator: In
                values:
                - myapp  # Avoid placing on the same node as other "myapp" pods
            topologyKey: kubernetes.io/hostname  # Ensure they don't run on the same node
```


You have a Kubernetes cluster with 2 worker nodes and deploy a 3 replica pod using a Pod Anti-Affinity rule. What will happen to the third pod?

A. All 3 pods will be scheduled on 2 workers \
B. The third pod will be scheduled but on the same node as the first one.\
C. The third pod will remain in Pending state.\
D. The cluster will auto-scale to accommodate the third pod.

