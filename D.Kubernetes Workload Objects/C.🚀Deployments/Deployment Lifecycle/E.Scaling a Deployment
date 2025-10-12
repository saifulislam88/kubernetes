## Scaling a Deployment
You can scale a Deployment by using the following command.
`kubectl scale deployment/nginx-deployment --replicas=10`


Assuming horizontal Pod autoscaling is enabled in your cluster, you can set up an autoscaler for your Deployment and choose the minimum and maximum number of Pods you want to run based on the CPU utilization of your existing Pods.

```
kubectl autoscale deployment/nginx-deployment --min=10 --max=15 --cpu-percent=80
```
