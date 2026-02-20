---
title: High S3 Administrative Fees
category: features
createdAt: '2023-08-10T16:00:00.000Z'
hidden: false
slug: high-s3-admin-fees
updatedAt: '2023-08-10T16:00:00.000Z'
---
Typically administrative fees and other miscellaneous costs for a single S3 bucket should not exceed 10% of the total cost of the bucket. Fees related to AWS StorageLens and StorageAnalytics are not included in this check. When administrative fees and miscellaneous costs exceed the 10% threshold, the excess cost usually points to inefficient use of the S3 bucket or potentially unused buckets. The cost impact for this Recommendation is calculated by subtracting the per bucket fees threshold (10% of the total 30 day bucket cost) from the total administrative fees for the specified S3 buckets.

**Threshold**: This Recommendation is created if the total cost impact exceeds $500 in real cost for the last 30 days. When the cost impact drops back below $500, the Recommendation will be resolved.

You can view the fees by grouping by `Service Detail`. They include:

| Fee                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                               |
| :-------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DeleteObject (Early Delete) | Some storage tiers are meant for infrequent access and have a minimum storage duration of 30 days. Objects deleted, moved, or overwritten prior to the minimum storage duration incur the normal storage change plus a pro-rated fee for the remaining days. These fees represent the pro-rated cost. Check that you are using the appropriate storage tiers and services based on your access patterns.                                  |
| SmObjects (Small Objects)   | Some storage tiers and services have minimum billable object size of 128KB. Objects smaller than 128KB are charged for 128KB. These fees represent the difference between the actual storage used and the minimum billable object size. Check that you are using the appropriate storage tiers and services based on your object sizes.                                                                                                   |
| Inventory                   | Amazon S3 Inventory is a service that generates reports on the content of your S3 buckets. These reports may be generated for your own management or auditing purposes, or they may be generated for use in conjunction with other AWS services, such as Intelligent Tiering. These fees are associated with the generation and storage of these reports. Check your usage of the inventory services and determine if they are necessary. |

<br />
