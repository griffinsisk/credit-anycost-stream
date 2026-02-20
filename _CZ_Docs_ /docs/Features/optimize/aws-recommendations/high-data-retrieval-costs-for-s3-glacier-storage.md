---
title: High Data Retrieval Costs for S3 Glacier Storage
category: features
createdAt: '2025-01-29T16:10:00.000Z'
hidden: false
slug: high-data-retrieval-costs-for-s3-glacier-storage
updatedAt: '2025-01-29T16:10:00.000Z'
---
This Recommendation identifies data retrieval costs for an S3 bucket occurring on an S3 Glacier storage tier. Data retrieval costs may indicate frequently accessed data that could be optimized by moving to a more cost-effective storage class.

**Threshold**: This Recommendation is created if data retrieval costs for data stored in long-term or archival storage on any S3 bucket exceeds $100 over the last 30 days. When the cost impact from all S3 buckets drops back to $100 or below, the Recommendation will resolve.

AWS charges for storing objects in your S3 buckets, and for certain tiers, data retrieval per gigabyte. Amazon S3 provides the following S3 Glacier storage classes:

* S3 Glacier Instant Retrieval (GLACIER_IR): Use for long-term data that is rarely accessed and requires milliseconds for retrieval. Data in this storage class is available for real-time access.
* S3 Glacier Flexible Retrieval (GLACIER): Use for archives where portions of the data might need to be retrieved in minutes. Data in this storage class is archived, and not available for real-time access.
* S3 Glacier Deep Archive (DEEP_ARCHIVE): Use for archiving data that rarely needs to be accessed. Data in this storage class is archived, and not available for real-time access.

While S3 buckets stored on these tiers have lower storage costs, there is a cost for retrieving data. Look at these buckets to determine why data retrieval is needed and consider moving frequently accessed data to the Standard storage tier, which does not charge for data retrieval.

<Callout icon="ℹ️" theme="info">
  A small fee is applied for objects transitioned between storage classes, which is usually very low. Learn more about S3 pricing and the additional costs associated with S3 [in this blog post](https://www.cloudzero.com/blog/s3-pricing/).

  Learn more about how to change the storage class for existing objects [in the AWS documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/sc-howtoset.html#changing-storage-class).
</Callout>
