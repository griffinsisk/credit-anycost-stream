---
title: Amazon EC2 Rightsize Instances
category: features
createdAt: '2025-10-17T00:00:00.000Z'
hidden: false
slug: Amazon_EC2_Rightsize_Instances
updatedAt: '2025-10-17T00:00:00.000Z'
---
<Callout icon="ℹ️">
  **Prerequisites:** To use this check, you must opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).
</Callout>

This Recommendation identifies EC2 instances that should be rightsized to optimize cost and performance.

# What it does

* Identifies EC2 instances that are over-provisioned or under-provisioned
* Provides estimated cost savings from rightsizing instances
* Uses AWS Trusted Advisor recommendations to identify optimal rightsizing targets

# Recommended actions

* Rightsize instances to match actual resource utilization
* Review CPU, memory, and network utilization metrics
* Test performance after rightsizing to ensure application requirements are met
* Consider using CloudWatch metrics to validate rightsizing recommendations
