### Monitor Kubernetes
Generate a token from existing service account:

```bash
kubectl create token vmagent-cluster{-service-account} -n vmagent
```

Copy the token!

Request Kubernetes API server metrics:

```bash
curl -kL -H "Authorization: Bearer eyJhb{-token-from-above-command}" https://10.10.10.3:6443/metrics
```

