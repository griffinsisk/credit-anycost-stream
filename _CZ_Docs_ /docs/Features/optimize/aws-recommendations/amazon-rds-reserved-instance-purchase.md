---
title: Amazon RDS Reserved Instance Purchase Recommendations
category: features
createdAt: '2025-10-17T00:00:00.000Z'
hidden: false
slug: Amazon_RDS_Reserved_Instance_purchase_recommendations
updatedAt: '2025-10-17T00:00:00.000Z'
---
<Callout icon="ℹ️">
  **Prerequisite:** To use this check, you must opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html).
</Callout>

This Recommendation identifies Amazon RDS Reserved Instance purchase opportunities based on AWS Trusted Advisor recommendations.

# Overview

AWS Trusted Advisor analyzes your RDS usage patterns to provide Reserved Instance purchase recommendations. This Recommendation surfaces those opportunities to help you identify potential savings through committed usage discounts for RDS database instances.

# What it identifies

* Reserved Instance purchase opportunities for RDS database instances
* Recommended Reserved Instance configurations (instance type, size, engine)
* Estimated monthly savings from purchasing Reserved Instances
* Database-specific purchase recommendations
* Cost optimization opportunities from AWS Cost Optimization Hub

# Key features

* Uses AWS Trusted Advisor's `c1z7kmr11n` check for RDS Reserved Instance recommendations
* Leverages Trusted Advisor's estimated savings calculations
* Provides dynamic titles with specific recommendations and savings percentages
* Covers all RDS database engines (MySQL, PostgreSQL, MariaDB, Oracle, SQL Server)
* Database-level recommendations for targeted optimization

# Cost impact

The recommendation calculates potential savings based on Trusted Advisor's estimates for RDS Reserved Instance purchases, including:

* Up to 69% savings compared to on-demand pricing
* Recommended instance types and sizes
* Expected monthly savings from Reserved Instance commitments
* Database engine-specific optimization opportunities

# Reserved Instance benefits

* **Significant cost savings**: Up to 69% compared to on-demand pricing
* **Predictable billing**: Fixed monthly costs for database instances
* **No upfront payment**: No Upfront option available for flexibility
* **Flexible terms**: 1 or 3-year commitment options
* **Engine coverage**: Available for all major RDS database engines
* **Multi-AZ support**: Reserved Instances work with Multi-AZ deployments

# Database engines supported

* Amazon Aurora (MySQL and PostgreSQL compatible)
* MySQL
* PostgreSQL
* MariaDB
* Oracle
* SQL Server

# Recommended actions

* Review RDS usage patterns to identify consistent workloads
* Consider Reserved Instances for production databases with steady usage
* Evaluate different Reserved Instance terms (1 vs 3 years)
* Plan for database growth when selecting Reserved Instance sizes
* Monitor Reserved Instance coverage to maximize savings
