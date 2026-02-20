---
title: Explorer
category: features
createdAt: '2020-02-13T19:39:05.331Z'
hidden: false
slug: explorer
updatedAt: '2022-05-03T15:17:57.640Z'
---
Using the CloudZero Explorer, you can view and examine your cloud bill by filtering and grouping your charges based on different Dimensions. The examples on this page refer to the AWS bill. If you have another cloud provider such as Snowflake connected to CloudZero, line items from your bill will be treated similarly.

The AWS bill is a large data file that lists every charge you have accrued. Each charge is a line item, a single line of the bill that specifies the time period that the charge originated from, as well as the service, resource, and consumption type that precipitated that charge. The time period is generally one hour. It cannot be less than an hour in the AWS billing. For services that charge for granularities of less than an hour, AWS will consolidate those charges for entry onto your bill, except for some things like taxes, Reserved Instances, and so on.

An example of a line item might be: you were charged for EC2 network costs on February 25 from 9:00-10:00 UTC, against the EC2 machine with ARN xyz, for a cost of $5.00.

The CloudZero Explorer is a visualization of your bill. At first glance the Explorer may seem similar to the AWS Cost Explorer. However, the CloudZero Explorer aims to augment the AWS tools by giving you more context that is relevant to your business. The Explorer shows Dimensions in an interface that focuses on helping you understand how your cloud costs changed over time and what is driving those costs.

# Cost Graph

The main part of the Explorer shows your cost graph, a graphical representation of your cloud costs (y-axis), over a span of time (x-axis.) You can choose the **Group By** method, The **Time Range**, and the time period to show in the graph.

<Image align="center" alt="Cost graph in Explorer" border={true} src="https://files.readme.io/56aed3fc0354966c4893cc4fbce78f268789773677bc9b79232283518bd01d0d-Explorer_Screenshot_20250827.jpg" className="border" />

In the upper left of the window that displays the graph, the total cost is displayed followed by the absolute and percentage change in cost from the previous time period. These values represent your **Cost of Change**, telling you how much the cost has changed when compared to the same filtered Dimensions in the preceding time period.

For example, if you are viewing all of your EC2 service charges for the last seven days, CloudZero shows you how this cost compares to your EC2 service charges for the seven days preceding that time. Note that the preceding time period is not represented on the chart visualization. The Cost of Change numbers let you see at a glance whether the data you are viewing represents an increase or decrease in spend.

# Cost Types

You can view the following different Cost Types: Billed Cost, Discounted Cost, Discounted Amortized Cost, Amortized Cost, Invoiced Amortized Cost, Real Cost, and On-Demand Cost.

## Billed Cost

Billed Cost reflects the exact prices you will be invoiced for. It is the simplest Cost Type with discounts, Reserved Instance (RI), and Savings Plan (SP) charges represented as distinct line items.

## Discounted Cost

Discounted Cost is similar to Billed Cost, except that any discounts are assigned to the applicable resource and operation usage charges instead of being distinct line items. This includes EDP Discounts, Private Rate Discounts, RI Volume Discounts, and so on.

## Discounted Amortized Cost

Discounted Amortized Cost starts with Discounted Cost but also amortizes any upfront or recurring Reserved Instance (RI) and Saving Plan charges across the resources to which they apply. This amortization is based on the amount of usage and therefore reflects the effective cost, taking into account the reduced rate for RIs and SPs.

<Callout icon="ℹ️" theme="info">
  The following explains Discounted Cost versus Discounted Amortized Cost for Azure Reserved Instances and Savings Plans.

  Azure manages the costs and usage for Reserved Instances and Savings Plans differently from other providers. Due to these differences, total amounts for **Discounted Cost** and **Discounted Amortized Cost** will not match when you are viewing Azure data over a given time frame.

  This may be because Azure provides information about upfront purchases of RIs and SPs only in the month that the purchase was made. In all subsequent months, the only visible costs for an upfront RI or SP will be the amortized usage. For example, if you fully paid upfront for a one year RI in March, the full upfront fee will appear in **Discounted Cost** only when you view the March data. There will be no purchase information when you view the data for April through February. However, when you are viewing **Discounted Amortized Cost**, the amortized usage of that RI will be visible in all months from March through February.

  Another cause for the lack of a match may be that when an RI or SP is billed in monthly installments, the monthly fee is based on the full cost of the agreement divided by the number of months in the agreement, while the daily amortized usage will be based on the full cost of the agreement divided by the number of days in the agreement. Therefore, the monthly fee for an RI will be the same for the months of February and July even though the number of days in each month is different. However, the daily amortized cost of the RI will be different for each of those months.
</Callout>

## Amortized Cost

Amortized Cost is the same as Discounted Amortized Cost but starts with Billed Cost (instead of Discounted Cost) before applying RI and SP amortization.

## Invoiced Amortized Cost

This cost type is supported only for AWS-related costs.

Invoiced Amortized Cost is similar to Discounted Amortized Cost, but only the recurring portion of RI and SP charges are amortized. This ensures that total cost for a billing period reflects only charges incurred in that billing period. Upfront RI and SP charges, either All Upfront or the upfront portion of Partial Upfront, are still represented as separate line items.

## Real Cost

Real Cost starts with Discounted Amortized Cost, but filters it to display only charges directly related to consumption. For example, charges stemming from Taxes and Support will be taken out of this view. For the **GCP provider**, this total will include committed use discount credits. The purpose of this view is to allow engineering teams to understand quickly how their cloud consumption is changing over time. This is the **default view** in the Explorer. Note that the cost for unused portions of RIs and SPs are not represented in this view.

## On-Demand Cost

On-Demand Cost shows what one would pay for equivalent usage of a particular resource absent any special pricing, discounts, or applicable RIs or SPs. The On-Demand Cost is useful for determining the ESR (effective savings rate). For line items that do not have an on-demand rate (taxes, fees, support, and so on) or for which the on-demand rate is unknown, the Billed Cost is used.

<Callout icon="ℹ️" theme="info">
  This cost type is not supported for Azure related costs. Azure does not provide on-demand pricing for all billing line items, making the results for Azure services inconsistent.
</Callout>

# Cost Types and the AWS Cost and Usage Report

The following explains the relationship of Cost Types to the columns on the [AWS Cost and Usage Report](https://docs.aws.amazon.com/cur/latest/userguide/data-dictionary.html).

* **Billed Cost**: equivalent to `lineItem/UnblendedCost`.
* **Amortized Cost**: a combination of `lineItem/UnblendedCost`, `reservation/EffectiveCost`, and `savingsPlan/SavingsPlanEffectiveCost`.
* **Discounted Cost**: equivalent to `lineItem/NetUnblendedCost`.
* **Discounted Amortized Cost**: a combination of `lineItem/NetUnblendedCost`, `reservation/NetEffectiveCost`, and `savingsPlan/NetSavingsPlanEffectiveCost`. In some cases, Discounted Amortized Cost may also include additional discounts not reflected in `lineItem/NetUnblendedCost`.
* **Invoiced Amortized Cost**: a combination of `lineItem/NetUnblendedCost`, `reservation/NetRecurringFeeForUsage`, and the recurring portion of `savingsPlan/NetSavingsPlanEffectiveCost`. The recurring portion of the SP cost is determined from `savingsPlan/NetAmortizedUpfrontCommitmentForBillingPeriod` and `savingsPlan/NetRecurringCommitmentForBillingPeriod`. In some cases, Invoiced Amortized Cost may also include additional discounts not reflected in `lineItem/NetUnblendedCost`.
* **Real Cost**: same as Discounted Amortized Cost but filtered to usage line item types (see `lineItem/LineItemType`).
* **On-Demand Cost**: `pricing/publicOnDemandCost` for any line item that matches the **Real Cost** filter (usage types, excluding Support). For all other cases, or if the `pricing/publicOnDemandCost` is NULL or 0, then `lineItem/UnblendedCost`.

# Change the time range

Use the **Time Range** drop-down menu in the upper left of the Explorer to view data for a specific time period. You can select from predefined views such as **Last 24 Hours**, **Last 7 Days**, **Last 30 Days**, and more or you can select your own start and end dates from the calendar to view a custom time range.

You can also set the granularity of data to **Hourly**, **Daily**, **Weekly**, or **Monthly**. There are several considerations to keep in mind when selecting each granularity option:

* **Hourly**: Hourly granularity is available only when you are viewing less than a week of data.
* **Daily**: Daily granularity is available only when you are viewing more than a day and less than three months of data.
* **Weekly**: Weekly granularity is available only when you are viewing more than a week and less than a year of data. Choosing the Weekly option may result in the selected date range being extended to show full weeks, which may impact the Cost displayed.
* **Monthly**: Monthly granularity is available only when you are viewing more than a month of data. Choosing the Monthly option may result in the selected date range being extended to show full months, which may impact the Cost displayed.

## Partial weeks

In the Explorer, weeks always start on Monday and end on Sunday. If you select a time range that does not begin on a Monday and end on a Sunday, CloudZero displays partial weeks at the start and end of the selected range.

For example, January 2025 began on a Wednesday and ended on a Friday. When you are viewing January 2025 with weekly granularity, the weeks are divided as follows:

* 1/1 to 1/5 (Wednesday - Sunday): partial week
* 1/6 to 1/12 (Monday - Sunday): full week
* 1/13 to 1/19 (Monday - Sunday): full week
* 1/20 to 1/26 (Monday - Sunday): full week
* 1/27 to 1/31 (Monday - Friday): partial week

The following illustrates how partial weeks are displayed in the Explorer, with the first and last weeks of January marked as partial weeks:

<Image align="center" alt="An example of partial week data in the Explorer" border={true} src="https://downloads.cloudzero.com/documentation/resources/explorer-partial-week-example.png" className="border" />

## Partial Months

If you select a time range that does not begin on the first day of a month or end on the last day of a month, CloudZero displays partial months at the start and end of the selected range.

For example, if you select the custom date range of November 15, 2024 to February 15, 2025 and view it with monthly granularity, the months are divided as follows:

* 11/15 to 11/30: partial month
* 12/1 to 12/31: full month
* 1/1 to 1/31: full month
* 2/1 to 2/15: partial month

The following illustrates how partial months are displayed in the Explorer, with the first and last months of the time range marked as partial months:

<Image align="center" alt="An example of partial month data in the Explorer" border={true} src="https://downloads.cloudzero.com/documentation/resources/explorer-partial-month-example-2.png" className="border" />

# Filter and group cloud spend

Cloud bills for most organizations are large enough that looking at them in totality makes it very difficult to answer most questions. A key goal of CloudZero is to help you understand what groups of resources are driving the charges and changes in those charges over time. To do that, much of the Explorer page helps you organize the data in ways you can examine it and then zoom in to parts of your bill by filtering to the things you care about.

## Group by Dimension

Use the **Group By** drop-down menu in the row of controls for the Explorer page to view your cloud cost by a different Dimension.

A **Cost Dimension** is a way to break your cost up into different buckets. CloudZero takes your cloud cost data in and standardizes it to the CloudZero cost data model. Each cloud cost charge has different Dimensions.

`AWS Services` is a classic cost Dimension. You may want to see your cost last month broken down by which services cost what. For example, your $100,000 monthly bill might be broken down into EC2 costs of $80,000 and S3 costs of $20,000. Without changing the overall cost, you could also see that same number broken down into AWS account groupings, with $90,000 cost in your production account and $10,000 cost in your R&D account. Note that these two Dimensions describe the same data. You could further explore the data by using a filter.

<Callout icon="ℹ️" theme="info">
  For Custom Dimensions, the related cost Dimension can be defined as part of the Custom Dimension definition by setting the `Child` property. For more information, see [Defining a Custom Dimension](/docs/costformation-definition-language-guide#/defining-a-custom-dimension).
</Callout>

## Filter Costs

To further explore the data by looking at the cost and corresponding resources that are from the EC2 service and in the production account, set up two filters, one for Services and one for Accounts to view the corresponding values.

To set a filter and only view costs that match that filter, you can use the filter expression builder or click within the cost table.

### Use the filter expression builder

To use the filter expression builder, click the **Add** button to create a new filter expression.

<Image align="center" alt="Add button to add a filter" border={true} src="https://downloads.cloudzero.com/documentation/resources/explorer-filter-add-button.png" className="border" />

Then, choose a **Dimension** to filter on.

<Image align="center" alt="Choose a Dimension" border={true} src="https://downloads.cloudzero.com/documentation/resources/explorer-filter-builder-dimension-selector.png" className="border" />

From here, you can use the drop-down to change the operator from `is` to `is not`or from  `contains` (case-sensitive) to `does not contain` (case-sensitive), or select the values you would like to add to the filter expression. Only one search term is accepted for `contains` and `does not contain`.

<Image align="center" alt="Change operator and values" border={true} src="https://downloads.cloudzero.com/documentation/resources/explorer-filter-choose-value.png" className="border" />

### Click an element to set a filter

The other way to set a filter is to click on an element in the cost table that follows the graph, which will set a filter for that element.

The table that follows the graph displays information about what groups of charges or resources go into the cost represented in the graph. By default, the table shows which elements of the Dimension your spend is grouped by are the most expensive in this time period compared to the previous time period, that is, have the largest Cost of Change. You can click on any of the column headers to sort the data based on that column.

<Image align="center" alt="Changes and resources contributing to the cost" border={true} src="https://downloads.cloudzero.com/documentation/resources/explorer-trend-table.png" className="border" />

## Investigate costs

You can drill down into specific areas to examine your costs more closely. Clicking on a cost Dimension element in the first column will refine your cost data by setting a filter to that element. When the cost table reloads, you will see only costs related to the element that you selected, and the costs will be grouped by a related cost Dimension. You can continue to drill down in the Explorer by clicking on other elements. Eventually the cost table will show your costs grouped by resources.

# Resource Detail and Views

The explorer lets you select a [View](https://docs.cloudzero.com/docs/views). This will set the active `Group By` to the Principal Dimension of the View, and apply the filter of the View. This provides access to the value of your Views within the Explorer.

<Image align="center" alt="Select a View" border={true} src="https://downloads.cloudzero.com/documentation/resources/explorer-select-views.png" className="border" />

When you are looking at your costs by resource, you can click on a resource name in the first column to open the resource detail page for that resource. This page allows you to quickly understand the high level properties and cost of a resource.

<Callout icon="ℹ️" theme="info">
  The majority of information for a resource will be visible on this page only if you have connected the AWS account it resides in.
</Callout>

The information on this page is organized into several sections:

**High level information**: at the top of the page you can see the resource's ARN, account, when CloudZero last saw a property on that resource change, and other information such as region it resides in.

**Cost graph**: Much like the Explorer, you can view cost information for this specific resource. Note that you can change the time span and group by options on the top right of this page.

**Tags**: Tag information follows, with all tag key values displayed for this resource.

**Additional properties**: The CloudZero app will scrape additional properties of this resource to help you understand how it is currently provisioned.

**Resource relationships**: If the CloudZero app has seen this relationship interact with other resources, those resources will be described here with links to them.

**Resource diff**: If the CloudZero app has seen a property of this resource change, the last change in properties will be displayed at the bottom of the page.
