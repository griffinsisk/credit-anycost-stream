---
title: 'Step 2: How to Craft Telemetry Records and Send to the API'
category: features
createdAt: '2022-01-11T23:09:32.210Z'
hidden: false
slug: how-to-craft-telemetry-records
updatedAt: '2022-01-14T22:20:27.693Z'
---
Now we will prepare our telemetry records for transmission to CloudZero. We will capture the number of write operations to RDS performed by each product, `Email` and `Messaging`. We will assume a simple system has been implemented in AWS to capture this metric and aggregate it daily. After this metric has been aggregated, we will form it into JSON for the API and send it to the [Allocation Telemetry API](/reference/allocation-telemetry-api-1#/).

# Telemetry data schema

Telemetry is sent to the telemetry API as records which specify:

* `telemetry-stream`: the name of the stream.  We will use a different stream for each metric we are measuring.  This value is provided in the URL path.
* `timestamp`: the date and time associated with the record as an ISO 8601 value.
* `granularity`: the time interval specifying how records will be aggregated and displayed. Choose `HOURLY`, `DAILY`, or `MONTHLY`.
* `element_name`: the tenant associated with this usage. These values will become the elements of the Dimension we create later.
* `filter`: this identifies the part of the cloud infrastructure being used. We will use the `Shared` elements of our `Shared RDS` dimension for this.
* `value`: the amount of activity, in this case the number of write operations performed. A good metric is a primary driver of the cost of the targeted resource.

We are looking to split RDS spend into two for our Products `Email` and `Messaging`. With the CostFormation we wrote in the previous step, we know that the costs we need to split the `Shared Data Lake` element of the `Shared RDS` dimension. The JSON payload and records we need would be formatted as follows:

```json
{
  "records": [
    {
      "timestamp": "2020-01-25T00:00:00Z",
      "granularity": "DAILY",
      "filter": { 
        "custom:Shared RDS": ["Shared Data Lake"] 
      },
      "element_name": "Email",
      "value": 100045
    },
    {
      "timestamp": "2020-01-25T00:00:00Z",
      "granularity": "DAILY",
      "filter": {
        "custom:Shared RDS": ["Shared Data Lake"]
      },
      "element_name": "Messaging",
      "value": 1000600
    }
  ]
}
```

# Sending Telemetry Data to CloudZero

Follow the instructions in the [Telemetry API Documentation](/docs/cloudzero-telemetry-api-1) to authenticate against the API and transmit your data.

When the Telemetry data starts flowing and the stream's `Ingest Status` on CloudZero's [Telemetry page](https://app.cloudzero.com/telemetry) is `Available`, we will be able to reference this stream in a new `Allocation` Dimension and we can proceed to the final step.  This can take up to two hours, but typically completes in about an hour.

<Image align="center" alt="Telemetry data ingest status" className="border" border={true} width="1143" src="https://files.readme.io/e403573-telemetry.png" />

<br />
