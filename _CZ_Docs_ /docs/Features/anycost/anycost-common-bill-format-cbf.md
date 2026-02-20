---
title: Common Bill Format (CBF)
category: features
createdAt: '2022-08-03'
hidden: false
slug: anycost-common-bill-format-cbf
updatedAt: '2024-09-10'
---
<br />

CloudZero has developed a standard data model to ingest cost data from any source, called the Common Bill Format (CBF).  
The CBF is modeled after the AWS CUR format, but is simpler and more generic. This allows the CBF to be used by many different cloud providers.

If you use an [AnyCost Bucket Adaptor](https://docs.cloudzero.com/docs/anycost-bucket-getting-started), write the CBF to a gzipped CSV file and upload a `manifest.json` with it. See [Configuring AnyCost Bucket File Drops](https://docs.cloudzero.com/docs/anycost-cbf-drop-specs).

If you use an [AnyCost Stream Adaptor](https://docs.cloudzero.com/docs/anycost-stream-getting-started), send the CBF to the CloudZero AnyCost API in a JSON request body. See [Sending AnyCost Stream Data to CloudZero](https://docs.cloudzero.com/docs/anycost-send-stream-data).

# How CBF is used in CloudZero

Before mapping your source data onto the CBF columns, consider how this data is typically used in CloudZero.

First, even though very few columns are explicitly required, there are a few columns which are used very frequently and are highly recommended to populate, even if you use the name of the cloud provider or data source. These columns are:

* Line Item (`lineitem/type`)
* Account (`resource/account`)
* Service (`resource/service`)
* Region (`resource/region`) Refer to the note that follows.
* Usage Amount (`usage/amount`) Refer to the note that follows.
* Usage Pricing Unit (`usage/units`) Refer to the note that follows.

<Callout icon="ℹ️" theme="info">
  Region (`resource/region`): The default is no-region; do not use global. The field is free-form, and the following are examples of regions: `AWS: ap-southeast-2`, `Databricks: US_EAST_N_VIRGINIA`, and `Azure: eastus`.

  Usage Amount (`usage/amount`) and Usage Pricing Unit (`usage/units`) are always recommended, but usually aspirational. Few vendors will have cost and usage data available through their APIs.

  If your source data has a lot of detailed information about usage, consider mapping the fields using the following implicit hierarchy: Service (`resource/service`) → Usage Family (`resource/usage_family`) → Usage Type (`action/usage_type`). If you have additional low-level detail about the usage, you can use Operation (`action/operation`) along with Usage Type (`action/usage_type`).
</Callout>

# Data file columns

<Callout icon="ℹ️" theme="info">
  `datetime` values should be ISO-formatted strings in the UTC timezone. Excel often auto-converts ISO-formatted dates to a human-readable format. Ensure dates are saved correctly in your CSV file.
</Callout>

## Required fields

| Name                                                                                | CBF Column (field) | Type     |
| :---------------------------------------------------------------------------------- | :----------------- | :------- |
| [Cost](/docs/anycost-common-bill-format-cbf#costcost)                               | `cost/cost`        | number   |
| [Resource](/docs/anycost-common-bill-format-cbf#resourceid). See note that follows. | `resource/id`      | string   |
| [Usage Date](/docs/anycost-common-bill-format-cbf#timeusage_start)                  | `time/usage_start` | datetime |

<Callout icon="ℹ️" theme="info">
  Resource (`resource/id`) is required only when a Tag (`resource/tag:<key>`) value is included for the charge.
</Callout>

## Recommended fields

| Name                                                                                          | CBF Column (field) | Type   |
| :-------------------------------------------------------------------------------------------- | :----------------- | :----- |
| [Account](/docs/anycost-common-bill-format-cbf#resourceaccount)                               | `resource/account` | string |
| [Line Item](/docs/anycost-common-bill-format-cbf#lineitemtype)                                | `lineitem/type`    | string |
| [Service](/docs/anycost-common-bill-format-cbf#resourceservice)                               | `resource/service` | string |
| [Usage Amount](/docs/anycost-common-bill-format-cbf#usageamount)                              | `usage/amount`     | number |
| [Usage Pricing Unit](/docs/anycost-common-bill-format-cbf#usageunits). See note that follows. | `usage/units`      | string |

<Callout icon="ℹ️" theme="info">
  Usage Pricing Unit (`usage/units`) is relevant only when you are mapping Usage Amount (`usage/amount`) numerical data.
</Callout>

## Optional Cost fields

For some cloud providers and data sources, you may be able to distinguish between different types of costs (for example, cost before and after discounts, with or without amortization). In those instances you can use the fields in this table. Note these all exist within CloudZero and will be populated with the required Cost field.

| Name                                                                                              | CBF Column (field)               | Type   |
| :------------------------------------------------------------------------------------------------ | :------------------------------- | :----- |
| [Cost - Amortized](/docs/anycost-common-bill-format-cbf#costamortized_cost)                       | `cost/amortized_cost`            | number |
| [Cost - Discounted](/docs/anycost-common-bill-format-cbf#costdiscounted_cost)                     | `cost/discounted_cost`           | number |
| [Cost - Discounted Amortized](/docs/anycost-common-bill-format-cbf#costdiscounted_amortized_cost) | `cost/discounted_amortized_cost` | number |
| [Cost - On-demand](/docs/anycost-common-bill-format-cbf#coston_demand_cost)                       | `cost/on_demand_cost`            | number |

## Optional Dimension fields

| Name                                                                          | CBF Column (field)        | Type     |
| :---------------------------------------------------------------------------- | :------------------------ | :------- |
| [Cloud Provider](/docs/anycost-common-bill-format-cbf#lineitemcloud_provider) | `lineitem/cloud_provider` | string   |
| [Description](/docs/anycost-common-bill-format-cbf#lineitemdescription)       | `lineitem/description`    | string   |
| [K8s Cluster](/docs/anycost-common-bill-format-cbf#k8scluster)                | `k8s/cluster`             | string   |
| [K8s Deployment](/docs/anycost-common-bill-format-cbf#k8sdeployment)          | `k8s/deployment`          | string   |
| [K8s Labels](/docs/anycost-common-bill-format-cbf#k8slabels)                  | `k8s/labels`              | string   |
| [K8s Namespace](/docs/anycost-common-bill-format-cbf#k8snamespace)            | `k8s/namespace`           | string   |
| [Invoice ID](/docs/anycost-common-bill-format-cbf#billinvoice_id)             | `bill/invoice_id`         | string   |
| [Operation](/docs/anycost-common-bill-format-cbf#actionoperation)             | `action/operation`        | string   |
| [Region](/docs/anycost-common-bill-format-cbf#resourceregion)                 | `resource/region`         | string   |
| [Tags](/docs/anycost-common-bill-format-cbf#resourcetagkey)                   | `resource/tag:<key>`      | string   |
| [Usage End Date](/docs/anycost-common-bill-format-cbf#timeusage_end)          | `time/usage_end`          | datetime |
| [Usage Family](/docs/anycost-common-bill-format-cbf#resourceusage_family)     | `resource/usage_family`   | string   |
| [Usage Type](/docs/anycost-common-bill-format-cbf#actionusage_type)           | `action/usage_type`       | string   |

## Deprecated fields

| Name                                                          | CBF Column / Field | Type   |
| :------------------------------------------------------------ | :----------------- | :----- |
| [Account](/docs/anycost-common-bill-format-cbf#actionaccount) | `action/account`   | string |
| [Region](/docs/anycost-common-bill-format-cbf#actionregion)   | `action/region`    | string |

# Field definitions

## Action columns

### `action/operation`

The thing that was done to the resource for which you are being charged.

### `action/usage_type`

A common subdivision of Service (`resource/service`) → Usage Family (`resource/usage_family`). For details, see the note in the section [How CBF is used in CloudZero](/docs/anycost-common-bill-format-cbf#how-cbf-is-used-in-cloudzero).

### `action/region`

Deprecated; use `resource/region`. The region in which the operation was performed. May not match the `resource/region` for cross-region operations.

### `action/account`

Deprecated; use `resource/account`. The account in which the operation was performed. May not match the `resource/account` for cross-region operations.

## Bill column

### `bill/invoice_id`

Uniquely identifies a particular bill. A single billing data ID for a single month may include multiple invoices. Ideally this field will not be populated until an Invoice is closed.

## Cost columns

The cost category columns are described in this section. Only `cost` is required. The others may be used to help smooth out charges not directly associated with the use of cloud services.

### `cost/cost`

The cost associated with this line item. May be negative for line items which represent discounts or credits. Sometimes referred to as unblended cost, billed cost, or invoiced cost.

### `cost/amortized_cost`

The effective cost associated with this line item after any committed use purchases (for example, AWS RIs or Savings Plans, GCP CUDs, and so on) are amortized over all the `Usage` line items to which they apply. CloudZero is not automatically amortizing based on the start and stop dates you send. The cost will be applied on the start date.

### `cost/discounted_cost`

The net cost associated with this line item after any discounts, credits, or private pricing are applied. Sometimes referred to as net cost or net unblended cost.

### `cost/discounted_amortized_cost`

The net effective cost associated with this line item after any discounts, credits, or private pricing are applied. It also includes any committed use purchases, for example, AWS RIs or Savings Plans, GCP CUDs, and so on, amortized over all the `Usage` line items to which they apply. Sometimes referred to as net amortized cost, net effective cost, or fully-loaded cost.

### `cost/on_demand_cost`

The cost of this line item if no mechanism for reducing costs had been applied. In other words, it is the cost as if there were no discounts, applicable committed use purchases, private pricing, and so on. This is often useful for determining one's effective savings rate.

### Precedence for cost columns

To ensure all cost columns are fully populated and may be used in the platform, blank values will fall back and use a different cost column. For example, if `discounted_amortized_cost` is left blank, `discounted_cost` will be used instead. The assumption is that no line items required amortization, that is, there are no committed use purchases, and thus the discounted cost could be used instead. Only blank or empty values trigger this behavior; if the value is set to `0`, it will be used as is. The complete set of fallback logic is:

* `discounted_amortized_cost` → `amortized_cost` → `discounted_cost` → `cost`
* `amortized_cost` → `cost`
* `discounted_cost` → `cost`
* `on_demand_cost` → `cost`

The total value across all line items for each of `cost`, `discounted_cost`, `amortized_cost`, and `discounted_amortized_cost` should be the same. Each represents a redistribution of charges (discounts or purchases or both), not the inclusion or exclusion of charges. This equivalence is not enforced by the billing ingest system, but may be in the future.

### How cost types are defined

CloudZero cost types are defined in terms of the `lineitem/type` and different cost category columns.

* Real Cost: Only `Usage` line item types are included. The `discounted_amortized_cost` column is used, if present, with fallback logic to the other `cost` values if it is not.
* Discounted Amortized Cost: All line item types are included. The `discounted_amortized_cost` column is used, if present, with fallback logic to the other cost categories if it is not.
* Amortized Cost: All line item types are included. The `amortized_cost column` is used, if present, with fallback to `cost` if not.
* Discounted Cost: All line item types are included. The `discounted_cost` column is used, if present, with fallback to `cost` if not.
* On-Demand Cost: All line item types are included. The `on_demand_cost` column is used, if present, with fallback to `cost` if not.
* Billed Cost: All line item types are included. The `cost` column is used.

## Kubernetes columns

### `k8s/cluster`

The Kubernetes cluster that is associated with the resource.

### `k8s/namespace`

The Kubernetes namespace that is associated with the resource.

### `k8s/deployment`

The Kubernetes deployment that is associated with the resource.

### `k8s/labels`

The Kubernetes labels that are associated with the resource.

## Line item columns

### `lineitem/cloud_provider`

Identifies the underlying cloud provider for each line item. The field supports values including `Anthropic`, `OpenAI`, `AWS`, `Azure`, and more, and enables you to track costs across multiple cloud providers. If you use an aggregator service that consolidates billing from multiple cloud providers into a single CBF file, you can distinguish between providers without any manual mapping or guesswork.

### `lineitem/description`

An optional description specifying additional information about this line item.

### `lineitem/type`

Uniquely identifies this specific line item in this specific bill, with the broad category of the line item: `Usage`, `Tax`, `Discount`, and so on. If not provided, assumed to be `Usage`. The `lineitem/type` column defines how each line item should be interpreted. Values have special meaning. The supported values are as follows:

* `Usage`: The most common type and the default. The line item represents a charge for the use of some cloud resource. Real Cost includes only `Usage` line items and uses the first available cost type provided from: `amortized_cost`, `discounted_cost`, or `cost`.
* `Tax`: This line item represents any tax charges. Time, resource, and action fields should be populated only if the tax is associated with applicable `Usage` changes. Otherwise these columns should be left blank.
* `Support`: Charges for support or other human services. Columns in the time category should specify the start and end of the support contract.
* `Purchase:` Charge for a one-time purchase or non-usage based subscription, for example, software bought from the AWS Marketplace. The time category columns should represent the span of time over which the purchase applies (for subscriptions with renewal) or the time of the purchase (for one-time charges).
* `CommittedUsePurchase`: Charges for a committed use (for example, RI, savings plan) purchase. This is a one-time, upfront fee for a committed use subscription. Committed use includes any instrument for which payment is made to receive a reduced rate on future usage. This may include one-time upfront purchases or recurring monthly charges. The time category columns should represent the span of time over which the charge applies (for example, one month for monthly recurring charges.) The amortized_cost cost column of this line item should always be zero (if used).
* `CommittedUseVacancy`: The unused portion of a committed use subscription.
* `CommittedUseRecurringFee`: Recurring, typically monthly, fee for a committed use subscription.
* `Discount`: A negative value cost associated with some `Usage` line item. Columns in the time, resource, and action categories of this line item should match those of the applicable Usage line item and the cost should be negative. The discounted_cost for this line item should be zero if this discount is fully accounted for in the discounted_cost of other Usage line items. (Note: you must still include discounted_cost if it should be zero)
* `Credit`: A negative value cost not associated with any specific `Usage` line items. May represent an adjustment due to an error, rounding, refund, and so on.
* `Fee`: A positive value charge for which no other line item type applies.
* `Adjustment`: An alteration made to the bill to correct for some error or rounding issue.

## Resource columns

### `resource/id`

Uniquely identifies the object for which this charge applies. This column is required if any `resource/tag:\<key>` columns are included. Tags are time independent so CloudZero uses only the most recent set of tags for each unique resource ID.

CloudZero reads the `resource/id` as two fields, a resource type and a resource name, concatenated together with a forward slash or a colon.

The following special characters colon (:) and forward slash (/) have special meaning. Avoid using those characters in the resource/id except to split the type and the name. A resource/id containing a colon or a forward slash will be split, and the first element will be taken as the resource type. The second element will be taken as the resource cloud local id. Using any additional slashes and colons can lead to parts being dropped. For example, the a resource/id of `a:b:c`, the **resource type** will be `a` and the **resource cloud local id** will be `b`. The `c` will be dropped.

Thus, given the `resource/id` of `a/b/c/d/e`:

* Resource type = `a`
* Resource cloud local id = `b`
* All other segments (`c`, `d`, and `e`) are dropped

Note that for the AWS lambda function `function/my-lambda-function`, the **resource type** is `function` and the **resource cloud local id** is `my-lambda-function`.

When `resource/id` is specified, you may also provide `resource/tag:<key>` columns to categorize the resource by `<key>`, which may be a purpose, owner, environment, or other criteria. When you include `resource/tag:<key>` data with a charge, the `resource/id` column is required. Only one `resource/tag:<key>` column `<value>` will be associated with each unique `resource/id` value. For more information, see the `resource/tag:<key> section`.

### `resource/service`

The category to which this resource belongs. Generally represents different kinds of services provided by the Cloud Provider for which the customer is charged.

### `resource/account`

The most specific account or project to which this resource belongs (if applicable). This concept has a different designation for each cloud provider. For the optimum experience, use a value that is as specific as possible.

### `resource/region`

The region to which this resource belongs (if applicable).

### `resource/usage_family`

Commonly a subdivision of `resource/service`.

### `resource/tag:<key>`

Custom attributes associated with the resource.

* Using this column requires that `resource/id` be populated.
* `resource/tag:<key>` columns allow you to categorize resources by purpose, owner, environment, or any other criteria.
* The `<key>` is case sensitive, and can consist of letters, numbers, and the following special characters `_ . : / = + - @.`.
  * No spaces, tabs, or returns are allowed.
  * For example, `resource/tag:team` or `resource/tag:Product-Type` are valid tag keys, while `resource/tag:Team Name` and `resource/tag:Product&Dev` are not.
* `resource/tag:<key>` will appear as Tag dimensions in the CloudZero platform, and can be used to filter or aggregate the cost of the tagged resources.
* You may include as many unique `resource/tag:<key>` columns as you need.
* Only one `<value>` will be associated with a `resource/tag:<key>` column for each unique `resource/id`.
  * If multiple values are supplied for the same ID, the value with the latest `time/usage_start` will be used.
  * If all instances for a given key have identical `time/usage_start` dates, then one is arbitrarily selected.
* The latest `<value>` of a given `resource/tag:<key>` for each `resource/id` will be retroactively applied to all data in the CloudZero system with the same `resource/id`.

### Example of `resource/id` and `resource/tag` usage

B Large, Inc. is using the CloudZero platform to monitor their cloud costs, and needs to easily identify their resources by the teams that own them. To assist with this, B Large creates a Resource Tag called `resource/tag:team`, and populates it with the names of the various teams that own the AWS resources in question.

Team Alpha owns an AWS Lambda function with the `resource/id` of `making-great-calculations`. Since these resources have been tagged as owned by Team Alpha using the `resource/tag:team` key with the value of `Alpha`, whenever anyone logs in to CloudZero, they can easily use the team Tag Dimension to view what Alpha's Lambda is costing B Large, and monitor trends over time.

Recently, B Large promoted more personalized team names, and Team Alpha voted to name themselves Team Batman. With this change, the `resource/tag:team` value in AWS is updated to reflect their new name, and CloudZero receives a new data drop that associates a new `resource/tag:team` value of Batman with the AWS Lambda function `resource/id` of `making-great-calculations`.

The CloudZero platform receives this updated tag information, and because only one value per `resource/tag:team` can be associated with a single `resource/id` of `making-great-calculations`, the platform retroactively applies this new tag to all historical data in the system for the `resource/id` of `making-great-calculations`.

Now when anyone at B Large logs into CloudZero, they can still see what Team Batman owns, and because the tag change was retroactively applied to all historical data. The monitoring of trends over time for the making-great-calculations Lambda sees no interruption, and reports continue to accurately reflect totals and trends, including those that were ingested prior to Team Batman's name change.

## Time columns

### `time/usage_start`

The hour during which the charged usage applies. This value should be aligned to the start of the hour and will be treated as such. Note that the current version of the Common Billing Format does not use `time/usage_end` date.

### `time/usage_end`

The end of a timespan to which the charged usage applies. Note that although this may be specified, all changes are treated as occurring in a single hour at `time/usage_start`. Future updates to the ingest process may take advantage of the `usage_end` value.

## Usage columns

### `usage/amount`

A numeric value describing an amount consumed or used, for example, GB stored or transferred, seconds executed, credits consumed.

### `usage/units`

A description of the units used for usage/amount.

# CBF examples

## Compute purchase from Simple Cloud example

In this example we purchased some Compute from Simple Cloud.  We also made an up-front committed use purchase, which lowered the normal hourly rate by 50%.  Simple Cloud is running a promotion, so we received the SpecialCompute discount for using a certain Compute instance type. We also received the MVP Discount.

This first version of the bill just includes the actual charges.  The cost for our Compute instances is at the reduced rate because of the committed use purchase; for example, `instance-0000` would have otherwise cost $24 during that hour. The sum of the values in the `cost/cost` column should equal exactly what we see on the bill for March: $105.30

| lineitem/type | resource/service | resource/id        | time/usage_start     | cost/cost |
| :------------ | :--------------- | :----------------- | :------------------- | :-------- |
| Usage         | Compute          | instance-0000      | 2022-03-16T13:00:00Z | 12        |
| Usage         | Compute          | instance-0001      | 2022-03-16T13:00:00Z | 20        |
| Usage         | Compute          | instance-0002      | 2022-03-16T13:00:00Z | 15.3      |
| Purchase      | CommitedUse      | commit-111-222-333 | 2022-03-01T00:00:00Z | 90        |
| Discount      | SpecialCompute   | special-01010101   | 2022-03-16T13:00:00Z | -12       |
| Discount      | MVPDiscount      | mvp-aaa-12345      | 2022-03-01T00:00:00Z | -20       |

## Discounted cost example

It would be helpful if the discount we received for using the promoted Compute instances were actually represented in the cost of those instances. In this example we will include the `cost/discounted_cost`.

| lineitem/type | resource/service | resource/id        | time/usage_start     | cost/cost | cost/discounted_cost |
| :------------ | :--------------- | :----------------- | :------------------- | :-------- | :------------------- |
| Usage         | Compute          | instance-0000      | 2022-03-16T13:00:00Z | 12        | 8                    |
| Usage         | Compute          | instance-0001      | 2022-03-16T13:00:00Z | 20        | 16                   |
| Usage         | Compute          | instance-0002      | 2022-03-16T13:00:00Z | 15.3      | 11.3                 |
| Purchase      | CommitedUse      | commit-111-222-333 | 2022-03-01T00:00:00Z | 90        | 90                   |
| Discount      | SpecialCompute   | special-01010101   | 2022-03-16T13:00:00Z | -12       | 0                    |
| Discount      | MVPDiscount      | mvp-aaa-12345      | 2022-03-01T00:00:00Z | -20       | -20                  |

The SpecialCompute discount was distributed evenly over the individual instances.  We also zeroed out the cost for the SpecialCompute line item because that discount has already been accounted for.  We chose not to distribute the MVPDiscount since it was unrelated to the Compute instances.  We copied over the values for the CommitedUse purchase and MVPDiscount, but we could have also left them blank and the `cost/cost` value would have been used by default.

## Amortized cost example

To help our engineers better understand the real cost of those Compute instances, we also want to include what we paid for the CommitedUse purchase.

| lineitem/type | resource/service | resource/id        | time/usage_start     | cost/cost | cost/discounted_cost | cost/amortized_cost |
| :------------ | :--------------- | :----------------- | :------------------- | :-------- | :------------------- | :------------------ |
| Usage         | Compute          | instance-0000      | 2022-03-16T13:00:00Z | 12        | 8                    | 38                  |
| Usage         | Compute          | instance-0001      | 2022-03-16T13:00:00Z | 20        | 16                   | 46                  |
| Usage         | Compute          | instance-0002      | 2022-03-16T13:00:00Z | 15.3      | 11.3                 | 41.3                |
| Purchase      | CommitedUse      | commit-111-222-333 | 2022-03-01T00:00:00Z | 90        | 90                   | 0                   |
| Discount      | SpecialCompute   | special-01010101   | 2022-03-16T13:00:00Z | -12       | 0                    |                     |
| Discount      | MVPDiscount      | mvp-aaa-12345      | 2022-03-01T00:00:00Z | -20       | -20                  |                     |

The cost of the CommitedUse purchase was evenly distributed over all the Compute instances to which it applied, which in this case was all of them. We left the `cost/amortized_cost` for the Discounts blank.  We could have also copied over the values from the `discounted_cost` (0 and -20).  The important thing is that the the sum of the values in the `cost/amortized_cost` column, including the default values for the blank cells, is still: $105.30

## Kubernetes-related columns example

In this example, we add Kubernetes-related columns to the existing CBF data to provide more context on resource usage within a Kubernetes environment.

| lineitem/type | resource/service | resource/id   | time/usage_start     | k8s/cluster | k8s/namespace | k8s/deployment | k8s/labels                                | cost/cost |
| :------------ | :--------------- | :------------ | :------------------- | :---------- | :------------ | :------------- | :---------------------------------------- | :-------- |
| Usage         | Compute          | instance-0000 | 2022-03-16T13:00:00Z | my-cluster  | default       | web-app        | \{"app": "frontend", "env": "production"} | 12        |
| Usage         | Compute          | instance-0001 | 2022-03-16T13:00:00Z | my-cluster  | default       | web-app        | \{"app": "frontend", "env": "production"} | 20        |
| Usage         | Compute          | instance-0002 | 2022-03-16T13:00:00Z | my-cluster  | default       | worker-app     | \{"app": "backend", "env": "production"}  | 15.3      |

Kubernetes-related information such as cluster, namespace, deployment, and labels is included. This allows tracking usage and costs within specific Kubernetes contexts.
