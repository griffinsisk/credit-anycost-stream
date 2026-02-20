---
title: Excessive RDS Backup Retention
category: features
createdAt: '2025-12-01T00:00:00.000Z'
hidden: false
slug: excessive-rds-backup-retention
updatedAt: '2025-12-01T00:00:00.000Z'
---
CloudZero has identified Amazon RDS backups and manual snapshots retained beyond 90 days, potentially exceeding business or compliance requirements. Long-term retention of RDS snapshots accumulates significant costs over time.

## What it does

This recommendation identifies RDS backups and snapshots that are:
- Older than 90 days
- Incurring ongoing storage costs
- Potentially exceeding necessary retention requirements

RDS automated backups retain for 7-35 days and auto-cleanup. This focuses on manual snapshots retained indefinitely unless explicitly deleted.

## Why it matters

- **Cost Accumulation**: Storage costs add up as snapshots accumulate ($0.095/GB-month)
- **Forgotten Snapshots**: Manual snapshots for one-time purposes often get forgotten
- **Example**: 50 old 500GB snapshots = **~$28,500/year** in unnecessary costs

## Recommended Actions

1. **Review Snapshot Inventory**:
   - Navigate to RDS → Snapshots → Filter "Manual snapshots" → Sort by date
   - Identify purpose of each snapshot (testing, compliance, migration, etc.)
   - Determine which are still needed

   ```bash
   aws rds describe-db-snapshots --snapshot-type manual \
     --query 'DBSnapshots[?SnapshotCreateTime<=`2023-01-01`].[DBSnapshotIdentifier,SnapshotCreateTime]'
   ```

2. **Establish Retention Policy**:
   - Daily backups: 7-30 days
   - Weekly backups: 4-12 weeks
   - Monthly backups: 12 months
   - Yearly backups: 7 years (compliance only)
   - Document and communicate policy

3. **Delete Unnecessary Snapshots**:

   **Important**: Deletion is permanent - always verify first

   ```bash
   aws rds delete-db-snapshot --db-snapshot-identifier mydb-snapshot-2023-01-15
   ```

4. **Implement Automated Lifecycle**:
   - Use AWS Lambda to auto-delete based on tags and age
   - Tag snapshots: `Purpose`, `RetentionDays`, `Retain`
   - Use AWS Backup for centralized lifecycle management

5. **Consider Alternative Storage**:
   - Export to S3 Glacier Deep Archive (~$0.00099/GB-month, 99% cheaper)
   - Use AWS Backup archive tier
   - Keep only "hot" backups in RDS format

6. **Monitor and Alert**:
   - Set up Cost Anomaly Detection for RDS backup storage
   - Create CloudWatch dashboards for snapshot age and costs
   - Alert on snapshots exceeding retention policy

## Cost Impact

- **Conservative estimate**: 50% reduction (assumes some retention needed)
- **Unnecessary snapshots**: 100% recoverable
- **Pricing**: ~$0.095/GB-month (standard), ~$0.021/GB-month (Aurora excess)

## Important Considerations

### Retention Best Practices
**Keep**:
- Compliance-required snapshots
- Recent backups (30-90 days) for disaster recovery
- Pre-migration/upgrade snapshots (until validated)

**Consider Deleting**:
- Ad-hoc test snapshots
- Post-deployment snapshots (after validation)
- Duplicate snapshots
- Decommissioned database snapshots

### Operational Risks
- Deletion is permanent (no undelete)
- Verify with database owners before deletion
- Export to S3 if uncertain
- Test that remaining snapshots are restorable

## AWS Backup Alternative

Use AWS Backup for automated lifecycle management:
- Centralized management across services
- Automated retention and expiration
- Compliance reporting
- Cold storage transitions
