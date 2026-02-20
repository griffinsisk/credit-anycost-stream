---
title: Snowflake Data Shares
category: features
createdAt: '2024-04-29T01:50:43.146Z'
hidden: false
slug: snowflake-data-shares
updatedAt: '2024-04-29T16:38:31.562Z'
---
CloudZero offers a self-service feature to create and manage billing data Views that can be easily shared with others through a Snowflake Data Share.

<Callout icon="⚠️" theme="warn">
  CloudZero facilitates sharing through Data Shares exclusively within the AWS us-east-1 region. If you require data availability outside of this region, you may replicate the Data Share from AWS us-east-1 to your desired region. For detailed instructions on how to set up this replication, see  [the Snowflake documentation](https://docs.snowflake.com/en/user-guide/secure-data-sharing-across-regions-platforms).
</Callout>

# What is a Snowflake Data Share?

A Snowflake Data Share is a secure and convenient way to share data between Snowflake accounts. It is essentially a virtual database that contains one or more shared data Views, which can be thought of as virtual database tables. The Snowflake Data Shares feature allows you to manage your own Views that become available to you by putting the View within a CloudZero-managed Snowflake Data Share that is securely shared to selected Snowflake accounts. For more information, see [the Snowflake documentation about data sharing](https://docs.snowflake.com/en/user-guide/data-sharing-intro).

Data Shares will include columns for each Cost and Usage Type that exist in CloudZero.

# Benefits of using a Snowflake Data Share

By using a Snowflake Data Share, you can:

* Access all of your data in a secure and controlled manner.
* Use your own SQL and Business Intelligence (BI) tools for deeper analysis and insights.
* Gain more value from the data collected by CloudZero.

This feature allows you to take control of your data and perform advanced analysis.

# Snowflake View management

<Callout icon="ℹ️" theme="info">
  You must have admin permissions to manage Snowflake Data Views.
</Callout>

## Create a View

To create a new Snowflake View:

1. Click the **settings icon** at the top right of the page.
2. Select **Data Sharing** under the navigation menu on the left.
3. Click **Add a Snowflake View** on the top right.
4. In **Snowflake View Name**, enter your desired name for the View.
5. Select the desired Dimensions that contain the data you would like to include in your Data Share.
6. Select the time range you would like your data to be restricted to
   Keep in mind that the longer your time range, the slower your share may perform. Ensure you select only the time range that best meets your needs to have the optimal experience.
7. Select the granularity you would like exposed within your Data Share
8. Choose the Snowflake Account(s) where your View will be shared. The list provided is limited to Snowflake account(s) that have already been connected to the CloudZero platform.
9. After saving the view, allow a moment for the system to create and share the Data Share.

## Edit View

1. Select a View that you like to edit.
2. Make the modifications you would like to the View.
3. Click **Save View**.

Once the View has been successfully modified, allow some time for the changes to be propagated to your selected Snowflake account(s).

<Callout icon="⚠️" theme="warn">
  If you change the name of the View, the original View will be removed from the Data Share.
</Callout>

## Delete View

1. Select a View that you like to delete.
2. Click **Delete**.

After the View has been successfully deleted, allow some time for the change to be propagated to your selected Snowflake account(s).

<Callout icon="ℹ️" theme="info">
  New Dimensions will not be available until the next data materialization cycle.
</Callout>

# Connect to the Shares View

When you have created and shared your Data Share and a Snowflake View with the desired Snowflake accounts, follow these steps to begin working with the shares.

1. In the appropriate Snowflake Account, as an Account Admin run `SHOW SHARES;` to display all of the available shares.
   For more details, see [Show Shares in the Snowflake documentation](https://docs.snowflake.com/en/sql-reference/sql/show-shares).
2. Your share will be listed as an `inbound` share type with the following naming pattern: `CLOUDZERO_<account_id>_<organization_id>`.
   Example: `“CLOUDZERO_ABC12345.AWS_US_EAST_1_ef307f91-e98d-4b82-8a10-afcf5a464345"`
3. To create a Snowflake database from the provided share, use the following command: `CREATE DATABASE <name> FROM SHARE <cloudzero_account>.<share_name>;`.
   Example:
   `CREATE DATABASE My_Database FROM SHARE ABC12345.“CLOUDZERO_ABC12345.AWS_US_EAST_1_ef307f91-e98d-4b82-8a10-afcf5a464345"`, where `ABC12345` is the account where the share resides in the customer’s Snowflake instance, and the rest is the name of the share.

<Callout icon="ℹ️" theme="info">
  The share name will have dashes in it, and so Snowflake will require double quotes around the name or there will be an error.
</Callout>

For more details, see the [Snowflake documentation on consuming imported data](https://docs.snowflake.com/en/user-guide/data-share-consumers).
