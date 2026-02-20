---
title: Inefficient AWS NAT Gateway Detected
category: features
createdAt: '2023-07-19T13:00:00.000Z'
hidden: false
slug: unused-nat-gateways-detected
updatedAt: '2023-07-19T13:00:00.000Z'
---
The AWS VPC service provides NAT Gateways so that resources in private subnets can access resources outside your VPC. When using NAT Gateways, you are charged per NAT Gateway-Hour (rounded up to the hour) and per GB Data Processed.

This Recommendation detects NAT Gateways that have hourly charges without appreciable corresponding data processing charges. This may indicate unused NAT Gateways that you may want to clean up.

**Threshold**: This Recommendation is created if the total real cost spend for the identified NAT Gateways with low data processing charges is at least $500 and will be marked as **Addressed** when the spend falls below $500.
