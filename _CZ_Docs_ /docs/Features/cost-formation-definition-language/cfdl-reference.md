---
title: CostFormation Definition Language Reference
category: features
createdAt: '2021-08-27T21:40:59.886Z'
hidden: false
metadata:
  title: CostFormation Definition Language Reference
slug: cfdl-reference
updatedAt: '2021-09-29T17:38:37.376Z'
---
This page defines the syntax of the CostFormation Definition Language. For more information, see [Allocation Short Form Rules](/docs/allocation-short-form-rules).

# Conditions

This section lists the supported conditions.

## And

This condition evaluates a list of conditions as a logical `And` operation. This condition evaluates to `True` only if all conditions evaluate to `True`. If a single condition in the list evaluates to `False`, then the entire condition evaluates to `False`.

```yaml
  - And:
    - <Condition 1>
    - <Condition 2>
    ...
    - <Condition N>
```

## Or

This condition evaluates the list of conditions as a logical `Or`. This condition evaluates to `True` if any of the list of conditions evaluate to `True`. If all conditions in the list evaluate to `False`, then the entire condition evaluates to `False`.

```yaml
  - Or:
    - <Condition 1>
    - <Condition 2>
    ...
    - <Condition N>
```

## Not

This condition evaluates the list of conditions as a logical `Or` and then negates the result. This condition evaluates to `True` only if all conditions evaluate to `False`. If a single condition in the list evaluates to `True`, then the entire condition evaluates to `False`.

```yaml
  - Not:
    - <Condition 1>
    - <Condition 2>
    ...
    - <Condition N>
```

## BeginsWith

This condition checks whether the source value begins with any of the specified strings. This condition can optionally specify its own [source properties](doc:costformation-definition-language-guide#specifying-sources).

```yaml
  - BeginsWith: <Value>
    <Source Properties>
```

Or

```yaml
  - BeginsWith:
      - <Value 1>
      - <Value 2>
      ...
      - <Value N>
    <Source Properties>
```

## Contains

This condition checks whether the source value contains any of the specified strings. This condition can optionally specify its own [source properties](doc:costformation-definition-language-guide#specifying-sources).

```yaml
  - Contains: <Value>
    <Source Properties>
```

Or

```yaml
  - Contains:
      - <Value 1>
      - <Value 2>
      ...
      - <Value N>
    <Source Properties>
```

## EndsWith

This condition checks whether the source value ends with any of the specified strings. This condition can optionally specify its own [source properties](doc:costformation-definition-language-guide#specifying-sources).

```yaml
  - EndsWith: <Value>
    <Source Properties>
```

Or

```yaml
  - EndsWith:
      - <Value 1>
      - <Value 2>
      ...
      - <Value N>
    <Source Properties>
```

If `<Value>` is `type`, then the condition evaluates to `True` for `A cost type`, `The cost type`, and `Example of a cost type`.

## Equals

This condition checks whether the source value equals any of the specified strings. This condition can optionally specify its own [source properties](doc:costformation-definition-language-guide#specifying-sources).

```yaml
  - Equals: <Value>
    <Source Properties>
```

Or

```yaml
  - Equals:
      - <Value 1>
      - <Value 2>
      ...
      - <Value N>
    <Source Properties>
```

## HasValue

This condition checks whether the source value has an actual value or not. This condition can optionally specify its own [source properties](doc:costformation-definition-language-guide#specifying-sources).

```yaml
  - HasValue: <True|False>
    <Source Properties>
```

If `HasValue` is set to `True`, then the condition evaluates to `True` if the source has a value. If `HasValue` is `False`, then the condition evaluates to `False` if the source does **not** have a value.

## Matches

This condition checks whether the source value matches any of the specified regular expressions.

```yaml
  - Matches: <RegEx>
    <Source Properties>
```

Or

```yaml
  - Equals:
      - <RegEx 1>
      - <RegEx 2>
      ...
      - <RegEx N>
    <Source Properties>
```

If `<RegEx>` is `".* (cost|product) types"`, then the condition evaluates to `True` for `Cost types`,  `Product types`, and `Another example of cost types` but not for `Cost type`.

A valid regular expression for the purposes of `Matches` is essentially a straight passthrough to Snowflake’s `REGEXP_LIKE` function and therefore uses Snowflake’s regex syntax. For more information, see the [String functions (regular expressions) Snowflake documentation](https://docs.snowflake.com/en/sql-reference/functions-regexp).

## Before

This condition checks whether any value comes before the provided value alphabetically.

```yaml
  - Before: <value>
```

## BeforeOrEquals

This condition checks whether any value comes before the provided value alphabetically or is the same.

```yaml
  - BeforeOrEquals: <value>
```

## After

This condition checks whether the source's value comes after the provided value alphabetically.

```yaml
  - After: <value>
```

## AfterOrEquals

This condition checks whether the source's value comes after the provided value alphabetically or is the same.

```yaml
  - AfterOrEquals: <value>
```

## ForDateRange

This condition checks whether there is cost data with usage that occurred between the specified start date and end date (inclusive). The recommended date format is `YYYY-MM-DD`.

```yaml
  - ForDateRange:
      From: <Date>
      Until: <Date>
```

# Source Dimensions

This section describes the available sources that can be used when building Custom Dimensions with CostFormation. The sources are broken down by types of sources (that is, sources direct from billing data, resource tags, and so on). Each table shows the **Source ID** which is the ID of the source that would be used in the Custom Dimension definition.

<Callout icon="ℹ️" theme="info">
  Not all source dimensions listed in this section are available in the Explorer or Views and some are located with a slightly different name than their ID. Check the **Name in Explorer/Views** column to see which source IDs are visible in the Explorer and Views and under which name.
</Callout>

## Core Cloud Provider Dimensions

These dimensions are sourced directly from billing data from your cloud provider.

| Source ID                  | Name in Explorer/Views | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| -------------------------- | ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Account`                  | Account                | Elements consist of the IDs for any cloud account you have connected to CloudZero (for example: Azure subscription ID, GCP project ID, AWS account ID).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `BillingConnectionID`      | Not Available          | Elements consist of the corresponding ID that ties back to the Billing Connection the charges are related to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `CloudProvider`            | Cloud Provider         | Elements consist of the cloud providers supported by CloudZero (for example: `AWS`, `GCP`).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `CommittedUseSubscription` | Not Available          | Elements consist of the details of the specific committed use subscription or plan: RI, Savings Plan, and so on, associated with the charge.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `Description`              | Not Available          | Elements consist of the detailed text field that explains the specific service, resource, or pricing component being charged.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `InvoiceID`                | Not Available          | Elements consist of the corresponding invoice ID of the charges.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `K8s:Pod`                  | Not Available          | Elements consist of the deployed pod resources in any of your Kubernetes clusters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `LineItemType`             | Not Available          | Elements consist of the type of charge for a given billing line item.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `Operation`                | Operation              | Elements consist of the specific cloud provider operation covered by the billing line item.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `PayerAccount`             | Not Available          | Elements consist of the Management Account associated with the charges.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `PricingTerm`              | Not Available          | Elements consist of how charges are priced (for example: `on-demand`, `reserved`.)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `PricingUnit`              | Not Available          | Elements consist of the unit of measurement used for billing purposes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `PricingUnits`             | Not Available          | Elements consist of the unit of measure used for pricing cloud resources (for example, GB, hours, requests). The following identifies the corresponding term used by cloud providers: **AWS**: `pricing/unit`; **GCP**: `usage.pricing_unit`; **Azure**: `unitOfMeasure`; **CBF**: `usage/units`; **CZ Dimension**: `PricingUnit`                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `ProductFamily`            | Not Available          | Elements consist of the product family that the resource is associated with, for example, Compute Instance, NAT Gateway, and so on.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `Region`                   | Region                 | Elements consist of the cloud region where the billed resource is located.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `Resource`                 | Not Available          | Element is the CloudZero Resource Name (CZRN) of the resource. The CZRN is a unique identifier formed from cloud provider metadata such as resource name, account, and region. <br /><br /> To avoid performance issues in the Explorer, CloudZero recommends using [`CZ:Defined:ResourceSummaryDisplay`](#additional-cloud-provider-dimensions) as a source in CostFormation instead, which groups logically related resources together (such as EKS clusters) and does not include individual instance IDs. <br /><br /> However, if you _must_ match resources based on IDs, use [`CZ:Defined:ResourceDisplay`](#additional-cloud-provider-dimensions) instead because it uses the native resource ID instead of the CZRN and therefore aligns with the resource values shown in the CloudZero UI. |
| `RequestType`              | Not Available          | Elements consist of incoming request type, such as from AWS CloudFront.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `Service`                  | Not available          | Elements consist of codes for the cloud provider service type. To find the service code, filter by Service in the Explorer and look at the URL. Alternatively, you can use the [`CZ:Defined:ServiceDisplay`](#additional-cloud-provider-dimensions) source instead, which aligns with the service values shown in the CloudZero UI.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `TransferType`             | Not Available          | Elements consist of the type of data transfer (for example: `outbound`, `intra-region`).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `UsageDay`                 | Not Available          | Elements consist of an ISO-formatted date for the day applied to each line item.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `UsageFamily`              | Usage Family           | Elements consist of the cloud service charges.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `UsageType`                | Usage Type             | Elements consist of the usage details of the billing line item in the cloud provider.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

## Additional Cloud Provider Dimensions

The following dimensions are defined by CloudZero, based on billing data from your cloud provider. They are available in the Explorer and Views.

| Source ID                           | Name in Explorer and Views (Found under Cloud Provider Dimensions) | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ----------------------------------- | ------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CZ:Defined:BillingLineItem`        | Billing Line Item                                                  | Elements consist of categories of billing line item (for example: `Usage`, `Support`).                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `CZ:Defined:Category`               | Service Category                                                   | Elements consist of the different categories of services similar to what you would see in your cloud provider console (for example: `Networking`, `Compute`).                                                                                                                                                                                                                                                                                                                                                  |
| `CZ:Defined:Elasticity`             | Elasticity                                                         | Elements include two types of spend: `Storage` and `Variable Costs`.                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `CZ:Defined:InstanceType`           | Instance Type                                                      | Elements are grouped by a sub-section of the `UsageType` name and filtered to show costs specifically related to the type, size, and family of a resource (for example: `AmazonEC2`, `ElasticMapReduce`).                                                                                                                                                                                                                                                                                                      |
| `CZ:Defined:NetworkingCategory`     | Networking Category                                                | Elements consist of the major types of networking spend (for example: `VPC Endpoints`, `Data Transfer`).                                                                                                                                                                                                                                                                                                                                                                                                       |
| `CZ:Defined:NetworkingSubCategory`  | Networking Sub-Category                                            | Elements are a deeper breakdown of networking-related costs (for example: `VPC Endpoint (Hours)`, `S3 Outbound`).                                                                                                                                                                                                                                                                                                                                                                                              |
| `CZ:Defined:PaymentOption`          | Payment Option                                                     | Elements consist of different payment types (for example: `Reservation`, `Discount`) grouped based on `LineItemType`, `UsageFamily`, and `UsageType`.                                                                                                                                                                                                                                                                                                                                                          |
| `CZ:Defined:ResourceDisplay`        | Not Available                                                      | Same as [`Resource`](#core-cloud-provider-dimensions), but uses native resource IDs instead of CZRNs and therefore aligns with the resource values shown in the CloudZero UI. <br /><br /> To avoid performance issues in the Explorer, CloudZero recommends using `CZ:Defined:ResourceSummaryDisplay` instead, which groups logically related resources (such as EKS clusters) and does not include individual instance IDs.                                                                                  |
| `CZ:Defined:ResourceNameOnly`       | Not Available                                                      | Deprecated. Use `CZ:Defined:ResourceSummaryDisplay` instead.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `CZ:Defined:ResourceSummaryDisplay` | Resource Summary                                                   | By default, the base of the hierarchy when a user drills down in the Explorer. This dimension groups resources that tend to be copious and are logically related (such as EKS clusters) into elements, omitting individual instance IDs. The dimension preserves standalone resources (such as database servers or lambdas) as individual elements. Use this dimension instead of [`Resource`](#core-cloud-provider-dimensions) or `CZ:Defined:ResourceDisplay` to prevent performance issues in the Explorer. |
| `CZ:Defined:ResourceSummaryID`      | Not Available                                                      | Same as `CZ:Defined:ResourceSummaryDisplay`, but uses CZRNs instead of the native resource IDs. When trying to match against resources in CostFormation, use `CZ:Defined:ResourceSummaryDisplay` instead, which aligns with the resource values shown in the CloudZero UI.                                                                                                                                                                                                                                     |
| `CZ:Defined:ResourceType`           | Resource Type                                                      | Elements consist of resource types for each cloud provider service (for example: `BigQuery: job`, `S3: bucket`).                                                                                                                                                                                                                                                                                                                                                                                               |
| `CZ:Defined:ServiceDisplay`         | Service                                                            | Same as `Service`, but aligns with the display values shown in the CloudZero UI.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `CZ:Defined:ServiceDetail`          | Service Detail                                                     | A normalized version of the more detailed data stored in [`UsageType`](#core-cloud-provider-dimensions) and/or [`Operation`](#core-cloud-provider-dimensions). This dimension selects whichever data is more relevant for each Service in terms of [`UsageFamily`](#core-cloud-provider-dimensions) and then optimizes it.                                                                                                                                                                                     |
| `CZ:Defined:TaggableVsUntaggable`   | Taggable vs. Untaggable                                            | Elements consist of taggable resources and types of untaggable resources (for example: `Taggable`, `Untaggable - Service Charges`).                                                                                                                                                                                                                                                                                                                                                                            |

<Callout icon="ℹ️" theme="info">
  This information provides help in choosing the Dimension to use.

  CloudZero supports multiple types of Dimensions related to resources and resource IDs:

  * [`Resource`](#core-cloud-provider-dimensions) uses CZRN identifiers. Example: `czrn:aws:ec2:us-east-2:123456789012:instance:i-056061216d0a1b2c3`
  * [`CZ:Defined:ResourceDisplay`](#additional-cloud-provider-dimensions) uses native resource IDs. Example: `i-056061216d0a1b2c3`
  * [`CZ:Defined:ResourceSummaryID`](#additional-cloud-provider-dimensions) uses CZRN for summarized resources. Example: `czrn:aws:ec2:us-east-2:123456789012:instances`
  * [`CZ:Defined:ResourceSummaryDisplay`](#additional-cloud-provider-dimensions) uses native IDs for summarized resources. Example: `ec2-instance`

  If you are writing CostFormation to match against resources, `CZ:Defined:ResourceSummaryDisplay` is almost always the best choice. This Dimension uses the native resource IDs shown in the CloudZero UI and improves Explorer performance by grouping logically related resources together instead of enumerating individual instance IDs.
</Callout>

## Tag Dimensions

The CloudZero platform inspects all of your cloud resources and compiles the list of tags, both AWS tags and user tags, and exposes them as Dimensions that can be used throughout the platform. All tags are available in the Explorer and Views.

| Source ID | Name in Explorer and Views (Found under Tags) | Description                                                 |
| --------- | --------------------------------------------- | ----------------------------------------------------------- |
| `Tag:`    | `Tag -> <Tag Name>`                           | Elements consist of the different values for the given tag. |

## Kubernetes Dimensions

Some dimensions are derived from dynamic data that is discovered through [Kubernetes](/docs/container-cost-track) integrations. All Kubernetes dimensions are available in the Explorer and Views.

| Source ID                | Name in Explorer and Views (Found under Kubernetes) | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------ | --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `K8s:Cluster`            | Cluster                                             | Elements consist of the Kubernetes cluster names.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `K8s:Namespace`          | Namespace                                           | Elements consist of the Kubernetes namespace across all Kubernetes clusters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `K8s:Workload`           | Workload                                            | Elements consist of the deployed workload resources in any of your Kubernetes clusters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `K8s:Label:<Label Name>` | Label > Label Name                                  | The [CloudZero Agent for Kubernetes](/docs/installation-of-cloudzero-agent-for-kubernetes) supports labels and annotations in Pods, Deployments, StatefulSets, DaemonSets, Jobs, CronJobs, Nodes, and Namespaces. <br /><br />Elements are formatted in CostFormation as follows: <br /><br />**Labels for Pods:** `K8s:Label:<label-key>: <label-value>`<br /> (Example: `K8s:Label:myKey: myValue`)<br /><br /> **Labels for Other Supported Resources:** `K8s:Label:<resource-type>:<label-key>: <label-value>`<br /> (Example: `K8s:Label:node:myKey: myValue`) <br /><br /> **Annotations for Pods:** `K8s:Label:annotation:<label-key>: <label-value>`<br /> (Example: `K8s:Label:annotation:myKey: myValue`)<br /><br /> **Annotations for Other Supported Resources:** `K8s:Label:<resource-type>:annotation:<label-key>: <label-value>`<br /> (Example: `K8s:Label:node:annotation:myKey: myValue`) |

## Custom Dimensions

All Custom Dimensions are available in the Explorer and Views.

| Source ID                     | Name in Explorer and Views | Description                                                                  |
| ----------------------------- | -------------------------- | ---------------------------------------------------------------------------- |
| `User:Defined:<Dimension ID>` | `<Dimension Name>`         | Elements are grouped according to the logic in the CostFormation definition. |

# Transforms

## Lower

This transform converts all of the letters in the source value to lowercase. This transform has no parameters.

```yaml
  - Type: Lower
```

EXAMPLE: **Source value:** `ProductionResource 1`, **Transform result:** `productionresource 1`

## Upper

This transform converts strings to uppercase for standardized formatting.

```yaml
- Type: Upper
```

EXAMPLE: **Source value:** `the cost types`, **Transform result:** `THE COST TYPES`

## Title

This transform converts strings to title case, that is, first letter of each word capitalized.

```yaml
Type: Title
```

EXAMPLE: **Source value:** `the cost types`, **Transform result:** `The Cost Types`

## Trim

This transform removes leading and trailing whitespace from string values.

```yaml
Type: Trim
```

EXAMPLE: **Source value:** `" the cost types "`, **Transform result:** `"the cost types"`

## Clean

This transform removes leading and trailing whitespace from string values and converts any instance of the characters  `.,/#!$%^&*;:=_~()\'` and spaces within the string to a dash (`-`). This transform has no parameters.

```yaml
Type: Clean
```

EXAMPLE: **Source value:** `" The:Cost!Types "`, **Transform result:** `"The-Cost-Types"`

## Normalize

This transform removes leading and trailing whitespace from string values, converts all of the letters in a source value to lowercase, and converts any instance of the characters  `.,/#!$%^&*;:=_~()\'` and spaces within the string to a dash (`-`). This transform has no parameters.

```yaml
  - Type: Normalize
```

EXAMPLE: **Source Value:** `Production/Resources#4561`, **Transform result:** `production-resources-4561`

## Split

This transform splits the source value into a list of substrings using a specified delimiter. It will then extract the substring based on the specified index. The index is 1-based.

```yaml
  - Type: Split
    Delimiter: <delimiter>
    Index: <1 based index>
```

EXAMPLE: **Parameters:** `Delimiter: '-' Index: 1`, **Source value:** `eu-west-1`, **Transform result:** `eu`
