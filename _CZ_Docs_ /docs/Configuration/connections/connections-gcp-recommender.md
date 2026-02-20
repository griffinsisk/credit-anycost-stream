---
title: Connecting to GCP - Recommender
category: features
createdAt: '2024-07-24'
hidden: false
slug: connections-gcp-recommender
updatedAt: ''
---
# How the GCP Recommender Connection works

CloudZero can ingest GCP Recommender data by connecting to your BigQuery tables that store this data. Recommender data provides valuable insights and recommendations about your GCP cloud costs:

* Insights: Identify issues such as overpayments for reserved instances.
* Recommendations: Suggest corrective actions, such as modifying your reservation plan.

CloudZero uses this Recommender data to enhance the CloudZero Optimize feature, offering a comprehensive view for optimizing your cloud costs.

For a full list of supported Recommenders, see [Supported GCP Recommenders](/docs/gcp-recommender-insights).

<Callout icon="ℹ️" theme="info">
  All of CloudZero's permissions are read-only. CloudZero has no access to data except where explicitly authorized. The **BigQuery Data Viewer** grants read access only, to allow loading data from Cloud Billing Export and Cloud files stored in BigQuery.
</Callout>

# Connect a GCP Recommender ingest

You must have an existing [GCP Billing Connection](/docs/connections-gcp-billing) before you can set up GCP Recommender ingest.

Setting up a GCP Recommender connection is similar to setting up a GCP Billing connection.

Complete the following steps to set up a GCP Recommender ingest:

1. [Configure a Data Transfer for recommendations in GCP.](#step-1-configure-a-data-transfer-for-recommendations-in-gcp)
2. [Set up Recommender ingest in CloudZero.](#step-2-set-up-recommender-ingest-in-cloudzero)
3. [Grant access to CloudZero.](#step-3-grant-access-to-cloudzero)
4. [Save the connection.](#step-4-save-connection-in-cloudzero)

## Step 1: Configure a Data Transfer for recommendations in GCP

First, you must configure a Data Transfer for Recommender data in the Google Cloud console. You may already have completed these steps for other purposes, but confirm the steps here match what you have previously set up.

1. Set up a **Data Transfer** in GCP BigQuery by following the Recommended instructions to [Create a Data Transfer for Recommendations](https://cloud.google.com/recommender/docs/bq-export/export-recommendations-to-bq).

2. When access is established to both the `insights_export` and `recommendations_export` tables, from the information on the GCP Recommender table, make note of each table's fully qualified name, the **Table ID**, for use in the next step, setting up Recommender ingest.
   This name consists of the Project ID, Dataset, and Table name of the table you configured.
   * For example:
     * `billing-administration-123456.all_recommender_data.insights_export`
     * `billing-administration-123456.all_recommender_data.recommendations_export`
   * In the examples:
     * Project ID: `billing-administration-123456`
     * Dataset: `all_recommender_data`
     * Table names: `insights_export` and`recommendations_export`

<Image align="center" alt="GCP Recommender Table with Table ID called out" border={true} caption="GCP Recommender Table" src="https://downloads.cloudzero.com/documentation/resources/gcp-recommender-insights-table-name.png" />

<Callout icon="ℹ️" theme="info">
  Note that it can take up to 24-48 hours for your export table to appear. It does not appear until GCP completes its first data drop, which can take a day or two. **Y**ou cannot continue the connection process until the table has been created.
</Callout>

## Step 2: Set up Recommender ingest in CloudZero

When the `insights_export` and `recommendations_export` tables are available, you can set up GCP Recommender ingest in the CloudZero platform.

1. In CloudZero, navigate to [Settings](https://app.cloudzero.com/organization/connections) by selecting the **gear icon** in the top navigation bar.
2. Select the **Add Connection** button.
3. Select **GCP Recommender > Get started**.
4. Enter a **Connection Name**.
   This is the name you will see throughout the CloudZero platform. It cannot contain spaces, periods, or special characters, except for hyphens and underscores.
5. In the **Ingest Usage Optimizations from GCP Recommender** section of the screen, enter the **Fully Qualified Insights Table Name** you copied when you configured the Data Transfer in the previous step.
   Example: `billing-administration-341920.all_recommender_data.insights_export`
6. Enter the **Fully Qualified Recommendations Table Name** you copied when you configured the Data Transfer in the previous step.
   Example: `billing-administration-341920.all_recommender_data.recommendations_export`

<Image align="center" alt="Complete the CGP Recommender table fields" border={true} src="https://files.readme.io/e22df64e7ac6f9b41921b37a4e322e553539acb29f533162766ab82b6ad0729a-CGP-recommender-screen-2025-08-12" className="border" />

## Step 3: Grant access to CloudZero

Grant CloudZero's service principal access to your GCP Recommender Data. Copy the **Service Principal** ID shown in the **Grant Access to CloudZero** section:

<Image align="center" alt="Copy the Service Principal ID" border={true} src="https://downloads.cloudzero.com/documentation/resources/gcp-recommender-service-principal-id.png" className="border" />

Follow these instructions to replace `<cz-service-principal>` with the service principal ID you copied.

1. Log into the GCP Console.
2. Select the Project which holds your Recommender data and go to BigQuery.
3. Find the `insights_export` table.
4. Select that table and click **[+SHARE]**.
5. Click **[+ ADD PRINCIPAL]**.
6. Add the service principal and role, then click **[SAVE]**.
   * Service Principalt: `<cz-service-principal>`
   * Role: `BigQuery Data Viewer`

## Step 4: Save Connection in CloudZero

In CloudZero, select the **Save** button. CloudZero redirects you to the [Cloud Integrations](https://app.cloudzero.com/organization/connections) page, where you can view your new GCP Recommender connection in the **Billing Connections** table:

<Image align="center" alt="GCP Recommender Connections in the Billing Connections table" border={true} src="https://downloads.cloudzero.com/documentation/resources/gcp-recommender-billing-connections-table.png" className="border" />

The GCP Recommender connection will have a **Status** of **Pending Data** and a **Last Checked** status of **Pending First Ingest** while CloudZero attempts to connect to your BigQuery table using the Service Principal assigned to your organization.

After CloudZero has processed the first ingest of data, the **Status** changes from **Pending Data** to **Healthy**. This can take several hours.

# View Connection details

After you have created the GCP Recommender connection, select its name on the [Cloud Integrations](https://app.cloudzero.com/organization/connections) page to view detailed information, including the following:

* Connection status
* Connection name
* Connection ID
* GCP connection ID
* Service principal name
* Fully qualified Insights table name
* Fully qualified Recommendations table name
* When the connection was created
* When the connection was most recently checked for new data

<Image align="center" alt="GCP Recommender connection details" border={true} src="https://downloads.cloudzero.com/documentation/resources/gcp-recommender-details-page.png" className="border" />
