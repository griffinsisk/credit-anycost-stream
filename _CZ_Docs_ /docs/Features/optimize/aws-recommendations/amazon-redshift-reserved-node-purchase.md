---
title: Amazon Redshift Reserved Node Purchase Recommendations
category: features
createdAt: '2025-10-17T00:00:00.000Z'
hidden: false
slug: Amazon_Redshift_reserved_node_purchase_recommendations
updatedAt: '2025-10-17T00:00:00.000Z'
---
<Callout icon="ℹ️">
  **Prerequisite:** To use this check, you must opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html).
</Callout>

This Recommendation identifies Redshift Reserved Node purchase opportunities based on AWS Trusted Advisor recommendations.

# What it does

AWS Trusted Advisor analyzes your Amazon Redshift usage patterns and recommends Reserved Node purchases that can reduce your data warehouse costs. This Recommendation surfaces those recommendations to help you optimize your Reserved Node portfolio for consistent workloads.

# Recommended actions

* Purchase Reserved Nodes for Redshift clusters with consistent usage patterns.
* Consider 1-year or 3-year term options based on workload stability.
* Evaluate payment options (All Upfront, Partial Upfront, No Upfront).
* Review node types and sizes to ensure optimal capacity planning.
* Consider Reserved Node purchases for both leader and compute nodes.

# Cost impact

Reserved Nodes can provide significant savings compared to On-Demand pricing for consistent workloads. The cost impact represents the potential monthly savings from implementing the recommended Reserved Node purchases.
