---
title: Delete Inactive Gateway Load Balancer Endpoint
category: features
createdAt: '2025-10-17T00:00:00.000Z'
hidden: false
slug: Inactive_Gateway_Load_Balancer_endpoints
updatedAt: '2025-10-17T00:00:00.000Z'
---
This Recommendation identifies Gateway Load Balancer endpoints that appear to be inactive and could be deleted to reduce costs.

# Overview

AWS Trusted Advisor monitors your Gateway Load Balancer (GWLB) endpoints and identifies endpoints that have processed 0 bytes of data in the last 30 days. Gateway Load Balancer endpoints incur hourly charges even when not actively processing traffic, making inactive endpoints a source of unnecessary spending.

# What it identifies

* Gateway Load Balancer endpoints with 0 bytes processed in the last 30 days
* Unused GWLB endpoints that are still incurring hourly charges
* Endpoints that may have been created for testing or temporary use
* Opportunities to clean up unused network infrastructure

# Recommended actions

* Delete Gateway Load Balancer endpoints that have not been used in the last 30 days
* Review your network architecture to ensure endpoints are still needed
* Verify that security appliances or inspection services no longer require the endpoint
* Confirm with application teams before deletion to avoid service disruption

# Key features

* Uses AWS Trusted Advisor's `c2vlfg0k35` check for inactive GWLB endpoints
* Identifies endpoints with zero data transfer over 30 days
* Provides endpoint IDs and ARNs for easy identification
* Focuses on reducing unnecessary hourly endpoint charges

# Cost impact

Gateway Load Balancer endpoints incur hourly charges that accumulate over time. Deleting inactive endpoints eliminates ongoing hourly charges and helps maintain a clean, cost-effective network architecture. While individual endpoint costs may be modest, multiple inactive endpoints can represent significant unnecessary spending.
