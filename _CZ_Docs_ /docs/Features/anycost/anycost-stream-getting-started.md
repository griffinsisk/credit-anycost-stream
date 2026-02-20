---
title: Getting Started with AnyCost Stream Adaptor
category: features
createdAt: '2024-09-10'
hidden: false
slug: anycost-stream-getting-started
updatedAt: ''
---
An AnyCost Stream Adaptor automates the flow of cost data into CloudZero by allowing you to send data from any cost source to the CloudZero REST API.

To set up an AnyCost Stream connection, complete the following steps:

1. [Register the connection in the CloudZero UI.](#step-1-register-the-connection-in-the-ui)
2. [Write the code that powers the Adaptor.](#step-2-write-code-to-create-a-custom-adaptor)
3. [Send cost data to CloudZero.](#step-3-send-cost-data-to-cloudzero)

# Prerequisites for the AnyCost Stream Adaptor

Ensure you have necessary permissions to create a new connection in CloudZero.

# Set up the AnyCost Stream Adaptor

## Step 1: Register the Connection in the UI

First, you must register your AnyCost Adaptor as a Billing Connection in the CloudZero UI.

1. In CloudZero, navigate to [Settings](https://app.cloudzero.com/organization/connections) by selecting the **gear icon** in the top navigation bar.
2. Click the **Add Connection** button.
3. Select the **AnyCost Stream** tile and select **Get started**.
4. Enter a **Connection Name**. This is the name you will see in the CloudZero UI. The connection name is typically used to distinguish accounts, environments, and instances of the AnyCost adaptors. It cannot contain spaces, periods, or special characters (except for hyphens and underscores).

   For example, if you are sending cost data from a service called Simple Cloud for both your production and dev environments, the connection name might be `simple-cloud-prod`.
5. Enter the **Cloud Provider**. For example, if your AnyCost Stream Adaptor will send cost data from a service called Simple Cloud, the cloud provider would be `Simple Cloud`.
6. Select **Save**.

After your AnyCost Stream Connection is created, it appears in the **Billing Connections** table of the [Cloud Integrations](https://app.cloudzero.com/organization/connections) page.

<Image align="center" alt="Billing Connections table" border={true} src="https://downloads.cloudzero.com/documentation/resources/billing-connections.png" className="border" />

## Step 2: Write code to create a Custom Adaptor

Next, you must write the code to create the AnyCost Adaptor. For details, see [Creating AnyCost Custom Adaptors](/docs/anycost-custom-adaptors).

## Step 3: Send cost data to CloudZero

Finally, you can start sending cost data to the CloudZero AnyCost API. For details, see [Sending AnyCost Stream Data to CloudZero](/docs/anycost-send-stream-data).

After you send cost data to the CloudZero AnyCost API, CloudZero processes the first ingest of data and the **Status** changes from **Pending Data** to **Healthy**. This can take several hours.

If your AnyCost Stream Adaptor is not sending data correctly, the **Status** is updated with details about the error.

<Callout icon="ℹ️" theme="info">
  It can take up to a day to synchronize new accounts before you see cost data in the [Explorer](/docs/explorer).
</Callout>
