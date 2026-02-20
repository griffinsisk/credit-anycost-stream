---
title: Underutilized Amazon Redshift Clusters
category: features
createdAt: '2025-10-17T00:00:00.000Z'
hidden: false
slug: Underutilized_Amazon_Redshift_Clusters
updatedAt: '2025-10-17T00:00:00.000Z'
---
This Recommendation identifies Amazon Redshift clusters that are underutilized and could benefit from optimization, based on AWS Trusted Advisor recommendations.

# Overview

AWS Trusted Advisor analyzes your Redshift cluster usage patterns and identifies clusters that are not being fully utilized. This surfaces recommendations to help you optimize your data warehouse resources and reduce costs for underutilized infrastructure.

# What it identifies

* Redshift clusters with low CPU utilization
* Clusters with minimal query activity
* Underutilized storage and compute resources
* Clusters that may be candidates for downsizing or deletion

# Key features

* Uses AWS Trusted Advisor's `G31sQ1E9U` check for underutilized Redshift clusters
* Leverages Trusted Advisor's estimated savings calculations
* Provides dynamic titles with specific recommended actions

# Cost impact

The recommendation calculates potential monthly savings from optimizing underutilized Redshift clusters, helping you eliminate costs for unused or underutilized data warehouse capacity.
