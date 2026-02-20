---
title: Allocation Short Form Rules
deprecated: false
hidden: false
metadata:
  robots: index
---
The Dimensions `AllocateByStreams` and `AllocateByRules` can be defined only by using the short form.

# `AllocateByStreams` short form rule

The `AllocateByStreams` Dimension allows splitting costs using telemetry. This Dimension can be defined only by using the short form. The syntax is as follows:

```yaml
  <DimensionId>:
    <Base Dimension Properties>
    Type: Allocation
    AllocateByStreams:
      Streams:
        - <Stream>
```

# `AllocateByRules` short form rule

The `AllocateByRules`Dimension allows splitting costs among the elements of another Dimension, either [evenly](#allocationmethod-even) or [proportionally](#allocationmethod-proportional). The `AllocateByRules`Dimension can be defined only by using the short form.

`AllocateByRules` supports four keys:

* `AllocationMethod`: How to split the costs, by the [Even](#allocationmethod-even) or [Proportional](#allocationmethod-proportional) allocation method
* `SpendToAllocate`: [What costs to split](#spendtoallocate)
* `AcrossElements`: What elements the cost will be split across, and the proportions for each element's cost, if you are using proportional allocation
* Optional: `ForEachElementOf`: How to [refine a proportional allocation](#using-foreachelementof-in-proportional-allocation) by splitting the costs proportionally across another dimension

The `AllocateByRules` syntax is as follows:

```yaml
  <DimensionId>:
    <Base Dimension Properties>
    Type: Allocation
    AllocateByRules:
      AllocationMethod: <...>
      SpendToAllocate: <...>
      AcrossElements: <...>
      ForEachElementOf: <...> # Optional; can only be used with proportional allocation
```

## `SpendToAllocate`

The `SpendToAllocate` attribute defines what spend you want to split.

Supported `SpendToAllocate` keys:

* `Source`
* `Sources`
* `CoalesceSources`
* `Conditions`

For example, the following code defines an Allocation Dimension with the ID `RDSSplitCosts` that splits the cost of AWS RDS spend in the account `123456789012`:

```yaml
  RDSSplitCosts:
    Name: RDS Split Costs
    Hide: True
    Type: Allocation
    AllocateByRules:
      AllocationMethod: <...>

      SpendToAllocate:
        Conditions:
          - And:
            - Source: Account
              Equals: 123456789012
            - Source: Service
              Equals: AWS RDS
```

## `AcrossElements`

`AcrossElements` defines the elements in the Custom Allocation Dimension. If you use the `Proportional` method, `AcrossElements` also defines the proportions for how the cost will be split.

Supported `AcrossElements` keys:

* `Source`
* `Sources`
* `Transforms`

For example, the following code defines an allocation dimension where the RDS spend is split across 3 elements in the `SingleTenantProduct` dimension, which are `Product A`, `Product B`, and `Product C`:

```yaml
  RDSSplitCosts:
    Name: RDS Split Costs
    Hide: True
    Type: Allocation
    AllocateByRules:
      AllocationMethod: <...>
      SpendToAllocate:
        Conditions:
          - And:
            - Source: Account
              Equals: 123456789012
            - Source: Service
              Equals: AWS RDS

      AcrossElements:
        Rules:
          - Type: GroupBy
            Source: SingleTenantProduct
            Conditions:
              - Equals:
                - Product A
                - Product B
                - Product C
```

## `AllocationMethod`: Even

If `AllocationMethod` is `Even`, the cost of each element in the Rules Allocation Dimension is the same. You can calculate it as:

* the cost defined in `SpendToAllocate`,
* divided by the number of distinct elements in `AcrossElements`.

Note that the `Even` allocation method uses the [Real Cost](/docs/explorer#real-cost) of the targets.

For example, the following code defines an Allocation Simension where the RDS spend is split evenly across three  elements in the `SingleTenantProduct` dimension, which are `Product A`, `Product B`, and `Product C`:

```yaml
  RDSSplitCosts:
    Name: RDS Split Costs
    Hide: True
    Type: Allocation
    AllocateByRules:
      AllocationMethod: Even
      SpendToAllocate:
        Conditions:
          - And:
            - Source: Account
              Equals: 123456789012
            - Source: Service
              Equals: AWS RDS

      AcrossElements:
        Rules:
          - Type: GroupBy
            Source: SingleTenantProduct
            Conditions:
              - Equals:
                - Product A
                - Product B
                - Product C
```

## `AllocationMethod`: Proportional

If `AllocationMethod` is `Proportional`, the cost of each element in the Rules Allocation Dimension is defined relative to cost of the other elements in the Dimension. You can calculate each element's cost as:

* the cost defined in `SpendToAllocate`,
* multiplied by the ratio of that element's cost versus. the sum of all elements in the inline dimension.

For example, if the Dimension `SingleTenantProduct` has three elements, `Product A`, `Product B`, and `Product C`, suppose that the total cost of all the elements in the `SingleTenantProduct` Dimension is $1200, split using the following ratios:

* **Product A:** 25% of $1200 = $300
* **Product B:** 25% of $1200 = $300
* **Product C:** 50% of $1200 = $600

As a result, if the `SpendToAllocate` is $100, each element would be allocated as follows:

* **Product A:** 25% of $100 = $25
* **Product B:** 25% of $100 = $25
* **Product C:** 50% of $100 = $50

The following code defines an Allocation Dimension where the RDS spend is split proportionally  across the three  elements in the `SingleTenantProduct` Dimension:

```yaml
  RDSSplitCosts:
    Name: RDS Split Costs
    Hide: True
    Type: Allocation
    AllocateByRules:
      AllocationMethod: Proportional
      SpendToAllocate:
        Conditions:
          - And:
            - Source: Account
              Equals: 123456789012
            - Source: Service
              Equals: AWS RDS

      AcrossElements:
        Rules:
          - Type: GroupBy
            Source: SingleTenantProduct
            Conditions:
              - Equals:
                - Product A
                - Product B
                - Product C
```

### Proportional allocation cost type and granularity

When you use the `Proportional` method of allocation, you can specify the cost type and level of granularity.

The default cost type is [`RealCost`](/docs/explorer#real-cost) and the default level of granularity is `UsageDaily`, but you can choose to use other supported values.

The supported cost types are:

* [`BilledCost`](/docs/explorer#billed-cost)
* [`DiscountedCost`](/docs/explorer#discounted-cost)
* [`DiscountedAmortizedCost`](/docs/explorer#discounted-amortized-cost)
* [`AmortizedCost`](/docs/explorer#amortized-cost)
* [`InvoicedAmortizedCost`](/docs/explorer#invoiced-amortized-cost)
* [`RealCost`](/docs/explorer#real-cost) (default)
* [`OnDemandCost`](/docs/explorer#on-demand-cost)
* `UsageAmount`: A cost type available in [Analytics](/docs/viewing-usage-data#accessing-usage-data-in-cloudzero)

The supported granularity values are:

* `UsageDaily` (default)
* `UsageMonthly`
* `BillingPeriod`

To specify a non-default cost type or level of granularity, format the CostFormation as follows:

```yaml
  RDSSplitCosts:
    Name: RDS Split Costs
    Hide: True
    Type: Allocation
    AllocateByRules:
      AllocationMethod:
        Method: Proportional
        Granularity: <Level of granularity>
        CostType: <Cost type>
```

Note that this syntax adds a new key, `Method`.

For example, the following code defines an Allocation Dimension where the RDS spend is split proportionally across Dimension elements, using ratios calculated based on monthly usage and [Discounted Cost](/docs/explorer#discounted-cost):

```yaml
  RDSSplitCosts:
    Name: RDS Split Costs
    Hide: True
    Type: Allocation
    AllocateByRules:
      AllocationMethod:
        Method: Proportional
        Granularity: UsageMonthly
        CostType: DiscountedCost
```

### Using `ForEachElementOf` in proportional allocation

`ForEachElementOf` is an optional attribute that further categorizes `SpendToAllocate` based on another Dimension. This is useful when you need to make a proportional allocation more nuanced, without having to create redundant filters or dimensions.

The supported `ForEachElementOf` keys are:

* `Source`
* `Sources`
* `Transforms`

For example, the following code defines an Allocation Dimension where the RDS spend is split proportionally across three elements in the `SingleTenantProduct` dimension, each of which is further divided proportionally across the types of `Environment` (either `dev` or `prod`):

```yaml
  RDSSplitCosts:
    Name: RDS Split Costs
    Hide: True
    Type: Allocation
    AllocateByRules:
      AllocationMethod: Proportional
      SpendToAllocate:
        Conditions:
          - And:
            - Source: Account
              Equals: 061190967865
            - Source: Service
              Equals: AWS RDS
      AcrossElements:
        GroupBy:
          Source: SingleTenantProduct
          Conditions:
            - Equals:
                - Product A
                - Product B
                - Product C

      ForEachElementOf:
        Source: Environment
        Values:
          - dev
          - prod
```

As a result of the preceding code, your RDS spend is allocated by product, and then by environment.
