### SSL Cert
To view CA cert of the cluster:

```bash
kubectl config view --raw -o jsonpath='{.clusters[0].cluster.certificate-authority-data}' | base64 --decode
```

### Patch
To help k8s! to delete resources, you can patch the resource's finalizers:

```bash
kubectl patch <RESOURCE_TYPE> <RESOURCE_NAME> -n <NAMESPACE> -p '{"metadata":{"finalizers":[]}}' --type=merge
```

To patch a namespace:

```bash
kubectl get namespace <NAMESPACE> -o json > ns.json
```

Edit file `ns.json` and remove Finalizer section and then:

```bash
kubectl replace --raw "/api/v1/namespaces/<NAMESPACE>/finalize" -f ./ns.json
```
