---
title: 'Step 1: What Cost Should be Split?'
category: features
createdAt: '2022-01-11T23:07:44.933Z'
hidden: false
slug: what-cost-should-be-split
updatedAt: '2022-02-08T16:04:06.080Z'
---
The first step towards splitting costs is identifying and grouping the cost you want to split. Is it a shared database or service, like Snowflake compute, or another data lake like RDS? Is it an S3 bucket or EC2 instance used by multiple teams or products?

Whatever this cost is, the simplest path forward is to structure the CostFormation so that this cost exists as an element in a Dimension. For example, we have some shared costs in RDS, so we will update our CostFormation to add a new Dimension:

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

We now have an element called `Shared Data Lake` in our `Shared RDS` dimension. This will allow us to reference that cost in a Proportional Allocation Dimension.

In the next step you will extend the CostFormation.
