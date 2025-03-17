### Monitor Kubernetes
#### Generate a token from existing service account:

```bash
kubectl create token vmagent-cluster{-service-account} -n vmagent
```

Copy the token!

#### Request Kubernetes API server metrics using token above!:

```bash
curl -kL -H "Authorization: Bearer {token}" https://10.10.10.3:6443/metrics
```

#### Output
```bash
# TYPE aggregator_discovery_aggregation_count_total counter
aggregator_discovery_aggregation_count_total 8
# HELP aggregator_unavailable_apiservice [ALPHA] Gauge of APIServices which are marked as unavailable broken down by APIService name.
# TYPE aggregator_unavailable_apiservice gauge
aggregator_unavailable_apiservice{name="v1."} 0
aggregator_unavailable_apiservice{name="v1.acme.cert-manager.io"} 0
aggregator_unavailable_apiservice{name="v1.scheduling.k8s.io"} 0
aggregator_unavailable_apiservice{name="v1.snapshot.storage.k8s.io"} 0
aggregator_unavailable_apiservice{name="v1.storage.k8s.io"} 0
....
.......
....
apiserver_request_duration_seconds_bucket{component="apiserver",dry_run="",group="operator.victoriametrics.com",resource="vmstaticscrapes",scope="cluster",subresource="",verb="LIST",version="v1beta1",le="+Inf"} 1
apiserver_request_duration_seconds_sum{component="apiserver",dry_run="",group="operator.victoriametrics.com",resource="vmstaticscrapes",scope="cluster",subresource="",verb="LIST",version="v1beta1"} 1.122618932
apiserver_request_duration_seconds_bucket{component="apiserver",dry_run="",group="operator.victoriametrics.com",resource="vmstaticscrapes",scope="cluster",subresource="",verb="WATCH",version="v1beta1",le="0.025"} 0
apiserver_request_duration_seconds_bucket{component="apiserver",dry_run="",group="operator.victoriametrics.com",resource="vmstaticscrapes",scope="cluster",subresource="",verb="WATCH",version="v1beta1",le="1"} 0

```

### Monitor ETCD
#### Manually get metrics

```bash
curl --cacert /etc/ssl/etcd/ssl/ca.pem  --cert /etc/ssl/etcd/ssl/cert.pem --key /etc/ssl/etcd/ssl/key.pem https://<ETCD_CLUSTER_MASTER_IP>:2379/metrics 
```

#### Scrape using VMAgent

To extract ETCD metrics by VMAgent, you should create a secret from these ssl certs manually or via a OS CronJob!

```bash
kubectl create secret generic etcd-certs -n vmagent --save-config --dry-run=client --from-file=/etc/ssl/etcd/ssl -o yaml |  kubectl apply -f -
```

Then use this secret in a vm static scraper:

```bash
apiVersion: operator.victoriametrics.com/v1beta1
kind: VMStaticScrape
metadata:
  name: '{{ .Values.environment }}-etcd'
  labels:
    environment: '{{ .Values.environment }}'
spec:
  jobName: '{{ .Values.environment }}-etcd'
  targetEndpoints:
    - targets:
        - <ETCD_CLUSTER_MASTER_1_IP>:2379
        - <ETCD_CLUSTER_MASTER_2_IP>:2379
      path: /metrics
      scheme: https
      tlsConfig:
        insecureSkipVerify: false
        ca:
          secret: # can reference the secret directly instead of needing to add it somewhere else
            name: etcd-certs
            key: ca.pem
        cert:
          secret:
            name: etcd-certs
            key: cert.pem
        keySecret:
          name: etcd-certs
          key: key.pem
      bearerTokenFile: "/var/run/secrets/kubernetes.io/serviceaccount/token"
```

Just this!
