---
title: Amazon EC2 Stop Instances
category: features
createdAt: '2025-10-17T00:00:00.000Z'
hidden: false
slug: Amazon_EC2_Stop_Instances
updatedAt: '2025-10-17T00:00:00.000Z'
---
<Callout icon="ℹ️">
  **Prerequisites:** To use this check, you must opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).
</Callout>

This Recommendation identifies EC2 instances that should be stopped to reduce costs.

# What it does

* Identifies EC2 instances that are candidates for stopping
* Provides estimated cost savings from stopping unused instances
* Uses AWS Trusted Advisor recommendations to identify optimal stop targets

# Recommended actions

* Stop instances that are not actively being used
* Review instance usage patterns before stopping
* Consider using scheduled stop/start for development instances
* Implement automated stop policies for non-production environments
