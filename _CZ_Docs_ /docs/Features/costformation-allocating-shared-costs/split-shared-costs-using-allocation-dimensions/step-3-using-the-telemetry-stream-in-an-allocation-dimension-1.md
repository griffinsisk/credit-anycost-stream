---
title: 'Step 3: Using the Telemetry Stream in an Allocation Dimension'
category: features
createdAt: '2022-01-14T20:52:45.696Z'
hidden: false
slug: step-3-using-the-telemetry-stream-in-an-allocation-dimension-1
updatedAt: '2022-02-03T15:32:41.057Z'
---
After the Telemetry data starts flowing and the stream's `Ingest Status` on CloudZero's [Telemetry page](https://app.cloudzero.com/telemetry) is `Available`, we can reference this stream in a new `Allocation` Dimension.

Add this `Allocation` Dimension to the CostFormation:

```yaml
...
  SplitDataLake:
    Type: Allocation
    Name: Split Data Lake
    AllocateByStreams:
      Streams:
        - rds-writes-by-product
```

Notice that we use the name of the stream `rds-writes-by-product` that matches the `telemetry-stream` field in the telemetry records [(see lines 10 and 20 of the telemetry record JSON)](doc:how-to-craft-telemetry-records#telemetry-data-schema). The `id` field in the telemetry record (`Email` and `Messaging`) will now correspond to elements in the `Split Data Lake` dimension.

In this case, the cost of each of these elements on a given day is a portion of the `Shared Data Lake` element in the `Shared RDS` dimension. This portion is defined by the proportional relationship between telemetry records. For example, in the previous step, we defined two records assigning the value `100045` to `Email` and `1000600` to `Messaging`, so approximately 9% of the shared cost would be allocated to the `Email` element and 91% would be allocated to the `Messaging` element for that day, `2020-01-25T00:00:00Z`.

The next step is reviewing the work.
