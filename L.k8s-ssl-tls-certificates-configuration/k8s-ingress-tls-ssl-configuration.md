
## Prerequisites - Knowledge Base

![image](https://github.com/saifulislam88/kubernetes/assets/68442870/973c1256-1a85-4583-af80-f552fc93813b)


- [Kubernetes Ingress](https://github.com/saifulislam88/kubernetes/blob/main/A.Kubernetes-principle-concept/(A).Kubernetes%20Principle%20&%20Concept.md#ingressresource) — Covers all Ingress concepts
- [Ingress controller](https://github.com/saifulislam88/kubernetes/blob/main/A.Kubernetes-principle-concept/(A).Kubernetes%20Principle%20&%20Concept.md#ingress-controller) — Detailed guide on ingress controller
- [SSL/TLS Certificates](https://www.hostinger.com/tutorials/what-is-ssl)

   ### - Self-Signed certificate

  You create and sign the certificate yourself. A self-signed certificate is a public key certificate that is signed and validated by the same person. It means that the certificate is signed with its 
  own private key and is not relevant to the organization or person identity that does sign process. Such certificate is ideally for testing servers.

   ### - What is CA-signed/Purchase/Commercial/Paid SSL certificate? 

  A reputable third-party certificate authority (CA) issues a certificate that requires verification of domain ownership, legal business documents, and other essential technical perspectives. To 
  establish certificate chain, certificate authority also itself issues a certificate that is named trusted root certificate.There are many CAs in SSL industry:

  - GeoTrust
  - RapidSSL
  - Digicert
  - Comodo
  - GlobalSign etc.

   ### - Free SSL

  Typically uses Domain Validation (DV) only. This verifies that you control the domain name associated with the certificate, but not your organization's identity.Suitable for personal websites, blogs, 
  or non-critical applications.There are many providers offering free SSL certificates.

  - Let's Encrypt
  - ZeroSSL
  - Cloudflare


## SSL/TLS Setup with Self-Signed Certificate Using Ingress-NGINX Controller

**Before proceeding, let's establish some baseline assumptions regarding the application setup:**

- The application is deployed on a Kubernetes cluster.
- The application can be accessed externally through an Ingress. (We'll need the load balancer IP address associated with the Ingress controller.)
- [Creating Self-Signed SSL Certificates Using OpenSSL](https://tecadmin.net/step-by-step-guide-to-creating-self-signed-ssl-certificates/)

   ```sh
        sudo apt update 
        sudo apt install openssl 
        openssl genrsa -out example.key 2048 
        openssl req -new -key example.key -out example.csr
        openssl x509 -req -days 365 -in example.csr -signkey example.key -out example.crt



- **Create Kubernetes TLS Secret using above CA key & CA Certificate**
  
      kubectl --namespace dev get services -o wide -w ingress-nginx-controller
      kubectl create -n dev


Save the following YAML as hello-app.yaml. It has a deployment and service object.

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

- Deploy the test application.

      kubectl apply -f hello-app.yaml

- Create a Kubernetes TLS Secret

You need the `server.crt` and `server.key` SSL files from a Certificate Authority, your organization, or self-signed. Where already we generated self-signed saiful.com.key & saiful.com.crt

Create a Kubernetes secret of type `TLS` with the `saiful.com.crt` and `saiful.com.crt` files in the `dev` namespace where the `hello-app` deployment is located. Run the following `kubectl` command from the directory where you have the `saiful.com.key` and `saiful.com.crt` files, or provide the absolute path of the files. `saiful-hello-app-tls` is an arbitrary name for the secret.

      ```sh
      kubectl create secret tls saiful-hello-app-tls \
          --namespace dev \
          --key saiful.com.key \
          --cert saiful.com.crt


You can also create the secret using a YAML file. Add the contents of the certificate and key files as follows:

      apiVersion: v1
      kind: Secret
      metadata:
        name: saiful-hello-app-tls
        namespace: dev
      type: kubernetes.io/tls
      data:
        server.crt: |
          saiful.com.crt
        server.key: |
          saiful.com.key



 - Add TLS Block to Ingress Object

The Ingress resource with TLS must be created in the same namespace where your application is deployed. Here, we create an example Ingress TLS resource in the dev namespace. Save the following YAML as ingress.yaml. **Replace app.saiful.com with your hostname.**



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
          secretName: hello-app-tls
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





