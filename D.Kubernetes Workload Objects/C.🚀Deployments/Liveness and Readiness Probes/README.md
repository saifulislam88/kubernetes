# Kubernetes Liveness and Readiness Probes 

Liveness and Readiness probes are used to control the health of an application running inside a Pod’s container. Kubernetes gives you two types of health checks, and it is important to understand the differences between the two, and their uses.


### Liveness probe
Liveness probes let Kubernetes know if your app is alive or dead. If your app is alive, then Kubernetes leaves it alone. If your app is dead, Kubernetes removes the Pod and starts a new one to replace it.

<p align="center">
<img width="500" height="350" src=https://github.com/user-attachments/assets/093431ee-9010-48a7-81a2-d29feb2a7e74>
</p>


### Readiness probe
Readiness probes are designed to let Kubernetes know when your app is ready to serve traffic. Kubernetes makes sure the readiness probe passes before allowing a service to send traffic to the pod. If a readiness probe starts to fail, Kubernetes stops sending traffic to the pod until it passes.

<p align="center">
<img width="500" height="350" src=https://github.com/user-attachments/assets/7d0b069e-b680-4825-89b6-7123be66fa48>
</p>

In this article, we will see how we can have the Liveness & Readiness probe defined and deployed in Kubernetes.


### Step-1: 
app.py is a simple Hello World Python Flask application, here we have defined multiple routes and based on the route, respective messages will be displayed to the end-user.

#### Python Flask Application

~~~
import time
from flask import Flask
app = Flask(__name__)

@app.route('/liveness')
def healthx():
  time.sleep(2);
  return "<h1><center>Liveness check completed</center><h1>"
  
@app.route('/readiness')
def healthz():
  time.sleep(20);
  return "<h1><center>Readiness check completed</center><h1>"
  
@app.route("/")
def hello():
  return "<h1><center>Hello World app! Version 1</center><h1>"

if __name__ == "__main__":

  app.run(host='0.0.0.0',port=5000)
~~~

### Step-2: 
We will Dockerize the app and push it to a Docker hub repository. The app will listen on port 5000.

#### Dockerfile
~~~
FROM alpine:3.8
RUN mkdir /var/flaskapp
WORKDIR /var/flaskapp
COPY .  .
RUN apk update
RUN apk add python3
RUN pip3 install -r requirement.txt
EXPOSE 5000 
CMD ["python3","app.py"]
~~~

##### requirement.txt
~~~
flask
~~~

```
docker build -t saifulislam88/k8s-readiness-liveness:v1 .
docker run -it -d saifulislam88/k8s-readiness-liveness:v1
docker exec -it 30108d950d4a sh
apk add --no-cache wget
curl -v http://localhost:5000/readiness
url -v http://localhost:5000/livenes
docker login
docker push saifulislam88/k8s-readiness-liveness:v1
```

I have uploaded this Container Image to docker hub and it is available in `saifulislam88/k8s-readiness-liveness:v1`

### Step-3:
As the app is now ready, we have to write the deployment manifest with LivenessProbe and ReadinessProbe defined along with service resource to deploy it on Kubernetes cluster.  

#### service-nodeport.yml

~~~
---
apiVersion: v1
kind: Service
metadata:
  name: service-nodeport

spec:
  type: NodePort
  ports:
    - port: 5000
      nodePort: 30000
      targetPort: 5000
      name: http
  selector:
    app: healthcheck
~~~


#### live-readiness.yml

~~~
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: healthcheck
  labels:
    app: healthcheck
	
spec:
  replicas: 4
  selector:
    matchLabels:
      app: healthcheck


  template:
    metadata:
      labels:
        app: healthcheck
            
    spec:
      containers:
        - name: healthcheck-pod
          image: saifulislam88/k8s-readiness-liveness:v1
          ports:
            - containerPort: 5000
		  
		  livenessProbe:
            httpGet:
              path: /liveness
              port: 5000
            initialDelaySeconds: 15
            timeoutSeconds: 2
            periodSeconds: 5
            failureThreshold: 2
            
          readinessProbe:
            httpGet:
              path: /readiness
              port: 5000
            initialDelaySeconds: 10
            timeoutSeconds: 3
            periodSeconds: 10
            failureThreshold: 3
~~~

### Common Fields
| Field | Description |
|-------|-------------|
| `initialDelaySeconds` | Time to wait after container start before first probe. |
| `periodSeconds` | How often to perform the probe. |
| `timeoutSeconds` | How long to wait for a response. |
| `failureThreshold` | Number of failures before action (restart or mark unready). |
| `successThreshold` | Number of successes before marking ready. |

### initialDelaySeconds

- What it is: The number of seconds Kubernetes waits after the container starts before performing the first probe.
- Why it’s important: Some applications need time to initialize before they can respond correctly. If Kubernetes probes too early, it might think the container is unhealthy and restart it unnecessarily.

### periodSeconds
- What it is: How often Kubernetes performs the probe after the initial delay.
- Why it’s important: Determines the frequency of health checks. A shorter interval detects failures faster but adds more load; a longer interval reduces load but detects failures slower.

---

## 3. Importance of Liveness and Readiness Probes

1. **Automatic Recovery**  
   Liveness probes detect hung or deadlocked containers and restart them automatically, improving reliability.

2. **Traffic Management**  
   Readiness probes prevent traffic from going to containers that are not ready, e.g., waiting for DB connections or initialization tasks.

3. **Zero Downtime Deployments**  
   Readiness probes ensure rolling updates don’t route traffic to unready pods, preventing failed requests during deployments.

4. **Resource Optimization**  
   Kubernetes stops sending requests to unready pods, reducing failed requests and CPU/memory waste.

---

## 4. Use Cases

| Probe Type | Use Case Example |
|------------|----------------|
| **Liveness**  | A web server gets stuck in a deadlock — restart automatically. |
| **Readiness** | App waits for database connection — mark unready until DB is available. |
| **Liveness + Readiness** | Microservices that need DB connection and periodic health checks — ensures reliability and safe traffic routing. |

Deploy the manifest through kubectl apply. Once deployed, I’ve run a --watch command to keep an eye on the deployment. Here’s what it looked like.

![alt text](https://i.ibb.co/61fMsC6/pod-status.png)

You’ll notice that the ready status showed 0/1 for about 49 seconds. Meaning that my container was not in a ready status for 50 seconds until the /readiness page became available through the startup script.

If we access the application service, we can see a successful response once /readiness page became available.

![alt text](https://i.ibb.co/7rfdBwW/app-browser.png)

## Summary

Both liveness and readiness probes are used to control the application's health. If the liveness probe fails, the container will be restarted, whereas the readiness probe will stop our application from serving traffic.


