---
title: GKE Cost Allocation
category: features
createdAt: '2024-11-01T15:24:58.439Z'
hidden: false
slug: gke-cost-allocation
updatedAt: '2024-12-11T15:24:58.439Z'
---
For users managing workloads in [Google Kubernetes Engine (GKE)](https://cloud.google.com/kubernetes-engine?hl=en), CloudZero offers integrated support to capture and analyze your cost data using Google Cloud's [GKE Cost Allocation](https://cloud.google.com/kubernetes-engine/docs/how-to/cost-allocations) feature.

<Callout icon="📘" theme="info">
  The following limitations apply to GKE Cost Allocation.

  Google Cloud's GKE Cost Allocation feature does not account for [Flexible Committed Use Discounts](https://cloud.google.com/kubernetes-engine/cud). As a result, the cost data shown in CloudZero may not reflect these discounts.

  In addition, GKE Cost Allocation cannot ingest resource usage data, and as a result, it cannot calculate idle cluster costs.
</Callout>

# Enable GKE Cost Allocation in Google Cloud

To enable CloudZero to integrate with GKE Cost Allocation, you must activate the GKE Cost Allocation feature in Google Cloud.

## Prerequisites for CKE Cost Allocation

* [An existing GCP Billing connection in CloudZero](/docs/connections-gcp-billing)
* [Permissions in Google Cloud to create or modify GKE clusters](https://cloud.google.com/kubernetes-engine/docs/concepts/access-control)

## Processes to activate GKE Cost Allocation

Repeat the following processes for each cluster where you plan to activate GKE Cost Allocation:

* To enable GKE Cost Allocation on an _existing cluster_, see [Update a cluster](https://cloud.google.com/kubernetes-engine/docs/how-to/cost-allocations#update_cluster) in the Google Cloud documentation.
* To enable GKE Cost Allocation when you create a _new cluster_, see [Create a new cluster](https://cloud.google.com/kubernetes-engine/docs/how-to/cost-allocations#create_cluster) in the Google Cloud documentation.

The GKE Cost Allocation data will be available in CloudZero after the next billing ingest for the associated GCP project. Note that this can take up to three days.

# View GKE Cost Allocation in CloudZero

After CloudZero has processed your GKE Cost Allocation data, you can [view it in CloudZero](/docs/exploring-container-cost). The example in the following image shows GCP cost data grouped by Kubernetes cluster:

<Image align="center" alt="Viewing GCP cost data grouped by cluster" className="border" border={true} src="https://downloads.cloudzero.com/documentation/resources/gke-groupby-cluster.png" />
