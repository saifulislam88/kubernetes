## Rolling Back a Deployment
Suppose that you made a typo while updating the Deployment, by putting the image name as nginx:1.161 instead of nginx:1.16.1.\
`kubectl set image deployment/nginx-deployment nginx=nginx:1.161`

The rollout gets stuck. You can verify it by checking the rollout status.\
`kubectl rollout status deployment/nginx-deployment`

Describe Deployment.\
`kubectl describe deployment nginx-deployment`

