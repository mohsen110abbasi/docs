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
