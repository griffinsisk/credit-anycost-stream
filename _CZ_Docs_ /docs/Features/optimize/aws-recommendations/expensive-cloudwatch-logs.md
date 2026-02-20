---
title: CloudWatch Costs Higher Than Expected
category: features
createdAt: '2023-08-09T13:00:00.000Z'
hidden: false
slug: expensive-cloudwatch-logs
updatedAt: '2023-08-09T13:00:00.000Z'
---
The AWS CloudWatch service should be only a small part of your cloud bill. This Recommendation detects increases in CloudWatch costs which indicate you may be using CloudWatch too extensively and may want to clean up any unnecessary CloudWatch log groups.

**Threshold**: This Recommendation is created if the total spend for the identified CloudWatch log groups exceeds a sliding scale cost that depends on your total 30 day real cost for all AWS services and is at least $500. The following table shows the sliding scale.

|   30 Day Spend for All AWS Services   | 30 Day Spend Threshold for CloudWatch Logs |
| :-----------------------------------: | :----------------------------------------: |
|             \< $10,000.00             |                   $50.00                   |
|   Between $10,000.00 and $50,000.00   |                   $100.00                  |
|   Between $50,000.00 and $100,000.00  |                   $250.00                  |
|  Between $100,000.00 and $500,000.00  |                   $500.00                  |
| Between $500,000.00 and $2,500,000.00 |                   $750.00                  |
|            > $2,500,000.00            |                  $1,000.00                 |

When your CloudWatch cost falls below the threshold based on your AWS spend, or if falls below $500, the Recommendation will automatically be closed.
