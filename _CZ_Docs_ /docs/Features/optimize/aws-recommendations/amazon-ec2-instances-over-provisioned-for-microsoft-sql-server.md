---
title: Amazon EC2 Instance Over-Provisioned for Microsoft SQL Server
category: features
createdAt: '2025-10-17T00:00:00.000Z'
hidden: false
slug: Amazon_EC2_instances_over_provisioned_for_Microsoft_SQL_Server
updatedAt: '2025-10-17T00:00:00.000Z'
---
This Recommendation identifies EC2 instances running Microsoft SQL Server that have more vCPUs than needed for SQL Server licensing, presenting opportunities to rightsize to smaller instance types and reduce costs.

# What it does

This Recommendation analyzes your EC2 instances running Microsoft SQL Server and identifies cases where:

* Instances have more vCPUs than the maximum recommended for the SQL Server workload
* The instance can be rightsized to a smaller, less expensive instance type
* SQL Server licensing costs can be reduced by using instances with fewer vCPUs

AWS Trusted Advisor provides:

* Current instance type and vCPU count
* Maximum recommended vCPU count based on workload analysis
* Recommended instance type to rightsize to
* Estimated monthly savings from rightsizing

# Why it matters

* **Cost Savings**: Rightsizing over-provisioned instances can lead to significant infrastructure savings
* **License Optimization**: SQL Server licensing is typically core-based; fewer vCPUs mean lower licensing costs
* **Efficiency**: Running appropriately sized instances improves resource utilization across your infrastructure
* **Performance**: Properly sized instances can actually improve performance by reducing unnecessary resource overhead

# Recommended actions

1. **Review Recommendations**: Examine each flagged instance, noting:
   * Current instance type and vCPU count
   * Maximum recommended vCPU count
   * Recommended instance type
   * Estimated monthly savings
   * SQL Server edition in use

2. **Analyze Workload Patterns**: Before rightsizing:
   * Review CPU utilization metrics over time
   * Identify peak usage periods
   * Verify that the recommended instance size can handle peak loads
   * Consider seasonal or cyclical workload variations

3. **Plan the Migration**: Develop a rightsizing strategy:
   * Prioritize instances with highest savings potential
   * Group similar workloads for batch processing
   * Schedule changes during maintenance windows
   * Prepare rollback procedures

4. **Test in Non-Production**: Before production changes:
   * Test the recommended instance type in dev/staging environments
   * Validate SQL Server performance with realistic workloads
   * Verify application behavior under load
   * Test backup and recovery procedures

5. **Execute Rightsizing**: During scheduled maintenance:
   * Stop the EC2 instance
   * Change the instance type to the recommended size
   * Start the instance and verify SQL Server starts correctly
   * Test application connectivity
   * Monitor performance for anomalies

6. **Monitor Post-Change**: After rightsizing:
   * Track CPU and memory utilization closely
   * Monitor SQL Server performance metrics
   * Verify application response times remain acceptable
   * Document any issues and adjustments made

# Additional Considerations

* **Burst Workloads**: If your workload has significant burst patterns, ensure the recommended instance type can handle peak loads
* **Licensing Compliance**: Verify that downsizing maintains compliance with Microsoft SQL Server licensing requirements
* **High Availability**: Consider the impact on your HA/DR strategy when changing instance types
* **Stop/Start Impact**: Changing instance types requires stopping the instance, which will cause downtime
* **Elastic IPs**: If using Elastic IPs, they will be retained when changing instance types
* **Instance Store**: If using instance store volumes, be aware that data will be lost when stopping the instance (EBS-backed volumes are preserved)
* **Performance Testing**: Always conduct thorough performance testing before and after rightsizing to ensure the new instance type meets your requirements
