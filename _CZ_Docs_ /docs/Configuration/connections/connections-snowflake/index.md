---
title: Connecting to Snowflake
category: getting-started
createdAt: '2020-02-13T19:39:05.363Z'
hidden: false
slug: connections-snowflake
updatedAt: '2021-11-30T17:29:59.987Z'
---
# How the Snowflake Connection works

CloudZero relies on account usage and cost information. Connecting to a Snowflake account will show Snowflake cost data alongside other Cost Sources in the Explorer, as well as enable anomaly alerts on Snowflake spend.

CloudZero gets access to your Snowflake data through a share from your account to the CloudZero Snowflake account in the same region using [Secure Data Sharing](https://docs.snowflake.com/en/user-guide/data-sharing-intro.html#introduction-to-secure-data-sharing).

<Callout icon="ℹ️" theme="info">
  CloudZero supports all Snowflake regions except for SnowGov.
</Callout>

You must connect each of your Snowflake accounts individually to CloudZero, except for reader accounts.

A Snowflake [reader account](https://docs.snowflake.com/en/user-guide/data-sharing-reader-create) should not be connected to CloudZero because the provider account assumes all responsibility for credit charges incurred by users of the reader account.

<Callout icon="ℹ️" theme="info">
  All of CloudZero's permissions are read-only. CloudZero has no access to data except where explicitly authorized. The SQL script CloudZero offers through the application does require write permissions in order to create the read-only resources for you.
</Callout>

The following summarizes the permissions needed by CloudZero.

* Roles: CLOUDZERO_COPY_BILLING_DATA_ROLE: role that can read data and execute the sync procedure
* Databases: CLOUDZERO_SHARED_DATA: database that sits between your billing views and the share with CloudZero
* Procedures: CLOUDZERO_COPY_BILLING_DATA: stored procedure to sync data periodically from the billing tables and views
* Tables and Views
  * ACCOUNT_USAGE.METERING_HISTORY
  * ACCOUNT_USAGE.METERING_DAILY_HISTORY
  * ACCOUNT_USAGE.DATABASE_STORAGE_USAGE_HISTORY
  * ACCOUNT_USAGE.STAGE_STORAGE_USAGE_HISTORY
  * ORGANIZATION_USAGE.USAGE_IN_CURRENCY_DAILY
  * ORGANIZATION_USAGE.REMAINING_BALANCE_DAILY
  * ACCOUNT_USAGE.WAREHOUSE_EVENTS_HISTORY
  * ACCOUNT_USAGE.QUERY_HISTORY (Note: The `query_text` column is excluded to avoid capturing sensitive data
  * ACCOUNT_USAGE.TAGS
  * ACCOUNT_USAGE.TAG_REFERENCES
* Shares: CLOUDZERO_SHARE: shares data from CLOUDZERO_SHARED_DATA database with CloudZero Snowflake account

# Connect a Snowflake Account

You must have the necessary permissions to add new Connections to the CloudZero platform. The steps follow.

## Start Creating the Snowflake Connection

1. Navigate to the Cloud Integrations page by using the gear icon on the top navigation bar and selecting **Cloud Integrations** or  opening [https://app.cloudzero.com/organization/connections](https://app.cloudzero.com/organization/connections)
2. The Cloud Integrations page shows all of the Connections in your system. To connect a Snowflake Account, click the **Add Connection** button.
3. On the next page, click the **Snowflake** tile.

<Image alt="CloudZero Add a New Connection" border={false} src="https://downloads.cloudzero.com/documentation/resources/billing-connections-add-connection.png" />

The page that opens summarizes how the Snowflake Connection works, as is explained in this documentation. Click the **Get started** button.

## Enter the Snowflake Account Information

1. Identify the following costs applicable to your Snowflake contract: **Cost Per Credit**: Your Snowflake account’s Capacity Credit Price and **Cost Per TB Month**: Your Snowflake account’s Capacity Storage Price. To do this, you can:
   1. Query the Snowflake [Rate_Sheet_Daily view](https://docs.snowflake.com/en/sql-reference/organization-usage/rate_sheet_daily) for the correct usage types and contract.
   2. OR identify the corresponding charges on your Snowflake bill, which will detail the rate being charged per credit and TB Month.
2. On the page that is open, enter your Snowflake account information:

   * **Connection Name**: This is the name you will see throughout the CloudZero UI, in addition to the Snowflake Account ID.
   * **Cost Per Credit**: The Snowflake account’s Capacity Credit Price you have identified.
   * **Cost Per TB Month**: The Snowflake account’s Capacity Storage Price you have identified.
   * **Cost Effective Date**: The date on which the`Cost Per` values became effective. If your `Cost Per`values have been the same since you created your Snowflake account, select a date from around the time the account was created.
   * **Snowflake Account ID**: The value returned from running `SELECT LOWER(CURRENT_ACCOUNT())` in your Snowflake account.
   * **Snowflake Account Region**: The value returned from running
     `SHOW REGIONS;
     SELECT display_name FROM TABLE(RESULT_SCAN(LAST_QUERY_ID())) WHERE snowflake_region = CURRENT_REGION();`
3. Click **Save**.

## Create a Share in your Snowflake account

After you save your account information, a SQL script opens in a text box.

1. Copy the SQL script.
2. Paste it into a Snowflake worksheet in your account.
3. Review the Script
4. Select the **All Queries** Checkbox
5. Click **Run** to create and share the necessary data with CloudZero

<Callout icon="ℹ️" theme="info">
  This script can take a while to run if you have no used these billing tables before. Based on CloudZero's experience, you can expect first use to take 3+ hours; however, subsequent uses usually take minutes.
</Callout>

The SQL script creates a direct share with a comment like `ref=<external_id>`. The comment is required to aid CloudZero in accurately identifying shares. The `external_id` used is arbitrary and does not reveal any information about your account or data.

## Return to the Cloud Integrations page

Refresh the Cloud Integrations page to see the status of your Snowflake Connection. When CloudZero discovers the share you have created, a Snowflake Connection will appear on the CloudZero Cloud Integrations page in the **Billing Connections** table.

<Image alt="Billing Connections table on Cloud Integration page" border={false} src="https://downloads.cloudzero.com/documentation/resources/billing-connections.png" />

When the connection has been verified, the **Health** column will update from **Pending Data** to **Healthy**. Discovery can take up to an hour. It can take up to a day to synchronize new accounts before you see cost data in the Explorer.

If something changes on your side and CloudZero can no longer use the role that was just granted permissions, the **Health** will change and provide details on why CloudZero cannot connect.

Connect additional Snowflake Accounts using the same process.
