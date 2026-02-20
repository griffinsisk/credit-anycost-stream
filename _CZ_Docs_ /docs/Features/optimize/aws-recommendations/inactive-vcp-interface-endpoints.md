---
title: Delete Inactive VPC Interface Endpoint
category: features
createdAt: '2025-10-17T00:00:00.000Z'
hidden: false
slug: Inactive_VPC_interface_endpoints
updatedAt: '2025-10-17T00:00:00.000Z'
---
This Recommendation identifies VPC interface endpoints that appear to be inactive and could be deleted to reduce costs.

# Overview

AWS Trusted Advisor monitors your VPC interface endpoints and identifies endpoints that have processed 0 bytes of data in the last 30 days. VPC interface endpoints incur hourly charges and data processing costs even when not actively used, making inactive endpoints a source of unnecessary spending.

# What it identifies

* VPC interface endpoints with 0 bytes processed in the last 30 days
* Unused PrivateLink connections that are still incurring hourly charges
* Endpoints that may have been created for testing or temporary use
* Opportunities to consolidate endpoints using centralized architectures

# Recommended actions

* Delete VPC interface endpoints that have not been used in the last 30 days
* Review your architecture to ensure endpoints are still needed
* Consider deploying VPC interface endpoints in a centralized architecture using Transit Gateway to reduce hourly charges on inactive endpoints
* Verify that applications no longer require the endpoint before deletion

# Key features

* Uses AWS Trusted Advisor's `c2vlfg0jp6` check for inactive VPC endpoints
* Identifies endpoints with zero data transfer over 30 days
* Provides endpoint IDs, VPC IDs, and subnet information for easy identification
* Focuses on reducing unnecessary hourly endpoint charges

# Cost impact

While individual VPC interface endpoints may have modest hourly costs, these charges accumulate over time and across multiple endpoints. Deleting inactive endpoints eliminates ongoing hourly charges and helps maintain a clean, cost-effective network architecture.
