---
title: Amazon RDS Delete Instances
category: features
createdAt: '2025-10-17T00:00:00.000Z'
hidden: false
slug: Amazon_RDS_Delete_Instances
updatedAt: '2025-10-17T00:00:00.000Z'
---
<Callout icon="ℹ️">
  **Prerequisites:** To use this check, you must opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).
</Callout>

This Recommendation identifies RDS instances that should be deleted to reduce costs.

# What it does

* Identifies RDS instances that are candidates for deletion
* Provides estimated cost savings from deleting unused instances
* Uses AWS Trusted Advisor recommendations to identify optimal deletion targets

# Recommended actions

* Delete RDS instances that are no longer needed
* Create final snapshots before deletion if data needs to be preserved
* Ensure no applications are dependent on the instances
* Review read replicas and other dependent resources before deletion
