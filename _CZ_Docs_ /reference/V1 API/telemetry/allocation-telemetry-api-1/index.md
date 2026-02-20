---
title: Allocation Telemetry
deprecated: false
hidden: false
metadata:
  robots: index
---
The CloudZero Allocation Telemetry API allows you to send, edit, and delete allocation data related to your system's operations. For more information about allocation data, see [Split Shared Costs Using Allocation Dimensions](/docs/split-shared-costs-using-allocation-dimensions).

For information about all of CloudZero's telemetry endpoints, including general usage limits, see [Getting Started With Telemetry](/reference/telemetry-api-1).

# CloudZero Allocation Telemetry Endpoints

**\{stream_name\}** is the user-defined name to associate with this allocation stream. When you use the `sum` and `replace` operations, if the stream does not exist, it will be created.

- [Sum telemetry records](/reference/sumallocationtelemetry): Send allocation telemetry data to a specified stream. URL: `https://api.cloudzero.com/unit-cost/v1/telemetry/allocation/{stream_name}/sum`
- [Replace telemetry records](/reference/replaceallocationtelemetry): Replace any data within the specified allocation stream that matches the supplied properties. URL: `https://api.cloudzero.com/unit-cost/v1/telemetry/allocation/{stream_name}/replace`
- [Delete telemetry records](/reference/deleteallocationtelemetry): Delete any data within the specified allocation stream that matches the supplied properties (*timestamp and granularity are minimally required*). URL: `https://api.cloudzero.com/unit-cost/v1/telemetry/allocation/{stream_name}/delete`

  Note that this is a **soft delete**, so the data will continue to exist in CloudZero's data stores, but it will be hidden. If you need a more permanent deletion, contact your FAM.

<Callout icon="ℹ️">
  The legacy [Post telemetry records](/reference/postallocationtelemetry) endpoint, `https://api.cloudzero.com/unit-cost/v1/telemetry/allocation/{stream_name}`, is deprecated. Instead, use the functionally identical [Sum telemetry records](/reference/sumallocationtelemetry) endpoint to add records to a stream.

  You can also use the [replace](/reference/replaceallocationtelemetry) or [delete](/reference/deleteallocationtelemetry) endpoints to replace or delete records.
</Callout>

# Examples
The following allocation telemetry records describe system activity by your customer, `Hooli`, where your production billing feature processed 250M records for this customer throughout the day of January 25th, 2020.

## Sum Allocation Telemetry Record

To add the following allocation telemetry record to a stream named `my-allocation-stream`, send the record to the [Sum telemetry records](/reference/sumallocationtelemetry) endpoint, `https://api.cloudzero.com/unit-cost/v1/telemetry/allocation/my-allocation-stream/sum`:

```json JSON
{
  "records": [
    {
    	"timestamp": "2020-01-25T00:00:00Z",
    	"granularity": "DAILY",
    	"filter": {
      	"custom:feature": [
        	"billing"
      	],
      	"tag:environment": [
          "prod"
        ],
        "tag:owner": [
          "frank",
          "sandy"
        ]
    	},
    	"element_name": "<HOOLI-CUSTOMER-ID>",
    	"value": "250000000"
    }
  ]
}
```

## Replace Allocation Telemetry Record

Send the following allocation telemetry record to the [Replace telemetry records](/reference/replaceallocationtelemetry) endpoint, `https://api.cloudzero.com/unit-cost/v1/telemetry/allocation/my-allocation-stream/replace`, to replace the existing record with a new value in `my-allocation-stream`:

```json JSON
{
  "records": [
    {
    	"timestamp": "2020-01-25T00:00:00Z",
    	"granularity": "DAILY",
    	"filter": {
      	"custom:feature": [
        	"billing"
      	],
      	"tag:environment": [
          "prod"
        ],
        "tag:owner": [
          "frank",
          "sandy"
        ]
    	},
    	"element_name": "<HOOLI-CUSTOMER-ID>",
    	"value": "150000000"
    }
  ]
}
```

## Delete Allocation Telemetry Record
Send the following allocation telemetry record to the [Delete telemetry records](/reference/deleteallocationtelemetry) endpoint, `https://api.cloudzero.com/unit-cost/v1/telemetry/allocation/my-allocation-stream/delete`, to delete the record in `my-allocation-stream`. Note that this is a **soft delete**:

```json JSON
{
  "records": [
    {
    	"timestamp": "2020-01-25T00:00:00Z",
    	"granularity": "DAILY",
    	"filter": {
      	"custom:feature": [
        	"billing"
      	],
      	"tag:environment": [
          "prod"
        ],
        "tag:owner": [
          "frank",
          "sandy"
        ]
    	},
    	"element_name": "<HOOLI-CUSTOMER-ID>"
    }
  ]
}
```

# Limits
* You may only associate **5** filter dimensions in a single stream. 
* All records within a given telemetry stream must filter on the same set of dimensions. 
* Filtering can specify multiple values for a dimension; a given telemetry record can specify at most 20 values for each filtered dimension.
* Filtering on multiple dimensions combine via a logical *"and"*; filtering on multiple values for a given dimension combine via a logical *"or"*
    * **For example:** `{ "account": ["1", "2"], "service": ["A"] }` will match those cost records having `service = "A"` AND either `account = "1"` OR `account = "2"`