---
title: Dimensions
category: features
createdAt: '2021-03-25T15:14:19.183Z'
hidden: false
slug: dimensions
updatedAt: '2024-11-18T16:04:13.235Z'
---
CloudZero Dimensions allow you to understand the costs of operating cloud software in ways that matter to your business.

An CloudZero organization has many Dimensions. You can use Dimensions to take actions such as the following:

* Group and filter spend in the [Explorer](/docs/explorer).
* Receive updates by Slack or email through [Views](/docs/views).
* [Allocate costs](/docs/costformation-allocating-shared-costs), such as cost per customer, cost per feature, cost per team, and so on.

All Dimensions begin with **charges**. A charge is the dollar amount that the cloud provider billed for a given thing at a given time. **Elements** are the values that a charge may have in a Dimension. For example, `us-east-1` is an element of the `Region` Dimension. In practice, elements are usually referred to using the Dimension name. For example:

* `us-east-1` is a region in the `Region` Dimension.
* `Billing` is a feature in a  `Feature` Custom Dimension.

CloudZero supports Custom Dimensions and Core Dimensions.

# Core Dimensions

Core Dimensions are built-in Dimensions provided by CloudZero, derived from cloud provider data such as billing line items or resource properties. They are split into several subtypes that you can use as a source for creating Custom Dimensions.

To learn how to use each subtype as a [Source Dimension in CostFormation](/docs/cfdl-reference#source-dimensions), see the following documentation:

* [Cloud Provider Billing Dimensions:](/docs/cfdl-reference#core-cloud-provider-dimensions) Sourced directly from your cloud provider's billing data.
* [Additional Cloud Provider Dimensions:](/docs/cfdl-reference#additional-cloud-provider-dimensions) Defined by CloudZero, based on your cloud provider's billing data.
* [Tag Dimensions:](/docs/cfdl-reference#tag-dimensions) Compiled dynamically from the list of tags CloudZero receives from your cloud provider.
* [Kubernetes Dimensions:](/docs/cfdl-reference#kubernetes-dimensions) Compiled dynamically through data CloudZero receives from a [Kubernetes](/docs/container-cost-track) integration.

# Custom Dimensions

**[Custom dimensions](/docs/cfdl-reference#custom-dimensions)** are user-defined dimensions that allow you to view cloud costs in the context of your business and engineering needs, enabling better cost analysis. You can use Custom Dimensions to filter and allocate costs by custom business bucket, such as product, microservice, engineering team, and more.

To define a Custom Dimension, you combine Core Dimensions in a YAML file using the [CostFormation](/docs/cost-formation-definition-language) language. The elements in a Custom Dimension are created through an [allocation telemetry stream](/docs/allocation-short-form-rules#allocatebystreams-short-form-rule) or [defined in the CostFormation file](/docs/cost-formation-definition-language#/).

For more information about using CostFormation to create Custom Dimensions, see [Guide to Using the CostFormation Definition Language](/docs/costformation-definition-language-guide) and the [CostFormation Language Reference](/docs/cfdl-reference).

# Using Dimensions in CloudZero

You can use Core and Custom Dimensions throughout CloudZero to understand your costs in the Explorer or to keep organization members updated about relevant spend through Views. For more information, see the following documentation:

* [Explorer](/docs/explorer)
* [Views](/docs/views)
