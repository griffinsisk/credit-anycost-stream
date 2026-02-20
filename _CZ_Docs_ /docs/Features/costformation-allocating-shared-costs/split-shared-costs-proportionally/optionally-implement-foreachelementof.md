---
title: Optionally Partition Rules Allocation Using ForEachElementOf
category: features
createdAt: ''
hidden: false
slug: optionally-implement-foreachelementof
updatedAt: ''
---
Now that we have successfully written a Rules Allocation Dimension, we have the option to add another element to allow for a more nuanced allocation of cost.

# Problem to solve

The CostFormation Language in the example up to now is sufficient for the majority of use cases. Previously, we allocated spend for a shared database relative to the cost of three products using the database. There may be instances where we want to allocate spend in a more nuanced way.

For example, suppose the shared database in the previous example is also shared across Development and Production environments. Each of our three products have some costs associated with Development, and some costs associated with Production. Rather than allocating the shared database costs by the overall proportions of SingleTenantProduct cost, we want to proportionally allocate spend to SingleTenantProduct by Environment as well.

Previously we were allocating the cost of the RDS Database to each product relative to that product's cost.

<Callout icon="ℹ️" theme="info">
  For the purposes of this exercise, we will assume we have already created a Dimension called `SingleTenantProduct` that describes the spend of Product A, Product B, and Product C.
</Callout>

Our goal now is to allocate the cost of the RDS Database to each product relative to that product's cost by environment, Development and Production. There is a shared database and a SplitDataLake for each environment.

![rules\_based\_allocation\_with\_foreachelementof.png](https://downloads.cloudzero.com/documentation/resources/rules_based_allocation_with_foreachelementof.png)

This allocation shifts $50 of spend shifted between Product B and Product C due to the higher relative ratio of Product C to Product B spend in Development.

# Writing the Cost Formation Language

<Callout icon="ℹ️" theme="info">
  For the purpose of this exercise, we will assume we have already created a Dimension called `Environment` that describes the spend of the Development and Production Environments.
</Callout>

We can add `ForEachElementOf` to the existing Dimension to achieve the desired result as illustrated in the problem statement.

```yaml
...
  SplitDataLake:
    ...
    ForEachElementOf:
      GroupBy:
        Source: User:Defined:Environment
```

Now the overall Dimension looks like this:

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
    AllocateByRules:
      AllocationMethod: Proportional
      SpendToAllocate:
        Source: User:Defined:SharedRDS
        Conditions:
          - Equals: Shared Data Lake
      AcrossElements:
        GroupBy:
          Source: User:Defined:SingleTenantProduct
          Conditions:
            - Equals:
              - Product A
              - Product B
              - Product C
      ForEachElementOf:
        GroupBy:
          Source: User:Defined:Environment
```

Note that under `ForEachElementOf` we have used the `GroupBy` shorthand to clearly express the logic. It is also possible to use the `Groups` shorthand or the standard `Rules` long form syntax.
