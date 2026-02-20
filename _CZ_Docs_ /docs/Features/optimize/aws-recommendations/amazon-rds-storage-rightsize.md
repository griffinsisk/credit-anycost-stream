---
title: Amazon RDS Storage Rightsize Recommendations
category: features
createdAt: '2025-10-17T00:00:00.000Z'
hidden: false
slug: Amazon_RDS_storage_Rightsize
updatedAt: '2025-10-17T00:00:00.000Z'
---
<Callout icon="ℹ️">
  **Prerequisites:** To use this check, you must opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).
</Callout>

This Recommendation identifies Amazon RDS database instances with storage that can be rightsized to reduce costs while maintaining performance.

# What this Recommendation identifies

* RDS database instances with over-provisioned storage
* Opportunities to reduce storage allocation to match actual usage
* Potential cost savings from rightsizing storage

# Recommended actions

* Review current storage utilization patterns
* Rightsize storage allocation to match actual usage
* Monitor performance after rightsizing to ensure no impact

# Cost impact

* Reduces storage costs by eliminating over-provisioned capacity
* Maintains database performance while optimizing costs
* Provides immediate cost savings on storage charges

# Implementation effort

Medium - Requires careful analysis of usage patterns and testing in non-production environments first.

# Additional notes

* Always test storage changes in non-production environments first
* Monitor database performance after rightsizing
* Consider future growth when determining new storage allocation
