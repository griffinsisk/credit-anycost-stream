---
title: Amazon EC2 Instances Stopped
category: features
createdAt: '2025-10-17T00:00:00.000Z'
hidden: false
slug: Amazon_EC2_instances_stopped
updatedAt: '2025-10-17T00:00:00.000Z'
---
This Recommendation identifies Amazon EC2 instances that are currently stopped and may be candidates for termination to reduce costs.

# Overview

AWS Trusted Advisor monitors your EC2 instances and identifies those that are in a stopped state. While stopped instances don't incur compute charges, they may still have associated costs from EBS volumes, Elastic IP addresses, and other resources that continue to be billed.

# What it identifies

* EC2 instances that are currently stopped
* Instances that have been stopped for extended periods
* Associated resources that may still be incurring costs
* Opportunities to terminate unused stopped instances
* Cost optimization recommendations from AWS Trusted Advisor

# Key features

* Uses AWS Trusted Advisor's `c18d2gz150` check for stopped EC2 instances
* Leverages Trusted Advisor's cost estimates and recommendations
* Provides dynamic titles with specific actions
* Covers all EC2 instance types and regions
* Instance-level recommendations for targeted optimization

# Cost impact

While stopped instances don't incur compute charges, they may still have associated costs from:

* EBS volumes (storage costs)
* Elastic IP addresses (if not attached to running instances)
* Data transfer costs
* Other associated resources

Terminating unused stopped instances can eliminate these ongoing costs.

# Recommended actions

* Review stopped instances to determine if they are still needed
* Check for associated EBS volumes and other resources
* Consider terminating instances that are no longer required
* Verify no critical data will be lost before termination
* Use this as an opportunity to clean up unused resources
