---
title: Kube-State-Metrics
category: features
createdAt: '2024-07-03T15:21:27.220Z'
hidden: false
slug: k8s-advanced-configuration-ksm
updatedAt: '2024-12-11T15:24:58.439Z'
---
<Callout icon="❗️" theme="error">
  CloudZero does  not recommend using a custom kube-state-metrics. This can lead to silent data loss and inaccurate data.

  By default, CloudZero uses a preconfigured version of kube-state-metrics that is tuned and isolated to CloudZero's install. We recommend using the CloudZero default version of kube-state-metrics.
</Callout>

The CloudZero Agent for Kubernetes requires an instance of kube-state-metrics. By default, the CloudZero Agent will take care of this. However, by following these advanced configuration steps, you can point the Agent at your own instance of kube-state-metrics, though it is **not recommended**.

1. Add the following to your `values.yaml` file and re-deploy.

```yaml values.yaml
  kubeStateMetrics:
    # Set enabled:false to disable the built in KSM
    enabled: false
    # Disable CloudZero KSM as a Scrape Target since the service endpoint is explicitly defined
    # by the Validators config file.
    prometheusScrape: false
    # Overriding static scrape target address for an existing KSM.
    # Set to service <service-name>.<namespace>.svc.cluster.local:port if built-in is disabled (`enabled=false` above)
    targetOverride: <URL_TO_YOUR_KSM>
```

2. Re-deploy the Agent with your updated values file.

```shell
helm upgrade --install cloudzero \
    --repo https://cloudzero.github.io/cloudzero-charts cloudzero-agent \
    --namespace cloudzero --create-namespace -f values.yaml
```
