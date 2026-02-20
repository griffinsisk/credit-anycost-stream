---
title: 'Step 1: What Cost Should be Split?'
category: features
createdAt: '2022-02-01T16:32:32.948Z'
hidden: false
slug: step-1-what-cost-should-be-split
updatedAt: '2022-02-28T15:21:29.692Z'
---
The first step towards splitting costs is identifying and grouping the cost you want to split. Is it a shared database or service, like Snowflake compute or another data lake like RDS? Is it an S3 bucket or EC2 instance used by multiple teams or products?

Whatever this cost is, the simplest path forward is to structure the CostFormation so that this cost exists as an element in a Dimension. For example, our business has some shared costs in RDS, so we will update our CostFormation to add a new Dimension:

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
```

We now have an element called `Shared Data Lake` in our `Shared RDS` Dimension. This is perfect because we can now reference that in a Rules Allocation dimension. The next step is extending the CostFormation.
