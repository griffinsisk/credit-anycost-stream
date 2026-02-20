---
title: Connecting to MongoDB
category: getting-started
createdAt: '2024-07-29'
hidden: false
slug: connections-mongodb-v2
updatedAt: '2024-10-16'
---
# How the MongoDB Connection works

The CloudZero MongoDB connection uses [API access](https://www.mongodb.com/docs/cloud-manager/core/api/) to MongoDB Atlas to gather [billing data](https://www.mongodb.com/docs/cloud-manager/reference/api/invoices/) for your organization. This also allows you to view and use standard tags, user-configurable tags, and any available MongoDB-provided metadata.

<Callout icon="ℹ️" theme="info">
  The CloudZero MongoDB connection supports MongoDB Atlas only. For self-hosted MongoDB deployments, billing data is integrated into the cost data of the cloud provider hosting the MongoDB infrastructure.
</Callout>

The following summarizes the billing period ingest windows:

* **Newly Created Connection**: CloudZero will ingest the most recent 24 months of billing periods, if available.
* **Re-enabled Connection**: CloudZero will ingest up to 24 months of billing periods starting from the current billing period and going back to the most recent billing period ingested.
* **Steady State**: CloudZero will ingest the current and previous billing period.

# Prerequisites for the MongoDB Connection

You must obtain a MongoDB API Key so the adaptor can have access to the data it needs from your MongoDB organization. Follow these steps:

1. Set up an API key for your MongoDB organization according to the MongoDB [Create an API Key](https://www.mongodb.com/docs/atlas/configure-api-access/#std-label-create-org-api-key) documentation.  The API Key will require `Organization Billing Viewer` permissions.
2. Make note of both the **public** and **private** keys for use creating a MongoDB Connection below.
3. Find and make note of your MongoDB **Organization ID** for later. This is typically found in the **Organization Settings** of your MongoDB admin console.

   <Image align="center" alt="Organization ID Location MongoDB admin console" className="border" border={true} src="https://files.readme.io/6be528f-Screen_Shot_2022-12-09_at_3.53.02_PM.png" />

<Callout icon="ℹ️" theme="info">
  To grant CloudZero access to linked MongoDB organizations, you must create a separate MongoDB API key and CloudZero connection for each organization. A MongoDB API key grants access only to the specific MongoDB organization where it was created; it does not grant access to any linked organizations.
</Callout>

# Create a MongoDB Connection

1. In CloudZero, navigate to [Settings](https://app.cloudzero.com/organization/connections) by selecting the **gear icon** in the top navigation bar.
2. Click the **Add Connection** button.
3. Click the **MongoDB** tile.

<Image align="center" alt="MongoDB Connection Tile" className="border" border={true} src="https://downloads.cloudzero.com/documentation/resources/cz_connections_tile_2024_08.png" />

4. Enter the connection metadata:

* **Public Key**: This is the **public** MongoDB API key you created when you set up the API key.
* **Private Key**: This is the **private** MongoDB API key you created when you set up the API key.
* **Organization ID**: This is your MongoDB Organization ID that you located when you set up the API key.
* **Use Fixed IP Egress**: Enable this if you would like to use MongoDB's fixed IP egress functionality. See [below](#mongodb-fixed-ip-egress).

5. Select the **Save** button.
   You will be redirected to the **Connection Details** page, where you should see your newly created connection.

# MongoDB Fixed IP Egress

To establish a MongoDB connection, you must provide an API key. MongoDB allows restricting API key usage to specific IP addresses, which can be configured as follows:

1. Enable **Use Fixed IP Address** for the CloudZero Managed MongoDB Connection.
2. In your MongoDB account, navigate to **Access Manager** > **Organization Access** > **API Keys**.
3. Edit the API key used for the CloudZero connection.
4. Click **Next**.
5. Select **Add Access List Entry** and enter `52.0.118.180`. Click **Save**.
6. Select **Add Access List Entry** again and enter `52.0.33.111`. Click **Save**.

The API Access List should match the following:

<Image align="center" alt="MongoDB API Access List" className="border" border={true} src="https://downloads.cloudzero.com/documentation/resources/connect-mongodb-enable-fixed-ip-egress.png" />
