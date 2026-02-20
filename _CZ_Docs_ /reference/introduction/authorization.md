---
title: Authorization
deprecated: false
hidden: false
metadata:
  robots: index
---
CloudZero uses key-based authorization to secure API access. To authenticate your requests, include your API key in the `Authorization` header:

```shell
curl -X GET https://api.cloudzero.com/v2/insights \
  -H "Authorization: AbCd1234EfGh5678AbCd1234EfGh5678AbCd12"
```

<Callout icon="ℹ️" theme="info">
  Note that this is not a bearer token, so there is no `Bearer` in the Authorization header.
</Callout>

# Managing API keys

An organization can have multiple API keys. To view and manage all API keys for your organization, navigate to [**Settings** > **API Keys**](https://app.cloudzero.com/organization/api-keys).

<Image align="center" alt="API Keys page in CloudZero Settings" border={true} src="https://downloads.cloudzero.com/documentation/resources/api-keys-list-2.png" className="border" />

Only users with the necessary permissions can manage keys. Users can assign each key zero or more API scopes, which grant access to endpoints in the [CloudZero API](https://docs.cloudzero.com/reference/introduction).

The [API Keys](https://app.cloudzero.com/organization/api-keys) page displays a list of keys with the following information:

* **Name**
* **Description**
* **Created By:** Email of the user who created it
* **Last Modified:** Last update timestamp (UTC)
* **Last Accessed:** Last usage timestamp (UTC)
* **Assigned Scopes:** Number of granted API scopes
* **Status:** `Enabled` or `Disabled`

If your organization had an API key before multiple keys were supported, it is listed as **Legacy API Key**.

<Callout icon="ℹ️" theme="info">
  CloudZero does not automatically grant access to new API endpoints. When new endpoints are released, you must [edit](https://docs.cloudzero.com/reference/authorization#edit-an-api-key) each API key to manually add the necessary scopes.
</Callout>

## Create a new API key

To create an API key:

1. Navigate to [**Settings** > **API Keys**](https://app.cloudzero.com/organization/api-keys).

2. Select **Create New API Key**.

   <Image align="center" alt="Create New API Key button" border={false} src="https://downloads.cloudzero.com/documentation/resources/create-new-api-key-button-2.png" />

3. Enter a name for the key.

4. Enter a description.

5. Select the appropriate **API Key Scopes** to assign specific permissions to the key. You must select at least one. For information about the scopes required for each endpoint, refer to the section [API key scopes](https://docs.cloudzero.com/reference/authorization#api-key-scopes).

   <Image align="center" alt="Create an API Key" border={false} width="400px" src="https://downloads.cloudzero.com/documentation/resources/create-new-api-key.png" />

6. Select **Create API Key**.

7. Copy the API key displayed. It will not be shown again.

   <Image align="center" alt="Copy the API key" border={true} width="400px" src="https://downloads.cloudzero.com/documentation/resources/copy-api-key-1.png" className="border" />

8. Select **Close**.

New keys are `Enabled` by default.

## Edit an API key

To edit an API key's **name** and/or **scopes**:

1. On the [API Keys](https://app.cloudzero.com/organization/api-keys) page, locate the key you plan to modify.

2. Select the three-dot icon in the **Actions** column.

   <Image alt="Select the three-dot icon in the Actions column" border={false} src="https://downloads.cloudzero.com/documentation/resources/api-key-actions-2.png" />

3. Select **Edit**.

4. Modify the **API Key Name** if needed.

5. Modify the **Description** if needed.

6. Select the appropriate **API Key Scopes** to assign specific permissions to the key. For information about the scopes required for each endpoint, refer to the section [API key scopes](https://docs.cloudzero.com/reference/authorization#api-key-scopes).

   <Image align="center" alt="Select the appropriate API key scopes" border={true} width="400px" src="https://downloads.cloudzero.com/documentation/resources/update-api-key-some-scopes-selected-1.png" className="border" />

7. Select **Update API Key**.

CloudZero displays the updated list of API keys.

## Enable or disable an API key

To disable or enable an API key:

1. On the [API Keys](https://app.cloudzero.com/organization/api-keys) page, locate the key you plan to modify.

2. Select the three-dot icon in the **Actions** column.

   <Image align="center" alt="Select the three-dot icon in the Actions column on the API Keys page" border={true} src="https://downloads.cloudzero.com/documentation/resources/api-key-actions-2.png" className="border" />

3. Select **Enable** or **Disable**.

The **Status** column is updated to display `Enabled` or `Disabled` for the key you modified.

## Delete an API key

<Callout icon="⚠️" theme="warn">
  Deleting an API key will immediately revoke access for any services using it.
</Callout>

To delete an API key:

1. On the [API Keys](https://app.cloudzero.com/organization/api-keys) page, locate the key you plan to delete.

2. Select the three-dot icon in the **Actions** column.

   <Image alt="Select the three-dot icon in the Actions column" border={false} src="https://downloads.cloudzero.com/documentation/resources/api-key-actions-2.png" />

3. Select **Delete**.

4. Type the name of the API key to confirm deletion.

   <Image align="center" alt="Type the name of the API key to confirm deletion" border={true} width="600px" src="https://downloads.cloudzero.com/documentation/resources/delete-api-key-1.png" className="border" />

5. Select **Delete API Key**.

CloudZero displays the message **API Key deleted successfully** and removes the key from the list of keys.

## API key scopes

CloudZero supports the following API scopes, which correspond to specific API endpoints:

* `billing:read_costs`: [Get billing costs](https://docs.cloudzero.com/reference/getbillingcosts)
* `billing:read_dimensions`: [Get billing dimensions](https://docs.cloudzero.com/reference/getbillingdimensions)
* `budgets:create_budget`: [Create budget](https://docs.cloudzero.com/reference/createbudget)
* `budgets:delete_budget`: [Delete budget](https://docs.cloudzero.com/reference/deleteonebudget)
* `budgets:read_budget`: [Get one budget](https://docs.cloudzero.com/reference/getonebudget)
* `budgets:read_budgets`: [Get a list of budgets](https://docs.cloudzero.com/reference/getbudgets)
* `budgets:update_budget`: [Update a budget](https://docs.cloudzero.com/reference/updateonebudget)
* `connections:create_billing`: [Create a billing connection](https://docs.cloudzero.com/reference/createbillingconnection)
* `connections:create_billing_anycost_billing_drop`: [Create an AnyCost Stream connection billing drop](https://docs.cloudzero.com/reference/createoneanycoststreamconnectionbillingdrop)
* `connections:create_billing_anycost_validate_billing_drop`: [Validate an AnyCost Stream connection billing drop](https://docs.cloudzero.com/reference/validateoneanycoststreamconnectionbillingdrop)
* `connections:delete_billing`: [Delete a billing connection](https://docs.cloudzero.com/reference/deleteonebillingconnection)
* `connections:read_billing`: [Get one billing connection](https://docs.cloudzero.com/reference/getonebillingconnection)
* `connections:read_billing_anycost_billing_drops`: [Get a list of billing drops for an AnyCost Stream connection](https://docs.cloudzero.com/reference/getanycoststreamconnectionbillingdrops)
* `connections:read_billing_anycost_billing_drops_month`: [Get contents of one billing drop for an AnyCost Stream connection](https://docs.cloudzero.com/reference/getanycoststreamconnectionbillingdropcontents)
* `connections:read_billings`: [Get a list of billing connections](https://docs.cloudzero.com/reference/getbillingconnections)
* `connections:update_billing`: [Update a billing connection](https://docs.cloudzero.com/reference/updateonebillingconnection)
* `container-metrics_v1:abandon`: Required scope for the [CloudZero Agent for Kubernetes](/docs/installation-of-cloudzero-agent-for-kubernetes)
* `container-metrics_v1:get-status`: Required scope for the [CloudZero Agent for Kubernetes](/docs/installation-of-cloudzero-agent-for-kubernetes)
* `container-metrics_v1:legacy`: Required scope for the [CloudZero Agent for Kubernetes](/docs/installation-of-cloudzero-agent-for-kubernetes)
* `container-metrics_v1:upload`: Required scope for the [CloudZero Agent for Kubernetes](/docs/installation-of-cloudzero-agent-for-kubernetes)
* `costformation:create_definition_version`: [Create a CostFormation definition version](https://docs.cloudzero.com/reference/createcostformationdefinitionversion)
* `costformation:read_definition_version`: [Get one CostFormation definition version](https://docs.cloudzero.com/reference/getonecostformationdefinitionversion)
* `costformation:read_definition_versions`: [Get a list of CostFormation definition versions](https://docs.cloudzero.com/reference/getcostformationdefinitionversions)
* `events_v1:create_event`: [Post an event](https://docs.cloudzero.com/reference/postevent)
* `insights:create_insight`: [Create an insight](https://docs.cloudzero.com/reference/createinsight)
* `insights:create_insight_comment`: [Create a comment for an insight](https://docs.cloudzero.com/reference/createcommentforoneinsight)
* `insights:delete_insight`: [Delete an insight](https://docs.cloudzero.com/reference/deleteoneinsight)
* `insights:read_insight`: [Get one insight](https://docs.cloudzero.com/reference/getoneinsight)
* `insights:read_insight_comments`: [Get a list of comments for an insight](https://docs.cloudzero.com/reference/getcommentsforoneinsight)
* `insights:read_insights`: [Get a list of insights](https://docs.cloudzero.com/reference/getinsights)
* `insights:update_insight`: [Update an insight](https://docs.cloudzero.com/reference/updateoneinsight)
* `insights:update_insight_comment`: [Update a comment for an insight](https://docs.cloudzero.com/reference/updateonecommentforoneinsight)
* `unit-cost_v1:manage_telemetry_records`:
  * **Allocation telemetry streams:**
    * [Post allocation telemetry records](https://docs.cloudzero.com/reference/postallocationtelemetry) and create stream if it does not exist
    * [Sum allocation telemetry records](https://docs.cloudzero.com/reference/sumallocationtelemetry) and create stream if it does not exist
    * [Replace allocation telemetry records](https://docs.cloudzero.com/reference/replaceallocationtelemetry) and create stream if it does not exist
    * [Delete allocation telemetryrecords](https://docs.cloudzero.com/reference/deleteallocationtelemetry)
  * **Unit cost metric telemetry streams:**
    * [Post unit cost metrics records](https://docs.cloudzero.com/reference/postmetrictelemetry) and create stream if it does not exist
    * [Sum unit cost metrics records](https://docs.cloudzero.com/reference/summetrictelemetry) and create stream if it does not exist
    * [Replace unit cost metrics records](https://docs.cloudzero.com/reference/replacemetrictelemetry) and create stream if it does not exist
    * [Delete unit cost metrics records](https://docs.cloudzero.com/reference/deletemetrictelemetry)
* `unit-cost_v1:delete_telemetry_stream`: [Delete a telemetry stream](https://docs.cloudzero.com/reference/delete_unit-cost-v1-telemetry-telemetry-stream-name)
* `unit-cost_v1:read_telemetry`:
  * [Get recently processed records for an allocation or unit cost metric stream](https://docs.cloudzero.com/reference/get_unit-cost-v1-telemetry-telemetry-stream-name-records) (Get telemetry stream records)
  * [Get recently submitted records for an allocation or unit cost metric stream](https://docs.cloudzero.com/reference/getmetrictelemetry) (Get metrics records)
* `views:read_view`: [Get one view](https://docs.cloudzero.com/reference/getoneview)
* `views:read_views`: [Get a list of views](https://docs.cloudzero.com/reference/getviews)
