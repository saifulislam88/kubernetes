## 🚀ReplicaSets

**A ReplicaSet is used for making sure that the designated number of pods is up and running.** It is convenient to use when we are supposed to run multiple pods at a given time. ReplicaSet requires labels to understand which pods to run, a number of replicas that are supposed to run at a given time, and a template of the pod that it needs to create.

**`kubectl create rs nginx --image=nginx --replicas=3 --dry-run=client -o yaml > nginx-replicaset.yaml`**


vim nginx-replicaset.yaml`

```sh
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: nginx-replicaset
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
