---
title: Reviewing Our Work
category: features
createdAt: '2022-01-12T17:30:59.580Z'
hidden: false
slug: reviewing-our-work
updatedAt: '2022-02-03T16:13:00.744Z'
---
In summary, we have CostFormation with Dimensions that looks like this:

```yaml
Dimensions:
  SharedRDS:
    Name: Shared RDS
    DefaultValue: Not Shared
    Rules:
      - Type: Group
        Name: Shared Data Lake
        Conditions:
          - Source: Service
            Equals: AmazonRDS
  SplitDataLake:
    Type: Allocation
    Name: Split Data Lake
    AllocateByStreams:
      Streams:
        - rds-writes-by-product
```

We are also sending daily Telemetry data with Telemetry Records shaped like this:

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
      "telemetry-stream": "rds-writes-by-product",
      "value": "100045"
    },
    {
      "timestamp": "2020-01-25T00:00:00Z",
      "granularity": "DAILY",
      "filter": {
        "custom:Shared RDS": ["Shared Data Lake"]
      },
      "element_name": "Messaging",
      "telemetry-stream": "rds-writes-by-product",
      "value": "1000600"
    }
  ]
}
```

At this point, we will be able to use the new `SplitDataLake` dimension in the Explorer and reference it in other Dimensions. We have successfully split a shared cost using telemetry.
