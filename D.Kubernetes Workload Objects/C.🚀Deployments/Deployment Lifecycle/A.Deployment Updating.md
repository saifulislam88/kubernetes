## Updating nginx-deployment deployment
Let's update the nginx Pods to use the nginx:1.16.1 image instead of the nginx:1.14.2 image.\
`kubectl set image deployment/nginx-deployment nginx=nginx:1.16.1`

Alternatively, you can edit the Deployment and change.\
`kubectl edit deployment/nginx-deployment`

To see the rollout status, run.\
`kubectl rollout status deployment/nginx-deployment`
