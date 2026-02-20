---
title: Sending AnyCost Stream Data to CloudZero
category: features
createdAt: '2024-09-10'
hidden: false
slug: anycost-send-stream-data
updatedAt: ''
---
An AnyCost Stream Adaptor sends Common Bill Format (CBF) data to the CloudZero [`/v2/connections/billing/anycost/{connection_id}/billing_drops`](https://docs.cloudzero.com/reference/createoneanycoststreamconnectionbillingdrop) API by creating a billing drop where the data is uploaded. You must map the CBF data into a JSON request body.

To send AnyCost Stream data to CloudZero, complete the following steps:

1. [Find the AnyCost Stream connection ID.](#step-1-find-the-anycost-stream-connection-id)
2. [Send billing data to the AnyCost Stream connection Billing Drop API.](#step-2-send-billing-data-to-the-anycost-stream-connection-billing-drop-api)

After you have sent the data, you can [retrieve it from the API](#how-to-retrieve-data-from-an-existing-billing-drop).

# Sending AnyCost Stream data to CloudZero

## Step 1: Find the AnyCost Stream Connection ID

After you [create the AnyCost Stream Connection in the CloudZero UI](/docs/anycost-stream-getting-started#step-2-register-the-connection-in-the-ui) but before you [author the Adaptor code](/docs/anycost-custom-adaptors) to send billing data to the CloudZero API, you must find the Connection ID.

Navigate to your CloudZero organization's [Settings](https://app.cloudzero.com/organization/connections) and select your AnyCost Stream connection from the **Billing Connections** table.

On the **AnyCost Stream Integration** details page, copy the **Connection ID**. It will look something like this: `1234abcd-1234-abcd-1234-abcd1234efgh`

<Image align="center" alt="Copy the AnyCost Stream Connection ID from the details page" border={true} src="https://downloads.cloudzero.com/documentation/resources/anycost-stream-connection-id.png" className="border" />

## Step 2: Send billing data to the AnyCost Stream API

To send the billing data to the [AnyCost Stream API](/reference/anycost_stream#/), you must first create a JSON request body that includes the elements explained in the subsequent sections:

* Mapped CBF data
* Month
* Operation type (optional)

### Map the CBF to JSON request body parameters

Your Adaptor must map the [CBF data](/docs/anycost-common-bill-format-cbf) to the required JSON request body parameters.

For example, in the CBF your Adaptor generates, the `lineitem/id` column corresponds to the request body parameter `lineitem/id`.

For a full list of data file columns, see the [CBF documentation](/docs/anycost-common-bill-format-cbf#data-file-columns).

For example, suppose your CBF data includes the following heading and row:

```
lineitem/type,resource/service,resource/id,time/usage_start,cost/cost
Usage,Compute,instance-0000,2024-08-16T13:00:00Z,12
```

In this example, you would create a JSON request body with the following `data` array. The full request body is in the example payload further on in these instructions.

```json
{
  "data": [
    {
      "lineitem/type": "Usage",
      "time/usage_start": "2024-08-16T13:00:00Z",
      "resource/id": "instance-0000",
      "resource/service": "Compute",
      "cost/cost": "12"
    }
  ]
}
```

Make sure the Adaptor adds an object to the `data` array for each row in the CBF.

### Specify the month

In the JSON body, include the `month` parameter, which is an ISO 8601 formatted `datetime`. All CBF data in the request body must be from the same month.

In this example, your JSON request body would now resemble the following. The full request body is in the example payload further on in these instructions.

```json
{
  "month": "2024-08",
  "data": [
    {
      "lineitem/type": "Usage",
      "time/usage_start": "2024-08-16T13:00:00Z",
      "resource/id": "instance-0000",
      "resource/service": "Compute",
      "cost/cost": "12"
    }
  ]
}
```

### Specify whether to replace or add data

The API supports three types of `operation` that determine how records are added and replaced. This allows you to upload data for either a full month or a partial month.

* `replace_drop` (default): Replace all existing data for the specified month. This requires you to provide the data for an _entire_ month in a single request body.
* `replace_hourly`: Replace only the existing data that has overlapping hours. This allows you to provide data for a partial  month in a single request body.
* `sum`: Append data to the existing data. This allows you to provide data for a partial month in a single request body.

The default operation is `replace_drop`. If you do not specify a different operation, be aware that any existing records associated with the AnyCost Stream Adaptor in the specified `month` will be overwritten by the records in the request body.

For all operation types, if no prior data exists, CloudZero creates a new billing drop for the specified month.

### Example Payload

For this example, to upload the data for a full month and replace any existing data, the completed payload would look as follows:

```json
{
  "month": "2024-08",
  "operation": "replace_drop",
  "data": [
    {
      "lineitem/type": "Usage",
      "time/usage_start": "2024-08-16T13:00:00Z",
      "resource/id": "instance-0000",
      "resource/service": "Compute",
      "cost/cost": "12"
    }
  ]
}
```

See the [API Reference](https://docs.cloudzero.com/reference/createoneanycoststreamconnectionbillingdrop) for instructions to send the `POST` request to the AnyCost Stream Billing Drops API.

<Callout icon="ℹ️" theme="info">
  The following limits apply to the AnyCost Stream API.

  * The AnyCost Stream Billing Drops API limits the size of the uncompressed JSON body to 5MB.
  * The AnyCost Stream API does not support concurrent requests for the same stream.
  * An individual AnyCost Stream is limited to one million rows and 70MB in total size per month.
</Callout>

# How to retrieve data from an existing AnyCost Stream billing drop

You can retrieve existing billing data for a given month by sending a [`GET` request](https://docs.cloudzero.com/reference/getanycoststreamconnectionbillingdropcontents) to the AnyCost Stream Billing Drops API and passing the desired month as a path parameter, along with the connection ID.
