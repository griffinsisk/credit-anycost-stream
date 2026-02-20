---
title: 'Step 2: Writing a Rules Allocation Dimension'
category: features
createdAt: '2022-02-01T16:49:47.637Z'
hidden: false
slug: step-2-writing-a-proportional-allocation-dimension
updatedAt: '2022-02-28T15:04:44.002Z'
---
When we have the RDS costs we want to split grouped as an element within a dimension, we are ready to build our Rules Allocation Dimension.

Stub out the Dimension to see what information we need to add:

```yaml
...
  SplitDataLake:
    Type: Allocation
    Name: Split Data Lake
    AllocateByRules:
      AllocationMethod: Proportional
      SpendToAllocate:
        ...
      AcrossElements:
        ...
```

Within the `AllocateByRules` rule, we can see the main pieces of information we must add.

* `AllocationMethod`: Here we have chosen `Proportional`, since we want the costs in this Dimension to follow the relative costs of our products. We could also have chosen `Even`, and have the cost of our RDS database spread evenly among this Dimension's elements.
* `SpendToAllocate`: This specifies what spend we want to split. In this case, it will reference the RDS spend we grouped in the previous step.
* `AcrossElements`: This specifies how we will split the cost. The elements referenced here will be the elements of our Rules Allocation Dimension as well, and their relative costs will define the proportionality of our split.

<Callout icon="ℹ️" theme="info">
  There is an additional optional element `ForEachElementOf` that allows for further segmentation of `SpendToAllocate`. For more information, see [Optionally Partition Rules Based Allocation Using ForEachElementOf](doc:optionally-implement-foreachelementof).
</Callout>

The goal in this exercise is to allocate the shared RDS spend to the Product A, Product B, and Product C, each a SingleTenantProduct, relative to the amount we are currently spending on each of those products. For this purpose we have a Shared Database and a SplitDataLake.

<Image align="center" alt="Diagram illustrating split cost for three products" className="border" border="#d8d6e3" width="665" src="https://files.readme.io/0b09e62-Screen_Shot_2022-02-03_at_10.50.35_AM.png" />

<Callout icon="ℹ️" theme="info">
  If we had chosen an `AllocationMethod` of `Even`, then $3,333 would be assigned to each SingleTenantProject, Product A, Product B, and Product C.
</Callout>

First, we will use `SpendToAllocate` to specify the `Shared Data Lake` element in the `Shared RDS` dimension.

```yaml
...
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
        ...
```

Next, we will use `AcrossElements` to define the output elements for our split. In this case, we want to split relative to the elements Product A, Product B, and Product C in the dimension `SingleTenantProduct`.

```yaml
...
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
```

Notice that under `AcrossElements` we have used the `GroupBy` shorthand to clearly express the logic. It is also possible to use the `Groups` shorthand or the standard `Rules` long form syntax.

The next step is to review the work so far.
