## Securing Applications in Kubernetes With SSL/TLS

If security has ever been important, it's even more crucial today. Imagine sending a confidential letter through a public mail system where anyone can read or change its content. That's what happens when we send data online without protection. This is where SSL/TLS comes in. Think of SSL/TLS as the security envelope of the digital world.

With the rise of cloud-native applications, microservices, and Software as a Service (SaaS), secure communication between front-end applications and users is more vital than ever. SSL/TLS (Secure Sockets Layer/Transport Layer Security) ensures this security.

<img src="https://github.com/saifulislam88/kubernetes/assets/68442870/3c3aef67-5658-46ad-9d84-4f7f2c88401b" alt="Kubernetes Ingress" width="400"/>

### SSL/TLS Setup in Kubernetes Applications with `Self-Signed Certificate` or `SSL files from a Certificate Authority` Using Ingress-NGINX Controller


- [Prerequisites - Knowledge Base](https://github.com/saifulislam88/kubernetes/blob/main/L.k8s-ssl-tls-certificates-configuration/k8s-ingress-tls-ssl-configuration.md#prerequisites---knowledge-base)
- [SSL/TLS Setup with `Self-Signed Certificate` or `SSL files from a Certificate Authority` Using Ingress-NGINX Controller](https://github.com/saifulislam88/kubernetes/blob/main/L.k8s-ssl-tls-certificates-configuration/k8s-ingress-tls-ssl-configuration.md#ssltls-setup-using-ingress-nginx-controller)


## Prerequisites - Knowledge Base

- [**Kubernetes Ingress**](https://github.com/saifulislam88/kubernetes/blob/main/A.Kubernetes-principle-concept/(A).Kubernetes%20Principle%20&%20Concept.md#ingressresource) — Covers all Ingress concepts
- [**Ingress Controller**](https://github.com/saifulislam88/kubernetes/blob/main/A.Kubernetes-principle-concept/(A).Kubernetes%20Principle%20&%20Concept.md#ingress-controller) — Detailed guide on ingress controller
- [**SSL/TLS Certificates**](https://www.hostinger.com/tutorials/what-is-ssl) — Explanation of SSL/TLS certificates

### - Self-Signed Certificate

You create and sign the certificate yourself. A self-signed certificate is a public key certificate that is signed and validated by the same person. It means that the certificate is signed with its own private key and is not relevant to the organization or person identity that does sign process. Such certificates are ideal for testing servers.

### - What is a CA-signed/Purchased/Commercial/Paid SSL Certificate?

A reputable third-party certificate authority (CA) issues a certificate that requires verification of domain ownership, legal business documents, and other essential technical perspectives. To establish a certificate chain, the certificate authority also issues a certificate called a trusted root certificate. There are many CAs in the SSL industry:

      - GeoTrust
      - RapidSSL
      - Digicert
      - Comodo
      - GlobalSign, etc.

   ### - Free SSL

   Typically uses Domain Validation (DV) only. This verifies that you control the domain name associated with the certificate, but not your organization's identity. Suitable for personal websites,    
   blogs, or non-critical applications. There are many providers offering free SSL certificates:

      - Let's Encrypt
      - ZeroSSL
      - Cloudflare

## SSL/TLS Setup Using Ingress-NGINX Controller

![image](https://github.com/saifulislam88/kubernetes/assets/68442870/0e49e925-68b2-42d5-bc4b-d2a216d932cf)

**Before proceeding, let's establish some baseline assumptions regarding the application setup:**
- The application is deployed on a Kubernetes cluster.
- The application can be accessed externally through an Ingress. We will need the load balancer IP address associated with the Ingress controller

   
### - Creating Self-Signed SSL Certificates Using OpenSSL

```sh
sudo apt update 
sudo apt install openssl 
openssl genrsa -out saiful.com.key 2048 
openssl req -new -key saiful.com.key -out saiful.com.csr
openssl x509 -req -days 365 -in saiful.com.csr -signkey saiful.com.key -out saiful.com.crt

```

### - Create Kubernetes TLS Secret

Create a Kubernetes secret of type `TLS` with the `saiful.com.crt` and `saiful.com.key` files in the `dev` namespace where the `hello-app` deployment is located. Run the following `kubectl` command    from the directory where you have the `saiful.com.key` and `saiful.com.crt` files, or provide the absolute path of the files. `saiful-hello-app-tls` is an arbitrary name for the secret.

**Base64 Encode the Certificate and Key:** YAML does not support binary data directly. Base64 encoding allows binary data (like certificates and keys) to be represented as plain text within the YAML format.\
`base64 -w 0 saiful.com.crt`\
`base64 -w 0 saiful.com.key`

**Verify Base64 Encoding of the Certificate and Key**\
`echo "<base64-encoded-certificate>" | base64 --decode`\
`echo "<base64-encoded-key>" | base64 --decode`


`vim saiful-hello-app-tls.yaml`

```sh
##namespace will be changed on based project
apiVersion: v1
kind: Secret
metadata:
  name: saiful-hello-app-tls
  namespace: dev
type: kubernetes.io/tls
data:
  tls.crt: <base64-encoded-certificate>
  tls.key: <base64-encoded-key>
```

`kubectl apply -f saiful-hello-app-tls.yaml`


**You can also create the secret Directly without `Base64 Encode`**

```sh
kubectl create secret tls saiful-hello-app-tls \
    --namespace dev \
    --key saiful.com.key \
    --cert saiful.com.crt
```

**Verify the TLS Secret**\
`kubectl get secret -n ingress-nginx`\
`kubectl get secret saiful-hello-app-tls -o yaml`\
`kubectl get secret saiful-hello-app-tls -o jsonpath='{.data.tls\.crt}' | base64 --decode`\
`kubectl get secret saiful-hello-app-tls -o jsonpath='{.data.tls\.key}' | base64 --decode`

**Recreate the TLS Secret (If Necessary)**\
`kubectl delete secret saiful-hello-app-tls`

`curl -v https://nginx1.example.com`\
`curl -v https://nginx2.example.com`


### - Deploy the Application

Save the following YAML as **hello-app.yaml**. It contains a deployment and a `service` object.

```sh
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-app
  namespace: dev
spec:
  selector:
    matchLabels:
      app: hello
  replicas: 2
  template:
    metadata:
      labels:
        app: hello
    spec:
      containers:
      - name: hello
        image: "gcr.io/google-samples/hello-app:2.0"
---
apiVersion: v1
kind: Service
metadata:
  name: hello-service
  namespace: dev
  labels:
    app: hello
spec:
  type: ClusterIP
  selector:
    app: hello
  ports:
  - port: 80
    targetPort: 8080
    protocol: TCP
```

**Deploy the application with the following command:**

```sh
kubectl apply -f hello-app.yaml
```

### - Add/Setup TLS Block to Ingress Object

**The Ingress resource with TLS must be created in the same namespace where your application is deployed. Save the following YAML as `ingress.yaml`. Replace `app.saiful.com` with your hostname.**

You need the `server.crt` and `server.key` SSL files from a Certificate Authority, your organization, or self-signed. Where already we generated self-signed saiful.com.key & saiful.com.crt. Create a Kubernetes secret of type `TLS` with the `saiful.com.crt` and `saiful.com.crt` files in the `dev` namespace where the `hello-app` deployment is located. Run the following `kubectl` command from the directory where you have the `saiful.com.key` and `saiful.com.crt` files, or provide the absolute path of the files. `saiful-hello-app-tls` is an arbitrary name for the secret.


```sh
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: hello-app-ingress
  namespace: dev
spec:
  ingressClassName: nginx
  tls:
  - hosts:
    - app.saiful.com
    secretName: saiful-hello-app-tls
  rules:
  - host: "app.saiful.com"
    http:
      paths:
        - pathType: Prefix
          path: "/"
          backend:
            service:
              name: hello-service
              port:
                number: 80

```


### - Explanation

In this example, we add the TLS block with the hostname (`app.saiful.com`) and the TLS secret (`saiful-hello-app-tls`) created in the previous step. The host in the TLS block and rules block should match.

```sh
tls:
  - hosts:
    - app.saiful.com
    secretName: saiful-hello-app-tls
```

### - Validate Ingress TLS

```sh
curl https://app.saiful.com -kv
```

### - Ingress SSL Termination

By default, SSL gets terminated in ingress the controller. So all the traffic from the controller to the pod will be without TLS (decrypted traffic). If you want full SSL, you can add the supported annotation by the ingress controller you are using. For example, In the Nginx ingress controller, to allow SSL traffic till the application, you can use the `nginx.ingress.kubernetes.io/backend-protocol: "HTTPS"` annotation. For this, your application should have SSL configured.
