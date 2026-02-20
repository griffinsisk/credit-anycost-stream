---
title: Connections
category: getting-started
createdAt: '2020-02-13T19:39:05.363Z'
hidden: false
slug: connections
updatedAt: '2021-11-30T17:29:59.987Z'
---
CloudZero ingests Billing, Resource, and other types of data from Cost Sources into the platform by means of Connections.

<Callout icon="ℹ️" theme="info">
  CloudZero ingests billing data from each connected cloud provider at minimum every 12 to 24 hours. However, the precise timing of data ingestion depends on several factors, including the cloud providers in question and how frequently data is provided to consume. If you do not see data you expect to be ingested within 32 hours of the time you expect, contact your FinOps Account Manager or customer success representative for help.
</Callout>

The Cloud Integrations page lists your Billing Connections. Use the **Add Connection** button to add another Connection.

<Image align="center" alt="CloudZero Connections" border={true} src="https://downloads.cloudzero.com/documentation/resources/billing-resource-tables.png" className="border" />

CloudZero supports ingesting any type of cost. There are CloudZero Adaptors for many Cost Sources, allowing you to get started right away.

<Callout icon="ℹ️" theme="info">
  The AnyCost framework enables your teams to build their own Adaptors for additional Cost Sources that CloudZero does not support with a CloudZero Adaptor. For information about creating your own AnyCost Adaptors, see the [AnyCost](/docs/anycost) section of the documentation.
</Callout>

Refer to the pages in this section for information about connecting to specific Cost Sources using CloudZero Adaptors. Details for specific Cost Sources are also provided in this section.

This section also includes the following pages:

* [Connecting Custom Data from AnyCost Adaptors](/docs/connections-custom#/)
* [Cost Allocation Tagging Configuration](/docs/cost#/)
* [Disconnecting Connections](/docs/disconnecting-connections)
