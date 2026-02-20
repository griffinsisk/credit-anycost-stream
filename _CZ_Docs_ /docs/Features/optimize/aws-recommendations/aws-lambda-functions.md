---
title: AWS Lambda Cost Optimization Recommendations for Functions
category: features
createdAt: '2025-10-17T00:00:00.000Z'
hidden: false
slug: AWS_Lambda_cost_optimization
updatedAt: '2025-10-17T00:00:00.000Z'
---
<Callout icon="ℹ️">
  **Prerequisites:** To use this check, you must opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).
</Callout>

This Recommendation identifies AWS Lambda functions that have cost optimization opportunities based on AWS Trusted Advisor recommendations.

# Overview

AWS Trusted Advisor continuously monitors your Lambda functions and provides recommendations for cost optimization opportunities. This Recommendation surfaces those recommendations to help you identify potential savings.

# What it identifies

* Lambda functions with cost optimization opportunities
* Functions that could benefit from memory allocation adjustments
* Underutilized Lambda functions that could be optimized
* Function configuration optimizations
* Cost optimization recommendations from AWS Trusted Advisor

# Key features

* Uses AWS Trusted Advisor's `c1z7kmr05n` check for Lambda cost optimization
* Leverages Trusted Advisor's estimated savings calculations
* Provides dynamic titles with specific recommendations and resource IDs
* Focuses on Lambda service costs and function-specific optimizations

# Cost impact

The recommendation calculates potential savings based on Trusted Advisor's estimates for cost optimization opportunities in Lambda functions, including memory allocation, timeout settings, and other function-specific optimizations.
