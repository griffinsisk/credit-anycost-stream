---
title: AWS Fargate Cost Optimization Delete Recommendations for Amazon ECS
category: features
createdAt: '2025-10-17T00:00:00.000Z'
hidden: false
slug: AWS_Fargate_cost_optimization_delete_recommendations_for_Amazon_ECS
updatedAt: '2025-10-17T00:00:00.000Z'
---
This Recommendation identifies unused or idle AWS Fargate services that should be deleted to eliminate unnecessary costs, based on AWS Trusted Advisor recommendations.

# Overview

AWS Trusted Advisor monitors your Fargate services for activity patterns and identifies services that appear to be unused or idle. This surfaces deletion recommendations to help you clean up unnecessary container infrastructure and stop incurring costs for services that are no longer needed.

# What it identifies

* Fargate services with no recent task executions
* Idle Fargate services that are running but not processing workloads
* Services that have been inactive for extended periods
* Delete recommendations from AWS Trusted Advisor for unused Fargate services

# Key features

* Uses AWS Trusted Advisor's `c1z7kmr06n` check filtered for delete actions
* Leverages Trusted Advisor's estimated savings calculations
* Provides clear titles identifying the specific unused service that should be removed
* Focuses specifically on eliminating costs from idle Fargate infrastructure

# Cost impact

The recommendation calculates potential monthly savings from deleting unused Fargate services, helping you eliminate all ongoing costs associated with idle container infrastructure including CPU, memory, and data transfer charges.
