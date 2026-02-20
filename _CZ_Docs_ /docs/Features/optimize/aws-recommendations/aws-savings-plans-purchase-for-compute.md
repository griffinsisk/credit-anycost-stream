---
title: AWS Savings Plans Purchase Recommendations for Compute
category: features
createdAt: '2025-10-17T00:00:00.000Z'
hidden: false
slug: AWS_Savings_Plans_recommendations
updatedAt: '2025-10-17T00:00:00.000Z'
---
<Callout icon="ℹ️">
  **Prerequisite:** To use this check, you must opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html).
</Callout>

This Recommendation identifies AWS Savings Plans purchase opportunities for compute resources based on AWS Trusted Advisor recommendations.

# Overview

AWS Trusted Advisor analyzes your compute usage patterns across Amazon EC2, AWS Fargate, and AWS Lambda to provide Savings Plans purchase recommendations. This Recommendation surfaces those opportunities to help you identify potential savings through committed usage discounts.

# What it identifies

* Savings Plans purchase opportunities for compute resources
* Recommended commitment amounts and terms
* Estimated monthly savings from purchasing Savings Plans
* Account-level purchase recommendations
* Cost optimization opportunities from AWS Cost Optimization Hub

# Key features

* Uses AWS Trusted Advisor's `c1z7kmr09n` check for Savings Plans recommendations
* Leverages Trusted Advisor's estimated savings calculations
* Provides dynamic titles with specific recommendations
* Covers EC2, Fargate, and Lambda compute resources
* Account-level recommendations rather than resource-specific

# Cost impact

The recommendation calculates potential savings based on Trusted Advisor's estimates for Savings Plans purchases, including recommended commitment amounts, terms, and expected monthly savings.
