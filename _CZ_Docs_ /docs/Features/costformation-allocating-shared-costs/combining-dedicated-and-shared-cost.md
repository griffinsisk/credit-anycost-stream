---
title: Combining Dedicated and Shared Cost
category: features
createdAt: '2022-01-14T21:11:36.260Z'
hidden: false
slug: combining-dedicated-and-shared-cost
updatedAt: '2022-02-01T16:47:53.347Z'
---
It is common for cost of a SaaS product to include some dedicated resources, used exclusively by the product, and some shared resources, used by many products.  [Split Shared Costs Using Telemetry](doc:split-shared-costs-using-allocation-dimensions) shows how to split the cost of shared resources proportionally among different products. Building on that, we make a new Dimension that combines the shared and dedicated cost.

# Split shared cost

This is the CostFormation YAML from the previous telemetry examples. It creates two Dimensions, one to isolate the cost of a `Shared Data Lake` and a second to split that cost using telemetry into two Elements: `Email` and `Messaging`. The element names are specified by the telemetry records not shown here.

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

# Create a `Product` Dimension

The following is the YAML to create a `Product` Dimension.

```yaml
...
  Product:
    Name: Product
    DefaultValue: Other
    Rules:
      - Type: Group
        Name: Email
        Conditions:
          - Source: Tag:Product
            Equals: email
      - Type: Group
        Name: Messaging
        Conditions:
          - Source: Tag:Product
            Equals: messaging
      - Type: GroupBy
        Source: User:Defined:SplitDataLake
```

## Group Rules

First, we create a `Group` rule for each product type.  In this example we only have two: `Email` and `Messaging`.  Each rule uses `Conditions` to specify the resources used exclusively by that product.  In this simple case these resources are identified simply by an AWS tag. In a real world case this would most likely be more complex.

## GroupBy Rule

The final rule is a `GroupBy` used to add in the shared cost from the `SplitDataLake` Dimension created earlier.  Since that Dimension uses the same element names, `Email` and `Messaging`, the result combines the shared and dedicated cost. This is shown in the preceding YAML for creating a Product Dimension:

```yaml
      - Type: GroupBy
        Source: User:Defined:SplitDataLake
```

<br />

<Callout icon="ℹ️" theme="info">
  The approach is the same for creating a `Product` Dimension where the split is done with a Proportional Allocation Dimension. The main difference is that the `Source` of the `GroupBy` rule would be adjusted to reference the Proportional Allocation Dimension.
</Callout>
