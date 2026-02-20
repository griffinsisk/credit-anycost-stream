---
title: Delete Inactive DynamoDB Tables
deprecated: false
hidden: false
metadata:
  robots: index
---
This Recommendation identifies DynamoDB tables that are incurring storage costs but show no usage activity. Inactive tables continue to accumulate charges based on data size (per GB-month) even when the tables are not being read from or written to. Unused DynamoDB tables represent pure waste. You are paying for storage without gaining any value. These tables are often remnants of:

* Completed projects or migrations
* Testing and development environments
* Deprecated features or services
* Data that should have been archived or deleted

**Threshold**: This Recommendation is created if a DynamoDB table has no read or write activity in the past thirty days.

**Recommended action**: Investigate ownership and verify if the table is truly unused. If so, delete the table to eliminate ongoing storage costs. If there is any chance the table may be be needed later, export the data to S3.

