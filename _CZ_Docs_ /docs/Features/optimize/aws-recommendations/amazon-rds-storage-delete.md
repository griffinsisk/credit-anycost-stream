---
title: Amazon RDS Storage Delete Recommendations
category: features
createdAt: '2025-10-17T00:00:00.000Z'
hidden: false
slug: Amazon_RDS_storage_Delete
updatedAt: '2025-10-17T00:00:00.000Z'
---
<Callout icon="ℹ️">
  **Prerequisites:** To use this check, you must opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).
</Callout>

This Recommendation identifies Amazon RDS database instances with storage that can be deleted to reduce costs, typically for unused or redundant storage.

# What this Recommendation identifies

* RDS database instances with unused storage allocations
* Redundant storage that can be safely removed
* Opportunities to eliminate unnecessary storage costs

# Recommended actions

* Review storage utilization and identify unused allocations
* Delete unused or redundant storage
* Clean up orphaned storage resources

# Cost impact

* Eliminates ongoing storage costs for unused capacity
* Provides immediate cost savings
* Reduces overall RDS storage expenses

# Implementation effort

Medium - Requires careful verification that storage is truly unused and safe to delete.

# Additional notes

* Ensure storage is truly unused before deletion
* Verify no dependencies exist before removing storage
* Consider backup requirements before deletion
* Test deletion process in non-production environments first
