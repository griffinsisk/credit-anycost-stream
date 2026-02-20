---
title: Kubernetes
category: features
createdAt: '2020-06-30T12:59:00.082Z'
hidden: false
slug: container-cost-track
updatedAt: '2024-12-11T15:24:58.439Z'
---
CloudZero combines container usage data with your cloud provider costs to give you accurate allocation of costs within a Kubernetes cluster.

Pod CPU and memory usage are automatically correlated with costs to give you detailed breakdowns of real cost by cluster, namespace, workload, or label down to the hour.

In addition, CloudZero does not require you to manually define complex rules for allocating Kubernetes costs. CloudZero uses a proprietary [algorithm](#how-kubernetes-cost-allocation-works) that automatically calculates costs based on industry best practices and CloudZero's experience working with customers.

# Kubernetes integration methods

CloudZero supports three methods of ingesting Kubernetes data:

* **Recommended:** [CloudZero Agent for Kubernetes](/docs/installation-of-cloudzero-agent-for-kubernetes)
* [AWS Elastic Kubernetes Service Split Cost Allocation Data (EKS SCAD)](/docs/eks-scad-support)
* [Google Kubernetes Engine (GKE) Cost Allocation](/docs/gke-cost-allocation)

<Callout icon="ℹ️" theme="info">
  CloudZero does not support **ECS SCAD**. Only EKS SCAD is supported.
</Callout>

The following table summarizes the differences between these methods:

| **Attribute**                             | **CloudZero Agent for Kubernetes**                                                                             | **EKS SCAD**                                                                                                                                                                     | **GKE Cost Allocation** |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| Supported platforms                       | Self-managed Kubernetes, AWS EKS, Azure Kubernetes Service (AKS), Google Cloud GKE                             | AWS EKS only                                                                                                                                                                     | Google Cloud GKE only   |
| Setup method                              | Install an agent on your clusters                                                                              | Enable a setting in AWS                                                                                                                                                          | Enable a setting in GCP |
| Data types collected                      | Resource usage data                                                                                            | **EKS SCAD with AMP:** Resource usage data, including resource requests and actual utilization. **EKS SCAD without AMP:** Resource usage data, including resource requests only. | Cost data               |
| Calculation of idle costs                 | Yes                                                                                                            | Yes                                                                                                                                                                              | No                      |
| Kubernetes labels and annotations support | Labels and annotations for Pods, Deployments, StatefulSets, DaemonSets, Jobs, CronJobs, Nodes, and Namespaces. | None                                                                                                                                                                             | Labels for Pods         |

Note that an organization is limited to **300** labels, annotations, and tags across all Kubernetes integrations. This is separate from and does not count toward the 300-tag limit for non-Kubernetes resources in the organization.

# How Kubernetes cost allocation works

For all integration methods except [GKE Cost Allocation](/docs/gke-cost-allocation), Kubernetes cost allocation is based on the cost of the node combined with pod-level CPU and memory usage, calculated using a custom cost model that CloudZero developed. This allows CloudZero to assign a portion of the node’s total cost to the pod. This is handled automatically in the CloudZero platform; there is no need for manual allocation rules.

Generally speaking, this proportional algorithm works across a broad range of instance types, including those with SSD, NVMe SSD, and networking enhancements.

The final result is a new way to explore your container costs over time by cluster, workload, namespace, or label using CloudZero. For example, you can use CloudZero to look at one of your clusters and see how its costs decrease as we scale down the cluster.

# Cluster idle costs

The CloudZero platform considers an instance's CPU or memory fully utilized in a given hour if pods running on that instance used or requested (maximum of the two) an average of 75% or more of available capacity. If a smaller amount was used, the difference is assigned to an **Idle** bucket representing the unused capacity of the instances comprising the cluster.

<Callout icon="ℹ️" theme="info">
  The [GKE Cost Allocation](/docs/gke-cost-allocation) integration method **cannot** provide resource usage data or calculate idle costs.
</Callout>

# Kubernetes Dimensions

CloudZero supports the following core Kubernetes dimensions:

* Cluster
* Namespace
* Workload
* Label (for [ingestion methods that support labels](#kubernetes-integration-methods))

For information on how to create Custom Dimensions sourced from core Kubernetes Dimensions, see the [CostFormation Language Reference](/docs/cfdl-reference#kubernetes-dimensions).
