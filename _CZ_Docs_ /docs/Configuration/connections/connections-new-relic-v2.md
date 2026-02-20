---
title: Connecting to New Relic
category: getting-started
createdAt: '2024-01-25'
hidden: false
metadata:
  title: Connecting to New Relic
slug: connections-new-relic-v2
updatedAt: '2024-07-15'
---
# How the New Relic Connection works

The CloudZero New Relic connection uses the New Relic Query Language to pull your New Relic consumption data and combine it with New Relic rate information provided by you to calculate your New Relic spend. The connection will pull as many accounts as the New Relic API key has access to query. To pull all New Relic consumption data you must provide an API key associated with your New Relic parent account.

The following summarizes the billing period ingest windows.

* **Newly Created Connection**: CloudZero will ingest the most recent 12 months worth of billing periods if available.
* **Re-enabled Connection**: CloudZero will attempt to ingest up to 24 months of billing periods starting from the current billing period and going back to the most recent billing period ingested.
* **Steady State**: CloudZero will ingest the current billing period and sometimes the previous billing period.

For more information, see the [New Relic Connection features section](/docs/connections-new-relic-v2#/new-relic-connection-features) of this page.

# Create a New Relic connection

Open the Connections page. From the **gear** icon on the top navigation, select **Connections**, or navigate to  [https://app.cloudzero.com/organization/connections](https://app.cloudzero.com/organization/connections).

When the Connection page opens, select the **Add New Connection** button. Then select the **New Relic** tile.
![](https://downloads.cloudzero.com/documentation/resources/billing-connections-add-connection.png)

Navigate to **Administration** > **Plan & Usage** > **Plan summary** in the New Relic app to locate information about your account.

<Image border={false} src="https://downloads.cloudzero.com/documentation/resources/new-relic-plan-summary-page.png" />

Enter the Connection metadata found in the New Relic app.

* **Connection Name**: A connection name that will appear in the CloudZero UI.
* **Billing Account ID**: Your New Relic parent account ID.
  ![](https://downloads.cloudzero.com/documentation/resources/new-relic-billing-account-id.png)
* **New Relic Account Region**: the region your New Relic account uses (`US` or `EU`)
  ![](https://downloads.cloudzero.com/documentation/resources/new-relic-account-region.png)
* **API Key**: a New Relic User API Key
  To create this key navigate to the **Administration** > **API Keys** page.
  ![](https://downloads.cloudzero.com/documentation/resources/new-relic-api-key-menu.png)

Click the **Create a key** button and proceed to create a **User** API key. Select the **Account ID and Name**, select the** User Key type, enter a **Name** for the key, and enter any **Notes**, for example, `For the CloudZero New Relic Connection`.

<Image border={false} src="https://downloads.cloudzero.com/documentation/resources/new-relic-create-api-key.png" />

<Callout icon="ℹ️" theme="info">
  The connection will pull data for all accounts available to the API key. If you would like to include data from all accounts, use an API key associated with your New Relic parent account.
</Callout>

Locate your rate Information; navigate to **Administration** > **Plan & Usage** > **Plan summary**.

* **Subscription Term Start Date**: The date you signed your contract with New Relic
* **Data**: The price you pay per GB of data ingested into New Relic
  ![](https://downloads.cloudzero.com/documentation/resources/new-relic-data-ingest-rate.png)
* **Basic Users**: The price you pay per Basic User (likely $0)
* **Core Users**: The price you pay per Core User
  ![](https://downloads.cloudzero.com/documentation/resources/new-relic-core-user-rate.png)
* **Full Platform Users**: The price you pay per Full Platform User
  ![](https://downloads.cloudzero.com/documentation/resources/new-relic-full-platform-user-rate.png)
* **Additional Synthetic Checks**: The price you pay per Synthetic Check
  ![](https://downloads.cloudzero.com/documentation/resources/new-relic-synthetic-check-rate.png)

<Callout icon="ℹ️" theme="info">
  New Relic has tiered pricing for some agreements, with rates that change depending on usage. If the amount you pay for **Data**, **Basic Users**, **Core Users**, **Full Platform Users**, or **Additional Synthetic Checks** changes based on your usage, click the **Add Tier** button for the relevant fields and provide that information. **Do not account for free usage with tiers.** For example, the first 100 GB per month is free.

  If your agreement with New Relic recently changed and you want to properly calculate old consumption data with your old agreement, contact your FinOps Account Manager or Customer Success representative.
</Callout>

Click the **Save** button to save the Connection.

You will be redirected back to the **Connection Details** page in the CloudZero platform; verify that you see your newly created New Relic Connection.

# New Relic Connection features

## Event data ingest usage calculation (beta)

New Relic provides [data ingest usage accurately for usage metric groups](https://docs.newrelic.com/docs/tutorial-optimize-telemetry/intro-to-optimal-telemetry/#understand-nr-consumption-metrics), but can provide only [estimated data ingestion figures for individual events](https://docs.newrelic.com/docs/accounts/accounts-billing/new-relic-one-pricing-billing/usage-queries-alerts/#byte-count-estimate). Data ingest usage with event granularity is calculated by assigning a portion of the total data ingest to each event where the ratio of the portion to the total data ingest is equal to the ratio of that event's estimated data ingest to the total estimated data ingest.

## Tags in the New Relic Connecton

The New Relic Connection includes tags:

* `nr_cz:account_name`: Human readable name of the account associated with the usage.
* `nr_cz:entity_name`: Name of the New Relic entity associated with the usage.
* `nr_cz:service.name` and `nr_cz:service.namespace`: Coalesce various facets of New Relic event types. The following table maps each event type and facet field to the corresponding tag:

| Event Type                       | Facet Field                                         | Tag                       |
| -------------------------------- | --------------------------------------------------- | ------------------------- |
| `Metric`                         | `newrelic.source`                                   | `nr_cz:service.name`      |
| `Log`                            | `plugin.type`                                       | `nr_cz:service.name`      |
| `PageView`                       | `appName`                                           | `nr_cz:service.name`      |
| `PageViewTiming`                 | `appName`                                           | `nr_cz:service.name`      |
| `AjaxRequest`                    | `appName`                                           | `nr_cz:service.name`      |
| `BrowserTiming`                  | `appName`                                           | `nr_cz:service.name`      |
| `JavaScriptError`                | `appName`                                           | `nr_cz:service.name`      |
| `PageAction`                     | `actionName OR appName`                             | `nr_cz:service.name`      |
| `Span`                           | `browserApp.name OR mobileApp.name OR service.name` | `nr_cz:service.name`      |
| `NetworkSample`                  | `hostname`                                          | `nr_cz:service.name`      |
| `StorageSample`                  | `hostname`                                          | `nr_cz:service.name`      |
| `SyntheticRequest`               | `monitorName`                                       | `nr_cz:service.name`      |
| `SyntheticPrivateLocationStatus` | `name`                                              | `nr_cz:service.name`      |
| `MobileSession`                  | `newRelicAgent`                                     | `nr_cz:service.name`      |
| `Mobile`                         | `name`                                              | `nr_cz:service.name`      |
| `MobileSession`                  | `osName`                                            | `nr_cz:service.name`      |
| `MobileHandledException`         | `osName`                                            | `nr_cz:service.name`      |
| `MobileCrash`                    | `osName`                                            | `nr_cz:service.name`      |
| `MobileRequestError`             | `osName`                                            | `nr_cz:service.name`      |
| `MobileRequest`                  | `osName`                                            | `nr_cz:service.name`      |
| `InfrastructureEvent`            | `provider`                                          | `nr_cz:service.name`      |
| `SyntheticsPrivateMinion`        | `minionIpv4`                                        | `nr_cz:service.name`      |
| `Metric`                         | `metricName`                                        | `nr_cz:service.namespace` |
| `Log`                            | `syslog.app.name`                                   | `nr_cz:service.namespace` |
| `Span`                           | `appName`                                           | `nr_cz:service.namespace` |
| `SyntheticRequest`               | `domain`                                            | `nr_cz:service.namespace` |
| `MobileSession`                  | `appName`                                           | `nr_cz:service.namespace` |
| `MobileHandledException`         | `appName`                                           | `nr_cz:service.namespace` |
| `MobileCrash`                    | `appName`                                           | `nr_cz:service.namespace` |
| `MobileRequestError`             | `appName`                                           | `nr_cz:service.namespace` |
| `MobileRequest`                  | `appName`                                           | `nr_cz:service.namespace` |
| `Mobile`                         | `device OR deviceType`                              | `nr_cz:service.namespace` |
| `InfrastructureEvent`            | `source`                                            | `nr_cz:service.namespace` |

## Usage Metric Group

The New Relic Connection merges a selection of facets for certain event types with the New Relic Usage Metric Group. Cost data from New Relic will always include the Usage Metric Group associated with the type of usage and, for certain event types, the value from the facet field in the following table:

| Event Type               | Facet Field       |
| ------------------------ | ----------------- |
| `Metric`                 | `dataType`        |
| `Log`                    | `newrelic.source` |
| `NetworkSample`          | `dataType`        |
| `StorageSample`          | `agentName`       |
| `MobileSession`          | `platform`        |
| `MobileHandledException` | `platform`        |
| `MobileCrash`            | `platform`        |
| `MobileRequestError`     | `platform`        |
| `MobileRequest`          | `platform`        |

<br />
