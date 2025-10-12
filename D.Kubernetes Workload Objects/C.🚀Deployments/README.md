## 🚀Deployments

A Deployment provides declarative updates for `Pods` and `ReplicaSets`.

You describe a desired state in a Deployment, and the Deployment Controller changes the actual state to the desired state at a controlled rate. You can define Deployments to create new ReplicaSets, or to remove existing Deployments and adopt all their resources with new Deployments.


This table compares the features provided by **Pod**, **ReplicaSet**, and **Deployment** in Kubernetes.

| Feature | Pod | ReplicaSet | Deployment |
|---------|-----|------------|------------|
| Maintains desired number of Pods | ❌ No | ✅ Yes | ✅ Yes |
| Rolling updates (zero downtime) | ❌ No | ❌ No | ✅ Yes |
| Rollback to previous versions | ❌ No | ❌ No | ✅ Yes |
| Version history (Revisions) | ❌ No | ❌ No | ✅ Yes |
| Declarative updates (apply new image/version safely) | ❌ No | ❌ No | ✅ Yes |

## Explanation

- **Pod**: The smallest deployable unit in Kubernetes. Does not provide self-healing or scaling features by itself.  
- **ReplicaSet**: Ensures a specified number of Pod replicas are running. Useful for high availability, but lacks advanced deployment strategies.  
- **Deployment**: Builds on top of ReplicaSet, adding rolling updates, rollback, version history, and declarative updates. It is the recommended way to manage stateless applications.  






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


