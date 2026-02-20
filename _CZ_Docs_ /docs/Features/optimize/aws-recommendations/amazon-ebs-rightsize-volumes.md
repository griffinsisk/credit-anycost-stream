---
title: Amazon EBS Rightsize Volumes
category: features
createdAt: '2025-10-17T00:00:00.000Z'
hidden: false
slug: Amazon_EBS_Rightsize_Volumes
updatedAt: '2025-10-17T00:00:00.000Z'
---
<Callout icon="ℹ️">
  **Prerequisites:** To use this check, you must opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).
</Callout>

This Recommendation identifies EBS volumes that should be rightsized to optimize cost and performance.

# What it does

* Identifies EBS volumes that are over-provisioned or under-provisioned
* Provides estimated cost savings from rightsizing volumes
* Uses AWS Trusted Advisor recommendations to identify optimal rightsizing targets

# Recommended actions

* Rightsize EBS volumes to match actual storage requirements
* Review volume utilization metrics and I/O patterns
* Consider performance requirements when rightsizing
* Test application performance after rightsizing to ensure requirements are met
