---
title: /v2/connections/billing/{connection_id}
excerpt: >
  Delete a single Billing Connection

  Upon disconnect of a billing connection, after the next ingest, all billing
  data related to that connection will be removed from the platform. However, be
  aware that although this data is no longer visible in the platform, it will
  still exist in the CloudZero data stores. If you need a more permanent
  deletion due to audit or security concerns, see your CloudZero Account
  Manager.

  Note: This is not supported for AWS and Snowflake connections
api:
  file: CloudZero-API-V2.yaml
  operationId: deleteOneBillingConnection
hidden: false
---