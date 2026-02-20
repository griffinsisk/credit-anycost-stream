---
title: Unarchived Old EBS Snapshots
category: features
createdAt: '2025-12-01T00:00:00.000Z'
hidden: false
slug: unarchived-old-ebs-snapshots
updatedAt: '2025-12-01T00:00:00.000Z'
---
CloudZero has identified Amazon EBS snapshots that have been stored for an extended period in standard snapshot storage. These long-term snapshots are excellent candidates for EBS Snapshot Archive, which can reduce storage costs by up to 75% for snapshots that are rarely accessed.

## What it does

This recommendation identifies EBS snapshots that are:
- Stored in standard EBS snapshot storage (not archived)
- Older than 90 days
- Incurring ongoing standard snapshot storage costs
- Good candidates for migration to EBS Snapshot Archive tier

EBS Snapshot Archive is designed for long-term retention of snapshots that are accessed infrequently—such as compliance archives, disaster recovery backups, or historical reference snapshots.

## Why it matters

- **Cost Savings**: Snapshot Archive storage costs ~75% less than standard snapshot storage ($0.0125/GB-month vs $0.05/GB-month)
- **Compliance**: Maintain required long-term backups while dramatically reducing costs
- **No Data Loss**: Archives preserve complete snapshot data—they're just stored in a lower-cost tier
- **Scalability**: As snapshot storage grows over time, these savings compound

For example, a 1TB snapshot stored for a year:
- Standard storage: $600/year
- Archive storage: $150/year
- **Savings: $450/year per TB**

## Recommended Actions

1. **Review Snapshot Usage Patterns**:
   - Identify snapshots that are retained for compliance or disaster recovery
   - Determine which snapshots are rarely or never restored
   - Confirm snapshots older than 90 days are good archival candidates
   - Verify that longer restore times (24-72 hours) are acceptable

2. **Archive Eligible Snapshots**:

   **Via AWS Console**:
   - Navigate to EC2 → Snapshots
   - Select snapshot(s) to archive
   - Actions → Archive snapshot

   **Via AWS CLI**:
   ```bash
   aws ec2 modify-snapshot-tier \
     --snapshot-id snap-1234567890abcdef0 \
     --storage-tier archive
   ```

   **Bulk Archive via CLI**:
   ```bash
   # List old snapshots
   aws ec2 describe-snapshots \
     --owner-ids self \
     --query 'Snapshots[?StartTime<=`2023-01-01`].SnapshotId' \
     --output text | \
   while read snap; do
     aws ec2 modify-snapshot-tier \
       --snapshot-id $snap \
       --storage-tier archive
   done
   ```

3. **Implement Automated Archival Policies**:
   - Use AWS Data Lifecycle Manager (DLM) to automatically archive snapshots based on age
   - Create lifecycle policies that:
     - Move snapshots to archive tier after 90 days
     - Delete archived snapshots after retention period expires
     - Apply to specific volumes by tags

4. **Set Up Monitoring**:
   - Track snapshot storage costs over time
   - Monitor archive vs standard storage distribution
   - Set CloudWatch alarms for unexpected snapshot growth
   - Review archived snapshots quarterly to confirm retention needs

5. **Document Restore Process**:
   - Document that archived snapshots take 24-72 hours to restore
   - Update disaster recovery runbooks with new restore timelines
   - Communicate changes to teams that may need to restore snapshots
   - Test restore process from archive to verify procedures

6. **Review Retention Policies**:
   - Evaluate whether all snapshots need to be retained
   - Delete snapshots that are no longer needed for compliance or recovery
   - Consider tiered retention: recent snapshots → archive → deletion

## Cost Impact Calculation

The cost impact represents potential savings from archiving:
- **Standard Storage**: ~$0.05 per GB-month (varies by region)
- **Archive Storage**: ~$0.0125 per GB-month (75% cheaper)
- **Savings**: 75% of current standard snapshot storage costs

For a snapshot older than 90 days with $100/month in storage costs:
- Moving to archive saves: $75/month or $900/year

## Important Considerations

### Restore Times
- **Standard snapshots**: Instant availability for volume creation
- **Archived snapshots**: 24-72 hours to restore to standard tier before use
- Only archive snapshots where slow restore is acceptable

### Use Cases for Archive
✅ **Good candidates**:
- Compliance/regulatory retention backups
- Long-term disaster recovery snapshots
- Historical reference snapshots
- End-of-month/quarter/year snapshots
- Snapshots of decommissioned resources

❌ **Poor candidates**:
- Snapshots for active disaster recovery (need fast restore)
- Recent snapshots (< 90 days old)
- Snapshots used for frequent testing or development
- Snapshots that may be needed quickly

### Pricing Considerations
- **Archive storage**: $0.0125/GB-month (~$12.75/TB-month)
- **Restore from archive**: $0.03/GB retrieval charge (one-time when restoring)
- **Standard storage**: $0.05/GB-month (~$51.20/TB-month)

If you need to restore an archived snapshot frequently, the retrieval charges can offset savings.

### Operational Impact
- No changes to snapshot permissions or sharing
- Snapshot IDs remain the same
- Tags and metadata are preserved
- Can restore to standard tier at any time (with 24-72 hour delay)

## Best Practices

1. **Age-Based Policy**: Archive snapshots automatically after 90-180 days
2. **Tag-Based Archival**: Use tags to identify archive candidates (e.g., `Archivable=true`)
3. **Test Restore Process**: Periodically test restoring from archive to verify procedures
4. **Lifecycle Management**: Use DLM for automated archival and eventual deletion
5. **Cost Tracking**: Monitor savings from archival using Cost Explorer tags
6. **Document Exceptions**: Clearly identify snapshots that should never be archived
