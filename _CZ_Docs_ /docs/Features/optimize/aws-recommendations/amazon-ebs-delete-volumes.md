---
title: Amazon EBS Delete Volumes
category: features
createdAt: '2025-10-17T00:00:00.000Z'
hidden: false
slug: Amazon_EBS_Delete_Volumes
updatedAt: '2025-10-17T00:00:00.000Z'
---
<Callout icon="ℹ️">
  **Prerequisites:** To use this check, you must opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).
</Callout>

This Recommendation identifies EBS volumes that should be deleted to reduce costs.

# What it does

* Identifies EBS volumes that are candidates for deletion
* Provides estimated cost savings from deleting unused volumes
* Uses AWS Trusted Advisor recommendations to identify optimal deletion targets

# Recommended actions

* Delete EBS volumes that are no longer needed
* Review volume snapshots before deletion
* Ensure volumes are not attached to running instances
* Consider creating snapshots for important data before deletion
