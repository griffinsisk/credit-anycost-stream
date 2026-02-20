---
title: Disk Snapshots Exceeds Target Threshold
category: features
createdAt: '2024-06-20T12:44:28.000Z'
hidden: false
slug: disk-snapshots-exceeds-target-threshold
updatedAt: '2024-06-20T12:44:28.000Z'
---
This Recommendation is created when the cost of GCP Cloud Engine disk snapshots exceeds 5% of the total Compute Engine disk storage costs.

**Threshold**: This Recommendation is created if the total real cost spend on GCP disk snapshots exceeds 5% of the total real cost for all Compute Engine disk storage and is at least $500. When the total spend for disk snapshots exceeds 5%, the Recommendation will automatically be closed.

This may indicate that there are an excessive number of snapshots. Consider the following to reduce cost of the snapshots:

* [Reduce the frequency of scheduled snapshots](https://cloud.google.com/compute/docs/disks/manage-snapshot-schedules) to weekly if the workload allows.
* [Delete snapshot schedules](https://cloud.google.com/compute/docs/disks/manage-snapshot-schedules) for workloads that no longer require it.
* Shorten the retention policy for auto generated snapshots.
  Note: If you do not set a retention policy, all your auto-generated snapshots will be retained indefinitely. You will incur storage costs for these snapshots until you delete them manually.
* Update the Source disk deletion policy to ensure snapshots from deleted disks are removed.
* Switch the location of snapshots to Regional instead of Multi-Regional when high availability is not necessary.
* Removie snapshots older than 90 days.

The 90-day cost graph shows the daily total spend for all GCP Cloud Engine disk snapshots and highlights the top five resources with the highest spend to evaluate. The resource table shows snapshots with spend greater than $5 in the last 30 days.
