---
title: Amazon Aurora Delete Clusters
category: features
createdAt: '2025-10-17T00:00:00.000Z'
hidden: false
slug: Amazon_Aurora_Delete_Clusters
updatedAt: '2025-10-17T00:00:00.000Z'
---
<Callout icon="ℹ️">
  **Prerequisites:** To use this check, you must opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).
</Callout>

This Recommendation identifies Aurora clusters that should be deleted to reduce costs.

# What it does

* Identifies Aurora clusters that are candidates for deletion
* Provides estimated cost savings from deleting unused clusters
* Uses AWS Trusted Advisor recommendations to identify optimal deletion targets

# Recommended actions

* Delete Aurora clusters that are no longer needed
* Create final snapshots before deletion if data needs to be preserved
* Ensure no applications are dependent on the clusters
* Review Aurora Serverless v1 clusters that may be candidates for deletion
* Consider the impact on read replicas and other dependent resources
