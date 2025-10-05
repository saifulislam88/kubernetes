
## Kubernetes: Namespaces, Contexts & kubeconfig --- Step-by-Step Guide

### Overview

-   **Namespace**: a virtual partition within a Kubernetes cluster. You
    can group resources (Pods, Services, etc.) into different namespaces
    so they don't collide, and you can apply quotas or RBAC separately.
-   **kubeconfig**: configuration file (usually `~/.kube/config`) that
    stores **clusters**, **users**, **contexts**, and **namespaces**.
    `kubectl` uses it to know where and as whom to talk.
-   **Context**: a shortcut in kubeconfig that ties **cluster + user +
    default namespace** together. You can switch contexts instead of
    retyping cluster URL, certificate, namespace, etc.

------------------------------------------------------------------------

### Sample kubeconfig fragment

Here's a minimal example of a kubeconfig file with two clusters, two
users, and two contexts:

``` yaml
apiVersion: v1
kind: Config
clusters:
- name: cluster-dev
  cluster:
    server: https://dev.example.com:6443
    certificate-authority: /home/user/.kube/ca-dev.crt
- name: cluster-prod
  cluster:
    server: https://prod.example.com:6443
    certificate-authority: /home/user/.kube/ca-prod.crt

users:
- name: dev-user
  user:
    client-certificate: /home/user/.kube/dev-user.crt
    client-key: /home/user/.kube/dev-user.key
- name: prod-admin
  user:
    token: my-production-token

contexts:
- name: dev-context
  context:
    cluster: cluster-dev
    user: dev-user
    namespace: dev-namespace
- name: prod-context
  context:
    cluster: cluster-prod
    user: prod-admin
    # no namespace here → default “default”

current-context: dev-context
```

In this setup:

-   When `dev-context` is active, `kubectl get pods` will talk to
    **cluster-dev**, as **dev-user**, in **dev-namespace**.
-   If you switch to `prod-context`, operations go to **cluster-prod**,
    as **prod-admin**, in the **default** namespace.

------------------------------------------------------------------------

### Common commands & steps

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Purpose            Command                                                                                                Notes / Example
  ------------------ ------------------------------------------------------------------------------------------------------ -------------------------------------------------------
  View all contexts  `kubectl config get-contexts`                                                                          Shows table of contexts. Current one has `*` marker.

  View current       `kubectl config current-context`                                                                       E.g. `dev-context`
  context                                                                                                                   

  Switch to another  `kubectl config use-context <context-name>`                                                            e.g. `kubectl config use-context prod-context`
  context                                                                                                                   

  Create or modify a `kubectl config set-context <ctx-name> --cluster=<cluster-name> --user=<user-name> --namespace=<ns>`   Adds or updates context.
  context                                                                                                                   

  Change default     `kubectl config set-context --current --namespace=<namespace>`                                         E.g.
  namespace of                                                                                                              `kubectl config set-context --current --namespace=qa`
  current context                                                                                                           

  Delete a context   `kubectl config delete-context <context-name>`                                                         Removes context from kubeconfig

  Inspect kubectl    `kubectl config view`                                                                                  Shows effective config (merged with KUBECONFIG)
  merged config                                                                                                             
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------

### Step-by-step: Example workflow

#### 1. Start fresh or back up your existing config:

``` bash
cp ~/.kube/config ~/.kube/config.backup
```

#### 2. Add cluster / user entries

``` bash
kubectl config set-cluster cluster-dev --server=https://dev.my.net:6443 --certificate-authority=/home/user/ca-dev.crt
kubectl config set-credentials dev-user --client-certificate=/home/user/dev.crt --client-key=/home/user/dev.key

kubectl config set-cluster cluster-prod --server=https://prod.my.net:6443 --certificate-authority=/home/user/ca-prod.crt
kubectl config set-credentials prod-admin --token=TOKENVALUE
```

#### 3. Create contexts

``` bash
kubectl config set-context dev-context --cluster=cluster-dev --user=dev-user --namespace=dev
kubectl config set-context prod-context --cluster=cluster-prod --user=prod-admin --namespace=prod
```

#### 4. Switch between contexts

``` bash
kubectl config use-context dev-context
kubectl get pods           # hits dev cluster namespace dev
kubectl config use-context prod-context
kubectl get pods           # hits prod cluster namespace prod (or default)
```

#### 5. Change default namespace within a context

Suppose you're in `dev-context` but you want default to be `testing`
instead of `dev`:

``` bash
kubectl config set-context --current --namespace=testing
kubectl config current-context
kubectl config view --minify | grep namespace:
```

#### 6. List / delete unused contexts

``` bash
kubectl config get-contexts
kubectl config delete-context old-context
```

------------------------------------------------------------------------

### Why use contexts & default namespaces

-   You avoid typing `--cluster`, `--user`, or `-n <namespace>` in every
    command.
-   Useful when you manage multiple clusters (dev, staging, prod) or
    multiple environments.
-   Ensures your commands go to the right place and avoid accidents
    (e.g. applying to prod when you intended dev).
