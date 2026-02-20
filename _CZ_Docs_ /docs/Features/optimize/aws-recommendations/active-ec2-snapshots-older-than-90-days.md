---
title: Delete EBS Snapshot Older Than 180 Days
category: features
createdAt: '2023-07-19T13:00:00.000Z'
hidden: false
slug: active-ec2-snapshots-older-than-90-days
updatedAt: '2023-07-19T13:00:00.000Z'
---
This Recommendation identifies EC2 snapshots that are older than 90 days and are still actively incurring costs. Often these snapshots can be outdated and no longer needed. Cleaning them up can save money.

**Threshold**: This Recommendation is created if the total spend for the identified snapshots exceeds $500 in real cost. When the total spend for those snapshots is reduced below $500 through cleaning them up, the Recommendation will automatically be closed.
