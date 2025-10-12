## Checking Rollout History of a Deployment

Use --record while creating the deployment so that it will start recroding the deployment.\
`kubectl create -f deploy.yaml --record=true`

First, check the revisions of this Deployment.\
`kubectl rollout history deployment/nginx-deployment`

To see the details of each revision, run.\
`kubectl rollout history deployment/nginx-deployment --revision=2`

How to check k8s deploy history.\
`kubectl rollout history deployment/erpbe-pod  --revision=1  -o yaml`

