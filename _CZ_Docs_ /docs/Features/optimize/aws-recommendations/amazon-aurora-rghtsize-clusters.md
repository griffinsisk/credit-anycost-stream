---
title: Amazon Aurora Rightsize Clusters
category: features
createdAt: '2025-10-17T00:00:00.000Z'
hidden: false
slug: Amazon_Aurora_Rightsize_Clusters
updatedAt: '2025-10-17T00:00:00.000Z'
---
<Callout icon="ℹ️">
  **Prerequisites:** To use this check, you must opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).
</Callout>

This Recommendation identifies Aurora clusters that should be rightsized to optimize cost and performance.

# What it does

* Identifies Aurora clusters that are over-provisioned or under-provisioned
* Provides estimated cost savings from rightsizing clusters
* Uses AWS Trusted Advisor recommendations to identify optimal rightsizing targets

# Recommended actions

* Rightsize Aurora clusters to match actual resource utilization
* Review CPU, memory, and I/O utilization metrics
* Consider performance requirements when rightsizing
* Test application performance after rightsizing to ensure requirements are met
* Monitor Aurora cluster performance metrics during and after rightsizing
* Consider Aurora Serverless v2 for variable workloads that may benefit from auto-scaling
