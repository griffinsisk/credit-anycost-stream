---
title: Disconnecting Connections
category: getting-started
createdAt: '2020-02-13T19:39:05.363Z'
hidden: false
slug: disconnecting-connections
updatedAt: '2021-11-30T17:29:59.987Z'
---
In certain scenarios, you may need to terminate a specific Connection for a variety of reasons.

<Callout icon="ℹ️">
  Deleting a Connection is not supported for AWS and Snowflake Connections
</Callout>

To delete a Connection, navigate to **Settings** > **Cloud Integrations** and select the desired Connection and then select the **Delete Connection** option.

When the Billing Connection has been disconnected, after the next ingest all billing data related to that Connection will be removed from the platform.

<Callout icon="ℹ️">
  Although the data related to the deleted Connection is no longer visible in the platform, it will still exist in the CloudZero data stores. If you need a more permanent deletion due to audit or security concerns, contact your FinOps Account Manager.
</Callout>
