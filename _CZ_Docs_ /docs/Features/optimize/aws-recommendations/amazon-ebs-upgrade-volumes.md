---
title: Amazon EBS Upgrade Volumes
category: features
createdAt: '2025-10-17T00:00:00.000Z'
hidden: false
slug: Amazon_EBS_Upgrade_Volumes
updatedAt: '2025-10-17T00:00:00.000Z'
---
<Callout icon="ℹ️">
  **Prerequisites:** To use this check, you must opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).
</Callout>

This Recommendation identifies EBS volumes that should be upgraded to newer generation types for cost optimization.

# What it does

* Identifies EBS volumes that are candidates for upgrading to newer generation types
* Provides estimated cost savings from upgrading to more efficient volume types
* Uses AWS Trusted Advisor recommendations to identify optimal upgrade targets

# Recommended actions

* Upgrade EBS volumes to newer generation types (e.g., gp3 instead of gp2)
* Review performance requirements before upgrading
* Test application performance after upgrade
* Consider the trade-offs between cost and performance
