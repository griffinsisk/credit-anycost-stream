---
title: CostFormation Definition Language
category: features
createdAt: '2021-08-24T18:55:18.404Z'
hidden: false
slug: cost-formation-definition-language
updatedAt: '2021-11-18T23:31:41.432Z'
---
CloudZero CostFormation enables you to use features of the CloudZero platform to view your cloud costs in the context of your business and engineering needs. With CostFormation, you can define Custom [Dimensions](/docs/dimensions), which consist of rules and conditions that are used to assign your cloud charges to different Elements based on billing line item data as well as other sources, like resource tags.

CostFormation uses a YAML-based language with syntax that is used to define your Custom Dimensions. The definitions of Custom Dimensions are written in a CostFormation Definitions file which can be uploaded into CloudZero. Custom Dimension definitions are published in CloudZero, enabling the Custom Dimensions to be used in CloudZero features such as the Explorer or Views, in the same way as the Core Dimensions.

# Example of a Custom Dimension

You may want to view your costs in the context of operating environments where your environments are Production, DevOps, and Development. Costs can usually be broken down into these environments by account, with several accounts being associated with each environment, but there are some cases where the account number cannot be used.

To see your costs in each operating environment, you can define a Custom Dimension named `Environment` that contains three rules, one for each of your operating environments. The rules would define each `Element _name` (here,`Production`, `DevOps`, and `Development`) and then define the conditions under which a charge should be attributed to a given element.

If `Production` resources are always deployed into accounts A, B, and C, then the conditions of the `Production` rule would specify that if `Account` equals `A`, `B`, or `C`, then those charges should be assigned to the `Production` element.

```yaml
  Environment:
    Name: Environment
    Source: Account
    Rules:
      - Type: Group
        Name: Production
        Conditions:
          - Equals:
              - 123456789010
              - 123456789011
              - 123456789012
        - And:
          - Equals: snowflake1234
          - Source: ProductFamily
            Equals: warehouse
          - Source: Resource
            Contains: prod
        - And:
          - Equals: snowflake1234
          - Source: ProductFamily
            Equals: database
          - Source: Resource
            Equals: live_billing
      - Type: Group
        Name: DevOps
        Conditions:
          - Source: CZ:Defined:Category
            Equals: Cloud Management
          - Source: Service
            Contains: Support
      - Type: Group
        Name: Development
        Conditions:
        - Equals:
            - 123456789013
            - 123456789014
```

# Using Custom Dimensions in CloudZero

You can see all of the published Custom Dimensions defined in the CostFormation Definition File from the [Explorer](doc:explorer).

Custom Dimensions are are available in the **Group By** selector as well as in the **Filters** selections. You can use Custom Dimensions to group the costs in the Explorer, to filter the costs, or both.

You can use Custom Dimensions with any of the other Dimensions for grouping and filtering your cost data.

All published Custom Dimensions can also be used with [Views](doc:views) as the either the **Principal Dimension** or as a **Filter Dimension**.
