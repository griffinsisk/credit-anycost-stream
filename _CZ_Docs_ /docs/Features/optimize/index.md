---
title: Optimize
deprecated: false
hidden: false
metadata:
  robots: index
---
The Optimize feature continually analyzes your environment and automatically generates **Recommendations** that will help your organization save money and avoid costs. Optimize collects the information for Recommendations from a variety of sources, including billing and usage data, resource utilization, and configuration detail. Each Recommendation contains observations about unexpected costs, further insight into affected resources, and specific suggestions for optimization.

The Optimize feature also supports user-created <Anchor label="**Insights**" target="_blank" href="#insights">**Insights**</Anchor>, which allow you to track cost trends or optimizations that you identify in your environment.

<Callout icon="ℹ️" theme="info">
  All of your Insights are on the <Anchor label="Insights" target="_blank" href="https://app.cloudzero.com/optimize/manual-insights">Insights</Anchor> tab on the <Anchor label="Optimize" target="_blank" href="https://app.cloudzero.com/optimize/overview">Optimize</Anchor> page. To see Anomalies, select <Anchor label="**Anomalies**" target="_blank" href="https://app.cloudzero.com/anomalies">**Anomalies**</Anchor> in the CloudZero top navigation.
</Callout>

# Optimize Overview

To discover all the different optimization opportunities across your environment, select <Anchor label="**Optimize**" target="_blank" href="https://app.cloudzero.com/optimize/overview">**Optimize**</Anchor> from the CloudZero top navigation. This will display the Optimize **Overview** tab.

## Summary of Costs, Potential Savings, and Recommendations

The Optimize **Overview** tab highlights your optimization opportunities, showing your total spend over the past 30 days, the total monthly potential savings, and the number of open Recommendations.

You can group the open Recommendations by different Dimensions, such as Account, Region, or Service, including Custom Dimensions your organization has defined, such as Team or Product.

The Recommendations you'll see depend on your role and the specific data access filters that have been applied. For example, if your role has access to a single account, only Recommendations associated with that account are shown.

## Realized Savings

On the Optimize **Overview** tab, you can track the savings realized from Recommendations that have been addressed. The total **Realized Savings** is a sum of all the savings for all of the Recommendations that have been marked as **Addressed**, either manually by a user or by automatic detection. CloudZero calculates the realized savings for all addressed Recommendations on a daily basis.

To view the Realized Savings for a given time range, scroll to the **Realized Savings** block, select the **date picker**, and enter a **custom time range** or select from the options, for example, the last thirty days of last year. To break down the savings by different Dimensions, for example, account or service, choose the **Dimension** from the **Group By** selector.

The following explains how the value of Realized Savings is calculated.

### Realized Savings Definitions

* `X`: The number of days since a recommendation has been **addressed**.
* `Y`: The number of days since a recommendation has been **addressed**, up to a maximum of 30.

### Realized Savings Calculation

Realized savings are calculated by comparing the initial `30-day cost impact` of a resource against its `30-day cost impact on day X`. This difference is then divided by `Y` to determine the average daily cost impact.

### Realized Savings Example

Consider a resource with an initial daily cost impact of `$100` (or `$3,000 over 30 days`). If a change is made that reduces this cost impact to `$0`, the Realized Savings over time would be as follows:

| 30-day cost impact before action | X   | Y  | Last 30-day cost impact on X | (Daily) Realized Savings |
| -------------------------------- | --- | -- | ---------------------------- | ------------------------ |
| $3,000                           | 0   | 0  | $3,000                       | $0                       |
| $3,000                           | 1   | 1  | $2,900                       | $100                     |
| $3,000                           | 5   | 5  | $2,500                       | $100                     |
| $3,000                           | 10  | 10 | $2,000                       | $100                     |
| $3,000                           | 30  | 30 | $0                           | $100                     |
| $3,000                           | 100 | 30 | $0                           | $100                     |

# Recommendations

CloudZero uses **Recommendation Types** to identify optimization opportunities across your cloud environment. A **Recommendation Type** is a specific pattern or rule that CloudZero evaluates (for example, [Fix Lambda Function with Excessive Error Rate](/docs/aws-lambda-functions-with-high-error-rates)). When CloudZero detects a resource matching a Recommendation Type's criteria, it generates a **Recommendation**, which is a specific instance identifying an affected resource and the potential savings from addressing it.

For example, if you have two AWS Lambda functions with excessive error rates, CloudZero would generate two separate Recommendations based on the same Recommendation Type.

The CloudZero platform automatically creates Recommendations for [AWS](/docs/aws-recommendations), [Azure](/docs/azure-recommendations), and [GCP](/docs/gcp-recommendations) from observations across all of your cloud spend. Recommendations will have the `Source` field set to `CloudZero` with a cost impact, title, and description specific to the potential savings identified.

To view details about your recommended actions, select the <Anchor label="**Recommendations**" target="_blank" href="https://app.cloudzero.com/optimize/recommendations">**Recommendations**</Anchor> tab or drill down from the **Overview** visualizations into a specific subset of Recommendations.

In the Recommendations tab, you can do the following:

* [Search](#search-recommendations) Recommendations.
* [Filter](#filter-recommendations) Recommendations by one or more Dimensions.
* [Group](#group-recommendations) Recommendations by a single Dimension.
* [Choose the columns](#choose-recommendation-table-columns) shown in the Recommendation table.
* [View details](#view-recommendation-details) for a single Recommendation.
* [Take action](#take-actions-on-recommendations) on one or more Recommendations.
* [Manage](#manage-recommendation-types) Recommendation Types **(beta)**.

## Search Recommendations

To search for Recommendations, click the **search text field** above the table that lists the Recommendations and type your query.

Search looks for Recommendations across your entire environment and matches the Recommendation ID, terms such as the title, and any other properties in the table of Recommendations.

## Filter Recommendations

You can use filters to see only the Recommendations you need to review. You can apply filters to most Dimensions in CloudZero and filter by most Recommendation properties. You can also apply different operators such as `is` or `is not` filters and combine filters to `show all`.

To apply a filter:

1. Click the **Add Filter** button above the table.
2. To find the filter you want to apply to the current list of Recommendations, navigate through the filter menu or use text search.
3. Click the filter that you want to apply.

You can filter by the following Dimensions in CloudZero:

* **Account**: The IDs for the cloud account where the Recommendation’s resource is located; for example: `Azure subscription ID`, `GCP project ID`, `AWS account ID`.
* **Category**: The type of Recommendation, for example, optimization.
* **Cloud Provider**: The cloud providers where the given Recommendation’s resource is located; for example: `AWS`, `GCP`, `Azure`.
* **Effort**: How much effort is required to address the Recommendation: `Low`, `Medium`, or `High`.
* **Insight ID**: Unique identifier for the type of Recommendation.
* **Potential Savings**: The current expectation of the potential savings from addressing the Recommendation. The amount of potential savings is calculated based on real cost against a projected 30 day window. This value does not indicate a guaranteed amount of savings, as different approaches to address the Recommendation may result in different amounts of savings.
* **Region**: The cloud region where the Recommendation’s resource is located.
* **Resource Name**: The resource name associated with the Recommendation.
* **Resource Type**: The resource type for the given Recommendation’s resource; for example, `BigQuery: job` or `S3: bucket`.
* **Service**: The cloud provider service type for the given Recommendation’s resource.
* **Source**: The source of the Recommendation; for example: `CloudZero`.
* **Title**: A short statement describing the recommended action.
* **Work Item**: The Jira work item associated with the Recommendation.

<Callout icon="ℹ️" theme="info">
  If you would like to filter by additional CloudZero Dimensions, reach out to your FinOps Account Manager.
</Callout>

### Use Quick Filters

You will see default quick filters above the table that apply filters for the Recommendations as follows:

* **Open**: Display recommendations with a status of either `Not Started` or `In Progress`.
* **Addressed**: Display Recommendations with a status of `Addressed`. These Recommendations can have a status of `Addressed` due either to manual action or to automatic detection based on continual analysis by CloudZero of the Recommendations.
* **Ignored**: Display Recommendations with a status of `Ignored`.

## Group Recommendations

In the Recommendations table, you can group Recommendations by any of the properties. Select **None** if you want to remove all groupings. This is especially useful when you are applying ordering and filters. When a `group by` has been applied, sorting by a property will affect all Recommendations listed in the group.

Beside each group, you will see the total potential savings for all Recommendations in the group.

## Choose Recommendation Table Columns

To choose the properties to display on Recommendations in the table, select the **Columns** button above the table.

This is different from filters; filters refine the list to show only Recommendations with certain properties, while the **Columns** option shows all Recommendations but hides or shows columns in the Recommendation table.

Columns include all the enabled CloudZero Dimensions.

## Take Actions on Recommendations

To display the **action bar** above the table, select a Recommendation or a set of Recommendations. From the action bar, select the action that you want to take.

* **Change Status**: Change the status for the selected Recommendations. The status helps manage a workflow for the Recommendations.
* **Change Effort Level**: Change the effort level for the selected Recommendations. This field indicates how much effort, `Low`, `Medium`, or `High`, is required to address the Recommendation. Each Recommendation contains a default value for the required effort level.
* **Post Comment**: Post a comment about the selected Recommendations.

## View Recommendation Details

Select a Recommendation to open a side panel with additional detail and context about the Recommendation.

* In the **Overview**, you can review the description of the Recommendation, which explains how a Recommendation was generated and the steps in remediation to take in order to realize the potential savings. There is a graph displaying the real cost over the past 30 days for the associated resource(s). You can select **View in Explorer** to open a new tab and interact with cost data through the **Explorer**.
* In the **Resource Details**, you can review additional configuration details and tags associated with the resource.
* In **Activity**, you can view all actions taken against the Recommendation, such as when a Recommendation was created or who changed a status. Comments are also included inline, and you can view, add, edit, and delete comments to help facilitate discussions about how best to act on the Recommendation.

## Manage Recommendation Types

<Callout icon="ℹ️" theme="info">
  The Optimize Settings feature is in **beta**. To request access, contact your FinOps Account Manager or Customer Success representative.
</Callout>

You can control which Recommendation Types are evaluated for your organization through the **Optimize Settings** panel **(in beta)**. When you disable a Recommendation Type, CloudZero stops evaluating it and hides existing Recommendations of that type. Changes take effect during the next daily analysis cycle.

To manage Optimize Settings, click **Settings** in the upper-right corner of the Optimize page. The list of **Recommendation Types** that appears allows you to:

* **View enabled and disabled Recommendation Types**: See a list of all Recommendation Types available, and within that list, which ones are enabled or disabled for your organization.
* **Enable or disable Recommendation types**: Click a checkbox to enable or disable which Recommendation Types run against your organization, then click **Save**.
* **Search**: Find Recommendation Types by name. The search is case-insensitive and supports partial matches. For example, you can search for `rds` to see all of the available Amazon RDS Recommendation Types. This searches all available Recommendation Types (whether enabled or disabled).

<Image align="center" alt="Recommendation Types settings panel" border={true} width="75% " src="https://files.readme.io/1aa41aaabb196d3a63f716b16d4a75a256e594d8561a0c4712e46aa99a961510-optimize-recommendation-settings-search.png" className="border" />

Note that Optimize Settings only shows Recommendation Types for providers you have connected to CloudZero. If you do not have a Microsoft Azure connection, for example, you will not see Recommendations for Azure.

<Callout icon="ℹ️" theme="info">
  To manage Recommendation Types, you must have a [role](/docs/view-and-manage-roles) that grants Read and Write permissions for Optimize.
</Callout>

# Insights

**Insights** are user-generated observations on cost trends or optimizations in your environment. You create Insights in the **Explorer** and they are displayed on the <Anchor label="**Insights**" target="_blank" href="https://app.cloudzero.com/optimize/manual-insights">**Insights**</Anchor> tab.

To create an Insight:

1. Navigate to the **Explorer** and select **Create Insight**.
2. Enter a title, description, and category, and optionally a cost impact.

The Link to Details will automatically populate with a direct URL to the relevant place in the Explorer.
