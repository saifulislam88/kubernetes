
## Prerequisites - Knowledge Base

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
