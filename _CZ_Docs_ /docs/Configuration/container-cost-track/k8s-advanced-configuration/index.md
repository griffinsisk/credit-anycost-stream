---
title: Advanced Kubernetes Configuration
category: features
createdAt: '2024-07-03T15:21:27.220Z'
hidden: false
slug: k8s-advanced-configuration
updatedAt: '2024-12-11T15:24:58.439Z'
---
The CloudZero agent for Kubernetes is powered by [Helm](https://helm.sh). The following are the recommended steps to get started with advanced Kubernetes configuration:

1. Create a values.yaml file with the following base configuration:

```yaml values.yaml
# -- CloudZero API key.
apiKey: <CloudZero_api_key>
# -- Friendly name of your cluster.
clusterName: <NAME_OF_YOUR_CLUSTER>
```

2. Deploy the agent with your new values file.

```shell
helm upgrade --install cloudzero \
    --repo https://cloudzero.github.io/cloudzero-charts cloudzero-agent \
    --namespace cloudzero --create-namespace -f values.yaml
```

3. Follow the table of contents below for customizing certain capabilities.

* [Labels and Annotations](/docs/k8s-advanced-configuration-labels-and-annotations)
* [Kube-State-Metrics](/docs/k8s-advanced-configuration-ksm)
* [Custom TLS](/docs/k8s-advanced-configuration-tls)
