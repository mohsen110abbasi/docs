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
aggregator_unavailable_apiservice{name="v1.admissionregistration.k8s.io"} 0
aggregator_unavailable_apiservice{name="v1.apiextensions.k8s.io"} 0
aggregator_unavailable_apiservice{name="v1.apps"} 0
aggregator_unavailable_apiservice{name="v1.authentication.k8s.io"} 0
aggregator_unavailable_apiservice{name="v1.authorization.k8s.io"} 0
aggregator_unavailable_apiservice{name="v1.autoscaling"} 0
aggregator_unavailable_apiservice{name="v1.batch"} 0
aggregator_unavailable_apiservice{name="v1.ceph.rook.io"} 0
aggregator_unavailable_apiservice{name="v1.cert-manager.io"} 0
aggregator_unavailable_apiservice{name="v1.certificates.k8s.io"} 0
aggregator_unavailable_apiservice{name="v1.coordination.k8s.io"} 0
aggregator_unavailable_apiservice{name="v1.discovery.k8s.io"} 0
aggregator_unavailable_apiservice{name="v1.events.k8s.io"} 0
aggregator_unavailable_apiservice{name="v1.flowcontrol.apiserver.k8s.io"} 0
aggregator_unavailable_apiservice{name="v1.gateway.networking.k8s.io"} 0
aggregator_unavailable_apiservice{name="v1.monitoring.coreos.com"} 0
aggregator_unavailable_apiservice{name="v1.networking.k8s.io"} 0
aggregator_unavailable_apiservice{name="v1.node.k8s.io"} 0
aggregator_unavailable_apiservice{name="v1.policy"} 0
aggregator_unavailable_apiservice{name="v1.postgresql.cnpg.io"} 0
aggregator_unavailable_apiservice{name="v1.rbac.authorization.k8s.io"} 0
aggregator_unavailable_apiservice{name="v1.scheduling.k8s.io"} 0
aggregator_unavailable_apiservice{name="v1.snapshot.storage.k8s.io"} 0
aggregator_unavailable_apiservice{name="v1.storage.k8s.io"} 0
....
.......
....
apiserver_request_duration_seconds_bucket{component="apiserver",dry_run="",group="operator.victoriametrics.com",resource="vmstaticscrapes",scope="cluster",subresource="",verb="LIST",version="v1beta1",le="+Inf"} 1
apiserver_request_duration_seconds_sum{component="apiserver",dry_run="",group="operator.victoriametrics.com",resource="vmstaticscrapes",scope="cluster",subresource="",verb="LIST",version="v1beta1"} 1.122618932
apiserver_request_duration_seconds_count{component="apiserver",dry_run="",group="operator.victoriametrics.com",resource="vmstaticscrapes",scope="cluster",subresource="",verb="LIST",version="v1beta1"} 1
apiserver_request_duration_seconds_bucket{component="apiserver",dry_run="",group="operator.victoriametrics.com",resource="vmstaticscrapes",scope="cluster",subresource="",verb="WATCH",version="v1beta1",le="0.005"} 0
apiserver_request_duration_seconds_bucket{component="apiserver",dry_run="",group="operator.victoriametrics.com",resource="vmstaticscrapes",scope="cluster",subresource="",verb="WATCH",version="v1beta1",le="0.025"} 0
apiserver_request_duration_seconds_bucket{component="apiserver",dry_run="",group="operator.victoriametrics.com",resource="vmstaticscrapes",scope="cluster",subresource="",verb="WATCH",version="v1beta1",le="0.05"} 0
apiserver_request_duration_seconds_bucket{component="apiserver",dry_run="",group="operator.victoriametrics.com",resource="vmstaticscrapes",scope="cluster",subresource="",verb="WATCH",version="v1beta1",le="0.1"} 0
apiserver_request_duration_seconds_bucket{component="apiserver",dry_run="",group="operator.victoriametrics.com",resource="vmstaticscrapes",scope="cluster",subresource="",verb="WATCH",version="v1beta1",le="0.2"} 0
apiserver_request_duration_seconds_bucket{component="apiserver",dry_run="",group="operator.victoriametrics.com",resource="vmstaticscrapes",scope="cluster",subresource="",verb="WATCH",version="v1beta1",le="0.4"} 0
apiserver_request_duration_seconds_bucket{component="apiserver",dry_run="",group="operator.victoriametrics.com",resource="vmstaticscrapes",scope="cluster",subresource="",verb="WATCH",version="v1beta1",le="0.6"} 0
apiserver_request_duration_seconds_bucket{component="apiserver",dry_run="",group="operator.victoriametrics.com",resource="vmstaticscrapes",scope="cluster",subresource="",verb="WATCH",version="v1beta1",le="0.8"} 0
apiserver_request_duration_seconds_bucket{component="apiserver",dry_run="",group="operator.victoriametrics.com",resource="vmstaticscrapes",scope="cluster",subresource="",verb="WATCH",version="v1beta1",le="1"} 0


```
