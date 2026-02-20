---
title: Connecting to Datadog
category: getting-started
createdAt: '2023-09-11'
hidden: false
slug: connections-datadog
updatedAt: '2023-09-11'
---
# How the Datadog Connection works

Connecting to a Datadog account will show Datadog cost data alongside other Cost Sources in the Explorer, as well as enable anomaly alerts on Datadog spend.

The CloudZero platform will ingest Datadog cost data by making requests to the Datadog Usage Metering API.

<Callout icon="ℹ️" theme="info">
  All of CloudZero's permissions are read-only. CloudZero has no access to data except where explicitly authorized.
</Callout>

The following summarizes the CloudZero Permissions:

* Usage Read Authorization Scope: grants read-only access to view usage and cost data associated with your Datadog account.
* Billing Read Authorization Scope: grants read-only access to view billing data associated with your Datadog account.
* Metrics Read Authorization Scope: grants-read only access to view custom metrics associated with your Datadog account.
* Timeseries Query Authorization Scope: grants read-only access to query Timeseries data associated with custom metrics.

For a new or re-authorized Connection, discovery, the act of switching from a `Pending First Ingest` to a `Healthy` status as reported on the Connections Detail page, can take up to an hour. It can take up to 24 hours to synchronize new accounts and begin to see cost data in the Explorer.

The following summarizes the billing period ingest windows:

* Newly Created Connection: CloudZero will ingest the most recent 12 months of billing periods if available.
* Re-enabled Connection: CloudZero will ingest up to 12 months of billing periods starting from the current billing period going back to the most recent billing period ingested.
* Steady State: CloudZero will ingest the current billing period every day of the month and also the previous billing period until the 17th of the month.

# Datadog Billing models

Datadog bills based on several pricing strategies that vary between products. As a result, costs are represented in the CloudZero platform using different models that depend on the Datadog product and how it is billed.

In the period preceding March 2024, there may be instances where costs exhibit a negative value.

## Pricing with commitment

Monthly commitments are fixed, and costs are shown evenly amortized over the entire month.

## On-demand pricing

On-demand pricing can vary by Datadog product and usage.

## Average Pricing Model

Products using the Average Pricing Model are billed based on the average usage over the month. Costs shown are amortized over the month and include only what was incurred to date.

## High-Water Mark Pricing Model

Products using the High-Water Mark Pricing Model are billed based on the maximum usage of a resource during any one hour of the month. For a newly established High-Water Mark for a particular month, costs will show an increase for the remainder of that month. Costs shown are amortized over the month and include only what was incurred to date.

# Datadog Cost

To determine a Datadog product's daily cost, CloudZero leverages Datadog's Estimated Cost [endpoint](https://docs.datadoghq.com/api/latest/usage-metering/#get-estimated-cost-across-your-account), which returns each product's _estimated_ aggregate monthly cost for every day of the month.

Data from the Estimated Cost endpoint is only available for the current and previous month at the time when the request is made. For months outside of this window, CloudZero leverages Datadog's Historical Cost endpoint. Since this endpoint provides a single cost per product for the entire month, cost is amortized evenly over the month. This will most frequently apply to historical months collected during initial ingest when the Estimated Cost data is not available.

On occasion, data from the Estimated Cost endpoint diverges from Datadog's reported usage. While cost is broken down by committed and on_demand, this split is not reported by any of Datadog's usage endpoints (for example, [Billable usage across your account](https://docs.datadoghq.com/api/latest/usage-metering/#get-billable-usage-across-your-account), [Hourly usage by product family](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-by-product-family), [Hourly usage attribution](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-attribution)). As a result, CloudZero uses the Estimated Cost data as a reference point to estimate usage.

# Cost by tags

<Callout icon="ℹ️">
  Breaking down usage by tags requires usage attribution. You must be on the Datadog Enterprise plan and have [usage attribution](https://docs.datadoghq.com/account_management/billing/usage_attribution) enabled for your organization.
</Callout>

Datadog allows organizations with usage attribution enabled to choose up to three existing tags to break down usage. If this feature is enabled for your organization, CloudZero will automatically bring in these tags with your Datadog connection. No additional permissions or configuration are required. You will be able to see costs broken down by all possible combinations of tag values, allowing you to allocate costs to individual resources.

# Create a Datadog connection

<Callout icon="ℹ️" theme="info">
  You must be a CloudZero Admin to add new Connections to the platform.

  You must also have the ability to grant `Usage Read`, `Billing Read`, `Metrics Read`, and `Timeseries Query` scopes in a _non-trial_ Datadog organization.

  If you have multiple Datadog parent organizations, sign out of all Datadog tenants before you create a Datadog connection.
</Callout>

1. Open the Cloud Integrations page. You can find the Cloud Integrations page by using the gear icon on the top navigation bar and selecting **Cloud Integrations** or at [https://app.cloudzero.com/organization/connections](https://app.cloudzero.com/organization/connections).

2. Select the **Add Connection** button.

3. On the page that opens, you will see a list of possible connection types. Select the **Datadog** tile to begin setting up a Datadog connection.

   <Image align="center" alt="Datadog Connection Tile" border={true} src="https://downloads.cloudzero.com/documentation/resources/connection-tiles.png" className="border" />

4. On the next page, enter a **name** for the connection and select the **site** on which your Datadog account is based, that is, the URL used to log in to your account. Then select **Get started**.

5. The **Add a New Datadog Connection** page opens. Give your connection a **name**, which will identify your Datadog connection throughout the CloudZero platform. Click the **Continue** button.

6. You will then be redirected to Datadog. Select the appropriate site from the drop-down list and log in to your Datadog account. :information_source: IMPORTANT: Parent-Level organization access is required. Usage data is available only for parent-level organizations. Be sure the site you select matches the location of your parent-level organization in Datadog.

<Image alt="Datadog site selecton drop-down menu" border={false} src="https://downloads.cloudzero.com/documentation/resources/datadog-region-dropdown.png" />

7. In response to the prompt to authorize CloudZero access to a Datadog organization, select the parent-level organization and then click the **Authorize** button. :information_source: In order for CloudZero to have access to the Datadog APIs, the user providing authorization must also have `Usage Read` and `Billing Read` permissions.

<Image alt="Datadog Authorize Access permissions list" border={false} src="https://downloads.cloudzero.com/documentation/resources/datadog-authorize-access.png" />

8. You will be redirected back to the **Connection Details** page in the CloudZero platform; verify that you see  your newly created Datadog connection.

# Reauthorize a Datadog Connection

In the event CloudZero no longer has access to Datadog through the existing authorization, you can reauthorize the Connection.

1. Open the **Cloud Integrations** page. You can find the Cloud Integrations page by selecting the gear icon from the sidebar and selecting **Cloud Integrations**, or at [https://app.cloudzero.com/organization/connections](https://app.cloudzero.com/organization/connections).

2. Select the Datadog connection you would like to reauthorize from the **Billing Connections** table.

3. The **Connection Details** page for a Datadog connection opens. Click the **Reauthorize** button near the top of the page, to the right of **Datadog Connection Details**.

   <Image align="center" alt="Datadog Reauthorize button on Connection Details page" border={true} src="https://downloads.cloudzero.com/documentation/resources/datadog-connection-details.png" className="border" />

4. You will then be redirected to Datadog. Select the appropriate site from the dropdown and log in to your Datadog account. :information_source: In order for CloudZero to have access to the Datadog APIs, the user providing authorization must also have `Usage Read` and `Billing Read` permissions.

5. You will be asked to authorize CloudZero access to a Datadog organization. Select the parent-level organization, and then click the **Authorize** button. :information_source: In order for CloudZero to have access to the Datadog APIs, the user providing authorization must also have `Usage Read` and `Billing Read` permissions.

6. You will be redirected back to the **Connection Details** page, where you should see the Datadog connection you have just reauthorized.

When your connection is saved, it will appear in the **Billing Connections** table of the CloudZero Cloud Integrations page with a status of **Pending Data** and a **Last Checked** status of **Pending First Ingest**.

<Image align="center" alt="Billing Connections table" border={true} src="https://downloads.cloudzero.com/documentation/resources/billing-connections.png" className="border" />

When the connection has been verified, the **Health** column will update from **Pending Data** to **Healthy**.

f there are issues with your connection, you may see a status of **Error** instead of **Healthy**. If this happens, you can hover over the status button or navigate to the connection details page to find additional information.
