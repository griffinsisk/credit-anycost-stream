---
title: Amazon EC2 Migrate to Graviton
category: features
createdAt: '2025-10-17T00:00:00.000Z'
hidden: false
slug: Amazon_EC2_Migrate_to_Graviton
updatedAt: '2025-10-17T00:00:00.000Z'
---
<Callout icon="ℹ️">
  **Prerequisites:** To use this check, you must opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).
</Callout>

This Recommendation identifies EC2 instances that can be migrated to Graviton-based instances for cost optimization.

# What it does

* Identifies EC2 instances that are candidates for migration to Graviton processors
* Provides estimated cost savings from the migration
* Uses AWS Trusted Advisor recommendations to identify optimal migration targets

# Recommended actions

* Migrate eligible instances to Graviton-based instance types
* Review application compatibility with ARM-based processors
* Test performance and functionality after migration
