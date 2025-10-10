## What is kubernetes api-resources
The kubectl api-resources command provides a concise overview of the available Kubernetes API resources. Here's a breakdown of the columns displayed:

`kubectl api-resources -o wide`

**NAME:** This column lists the names of the API resources. Each resource represents a particular object type that can be managed within Kubernetes.

**SHORTNAMES:** Some resources have abbreviated shortnames for convenience. These shortnames can be used as shortcuts when running commands.

**APIGROUP:** API groups are a way to group related resources together under a common namespace. This column indicates the API group to which each resource belongs. If the resource doesn't belong to any specific group, it will be blank.

**NAMESPACED:** This column indicates whether the resource is namespaced. Namespaced resources are scoped to a specific namespace within the Kubernetes cluster. If a resource is namespaced, it means you can create multiple instances of that resource in different namespaces.

**KIND:** The "Kind" column indicates the type of object the resource represents. For example, Deployment, Pod, Service, etc.

**VERBS:** This column lists the verbs that can be used with each resource. Verbs represent the actions that can be performed on the resource, such as create, delete, get, list, patch, update, and watch.
