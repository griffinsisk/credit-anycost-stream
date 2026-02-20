---
title: Getting Started with Telemetry
deprecated: false
hidden: false
metadata:
  robots: index
---
The CloudZero Telemetry APIs, Unit Metric and Allocation, allow you to send additional data related to your system's operation, the actions taken by your own users, and more. For example, you can send data about the number of requests issued to one of your services by a given customer, or about the number of queries made to a shared database by one of your features. This data provides context that the CloudZero platform can combine with your cloud costs to produce unit cost metrics or to further allocate your costs via custom dimensions.

## Limits
* You can send at a rate of up to 100 records per second, with a maximum burst of one day's worth of records (8,640,000)
* Max request size: there is a 5MB size limit per request, meaning the API will accept up to approximately 10,000 records of 512 bytes each 
* When sending a large number of individual requests very rapidly, the API may return a 503 "slow down" error; you can address this by either adding a delayed retry or by batching larger numbers of records into fewer requests

## Additional Reading

- [Allocation Telemetry Documentation](/reference/allocation-telemetry-api-1)
- [Unit Metric Telemetry Documentation](/reference/unit-metric-telemetry-api-1)