---
title: RDS Clusters Incurring Extended Support Charges
category: features
createdAt: '2025-12-01T00:00:00.000Z'
hidden: false
slug: rds-clusters-incurring-extended-support-charges
updatedAt: '2025-12-01T00:00:00.000Z'
---
CloudZero has identified Amazon RDS database instances and clusters that are running on outdated engine versions and incurring AWS extended support charges. These charges apply when you continue running RDS database engines beyond their standard support end date.

AWS extended support fees can add significant costs to your RDS spending—often 50-100% more than the base instance cost for older engine versions. By upgrading to a supported engine version, you can eliminate these charges entirely while also benefiting from security patches, bug fixes, and performance improvements.

## What it does

This recommendation identifies RDS resources that are:
- Running database engine versions that are past their standard support period
- Incurring AWS extended support charges (typically identified by "ExtendedSupport" in usage types or line item descriptions)
- Eligible for upgrade to newer, supported engine versions without extended support fees

Common database engines affected include:
- MySQL 5.7 and earlier versions
- PostgreSQL 11 and earlier versions
- MariaDB 10.3 and earlier versions
- Oracle database versions past their support dates
- SQL Server versions past their support dates

## Why it matters

- **Cost Savings**: Extended support charges can double your RDS costs for affected instances—upgrading eliminates these fees completely
- **Security**: Newer engine versions receive active security patches and vulnerability fixes
- **Performance**: Modern database versions include performance optimizations and new features
- **Compliance**: Many compliance frameworks require running currently supported software versions
- **Future-Proofing**: Avoiding technical debt by staying on supported versions

## Recommended Actions

1. **Review Affected Resources**: Identify all RDS instances/clusters incurring extended support charges and their current engine versions

2. **Plan Upgrades**: For each affected resource:
   - Check AWS documentation for the upgrade path to the latest supported version
   - Review application compatibility with newer database versions
   - Identify any deprecated features your application may be using
   - Plan maintenance windows for the upgrade

3. **Test in Non-Production**: Before upgrading production databases:
   - Restore a snapshot to a test environment
   - Upgrade the test instance to the target version
   - Run application regression tests
   - Verify query performance and compatibility
   - Test backup and restore procedures

4. **Perform Upgrades**: Execute the upgrade during scheduled maintenance windows:
   - For minor version upgrades: can often be done with minimal downtime
   - For major version upgrades: may require more planning and testing
   - Use RDS Blue/Green deployments for zero-downtime upgrades when available
   - Take a manual snapshot before upgrading as a safety measure

5. **Monitor Post-Upgrade**: After upgrading:
   - Verify application connectivity and functionality
   - Monitor database performance metrics
   - Check for any application errors or warnings
   - Confirm extended support charges stop appearing in billing

6. **Establish Upgrade Cadence**: Prevent future extended support charges:
   - Track RDS engine version end-of-support dates
   - Schedule regular database upgrades before support ends
   - Test new versions early in non-production environments
   - Keep documentation of version-specific application requirements

## Additional Considerations

- **Upgrade Paths**: Some major version upgrades require intermediate steps (e.g., MySQL 5.7 → 8.0 may require upgrading to 5.7.latest first)
- **Downtime**: Plan for maintenance windows; consider using read replicas for minimal downtime migrations
- **Parameter Groups**: Review and update parameter groups to ensure compatibility with new versions
- **Application Changes**: Some applications may need code changes for newer database versions
- **Backup Strategy**: Always take manual snapshots before major version upgrades
- **Blue/Green Deployments**: Use RDS Blue/Green deployments for safer, zero-downtime upgrades when available

For detailed upgrade procedures, consult the AWS RDS documentation for your specific database engine.
