---
title: EKS SCAD Support
category: features
createdAt: '2024-11-01T15:24:58.439Z'
hidden: false
slug: eks-scad-support
updatedAt: '2024-12-11T15:24:58.439Z'
---
<Callout icon="ℹ️" theme="info">
  CloudZero recommends using the [CloudZero Agent for Kubernetes](/docs/installation-of-cloudzero-agent-for-kubernetes) to get the clearest view of your Kubernetes costs. The CloudZero Agent is cloud-agnostic and offers more features, including label ingestion, whereas EKS SCAD is more limited.
</Callout>

For users who are managing Kubernetes workloads on the AWS [Elastic Kubernetes Service (EKS)](https://aws.amazon.com/eks/) on EC2, CloudZero offers integrated support to capture resource usage data using the [split cost allocation data (SCAD)](https://docs.aws.amazon.com/cur/latest/userguide/split-cost-allocation-data.html) feature in AWS. Enabling SCAD allows you to allocate Amazon EC2 costs at the Kubernetes pod level by combining usage data from EKS SCAD with billing data from the associated AWS connection.

For more information about SCAD, see [Improve cost visibility of Amazon EKS with AWS Split Cost Allocation Data](https://aws.amazon.com/blogs/aws-cloud-financial-management/improve-cost-visibility-of-amazon-eks-with-aws-split-cost-allocation-data/) on the AWS Blog.

<Callout icon="ℹ️" theme="info">
  CloudZero does not support **ECS SCAD**. Only EKS SCAD is supported.
</Callout>

# Enable SCAD in AWS EKS

To enable CloudZero to integrate with EKS SCAD, you must opt in to SCAD in the [AWS Cost Management Console](https://console.aws.amazon.com/cost-management/home) and select one of the following methods of allocation:

* **By resource requests:** This method allocates your Amazon EC2 costs by Kubernetes pod CPU and memory resource requests only (not actual usage).
* **By resource requests and actual usage:** This method uses [Amazon Managed Service for Prometheus (AMP)](https://docs.aws.amazon.com/prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.html) to allocate your Amazon EC2 costs by Kubernetes pod CPU and memory _resource requests_ or _actual usage_, whichever is higher. You may incur additional costs for setting up and running AMP, which is a prerequisite.

## Prerequisites for SCAD

To enable SCAD you must have the following prerequisites:

* For both methods of EKS SCAD allocation:
  * [An existing AWS connection in CloudZero](/docs/connections-aws-automated)
  * [Permissions in AWS to manage Cost and Billing](https://docs.aws.amazon.com/cost-management/latest/userguide/control-access-billing.html)
* For EKS SCAD allocation using AMP only:
  * [An existing AMP service](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-getting-started.html)
  * [All features enabled for your AWS Organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html)

## Opt in to SCAD

To opt in to SCAD, follow the steps in [Enabling split allocation data](https://docs.aws.amazon.com/cur/latest/userguide/enabling-split-cost-allocation-data.html) in the AWS documentation. Ensure you select the appropriate allocation method during setup, either **Resource requests** or **Amazon Managed Service for Prometheus**.

# View EKS SCAD data in CloudZero

The EKS SCAD data will be available in CloudZero after the next billing ingest for the associated AWS account. Note that this can take up to three days.

After CloudZero has processed your EKS SCAD data, you can [view it in CloudZero](/docs/exploring-container-cost). The example in the following image shows EKS SCAD cost data with the [tag](#cost-allocation-tags-created-for-eks-scad-clusters) key `aws:eks:cluster-name` and value `cz-agent-demo`, grouped by Kubernetes namespace:

<Image align="center" alt="Viewing EKS SCAD cost data grouped by namespace" className="border" border={true} src="https://downloads.cloudzero.com/documentation/resources/explorer-groupby-k8s-eks-namespace.png" />

## Cost Allocation Tags created for EKS SCAD clusters

When you enable EKS SCAD, AWS creates the following cost allocation tags:

* `aws:eks:cluster-name`
* `aws:eks:deployment`
* `aws:eks:namespace`
* `aws:eks:node`
* `aws:eks:workload-name`
* `aws:eks:workload-type`

## Kubernetes labels are not supported

EKS SCAD does not support Kubernetes labels. If you would like to ingest labels from your Kubernetes resources, consider using the [CloudZero Agent for Kubernetes](/docs/installation-of-cloudzero-agent-for-kubernetes).

<br />
