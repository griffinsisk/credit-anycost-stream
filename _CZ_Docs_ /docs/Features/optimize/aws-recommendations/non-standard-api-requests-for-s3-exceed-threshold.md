---
title: High Non-Standard API Requests for S3
category: features
createdAt: '2024-12-19T16:10:00.000Z'
hidden: false
slug: non-standard-api-requests-for-s3-exceed-threshold
updatedAt: '2024-12-19T16:10:00.000Z'
---
This Recommendation identifies high spend on non-standard API requests to S3. This high spend may indicate excess overhead operations on your objects in S3.

**Threshold**: This Recommendation is created if reducing non-standard S3 API calls will save at least $500 based on a 95% savings rate. When reducing non-standard S3 API calls results in savings less than $500, the Recommendation will automatically be closed.

Non-standard API requests for S3 include operations like LIST and HEAD. The LIST operation is used for retrieving various configuration information for S3 buckets and the HEAD operation is used for retrieving metadata about an object without retrieving the object itself. These operations are categorized as overhead costs, while all other request types, such as GET and PUT, are considered operational costs.

High spend on these overhead operations in comparison to operational costs may indicate these operations are creating costly overhead. This may be normal if you are serving private objects, since HEAD requests for private objects cannot be cached due to the need to generate a signed URL. Public objects can be cached because they do not require a signed URL. For publicly served objects, consider caching these requests with CloudFront to reduce costs.

<Callout icon="ℹ️" theme="info">
  If object metadata changes frequently, you might need to set shorter cache expiration times to ensure your application is receiving the latest information.
</Callout>

<br />
