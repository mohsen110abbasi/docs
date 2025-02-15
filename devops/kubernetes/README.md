### SSL Cert
To view CA cert of the cluster:

```bash
kubectl config view --raw -o jsonpath='{.clusters[0].cluster.certificate-authority-data}' | base64 --decode
```