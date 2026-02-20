---
title: Connecting to GCP - Billing
category: getting-started
createdAt: '2020-02-13T19:39:05.363Z'
hidden: false
slug: connections-gcp-billing
updatedAt: '2021-11-30T17:29:59.987Z'
---
# How the GCP Billing Connection works

Connecting to a GCP account will show GCP cost data alongside other Cost Sources in the Explorer, as well as enable anomaly alerts on GCP spend.

The CloudZero platform will ingest GCP Cost data by using the GCP Cloud Billing Data Export to BigQuery feature. The Billing Data Export will enable the CloudZero platform to get accurate cost information. After the export is created, you must grant access to the data to a CloudZero service principal.

After you have created an export, it can take 24-48 hours for your export table to appear. It does not appear until GCP does its first data drop, which can take a day or two. You cannot configure your Connection in the CloudZero platform until the table has been created.

In addition, when the export is newly set up, GCP loads billing data into the BigQuery dataset in chronological order, so older data will appear first.

If you are connecting to an existing BigQuery dataset that already has export data, CloudZero will process the most recent data first, aligning with the normal behavior of the CloudZero application.

When you have finished creating the Connection, Discovery (the act of switching from a **Pending First Ingest** to a **Healthy** status in the Billing Connections table on the Integrations page) can take up to an hour. It can take up to 24 hours to synchronize new accounts and to see cost data in the Explorer.

In the steps on this page, you will find instructions on how to create Billing Data Exports and configure CloudZero's access to the cost data.

<Callout icon="ℹ️" theme="info">
  All of CloudZero's permissions are read-only. CloudZero has no access to data except where explicitly authorized.

  For GCP - Billing, CloudZero has the BigQuery Data Viewer permission. This grants read access only, to allow loading data from Cloud Billing Export files stored in BigQuery.
</Callout>

# Connect a GCP Billing Account

## Step 1: Configure Cloud Billing Data Exports

The first step is to configure your Cloud Billing Data Exports in the Google Cloud console. You may already have completed these steps for other purposes, but you must confirm the steps here match what you have previously set up.

1. Set up a **Detailed usage cost data** export in GCP BigQuery by following the instructions to [Set up Cloud Billing data export to BigQuery](https://cloud.google.com/billing/docs/how-to/export-data-bigquery-setup).

2. You may have already created usage cost data exports for other purposes, but CloudZero requires the [Detailed usage cost data](https://cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage) exports. Confirm which type of export you have already configured and create additional **Detailed** exports if necessary.

3. After the table is available, make note of its fully qualified name for use in later steps. This name consists of the Project ID, Dataset, and Table name of the table you configured. You can copy the name from the table details listed next to the **Table ID**:

In this example: `billing-administration-123456.all_billing_data.gcp_billing_export_resource_v1_123456_123456_123456`, the components are:

* Project ID: `billing-administration-123456`
* Dataset: `all_billing_data`
* Table name: `gcp_billing_export_resource_v1_123456_123456_123456`

<Callout icon="ℹ️" theme="info">
  The fully qualified table name will always include the word `resource`. If this is missing, reconfirm your export type is **Detailed** usage cost data.
</Callout>

You can copy this name easily from the table details, listed next to the **Table ID**.

<Callout icon="ℹ️" theme="info">
  After you have created an export, it can take 24-48 hours for your export table to appear. It does not appear until GCP does its first data drop, which can take a day or two. You cannot configure your Connection in the CloudZero platform until the table has been created.
</Callout>

<Image align="center" alt="Export table" border={true} src="https://downloads.cloudzero.com/documentation/resources/43d1c83-Screen_Shot_2022-09-09_at_10.14.46_AM.png" className="border" />

## Step 2: Configure your Connection

After your Cloud Billing Data Export table is available, you can create your connection in the CloudZero platform.

<Callout icon="ℹ️" theme="info">
  You must be a CloudZero Admin to add new Connections to the platform.
</Callout>

1. Open the **Cloud Integrations** page. From the **gear** icon from the top navigation, select **Cloud Integrations**, or navigate to to [https://app.cloudzero.com/organization/connections](https://app.cloudzero.com/organization/connections).
2. Click the **Add Connection** button.
3. On the page that opens, from the list of possible connection types, select the **GCP** tile to begin setting up a GCP connection.
4. On the subsequent page, review the information and when you are ready, click **Get started**.
5. When the **Connection Details** page for a GCP Connection opens, enter the information as follows:
   * **Connection Name**: This is the name you will see throughout the CloudZero platform, in addition to your GCP Account ID.
   * **Service Principal**: This is the Service Principal CloudZero uses to access your GCP data. Make note of this value, as you will need it to grant access to CloudZero.
   * **Fully Qualified Table Name**: This is the name of the billing data table that copied in the first step.
   * **Convert all currency to USD**: Selected by default. You can deselect the checkbox to ingest billing data in the local currency of your GCP account instead of converting to the exchange rates specified by Google. Other billing connections will not be affected and will continue to ingest cost data in the currencies used now. This will cause mixing of currencies on the platform, leading to inaccurate reports and analytics.

     <Callout icon="⚠️" theme="warning">
       You cannot modify this setting after the connection is created. If you need to change this setting after creation, contact your FinOps Account Manager for assistance.
     </Callout>
6. Click the **Save** button to save your Connection.
7. Verify that you see the Connection on the **Connection Details** page. Your connection may be in error until you complete the next step, to grant CloudZero access to your GCP billing data.

## Step 3: Grant access to CloudZero

Next, grant CloudZero access to your GCP Billing Data. You will use the **Service Principal** saved when you set up the Connection in the previous step. In the following instructions, replace `<cz-service-principal>` anywhere you see it with the **Service Principal** value you copied.

1. Log in to the GCP Console.
2. Select the Project which holds your billing account data and go to BigQuery.
3. Find the billing data export table. It should look like this: `gcp_billing_export_resource_v1_<billing_account_id>`
   ![](https://files.readme.io/987b4bb-Screen_Shot_2022-09-09_at_10.12.44_AM.png)
4. Select that table and click **[+SHARE]**:
   ![](https://downloads.cloudzero.com/documentation/resources/0eaf7b2-Screen_Shot_2022-09-09_at_10.13.16_AM.png)
5. Click **[+ ADD PRINCIPAL]**:
   ![](https://files.readme.io/b4f07c2-Screen_Shot_2022-09-09_at_10.13.36_AM.png)
6. Add the Service Principal and role, then click **[SAVE]**.
   * Service Account: `<cz-service-principal>`
   * Role: `BigQuery Data Viewer`
     ![](https://downloads.cloudzero.com/documentation/resources/b6d607e-Screen_Shot_2022-09-09_at_10.14.01_AM.png)

## Step 4: Return to the Cloud Integrations page

After your Connection is saved, it will appear in **Billing Connections** table of the CloudZero Cloud Integrations page with a status of **Pending Data** and a **Last Checked** status of **Pending First Ingest**.

At this time, the CloudZero platform will attempt to connect to your BigQuery table using the Service Principal assigned to your organization.

<Image align="center" alt="Billing Connections table" border={true} src="https://downloads.cloudzero.com/documentation/resources/billing-connections.png" className="border" />

After the connection has been verified, the **Health** column will update from **Pending Data** to **Healthy**.

If there are issues with your connection, you may see an **Error** status instead of a **Healthy** one. If this happens, you can hover over the status button to get additional information. You may also want to verify your GCP table name saved to the Connection, and that your Service Principal was properly granted access to the table when you granted access to CloudZero.

<Callout icon="ℹ️" theme="info">
  Discovery (the act of switching from a **Pending First Ingest** to a **Healthy** status) can take up to an hour. It can take up to 24 hours to synchronize new accounts and to see cost data in the Explorer.
</Callout>
