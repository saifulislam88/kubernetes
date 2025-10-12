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
