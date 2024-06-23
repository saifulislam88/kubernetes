![Kubernetes Ingress](https://github.com/saifulislam88/kubernetes/assets/68442870/973c1256-1a85-4583-af80-f552fc93813b)

## Prerequisites - Knowledge Base

- [**Kubernetes Ingress**](https://github.com/saifulislam88/kubernetes/blob/main/A.Kubernetes-principle-concept/(A).Kubernetes%20Principle%20&%20Concept.md#ingressresource) — Covers all Ingress concepts
- [**Ingress Controller**](https://github.com/saifulislam88/kubernetes/blob/main/A.Kubernetes-principle-concept/(A).Kubernetes%20Principle%20&%20Concept.md#ingress-controller) — Detailed guide on ingress controller
- [**SSL/TLS Certificates**](https://www.hostinger.com/tutorials/what-is-ssl) — Explanation of SSL/TLS certificates

### Self-Signed Certificate

You create and sign the certificate yourself. A self-signed certificate is a public key certificate that is signed and validated by the same person. It means that the certificate is signed with its own private key and is not relevant to the organization or person identity that does sign process. Such certificates are ideal for testing servers.

### What is a CA-signed/Purchased/Commercial/Paid SSL Certificate?

A reputable third-party certificate authority (CA) issues a certificate that requires verification of domain ownership, legal business documents, and other essential technical perspectives. To establish a certificate chain, the certificate authority also issues a certificate called a trusted root certificate. There are many CAs in the SSL industry:
- GeoTrust
- RapidSSL
- Digicert
- Comodo
- GlobalSign, etc.

### Free SSL

Typically uses Domain Validation (DV) only. This verifies that you control the domain name associated with the certificate, but not your organization's identity. Suitable for personal websites, blogs, or non-critical applications. There are many providers offering free SSL certificates:
- Let's Encrypt
- ZeroSSL
- Cloudflare

## SSL/TLS Setup with Self-Signed Certificate Using Ingress-NGINX Controller

**Before proceeding, let's establish some baseline assumptions regarding the application setup:**
- The application is deployed on a Kubernetes cluster.
- The application can be accessed externally through an Ingress. (We'll need the load balancer IP address associated with the Ingress controller.)

### Creating Self-Signed SSL Certificates Using OpenSSL

   sudo apt update 
   sudo apt install openssl 
   openssl genrsa -out saiful.com.key 2048 
   openssl req -new -key saiful.com.key -out saiful.com.csr
   openssl x509 -req -days 365 -in saiful.com.csr -signkey saiful.com.key -out saiful.com.crt

# Create Kubernetes TLS Secret

Create a Kubernetes secret of type `TLS` with the `saiful.com.crt` and `saiful.com.key` files in the `dev` namespace where the `hello-app` deployment is located. Run the following `kubectl` command from the directory where you have the `saiful.com.key` and `saiful.com.crt` files, or provide the absolute path of the files. `saiful-hello-app-tls` is an arbitrary name for the secret.


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
          <crt contents here>
        server.key: |
          <private key contents here>



