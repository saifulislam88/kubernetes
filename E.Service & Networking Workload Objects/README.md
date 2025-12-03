
  - [Kubernetes Service & Networking Objects](#kubernetes-service--networking-objects)
    - [Kubernetes Services Type](#kubernetes-services-type)
      - [ClusterIP](#1-clusteripdefault)
      - [NodePort](#2-nodeport)
      - [LoadBalancer](#3-loadbalancer)
      - [Headless]()
      - [ExternalName](#4-externalname)
      - [Endpoint(ep) | Pod IP - is not a service ](#endpointep--pod-ip---is-not-a-service)
      - [Ingress - is not a service](#ingress---is-not-a-service)
    - [Kubernetes Resources](#kubernetes-resources)
      - [Kubernetes Ingress](#ingress)
        - [Ingress Controlller](#ingress-controller)
          - [MetalLB | BareMetal LB](#metallb--baremetal-lb)




          ## [Kubernetes Service & Networking Objects](#kubernetes-service--networking-objects)


A service is an abstract mechanism for exposing pods on a network. Kubernetes workloads aren’t network-visible by default. You make containers available to the local or outside world by creating a service. Service resources route traffic into the containers within pods. Kubernetes supports several ways of getting external traffic into your cluster. 

**Why use a Service?**

Suppose you decide to create an HTTP server cluster to manage request coming from thousands of browsers, you create a deployment file where you specify to run an Nginx application in 3 copies on 3 Pods. These Pods are accessible via the node IP. If a Pod on a node goes down and recreated on another node its IP change and the question is: how can I reference that Pod?
To make Pods accessible from external, Kubernetes uses a Service as a level of abstraction. A Service, basically, lives between clients and Pods and when an HTTP request arrives, it forwards the request to the right Pod.

Service get a stable IP address that can use to contact Pods. A client sends a request to the stable IP address, and the request is routed to one of the Pods in the Service.
A Service identifies its member Pods with a selector. For a Pod to be a member of the Service, the Pod must have all of the labels specified in the selector. A label is an arbitrary key/value pair that is attached to an object.

The following Service manifest has a selector that specifies two labels. The selector field says any Pod that has both the app: metrics label and the department: engineering label is a member of this
 
```sh
  Service.
  apiVersion: v1
  kind: Service
  metadata:
    name: my-service
  spec:
    selector:
      app: metrics
      department: engineering
    ports:
```
## [Kubernetes Services Type](#kubernetes-services-type)





[**5.Headless**]()



------------------------------------------------------------------------------------------------------------------------------------------------------------------


### [Endpoint(ep) | Pod IP - is not a service](#endpointep--pod-ip---is-not-a-service)

**Endpoints are not services;** they are objects that store the actual IP addresses of the pods that match a service selector, used internally by services to direct traffic to the correct pods.

`kubectl get endpoints`\
`kubectl get pods -o wide`\
`kubectl describe endpoints <endpoint-name>`\
`kubectl get endpoints <service-name>`\
`kubectl get endpoints <service-name> -o wide`\
`kubectl get endpoints <service-name> -o yaml`\
`kubectl get endpoints <service-name> -o json`

### [Ingress - is not a service](#ingress---is-not-a-service)

**Ingress is not a service;** it is a resource that manages external access to services, typically HTTP, and can provide `Load balancing`, `SSL termination`, and `Name-based virtual hosting`,`Path-based`,`URL Routing`.

`kubectl apply -f ingress.yaml`\
`kubectl get ingress`\
`kubectl describe ingress <ingress-name>`\
`kubectl delete ingress <ingress-name>`\
`kubectl get pods -n <ingress-namespace> -l app.kubernetes.io/name=ingress-nginx`\
`kubectl logs <ingress-controller-pod> -n <ingress-namespace>`\
`kubectl get svc -n <ingress-namespace>`\
`curl -H "Host: <your-hostname>" http://<ingress-ip>`
