---
title: Amazon RDS Storage Upgrade Recommendations
category: features
createdAt: '2025-10-17T00:00:00.000Z'
hidden: false
slug: Amazon_RDS_storage_Upgrade
updatedAt: '2025-10-17T00:00:00.000Z'
---
<Callout icon="ℹ️">
  **Prerequisites:** To use this check, you must opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).
</Callout>

This Recommendation identifies Amazon RDS database instances where storage can be upgraded to more cost-effective options or better performance tiers.

# What this Recommendation identifies

* RDS database instances using outdated storage types
* Opportunities to upgrade to more cost-effective storage options
* Storage that can benefit from performance improvements

# Recommended actions

* Review current storage type and performance requirements
* Upgrade to more cost-effective storage options
* Consider performance improvements available with newer storage types

# Cost impact

* Reduces storage costs through more efficient storage types
* May improve performance while reducing costs
* Provides long-term cost optimization benefits

# Implementation Effort

Medium - Requires planning for storage migration and potential downtime.

# Additional Notes

* Plan for potential downtime during storage upgrades
* Test upgrade process in non-production environments first
* Consider performance impact of storage changes
* Verify compatibility with current database configuration
