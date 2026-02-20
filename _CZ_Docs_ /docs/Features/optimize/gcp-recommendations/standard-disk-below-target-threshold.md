---
title: Standard Disk Below Target Threshold
category: features
createdAt: '2024-06-21T12:44:28.000Z'
hidden: false
slug: standard-disk-below-target-threshold
updatedAt: '2024-06-21T12:44:28.000Z'
---
This Recommendation focuses on usage of Standard Persistent Disk storage. Standard Persistent Disks are a type of disk storage in GCP that is suitable for large data processing workloads that primarily use sequential I/Os and is backed by standard hard disk drives (HDD), providing efficient and reliable block storage for a variety of use cases. Changing your storage option to Standard Persistent Disk can result in cost savings.

**Threshold**: This Recommendation is created if the total real cost spend on Standard Persistent Disk falls below 50% of the total real cost for all Compute Engine disk storage and is at least $500. When the total spend for Standard Persistent Disk exceeds 50%, the Recommendation will automatically be closed.

CloudZero has a target threshold for Standard Persistent Disk of 50%.

For high cost [GCE storage](https://cloud.google.com/compute/docs/disks/), evaluate the workload and consider changing the disk type to Standard Persistent Disk.

The type of an existing Persistent Disk volume cannot be changed. To switch to a disk of a different type, you must migrate your data.

To migrate your data to a new type of disk:

* You must [create a snapshot of the existing disk](https://cloud.google.com/compute/docs/disks/create-snapshots#create_snapshots) and then use that snapshot to [create a disk of the new type](https://cloud.google.com/compute/docs/disks/restore-snapshot#create-disk-from-snapshot)
* After you create and test the new disk, you can [delete the snapshot](https://cloud.google.com/compute/docs/disks/manage-snapshots#delete_a_snapshot) and [delete the original disk](https://cloud.google.com/compute/docs/samples/compute-disk-delete)

The 90-day cost graph shows the daily total spend for all GCP Cloud Engine disk storage resources that are not Standard Persistent Disk and highlights the top five resources with the highest spend to consider optimizing. The resource table shows Disks with spend greater than $100 in the last 30 days.
