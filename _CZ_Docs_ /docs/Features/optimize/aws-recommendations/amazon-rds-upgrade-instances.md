---
title: Amazon RDS Upgrade Instances
category: features
createdAt: '2025-10-17T00:00:00.000Z'
hidden: false
slug: Amazon_RDS_Upgrade_Instances
updatedAt: '2025-10-17T00:00:00.000Z'
---
<Callout icon="ℹ️">
  **Prerequisites:** To use this check, you must opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).
</Callout>

This Recommendation identifies RDS instances that should be upgraded to newer generation types for cost optimization.

# What it does

* Identifies RDS instances that are candidates for upgrading to newer generation types
* Provides estimated cost savings from upgrading to more efficient instance types
* Uses AWS Trusted Advisor recommendations to identify optimal upgrade targets

# Recommended actions

* Upgrade RDS instances to newer generation types for better price-performance
* Review application compatibility with newer instance types
* Plan for maintenance windows during upgrades
* Test performance and functionality after upgrade
* Consider reserved instances for upgraded instances to maximize savings
