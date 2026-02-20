---
title: Amazon DynamoDB Reserved Capacity Purchase Recommendations
category: features
createdAt: '2025-10-17T00:00:00.000Z'
hidden: false
slug: Amazon_DynamoDB_reserved_capacity_purchase_recommendations
updatedAt: '2025-10-17T00:00:00.000Z'
---
<Callout icon="ℹ️">
  **Prerequisite:** To use this check, you must opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html).
</Callout>

This Recommendation identifies Amazon DynamoDB reserved capacity purchase opportunities based on AWS Trusted Advisor recommendations.

# Overview

AWS Trusted Advisor analyzes your DynamoDB usage patterns to provide reserved capacity purchase recommendations. This Recommendation surfaces those opportunities to help you identify potential savings through committed usage discounts for DynamoDB read and write capacity units.

# What it identifies

* Reserved capacity purchase opportunities for DynamoDB tables
* Recommended reserved capacity amounts for read and write units
* Estimated monthly savings from purchasing reserved capacity
* Table-specific purchase recommendations
* Cost optimization opportunities from AWS Cost Optimization Hub

# Key features

* Uses AWS Trusted Advisor's `c1z7kmr15n` check for DynamoDB reserved capacity recommendations
* Leverages Trusted Advisor's estimated savings calculations
* Provides dynamic titles with specific recommendations
* Covers DynamoDB read and write capacity units
* Table-level recommendations for targeted optimization

# Cost impact

The recommendation calculates potential savings based on Trusted Advisor's estimates for DynamoDB reserved capacity purchases, including recommended capacity amounts, terms, and expected monthly savings compared to on-demand pricing.

# Reserved capacity benefits

* Up to 70% savings compared to on-demand pricing
* Predictable billing for consistent workloads
* No upfront payment required (No Upfront option available)
* Flexible terms (1 or 3 years)
* Automatic application to matching tables
