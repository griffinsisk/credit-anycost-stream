---
title: Delete Idle Load Balancer
category: features
createdAt: '2025-10-17T00:00:00.000Z'
hidden: false
slug: Amazon_Load_Balancer_Idle_Instances_classic
updatedAt: '2025-10-17T00:00:00.000Z'
---
This Recommendation identifies AWS Classic Load Balancers (ELBs) that are idle and can be deleted to reduce costs.

# What it does

This Recommendation uses AWS Trusted Advisor data to identify Classic Load Balancers that have been idle for an extended period. These load balancers continue to incur charges even when not actively serving traffic.

# Why it matters

* **Cost Savings**: Idle ELBs incur hourly charges even when not in use
* **Resource Cleanup**: Helps maintain a clean AWS environment
* **Security**: Reduces attack surface by removing unused resources

# Recommended actions

1. **Review**: Verify the ELB is truly unused by checking application logs and monitoring
2. **Backup**: Document the ELB configuration before deletion
3. **Delete**: Remove the idle ELB through AWS Console or CLI
4. **Monitor**: Ensure no applications were depending on the deleted ELB
