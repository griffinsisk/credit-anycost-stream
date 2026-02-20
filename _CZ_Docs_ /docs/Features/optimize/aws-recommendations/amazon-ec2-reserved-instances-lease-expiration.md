---
title: Amazon EC2 Reserved Instance Lease Expiration
category: features
createdAt: '2025-10-17T00:00:00.000Z'
hidden: false
slug: Amazon_EC2_Reserved_Instance_lease_expiration
updatedAt: '2025-10-17T00:00:00.000Z'
---
This Recommendation identifies Amazon EC2 Reserved Instances that are approaching their lease expiration date and provides recommendations for renewal or replacement.

# Overview

AWS Trusted Advisor monitors your EC2 Reserved Instance leases and identifies those that are approaching expiration. This Recommendation helps you plan for renewals or identify opportunities to optimize your Reserved Instance portfolio before leases expire.

# What it identifies

* EC2 Reserved Instances approaching lease expiration
* Reserved Instances that have expired or will expire soon
* Recommendations for renewal, modification, or replacement
* Cost impact of allowing Reserved Instances to expire
* Opportunities to optimize Reserved Instance coverage

# Key features

* Uses AWS Trusted Advisor's `1e93e4c0b5` check for Reserved Instance lease expiration
* Leverages Trusted Advisor's cost estimates and recommendations
* Provides dynamic titles with specific actions
* Covers all EC2 Reserved Instance types and regions
* Reserved Instance-level recommendations for targeted optimization

# Cost impact

When Reserved Instance leases expire:

* Instances continue running but lose the Reserved Instance discount
* Costs increase to on-demand pricing (up to 72% higher)
* May result in significant cost increases for production workloads
* Opportunity to re-evaluate and optimize Reserved Instance coverage

# Recommended actions

* Review Reserved Instances approaching expiration
* Consider renewing leases for consistent workloads
* Evaluate if Reserved Instances still match current usage patterns
* Consider converting to Savings Plans for more flexibility
* Plan for renewal well before expiration to avoid cost spikes
* Use expiration as an opportunity to optimize Reserved Instance portfolio

# Timing considerations

* Plan renewals 30-60 days before expiration
* Consider usage patterns and workload changes
* Evaluate if Reserved Instances still provide optimal coverage
* Review instance types and sizes for current needs
