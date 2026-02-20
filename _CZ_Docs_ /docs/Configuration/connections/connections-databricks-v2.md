---
title: Connecting to Databricks
category: getting-started
createdAt: '2024-03-21'
hidden: false
metadata:
  title: Connecting to Databricks
slug: connections-databricks-v2
updatedAt: '2024-05-16'
---
**Connections** are how CloudZero manages the [various Cost Sources](/docs/connections) that bring Billing, Resource, and other types of data into the platform.

# How the Databricks connection works

The CloudZero Databricks connection uses API access to a single Databricks workspace to gather consumption and pricing data for all workspaces in the account by querying the [Billable Usage](https://docs.databricks.com/en/administration-guide/system-tables/billing.html), [Pricing](https://docs.databricks.com/en/administration-guide/system-tables/pricing.html), and [compute](https://docs.databricks.com/en/administration-guide/system-tables/compute.html) system tables.

You must use this billing connection if you are using Databricks on AWS that you have purchased directly from Databricks.

<Callout icon="ℹ️" theme="info">
  If you are using Databricks purchased through the Azure or GCP Marketplace, those services provide cost and usage data as part of their billing connections.

  You can use the CloudZero connector for Databricks purchased through the Azure or GCP Marketplace to obtain better data granularity, but if you do, you will run the risk of introducing duplicate Databricks cost and usage data into CloudZero.
</Callout>

# Connection prerequisites for Databricks

## Databricks settings

### Unity Catalog

To access Databricks system tables, you must have a workspace enabled for Unity Catalog. For details, see [Databricks Unity Catalog](https://docs.databricks.com/en/data-governance/unity-catalog/index.html)

### Billing and compute schemas

The `system.billing` and `system.compute` "system schemas" must then be enabled in that workspace.

### Service principal

CloudZero requires credentials for a Databricks service principal that can access tables in those schemas in that workspace. CloudZero recommends you create a new service principal with narrowly scoped permissions. For details see the section [Configuring a Databricks service principal](/docs/connections-databricks-v2#configuring-a-databricks-service-principal).

### Warehouse

CloudZero requires the warehouse id of a warehouse to use while querying billing and usage information. CloudZero does not require a dedicated warehouse.

<Callout icon="ℹ️" theme="info">
  If you are creating a new warehouse for CloudZero billing queries, CloudZero recommends specifying a serverless warehouse with the lowest Auto Stop, Scaling, and Cluster Size settings possible.
</Callout>

## Enabling the billing and compute schemas

The goal is to make available the billing and usage data CloudZero needs to query. The data will be made available in the Unity Catalog enabled workspace identified in the pre-requisites section. This can be done through the Databricks CLI.

### Installing the Databricks CLI

If you have not used it before, [Download and install the Databricks CLI.](https://docs.databricks.com/en/dev-tools/cli/install.html)
You can set up a Databricks CLI profile that connects to your account with the command `databricks auth login`.

This command prompts for the following information:

* **Databricks Profile Name:** `account`

* **Databricks Host:** `https://accounts.cloud.databricks.com`

* **Databricks Account ID:** `<Account ID>` [Locate your account ID](https://docs.databricks.com/en/administration-guide/account-settings/index.html#locate-your-account-id)

### Commands to enable

To get the Metastore-ID first, make sure you have the ID of the workspace. Use the following command to see all the workspaces: `databricks account workspaces list`.

Then you can list what metastores are available to that workspace: `databricks account metastore-assignments get <workspace-id>`.

When you have the Metastore-ID you can enable the system-schemas for that metastore:
`databricks system-schemas enable <METASTORE-ID> compute`
`databricks system-schemas enable <METASTORE-ID> billing`

For more information about system tables, see the [Databricks documentation](https://docs.databricks.com/en/administration-guide/system-tables/index.html#enable).

## Configuring a Databricks service principal

You must have the following information to create the Databricks connection:

* **databricks host**: Url for the workspace
* **client id**: UUID for the service principal
* **client secret**: secret so CloudZero may use Databricks API as the service principal

### Create the service principal and secret

* Log into the Databricks account console and navigate to **User Management**.[https://accounts.cloud.databricks.com/users](https://accounts.cloud.databricks.com/users)
* Click **Service principals**.
* Click **Add Service principal**.
* Enter a name and click **Add**.
* Click the new Principal in the list of Service Principals
* Click **Generate Secret**. Note the **Secret** and **Client ID** for later. You can always view the Client ID, which is the UUID for the service principal.

<Callout icon="ℹ️" theme="info">
  You must be sure to generate an OAuth secret in order for the Service principal to function correctly. For more information, refer to [Databricks authorization methods](https://docs.databricks.com/aws/en/dev-tools/auth#databricks-authorization-methods).
</Callout>

### Give the service principal access to the workspace

* Log in to the Databricks account console and navigate to **Workspaces** [https://accounts.cloud.databricks.com/workspaces](https://accounts.cloud.databricks.com/workspaces).
* Find the workspace that has the billing and compute schemas enabled and click on the kebab on the far right to **Update**.
* Click **Permissions** > **Add permissions**.
* Add the Service Principal by its Client ID (UUID guid). It needs only `User` permissions in the workspace.

### Ensure the Service Principal has warehouse access

* Log int o the workspace.
* Select the warehouse provided in the connection configuration.
* Click **Permissions**. You must have `admin` access to the workspace to see this.
* Ensure the Service Principal has the `Can Use` permission. If you enabled the permission after it was previously disabled, it may take a while for the Databricks connection to read from the warehouse.

### Ensure the service principal has sql access

* Follow the [Databricks documentation to find entitlement management for the workspace](https://docs.databricks.com/en/security/auth-authz/entitlements.html#manage-entitlements-on-service-principals)
* Ensure the Service Principal has the `Databricks SQL access` entitlement enabled.
  Alternatively, you can manage the Service Principal entitlements through its group membership.

### Give the service principal access to the system tables

* Log in to the workspace.
* Open an SQL editor and issue the following commands:

```sql
GRANT USE SCHEMA ON SCHEMA system.compute TO `<service principal client id>`;
GRANT SELECT ON TABLE system.compute.clusters TO `<service principal client id>`;
GRANT USE SCHEMA ON SCHEMA system.billing TO `<service principal client id>`;
GRANT SELECT ON TABLE system.billing.list_prices TO `<service principal client id>`;
GRANT SELECT ON TABLE system.billing.account_prices TO `<service principal client id>`;
GRANT SELECT ON TABLE system.billing.usage TO `<service principal client id>`;
```

The Service Principal now has permission to query tables in the compute and billing schemas.

# Create a Databricks connection

Navigate to **Settings** > **Cloud Integrations** and select **Add Connection**.

On the **Add a New Connection** page, delect the **Databricks** tile.

Enter the connection metadata:

* **Connection Name**: A connection name that will appear in the CloudZero UI.
* **Billing Account ID**: Your Databricks parent account ID ([Locate your account ID](https://docs.databricks.com/en/administration-guide/account-settings/index.html#locate-your-account-id)).
* **Workspace URL**: The URL to access the workspace where you have [enabled the billing and compute system schemas ](/docs/connections-databricks-v2#enabling-the-billing-and-compute-schemas) that CloudZero will use to pull your cost and usage data.
* **Warehouse ID**: ID of the warehouse to use to query for billing and usage information.
* **Client ID**: ID of the Service Principal created for CloudZero to access billing and compute data.
* **Client Secret**: Secret for that Service Principal.
* **Use Fixed IP Egress**: Enable to use Databricks fixed IP egress functionality. See the [Fixed IP Egress](#fixed-ip-egress) section.

To save the connection, select the **Save** button. You will return to the **Connection Details** page in the CloudZero platform, where you should see your newly created connection.

# Databricks connection notes

## Billing period ingest windows

* **Newly Created Connection**: CloudZero will ingest the most recent 12 months of billing periods if available.
* **Re-enabled Connection**: CloudZero will attempt to ingest up to 24 months of billing periods starting from the current billing period and going back to the most recent billing period ingested.
* **Steady State**: CloudZero will ingest the current billing period and the previous billing period if it is likely to have changed.

## Tag prefix

Some information from the Databricks platform will be provided in CloudZero as tags with a prefix of `dbx_cz`. For example, cluster name is available when you use the CloudZero tag `dbx_cz:cluster_name`.

Customer-created tags will be passed through exactly as they appear in Databricks.

A list of Databricks information that can be assigned a `dbx_cz tag` follows:

* cluster_name
* cluster_id
* cluster_source
* dbr_version
* dlt_pipeline_id
* driver_instance_pool_id
* driver_node_type
* instance_pool_id
* job_id
* job_run_id
* notebook_id
* owned_by
* warehouse_id
* worker_instance_pool_id
* worker_node_type
* workspace_id

## Multiple workspaces in an account

Access to one workspace as described in this document will provide CloudZero with data for all spend associated with the Databricks account. It is not necessary to set up a connection for each workspace.

## Pricing and discounts

The Databricks cost adaptor uses default pricing for Databricks SKUs.

### Automated pricing with Account Prices (Databricks Private Preview)

CloudZero now supports automatic detection and application of customer-specific pricing and discounts through the Databricks `account_prices` system table. If you take advantage of this table, CloudZero will use it. If you need to request access, contact your Databricks account team.

To enable this feature, ensure your Service Principal has been granted the appropriate permissions to the `account_prices` table as described in section [Configuring a Databricks service principal](/docs/connections-databricks-v2#configuring-a-databricks-service-principal).

This automated approach eliminates the need for manual pricing overrides and ensures your cost data is always up-to-date with your latest pricing agreements, and helps you to:

* Detect and use your negotiated rates and discounts.
* Apply all promotions and pricing adjustments without manual intervention.
* Provide accurate cost data that reflects your actual billing.

### Manual pricing overrides

For customers without access to the `account_prices` table, CloudZero continues to support manual SKU rate overrides that can be configured upon request through the CloudZero support team.

## Fixed IP egress

Databricks allows access to be restricted to specific IP addresses at both the account and workspace level. If your organization restricts IP access at the account level, you can configure access as follows:

1. Enable **Use Fixed IP Address** for the CloudZero managed Databricks connection.
2. In your Databricks account, navigate to **Account Console** > **Settings** > **Security tab** > **IP Access List**.
3. Add a rule that allows the following IP addresses: `52.0.118.180, 52.0.33.111`

If your organization also restricts access to specific IP addresses at the workspace level, you must add the same IP addresses to the workspace IP Access List.

## Databricks region and service details

You may see a discrepancy between raw data in Databricks and CloudZero data in the Explorer.

This happens because when Databricks data is ingested into CloudZero, the `sku_name_with_region` field is split into two separate fields, one for the SKU name, displayed as Service in CloudZero, and one for the Region.

For example:

`sku_name_with_region = ENTERPRISE_SERVERLESS_SQL_COMPUTE_US_EAST_N_VIRGINIA`is split into

`Service = ENTERPRISE_SERVERLESS_SQL_COMPUTE` and `Region = US_EAST_N_VIRGINIA`.

This results in slightly different behavior when you filter and group spend in CloudZero compared to Databricks.

For example, in Databricks, entries like ⁠`ENTERPRISE_SERVERLESS_SQL_COMPUTE_US_WEST_OREGON` and ⁠`ENTERPRISE_SERVERLESS_SQL_COMPUTE_US_EAST_N_VIRGINIA` appear as separate entities. In CloudZero, grouping by Service combines costs from different regions, such as US-West and US-East into one service titled `ENTERPRISE_SERVERLESS_SQL_COMPUTE`.

To replicate a Databricks view in CloudZero, you can group by service and add a filter for region.

Note that some Databricks SKUs do not contain any region information, for example: `INTER_AVAILABILITY_ZONE_EGRESS`. In these cases, the Region in CloudZero will be set to None.
