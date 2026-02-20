---
title: Kubernetes Istio Configuration
category: features
createdAt: '2024-07-03T15:21:27.220Z'
hidden: false
slug: k8s-advanced-configuration-istio
updatedAt: '2024-12-11T15:24:58.439Z'
---
When you are installing the CloudZero Agent in a Kubernetes cluster that is Istio-enabled, you may have to perform additional steps to ensure proper functioning. This is because Istio automatically configures sidecars to use `mutual TLS (mTLS)`, which can interfere with the Agent's existing TLS communication.

The CloudZero Agent for Kubernetes includes a webhook server component responsible for handling admission review requests from the Kubernetes API server. These requests use TLS, and when these requests are intercepted by an Istio sidecar, Istio may attempt to apply its `mTLS` policies. These policies are not always compatible with the webhook’s TLS configuration.

While this does not block pod deployments, it prevents the `insightsController` from collecting critical pod labels, which are necessary for accurate cost allocation.

To ensure the CloudZero Agent for Kubernetes works correctly in Istio-enabled clusters, you can use one of the following options:

* [Disable sidecar injection for the webhook-server pods only](#option-1-disable-sidecar-injection-for-kubernetes-webhook-server-pods-only): Completely removes the Istio sidecar from the webhook server, avoiding any interference.
* [Disable envoy for webhook ports only](#option-2-disable-envoy-for-webhook-ports-only): Keeps the sidecar but excludes webhook traffic, preserving Istio functionality for all other traffic.
* [Disable mTLS for the webhook-server pods](#option-3-disable-mtls-for-the-cloudzero-agent-for-kubernetes): Keeps the sidecar but disables mTLS enforcement specifically for webhook-server traffic.

# Option 1: Disable sidecar injection for Kubernetes webhook-server pods only

To disable the sidecar injection only for a subset of the pods deployed by the cluster, update the chart input values with the following annotation:

```yaml
insightsController:
  server:
    podAnnotations:
      sidecar.istio.io/inject: "false"
```

This annotation prevents the Istio sidecar from being injected into the `webhook-server` pods, while the rest of the cluster retains normal Istio functionality.

# Option 2: Disable envoy for webhook ports only

To prevent only requests to a single port on the webhook-server pods from being routed through envoy, apply the following annotation:

```yaml
insightsController:
  server:
    podAnnotations:
      traffic.sidecar.istio.io/excludeInboundPorts: "8443"
```

In this case, the pods will still have an Istio sidecar injected, but traffic to port 8443 (the webhook port) will bypass envoy.

For more details, see [the Istio documentation](https://istio.io/latest/docs/reference/config/annotations/#SidecarTrafficExcludeInboundPorts).

# Option 3: Disable mTLS for the CloudZero Agent for Kubernetes

To disable mTLS for the CloudZero Agent for Kubernetes service, apply the following `PeerAuthentication` resource:

```yaml
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: cloudzero-agent-mtls
  namespace: <cloudzero-namespace>
spec:
  selector:
    matchLabels:
      app.kubernetes.io/component: webhook-server
  mtls:
    mode: DISABLE
```

Follow these steps to apply the `PeerAuthentication` resource:

1. Replace `<cloudzero-namespace>` with the namespace where `cloudzero-agent` is deployed.
2. Apply the resource: `kubectl apply -f cloudzero-agent-mtls.yaml`.
3. Deploy the `cloudzero-agent` chart as instructed in the [documentation](/docs/installation-of-cloudzero-agent-for-kubernetes#/set-up-the-cloudzero-agent).

This configuration disables mTLS for `cloudzero-agent` webhook-server pods only, while keeping it enabled for the rest of the cluster.
