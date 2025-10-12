## Rolling Back to a Previous Revision 

Now you've decided to undo the current rollout and rollback to the previous revision.\
`kubectl rollout undo deployment/nginx-deployment`

Alternatively, you can rollback to a specific revision by specifying it with --to-revision.\
`kubectl rollout undo deployment/nginx-deployment --to-revision=2`

Check if the rollback was successful and the Deployment is running as expected, run.\
`kubectl get deployment nginx-deployment`

Get the description of the Deployment.\
`kubectl describe deployment nginx-deployment`
