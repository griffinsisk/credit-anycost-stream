---
title: Redundant CloudTrail Usage Detected
category: features
createdAt: '2023-07-19T13:00:00.000Z'
hidden: false
slug: redundant-cloudtrail-usage-detected
updatedAt: '2023-07-19T13:00:00.000Z'
---
The AWS CloudTrail service typically does not cost anything unless you have more than an one instance in an account. This Recommendation detects whether you are being charged for CloudTrail events, which indicates you have more than one instance in an account and may want to clean up any redundant CloudTrail instances to eliminate unnecessary spend.

**Threshold**: This Recommendation is created if the total spend for the identified CloudTrail events exceeds a sliding scale cost that depends on your total 30 day real cost for all AWS services, and the CloudTrail cost is at least $500. The following table shows the sliding scale.

|   30 Day Spend for All AWS Services   | 30 Day Spend Threshold for CloudTrail |
| :-----------------------------------: | :-----------------------------------: |
|             \< $10,000.00             |                $100.00                |
|   Between $10,000.00 and $50,000.00   |                $250.00                |
|   Between $50,000.00 and $100,000.00  |                $500.00                |
|  Between $100,000.00 and $500,000.00  |               $1,000.00               |
| Between $500,000.00 and $2,500,000.00 |               $2,500.00               |
|            > $2,500,000.00            |               $5,000.00               |

When your CloudTrail cost falls below the threshold based on your AWS spend, or if falls below $500, the Recommendation will be closed automatically.
