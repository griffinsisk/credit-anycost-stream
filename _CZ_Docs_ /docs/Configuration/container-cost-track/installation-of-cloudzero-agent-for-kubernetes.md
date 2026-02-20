---
title: Install Kubernetes Agent
category: features
createdAt: '2024-07-03T15:21:27.220Z'
hidden: false
slug: installation-of-cloudzero-agent-for-kubernetes
updatedAt: '2024-12-11T15:24:58.439Z'
---
The [CloudZero Agent for Kubernetes](https://github.com/Cloudzero/cloudzero-charts/tree/develop/charts/cloudzero-agent#readme) collects and forwards container metrics to CloudZero, combining them with data from your cloud provider to determine how to allocate your Kubernetes costs.

You can find the [Latest version](https://github.com/Cloudzero/cloudzero-charts/releases) in GitHub.

# Supported Kubernetes installations

The CloudZero Agent supports the following Kubernetes installations:

* Self-managed Kubernetes in AWS, Azure, and Google Cloud
* AWS Elastic Kubernetes Service (EKS)
* Azure Kubernetes Service (AKS)
* Google Kubernetes Engine (GKE)

# Set up the CloudZero Agent

<Callout icon="ℹ️" theme="info">
  CloudZero recommends installing the CloudZero Agent for Kubernetes in the `cloudzero` namespace. Do not install the agent in the default namespace.
</Callout>

## Prerequisites for the CloudZero Agent

* [Helm v3+](https://helm.sh)
* [Kubernetes v1.23+](https://github.com/kubernetes/kubernetes/tags)
* [A CloudZero API key](https://docs.cloudzero.com/reference/authorization#creating-a-new-api-key) with the following scopes:
  * `container-metrics_v1:abandon`
  * `container-metrics_v1:get-status`
  * `container-metrics_v1:legacy`
  * `container-metrics_v1:upload`
  * `insights:read_insights`
* Each Kubernetes cluster must have a route to the internet and a rule that allows egress from the agent to the CloudZero collector endpoint at [https://api.cloudzero.com](https://api.cloudzero.com) on port 443

## Helm installation (recommended)

```shell
helm upgrade --install cloudzero \
    --repo https://cloudzero.github.io/cloudzero-charts cloudzero-agent \
    --namespace cloudzero --create-namespace \
    --set apiKey=<CLOUDZERO_API_KEY>
    --set clusterName=<NAME_OF_YOUR_CLUSTER>
```

## Raw YAML installation

You can run helm template against the CloudZero chart to generate flat manifests that can be deployed directly.

```shell
helm template cloudzero \
    --repo https://cloudzero.github.io/cloudzero-charts cloudzero/cloudzero-agent \
    --namespace cloudzero --create-namespace \
    --set apiKey=<CLOUDZERO_API_KEY>
    --set clusterName=<NAME_OF_YOUR_CLUSTER>

kubectl apply -f cloudzero.yaml
```

## Validating the install

If all went well, you should have received an install success message letting you know that the agent has been installed.

# View CloudZero Agent for Kubernetes Cost Data

After your CloudZero agent is installed, wait at least 48 hours for data collection to occur. Then you can [view it in CloudZero](/docs/exploring-container-cost). For example, the following image shows Kubernetes cost data grouped by cluster:

<Image align="center" alt="Explorer showing Kubernetes cost" border={true} src="https://files.readme.io/77c18f185d131df5e2febea2eb5932d1837cf83b723b462e3fe2835f46984bfc-Explorer-showing-Kubernetes-cost.jpg" className="border" />
