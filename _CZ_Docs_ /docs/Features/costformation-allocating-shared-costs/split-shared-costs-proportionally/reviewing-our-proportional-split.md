---
title: Reviewing Our Rules-Based Proportional Split
category: features
createdAt: '2022-02-03T15:09:47.507Z'
hidden: false
slug: reviewing-our-proportional-split
updatedAt: '2022-02-28T15:23:16.931Z'
---
In summary, we have added two Dimensions to our CostFormation that look like this:

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
```

At this point, we will be able to use the new `SplitDataLake` dimension in the Explorer and reference it in other dimensions. We have successfully split a shared cost using a Rules Allocation dimension.
