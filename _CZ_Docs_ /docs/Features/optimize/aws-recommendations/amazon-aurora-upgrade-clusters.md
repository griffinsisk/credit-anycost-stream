---
title: Amazon Aurora Upgrade Clusters
category: features
createdAt: '2025-10-17T00:00:00.000Z'
hidden: false
slug: Amazon_Aurora_Upgrade_Clusters
updatedAt: '2025-10-17T00:00:00.000Z'
---
<Callout icon="ℹ️">
  **Prerequisites:** To use this check, you must opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).
</Callout>

This Recommendation identifies Aurora clusters that should be upgraded to newer generation types for cost optimization.

# What it does

* Identifies Aurora clusters that are candidates for upgrading to newer generation types
* Provides estimated cost savings from upgrading to more efficient cluster types
* Uses AWS Trusted Advisor recommendations to identify optimal upgrade targets

# Recommended actions

* Upgrade Aurora clusters to newer generation types for better price-performance
* Review application compatibility with newer cluster types
* Plan for maintenance windows during upgrades
* Test database performance and functionality after upgrade
* Consider Aurora Serverless v2 for variable workloads
* Evaluate the benefits of upgrading to newer Aurora engine versions
