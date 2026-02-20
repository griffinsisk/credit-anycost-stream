---
title: AWS Fargate Cost Optimization Recommendations for Amazon ECS
category: features
createdAt: '2025-10-17T00:00:00.000Z'
hidden: false
slug: AWS_Fargate_cost_optimization_recommendations_for_Amazon_ECS
updatedAt: '2025-10-17T00:00:00.000Z'
---
<Callout icon="ℹ️">
  **Prerequisites:** To use this check, you must opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).
</Callout>

This Recommendation identifies AWS Fargate services with over-provisioned CPU or memory allocations that should be rightsized to optimize costs, based on AWS Trusted Advisor recommendations.

AWS Trusted Advisor analyzes your Fargate service configurations and usage patterns to identify services that are allocated more CPU or memory than they actually need. This surfaces rightsizing recommendations to help you reduce costs while maintaining performance for your containerized workloads.

# What it identifies

* Fargate services with CPU allocations higher than utilization
* Services with memory allocations exceeding actual usage
* Opportunities to reduce Fargate vCPU and memory configurations
* Rightsizing recommendations from AWS Trusted Advisor for ECS services

# Key features

* Uses AWS Trusted Advisor's `c1z7kmr06n` check filtered for rightsizing actions
* Leverages Trusted Advisor's estimated savings calculations
* Provides dynamic titles showing current vs recommended resource configurations
* Focuses specifically on rightsizing over-provisioned Fargate services

# Cost impact

The recommendation calculates potential monthly savings from rightsizing Fargate services to more appropriate CPU and memory allocations, eliminating costs for unused compute resources.
