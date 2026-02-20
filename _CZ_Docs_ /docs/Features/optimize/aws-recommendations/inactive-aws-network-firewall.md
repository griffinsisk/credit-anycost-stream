---
title: Delete Inactive AWS Network Firewall
category: features
createdAt: '2025-10-17T00:00:00.000Z'
hidden: false
slug: Inactive_AWS_Network_Firewall
updatedAt: '2025-10-17T00:00:00.000Z'
---
This Recommendation identifies AWS Network Firewalls that appear to be inactive and could be deleted to reduce costs.

# Overview

AWS Trusted Advisor monitors your AWS Network Firewalls and identifies firewalls that have processed 0 bytes of data in the last 30 days. Network Firewalls incur significant hourly charges even when not actively processing traffic, making inactive firewalls a major source of unnecessary spending.

# What it identifies

* Network Firewalls with 0 bytes processed in the last 30 days
* Unused firewalls that are still incurring hourly charges
* Firewalls that may have been provisioned but never used or are no longer needed
* Opportunities to eliminate unused network security infrastructure

# Recommended actions

* Delete Network Firewalls that have not processed any traffic in the last 30 days
* Review your VPC security architecture to ensure firewalls are still required
* Verify that the firewall is not being used for security inspection or filtering
* Consider consolidating multiple firewalls if possible
* Confirm with security and network teams before deletion to avoid creating security gaps

# Key features

* Uses AWS Trusted Advisor's `c2vlfg0bfw` check for inactive Network Firewalls
* Identifies firewalls with zero data transfer over 30 days
* Provides Network Firewall ARNs for easy identification
* Focuses on reducing unnecessary hourly firewall charges

# Cost impact

AWS Network Firewalls have substantial hourly charges that accumulate continuously. Each inactive Network Firewall represents significant ongoing waste that can be eliminated immediately. Deleting inactive Network Firewalls provides immediate and substantial cost savings.
