---
title: CloudZero Documentation
category: documentation
createdAt: '2020-02-13T19:39:05.304Z'
hidden: false
slug: cloudzero
updatedAt: '2021-09-10T15:30:48.764Z'
---
CloudZero is an AI and cloud cost intelligence platform that helps organizations understand, optimize, and control their spending. CloudZero automates the collection, analysis, and allocation of your costs for AI and  cloud infrastructure, inclusive of IaaS and Paas.

CloudZero is the first platform to put relevant and timely cost data at engineers’ fingertips, letting them proactively manage their cloud costs and overcome limitations of traditional cost management.

CloudZero brings engineering, FinOps, and finance teams together to have complete and accurate visibility into all of their AI and cloud spend, so that they can optimize and ascertain the ROI of their cloud investments through unit economics.

<Callout icon="ℹ️" theme="info">
  Looking to set up your CloudZero account?
  See [Getting Started With CloudZero](/docs/getting-started).
</Callout>

The documentation helps you [set up and configure CloudZero](/docs/cloudzero#cloudzero-configuration), [collect cost data](#collect-cost-data), [analyze cost](#analyze-cost), [allocate cost](#allocate-cost), [detect anomalous spend](#detect-anomalous-spend), [optimize cost and spend in the cloud](#optimize-cost-and-spend), [control spend](#control-spend), and [get visibility into unit economics](/docs/cloudzero#get-visibility-into-unit-economics).

# CloudZero configuration

The [Authentication](https://docs.cloudzero.com/docs/authentication) pages explain how to set up single sign-on to CloudZero from your identity provider. The [Connections](https://docs.cloudzero.com/docs/connections) pages explain how to connect to supported Cost Sources to ingest Billing, Resource, and other types of data into the platform.

Refer to the [Kubernetes](https://docs.cloudzero.com/docs/container-cost-track) pages for information on integrating Kubernetes to combine container usage data with your cloud provider costs. This gives you accurate allocation of costs within a Kubernetes cluster.

The [App integrations](https://docs.cloudzero.com/docs/app-integrations) pages explain how to configure CloudZero to send [notifications](https://docs.cloudzero.com/docs/notifications) to Slack and [integrate with Jira](/docs/jira-integration) so you can create work items from Insights and afterward view the item status within CloudZero.

The [User Management](/docs/user-management) pages explain how to assign roles to users and users to groups, and how to enable single-sign-on for groups.

For Managed Service Providers (MSPs) and others with the need, the [Organization Management](/docs/organization-management) pages explain how to provision and manage several accounts from one centralized location.

# Collect cost data

[AnyCost](/docs/anycost) is the framework that allows you to ingest cost data from any Cost Source established through [Connections](/docs/connections), and automate the processing of that data. AnyCost uses the standard Common Bill Format (CBF) data model to ingest cost data, and enables you to build customer Adaptors for Cost Sources, to bring in costs in addition to those supported.

# Analyze cost

[Analytics](/docs/analytics) provide the capability for you to view, share, and act on your cost data on standard or custom Dashboards, which are saved queries displayed as visualization or text tiles together on one page.

A [Dimension](/docs/dimensions) provides a way to make costs visible so you can use the [Explorer](/docs/explorer) to view and explore your cloud bill by filtering and grouping your charges based on different Dimensions, and to keep users updated about spend through [Views](/docs/views). CloudZero provides Core Dimensions and you can define Custom Dimensions using the [CostFormation Definition Language](/docs/cost-formation-definition-language).

You can create and examine [Views](/docs/views) to help decentralize cost management in your engineering organization by providing targeted cost visibility to individual teams. Each View includes a Principal Dimension, at least one Filter to refine the costs displayed, and a connection to a notification channel, Slack or email.

# Allocate cost

Use the [CostFormation Definition Language](/docs/costformation-allocating-shared-costs) to create Allocation Dimensions, a type of Custom Dimension that can be based on rules or telemetry. Rules include an `AllocationMethod`, the `SpendToAllocate`, and how the cost will be split `AcrossElements`. Telemetry refers to a data stream from records you create of operations on an element in a Dimension. Allocation Dimensions keep costs visible in the same ways as other Custom Dimensions.

# Detect anomalous spend

[Anomaly Detection](/docs/anomaly-detection) finds and flags abnormal spend events based on your billing data, down to hourly granularity. To see Anomalies, use the new **Anomalies** option in the CloudZero top navigation. For more information, see the [Optimize](/docs/optimize) documentation.

# Optimize cost and spend

The Optimize feature is available on the CloudZero top navigation. There are three tabs: **Overview**, **Recommendations**, and **Insights**. Insights provide recommendations that will help you save money or avoid costs by addressing the issues including in the Insight. For more information, see the [Optimize](/docs/optimize) documentation.

# Control spend

You can create a [Budget](/docs/budgets) form in  format based on a [View](/docs/views) to track costs against business metrics. After you populate the form, you can upload the budget into CloudZero. Budgets can provide [notifications](/docs/notifications) when spending does not adhere to the budget.

You can use the Events API to send records of [Engineering Events](/docs/engineering-activity-correlation)  to CloudZero. An example of an Engineering Event is the use of an active feature in continuous integration that has an impact on cost. You can view these events in the [Explorer](/docs/explorer) with a graph that correlates your event to costs.

# Get visibility into Unit Economics

You can set up and monitor [Unit Cost Analytics](/docs/unit-cost-analytics) to implement Unit Economics by capturing and reporting the total cost of a specified metric for the business. Unit Economics measures the direct revenues and costs associated with a particular business model unit, such as per customer, per transaction, or per user, to determine the profitability and scalability of that unit. This determination helps with understanding the efficiency and effectiveness of a system.

<br />
