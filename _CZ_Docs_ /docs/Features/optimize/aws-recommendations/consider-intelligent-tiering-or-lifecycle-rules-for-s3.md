---
title: Consider Intelligent-Tiering or Lifecycle Rules for S3
category: features
createdAt: '2024-12-13T13:00:00.000Z'
hidden: false
slug: consider-intelligent-tiering-or-lifecycle-rules-for-s3
updatedAt: '2024-12-13T13:00:00.000Z'
---
This Recommendation is created when there are S3 buckets with spend only on Standard Storage, indicating that use of Intelligent-Tiering or Lifecycle policies could be applied to reduce cost.

**Threshold**: This Recommendation is created if 10% of the total spend on S3 buckets that use Standard storage only is greater than $500.

Standard storage is the default storage class for objects in S3 and is the most expensive. Standard storage is best used for data that needs to be accessed frequently with fastest access time for data retrieval.

Consider the following when determining if S3 Intelligent-Tiering or S3 Lifecycle could be applied to the S3 resources listed to save up to 10% on storage costs.

**S3 Intelligent-Tiering:**

* Amazon S3 Intelligent-Tiering is an Amazon S3 storage class designed to optimize storage costs by automatically moving data to the most cost-effective access tier when access patterns change, without performance impact or operational overhead.
* S3 Intelligent-Tiering automatically stores objects in three access tiers:
  * **Frequent Access tier:** The default access tier that any object created or transitioned to S3 Intelligent-Tiering begins its lifecycle in. An object remains in this tier as long as it is being accessed. If objects in other tiers are accessed later, S3 Intelligent-Tiering automatically moves the objects back to this tier.
  * **Infrequent Access tier:** If an object is not accessed for 30 consecutive days, the object moves to the Infrequent Access tier with savings up to 40%.
  * **Archive Instant Access tier**: If an object is not accessed for 90 consecutive days, the object moves to the Archive Instant Access tier with savings up to 68%.
* When to use Intelligent-Tiering: Ideal for data with unknown, changing, or unpredictable access patterns, independent of object size or retention period. This includes data for new applications, data analytics, user-generated content, and data lakes.

**S3 Lifecycle Rules:**

* S3 Lifecycle helps users store objects in a cost effective way throughout their lifecycle by transitioning them to lower-cost storage classes or deleting expired objects on your behalf.
* Lifecycle rules are applied to all existing and future objects in an S3 bucket
* When to use Lifecycle policies: If you have a well-defined access pattern for your data. Ideal for data needing access for a specific period and then archiving at a cheaper storage tier.

<Callout icon="ℹ️" theme="info">
  Object monitoring and automation for Intelligent-Tiering incurs a small monthly charge. Learn more about S3 pricing and the additional costs associated with S3 [in this blog post](https://www.cloudzero.com/blog/s3-pricing/).

  Amazon S3 Lifecycle can be used to transition new objects that are programmatically uploaded  to the S3 Intelligent-Tiering storage class.
</Callout>

The resource table shows the list of buckets with spend only on Standard storage.
