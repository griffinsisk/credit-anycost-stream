---
title: RDS Snapshot Costs Are Higher Than Expected
category: features
createdAt: '2023-07-19T13:00:00.000Z'
hidden: false
slug: rds-snapshot-costs-are-higher-than-expected
updatedAt: '2023-07-19T13:00:00.000Z'
---
This Recommendation is created when the percentage of RDS snapshots exceeds 10% of the total RDS costs. A typical organization's RDS snapshot costs will represent 1% to 5% of the total cost of the entire RDS service. When RDS snapshot costs exceed that, it may indicate that there are an excessive number of snapshots. This may be due to missing or inadequate snapshot retention rules that leave large number of automatic snapshots around, as well as manual snapshots that are not managed by the snapshot retention rules. Think about tightening up snapshot retention rules and cleaning up any unnecessary snapshots in order to save money.

**Threshold**: This Recommendation is created if the total real cost spend for the identified snapshots exceeds 10% of the real cost for all of the RDS service and is at least $500. When the total spend for RDS snapshots falls below 10%, the Recommendation will automatically be closed.
