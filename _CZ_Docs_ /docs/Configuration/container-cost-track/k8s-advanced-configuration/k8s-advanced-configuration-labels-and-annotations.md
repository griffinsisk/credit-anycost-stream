---
title: Kubernetes Labels and Annotations
category: features
createdAt: '2024-07-03T15:21:27.220Z'
hidden: false
slug: k8s-advanced-configuration-labels-and-annotations
updatedAt: '2024-12-11T15:24:58.439Z'
---
The CloudZero agent for Kubernetes requires you to allowlist the labels and annotations that you would like to use in the CloudZero platform.

This is an advanced configuration setting. Refer to the [Advanced Configuration](/docs/k8s-advanced-configuration) section of the documentation to get started.

<Callout icon="⚠️" theme="warn">
  CloudZero limits you to 300 Kubernetes labels and annotations in the platform. Enabling any more than 300 will result in extra labels and annotations being dropped.

  Annotations and labels on resources other than pods are only supported in CloudZero agent versions post-1.0.0.
</Callout>

# Add labels

The steps to add labels follow:

1. Add the following to your `values.yaml` file and re-deploy.

```yaml values.yaml
insightsController:
  labels:
    # -- This value MUST be set to a list of regular expressions which will be used to gather labels from pods, deployments, statefulsets, daemonsets, cronjobs, jobs, nodes, and namespaces
    patterns:
    #    By default, only the app.kubernetes.io/component label is captured. Use the examples below to add others.
      - 'app.kubernetes.io/component'
    # - '^foo' -- Match all labels whose key starts with "foo"
    # - 'bar$' -- Match all labels whose key ends with "bar"
    # -- Labels are gathered from pods and namespaces by default.
    # -- Other supported resource types are: deployments, statefulsets, nodes, jobs, cronjobs, daemonsets
    resources:
      pods: true
      namespaces: true
```

2. Re-deploy the Agent with your updated values file.

```shell
helm upgrade --install cloudzero \
    --repo https://cloudzero.github.io/cloudzero-charts cloudzero-agent \
    --namespace cloudzero --create-namespace -f values.yaml
```

# Add annotations

1. Add the following to your `values.yaml` file and re-deploy.

```yaml values.yaml
insightsController:
  annotations:
    # -- By default, annotations are not captured. Set enabled:true to capture them.
    enabled: true
    # -- This value MUST be set to a list of regular expressions which will be used to gather annotations from pods, deployments, statefulsets, daemonsets, cronjobs, jobs, nodes, and namespaces
    patterns:
     - '.*' # -- Capture all annotations
    # -- Other supported resource types are: deployments, statefulsets, nodes, jobs, cronjobs, daemonsets
    resources:
      pods: true
      namespaces: true
```

2. Re-deploy the Agent with your updated values file.

```shell
helm upgrade --install cloudzero \
    --repo https://cloudzero.github.io/cloudzero-charts cloudzero-agent \
    --namespace cloudzero --create-namespace -f values.yaml
```
