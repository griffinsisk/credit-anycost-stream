---
title: Unit Cost Metric Telemetry
deprecated: false
hidden: false
metadata:
  robots: index
---
The CloudZero Unit Cost Metric Telemetry APIs allow you to send, edit, and delete unit cost metric data related to your system's operations. For more information about unit cost metric data, see [Unit Cost Analytics](/docs/unit-cost-analytics). For examples and case studies, see [Unit Metric Case Studies](/docs/unit-metric-case-studies).

For information about all of CloudZero's telemetry endpoints, including general usage limits, see [Getting Started With Telemetry](/reference/telemetry-api-1).

# CloudZero Unit Cost Metric Telemetry Endpoints

**\{metric_name\}** is the user-defined name to associate with this unit cost metric stream. When you use the `sum` and `replace` operations, if the stream does not exist, it will be created.

- [Sum metrics records](/reference/summetrictelemetry): Send unit cost metric telemetry data to a specified stream. URL: `https://api.cloudzero.com/unit-cost/v1/telemetry/metric/{metric_name}/sum`
- [Replace metrics records](/reference/replacemetrictelemetry): Replace any data within the specified unit cost metric stream that matches the supplied properties. URL: `https://api.cloudzero.com/unit-cost/v1/telemetry/metric/{metric_name}/replace`
- [Delete metrics records](/reference/deletemetrictelemetry): Delete any data within the specified unit cost metric stream that matches the supplied properties (*timestamp is minimally required*). URL: `https://api.cloudzero.com/unit-cost/v1/telemetry/metric/{metric_name}/delete`

  Note that this is a **soft delete**, so the data will continue to exist in CloudZero's data stores, but it will be hidden. If you need a more permanent deletion, contact your FAM.

<Callout icon="ℹ️">
  The legacy [Post metrics records](/reference/postmetrictelemetry) endpoint, `https://api.cloudzero.com/unit-cost/v1/telemetry/metric/{metric_name}`, is deprecated. Instead, use the functionally identical [Sum metrics records](/reference/summetrictelemetry) endpoint to add records to a stream.

  You can also use the [replace](/reference/replacemetrictelemetry) or [delete](/reference/deletemetrictelemetry) endpoints to replace or delete records.
</Callout>

# Examples
The following unit cost metric records specify some system activity -- a count of audio streams on December 7, 2023, when 12,325 people listened to a particular sea star attempt to play mayonnaise as an instrument.

## Sum Unit Cost Metric Record

To add the following unit cost metric telemetry record to a stream named `my-metric-stream`, send the record to the [Sum unit cost metric records](/reference/summetrictelemetry) endpoint, `https://api.cloudzero.com/unit-cost/v1/telemetry/metric/my-metric-stream/sum`:

```json JSON
{
  "records": [
    {
      "timestamp": "2023-12-07T00:00:00",
      "value": "12345",
      "associated_cost": 
        {
          "custom:Client": "Patric Star",
          "custom:Product": "Mayonaise",
          "custom:Product Group": "Instruments"
        }
      }
   ]
}
```

## Replace Unit Cost Metric Record

Send the following unit cost metric record to the [Replace unit cost metric records](/reference/replacemetrictelemetry) endpoint, `https://api.cloudzero.com/unit-cost/v1/telemetry/metric/my-metric-stream/replace`, to replace the existing record with a new value in `my-metric-stream`:

```json JSON
{
  "records": [
    {
      "timestamp": "2023-12-07T00:00:00",
      "value": "67890",
      "associated_cost": 
        {
          "custom:Client": "Patric Star",
          "custom:Product": "Mayonaise",
          "custom:Product Group": "Instruments"
        }
      }
   ]
}
```

## Delete Unit Cost Metric Record
Send the following unit cost metric record to the [Delete unit cost metric records](/reference/deletemetrictelemetry) endpoint, `https://api.cloudzero.com/unit-cost/v1/telemetry/metric/my-metric-stream/delete`, to delete the record in `my-metric-stream`. Note that this is a **soft delete**:

```json JSON
{
  "records": [
    {
      "timestamp": "2023-12-07T00:00:00",
      "associated_cost": 
        {
          "custom:Client": "Patric Star",
          "custom:Product": "Mayonaise",
          "custom:Product Group": "Instruments"
        }
      }
   ]
}
```

# Fields

* `timestamp`: ISO formatted date and time. Time can be included in this data, but will be ignored. Granularity of unit cost metrics is daily by default. Time will be converted to UTC.

* `value` : the metric to associate. This is a number. Decimals are allowed but are not required and do not include commas. **Note:** This field is not allowed on the **delete** operation.

    > CloudZero supports 15 significant digits for the value, so the value is rounded to the 15th significant digit.

* `associated_cost` : (optional) a dictionary of CloudZero dimensions which further categorize the cost data such that the resulting unit metric can be filtered.

    * The keys and values in the associated_cost list must appear in this format: `<Dimension Name>`: `<Dimension Value>`

      * The `<Dimension Name>` is the human readable display name of your dimension. If the dimension you are referencing is custom (that is, not a dimension native to CloudZero), then it must include the custom: prefix.

          > For example, if you made a custom dimension called **My Awesome Dimension**, then your `<Dimension Name>` would be `custom:My Awesome Dimension`.
          >
          > If the dimension you wanted to filter by is the CloudZero Region dimension, then your `<Dimension Name>` would simply be `Region`.

      * The `<Dimension Value>` must be a single value for the dimension. The value must be a string and it may not be a list.

# Limits
* Granularity is **daily** by default. You may send data in at a higher granularity, but the data will be aggregated together to the day.

* You may only associate **5** `associated_cost` dimensions with a Unit Metric.
    
    * All records within a stream must have the same set of dimensions defined in their associated cost parameter.