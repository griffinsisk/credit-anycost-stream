---
title: Multi-Region Storage Exceeds Target Threshold
category: features
createdAt: '2024-06-24T12:44:28.000Z'
hidden: false
slug: excessive-gcp-multi-region-storage-usage
updatedAt: '2024-06-24T12:44:28.000Z'
---
This Recommendation focuses on optimizing GCP Cloud Storage with Multi-Region bucket location by spend. By default, buckets are set to the Multi-Region which is the most expensive and the most redundant configuration option. The threshold for Multi-Region bucket location spend is 30%. Additional spend over that can indicate that storage is not optimized.

**Threshold**: This Recommendation is created if the total real cost spend on Multi-Region storage class exceeds 30% of the total real cost for all GCP Cloud Storage and is at least $500. When the total spend for Multi Region storage falls below 30%, the Recommendation will automatically be closed.

GCP has two other bucket location types that should be considered based on data access patterns and redundancy needs:

**Region**: Optimized latency, bandwidth, and cross-zone redundancy. Example workloads:  Analytics, Backup and Archive.

**Dual-Region**: Optimized latency, bandwidth, and cross-region redundancy. Example workloads: Analytics, Backup and Archive, Disaster Recovery.

Note that Region has the lowest data storage cost. Dual-Region has the highest base storage price but does not have outbound data transfer charges when reading data within either region, unlike Multi-Region.

Pricing costs for each bucket location in each region can be found [in the GCP documentation](https://cloud.google.com/storage/pricing#multi-regions).

Note that Bucket location cannot be changed after creation. To change the location, you can move your data to a bucket in a different location. Check the [GCP documentation](https://cloud.google.com/storage/docs/moving-buckets) for any costs that may be incurred from moving data between locations.

The 90-day cost graph shows the daily total spend for all GCP Cloud Storage resources with Multi-Region storage locations and highlights the top five resources with the highest spend to consider optimizing.

<br />
