---
title: High Ratio of S3 API Cost to Storage Cost
category: features
createdAt: '2024-12-19T16:10:00.000Z'
hidden: false
slug: high-ratio-of-s3-api-costs-to-storage-costs
updatedAt: '2024-12-19T16:10:00.000Z'
---
This Recommendation is created when spend on API requests to an S3 bucket represents greater than 80% of costs for that bucket. This high ratio of requests to storage cost may indicate that there is frequently accessed data that could be moved to a different storage class.

**Threshold**: This Recommendation is created if reducing non-standard S3 API calls will save at least $500 based on a 95% savings rate. When reducing non-standard S3 API calls results in savings less than $500, the Recommendation will automatically be closed.

When API requests costs are high, this may be because the data being accessed is in an Infrequent Access tier. While Infrequent Access tiers have lower storage costs, there is a cost for every gigabyte of data retrieved and it is billed as an API request.

Consider moving frequently accessed data to Standard storage tier, which does not charge for data retrieval, to save up to 50% on S3 spend.

