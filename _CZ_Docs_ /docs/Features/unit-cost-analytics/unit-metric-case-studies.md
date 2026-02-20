---
title: Unit Metric Case Studies
category: features
hidden: false
slug: unit-metric-case-studies
---
# Case Study 1

Company 1 wants to understand a single unit cost.

## Scenario

Company 1 wants to analyze their cost per daily active user in their platform. There is no additional information they need other than cost data divided by the number of users in their system, broken out by day.

## Solution

Example shape of the stream data posted to their `daily-active-user` stream

```json JSON
{
  "records": [
      {
        "timestamp": "2023-11-07",
        "value": 10011
      }
   ]
}

```

When you use the new Unit Metric Telemetry API, the stream name will now be derived from the path parameter as outlined in the [API documentation](https://docs.cloudzero.com/reference/unit-metric-telemetry-api-1). For example, using this example, stream path would be `https://api.cloudzero.com/unit-cost/v1/telemetry/metric/daily-active-user`

# Case Study 2

Company 2 has a single, simple associated cost.

## Scenario

Company 2 wants to analyze their spend data per API call, broken out by Service.

## Solution

In order for the metric data to filter by Service appropriately when the Service Dimension is used in the dashboard, the metric data must include the appropriate `service` associated to each value in the data CloudZero receives.

Example shape of the stream data posted to their `https://api.cloudzero.com/unit-cost/v1/telemetry/metric/spend-by-api-call` stream:

```json JSON
{
  "records": [
    {
      "timestamp": "2023-11-06",
      "associated_cost": {
        "custom:Company Services": "aggregation"
      },
      "value": 10011
    }

    {
      "timestamp": "2023-11-07",
      "associated_cost": {
        "custom:Company Services": "streaming"
      },
      "value": 458.33
    }

    {
      "timestamp": "2023-11-06",
      "associated_cost": {
      "custom:Company Services": "allocate"
      },
      "value": 112.53
    }

    {
      "timestamp": "2023-11-07",
      "associated_cost": {
        "custom:Company Services": "budget"
      },
      "value": 225
    }
   ]
}
```

In this case, there is a single value, number of API calls per hour, each associated with different values for the `Company Services` Dimension.

# Case Study 3

Company 3 has a single associated cost and multiple streams.

## Scenario

Company 3 is a video streaming service and they want to analyze their cost per user per user type, in addition to their total plays per user per user type. This request requires two streams, one providing the number of users per day and another providing number of plays per day, both broken out by user type (logged-in vs anonymous).

## Solution

In order for the metric data to filter appropriately when the User Type Dimension is used in the dashboard, the metric data must include the appropriate `User Type` associated to each value in the data CloudZero receives.

Example shape of their `https://api.cloudzero.com/unit-cost/v1/telemetry/metric/total-streams-by-day` stream:

```json JSON
{
  "records": [
      {
        "timestamp": "2023-11-06",
        "associated_cost": {
          "custom:User Type": "logged-in"
        },
        "value": 591063.958333333
      }
   ]
}
```

Example shape of their `https://api.cloudzero.com/unit-cost/v1/telemetry/metric/total-users-by-day` stream:

```json JSON
{
  "records": [
      {
        "timestamp": "2023-11-06",
        "associated_cost": {
          "custom:User Type": "anonymous"
        },
        "value": 359491.333333333
      }
   ]
}
```

# Case Study 4

Company 4 has multiple associated costs and a single stream.

## Scenario

Company 4 wants to analyze their cost per client per region. This request requires two associated cost Dimensions, Client and Region.

## Solution

In order for the metric data to be filtered appropriately when the Client and Region Dimensions are used in the dashboard, the metric data must include the appropriate `Client` and `Region` associated to each value in the data CloudZero receives.

Example shape of their `https://api.cloudzero.com/unit-cost/v1/telemetry/metric/client-and-region` stream:

```json JSON
{
  "records": [
      {
        "timestamp": "2023-11-01",
        "associated_cost": {
          "custom:Client": "Client 123",
          "Region": "Australia"
        },
        "value": 84
      },
      {
        "timestamp": "2023-11-01",
        "associated_cost": {
          "custom:Client": "Client 456",
          "Region": "Europe"
        },
        "value": 2978
      },
      {
        "timestamp": "2023-11-01",
        "associated_cost": {
          "custom:Client": "Client 789",
          "Region": "North America"
        },
        "value": 26
      }
   ]
}
```

<Callout icon="ℹ️" theme="info">
  Note that in this example, both a Custom Dimension and a CloudZero default dimension of `Region` are used. As you can see in the preceding example, when you are using a default Dimension you should not provide the `custom:` prefix.
</Callout>

# Case Study 5

Company 5 has Dimensions defined from associated dimensions.

## Scenario

Company 5 wants to analyze their cost per API call broken out by Customer. This is a simple filtered metric situation.

Example shape of their `https://api.cloudzero.com/unit-cost/v1/telemetry/metric/my-customer-ids` stream:

```json JSON
{
  "records": [
      {
        "timestamp": "2023-12-07",
        "associated_cost": {
          "custom:CustomerID": "743e5233-82a1-42e0-a7a0-c66ac6778558"
        },
        "value": 999
      }
   ]
}
```

This works fine for the `Customer ID` Dimension, but they have a Dimension called `CustomerName` that is derived from `Customer ID` and intuitively, they expect this derived Dimension would filter the metric data with the cost data.

However, they are surprised to discover that this is not the case. Why did this not work?

## Solution

The answer is that you must explicitly define all Dimensions you expect to filter the metric data in the `associated_cost` parameter.

<Callout icon="⚠️" theme="warn">
  In addition, any Dimension you associate with a metric must be as static as possible. That is, if any value changes in the underlying data, it will break any historical records that contained the previous value.

  For example, if `CustomerID` in the preceding example is sent to CloudZero, and then the customer changes that ID, the data CloudZero already received with the old ID value will not be automatically updated to reflect the new name.

  This warning does not address additions to the data, only modifications.
</Callout>
