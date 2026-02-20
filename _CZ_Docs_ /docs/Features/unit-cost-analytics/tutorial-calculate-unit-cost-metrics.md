---
title: 'Tutorial: Calculate Unit Cost by Creating a Telemetry Stream'
category: features
createdAt: '2024-09-23T19:40:03.416Z'
hidden: false
slug: tutorial-calculate-unit-cost-metrics
updatedAt: '2024-10-25T19:40:03.416Z'
---
Suppose you work at a food delivery company called EatIn. You have connected your cloud provider account to CloudZero, and now you want to determine how best to optimize your cloud costs, as described in [What Is Cloud Unit Economics (CUE)? A Comprehensive And, More Importantly, Fun Guide](https://www.cloudzero.com/guide/cloud-unit-economics/). One way to do that is by calculating a **unit cost**: a system of using objective measurements to ensure your business is maximizing profit when delivering and developing cloud-based software and services.

To define a [unit cost](/docs/unit-cost-analytics), you calculate `consumption divided by demand driver`.

In this case, the consumption is your **cloud spend** for operating EatIn. The demand driver is the **number of orders** EatIn processes. Thus, one unit cost you can track is **cost per order**.

Suppose you have created a [Custom Dimension](/docs/dimensions) to allocate your cloud costs by engineering team as well. You can combine your Custom Dimension with the cost per order unit metric to determine a second unit metric, `cost per order per engineering team`.

This tutorial shows how to calculate unit costs with CloudZero. In this guide, you will take the following steps:

1. [Prepare a CSV file containing cloud usage data](#step-1-prepare-the-data). This tutorial providesthe [example CSV file](https://downloads.cloudzero.com/documentation/resources/example_data.csv).
2. [Upload the CSV file to create a unit cost telemetry stream to send cloud usage data to CloudZero.](#step-2-upload-the-csv-to-cloudzero)
3. [Create an Analytics dashboard to calculate and display your `cost per order per engineering team` unit cost.](#step-3-create-a-dashboard)

Completing this simple tutorial will take about ten minutes. You can take a break during the process while CloudZero loads the unit cost telemetry stream with data from your cloud provider.

The example Analytics dashboard for Unit Cost by Engineering Team illustrates Cost per Order per Engineering Team per day in a bar graph and per month in a bar chart, Total Orders per Day in a line graph, and Cost Allocation by Engineering Team in a pie chart. There are 604,523 total orders per month.

<Image align="center" alt="An analytics dashboard in CloudZero displays unit cost data" border={true} src="https://downloads.cloudzero.com/documentation/resources/uca-cost-per-1k-orders-full-dashboard.png" className="border" />

# Methods of sending data to CloudZero

There are three methods of sending unit cost telemetry data to CloudZero:

1. [Import a CSV file](/docs/csv-import-telemetry) through the CloudZero UI.
2. Send a `POST` request to the [`/unit-cost/v1/telemetry/metric/{metric_name}/sum`](https://docs.cloudzero.com/reference/summetrictelemetry) API endpoint.
3. Email a CSV file to the CloudZero team. Note that email is sent in plaintext, so be mindful of attaching sensitive data. Consider emailing a link through an encrypted file-sharing service.

This tutorial focuses on the first method, importing a CSV file.

# Prerequisites for creating a telemetry stream with a CSV file

* A CloudZero account with the necessary permissions.
* An existing cloud provider connection in CloudZero, for example, [AWS](docs/connections-aws-automated), [Azure](/docs/connections-azure), or [Google Cloud](/docs/connections-gcp-billing).
* An existing [Custom Dimension](/docs/dimensions) named `Engineering Team` to track spending by engineering team. To learn how to create a Custom Allocation Dimension, see [Allocation Dimensions](/docs/costformation-allocating-shared-costs#allocation-dimensions).
* Usage data to calculate the unit cost with. This example provides a sample CSV file with the number of orders attributed to each engineering team for the month of September 2024.

This example uses a Custom Dimension to demonstrate how to refine a unit cost, but you can create a simple unit cost without allocation. For example, if you just wanted to determine `cost per order`, you would not need to define a Custom Dimension.

# Step 1: Prepare the data

An important part of preparing the data is determining which demand driver to track and then collecting its relevant data from system logs, sales systems, or anywhere else the data is sourced.

The demand driver will differ for every organization, but you can learn more about demand drivers in the [What Is Cloud Unit Economics?](https://www.cloudzero.com/guide/cloud-unit-economics/) guide. For more information about gathering demand driver data, see [Common Sources of Unit Cost Telemetry Data](/docs/collecting-unit-cost-telemetry).

This example tracks the number of orders processed by the fictional company EatIn, and we have already gathered the data from EatIn's application logs.

[Download this tutorial's example CSV file](https://downloads.cloudzero.com/documentation/resources/example_data.csv) containing the data required to calculate the unit cost.

The example CSV file includes the following columns:

* Date
* Number of Orders
* Engineering Team

Only a `timestamp` column and `unit value` column are required when creating a unit cost telemetry stream. However, because we intend to filter the costs by engineering team in this example, the file also includes a column where each value is a specific engineering team name. These values match the elements defined in the `Engineering Team` Dimension.

The first few rows of the example CSV file are shown here:

```
Date,Engineering Team,Number Of Orders
2024-09-01,Leonardo,2717
2024-09-01,Raphael,2779
2024-09-01,Michelangelo,6242
2024-09-01,Donatello,3451
```

In summary, each row in the CSV file represents the number of EatIn orders associated with an engineering team for each day in September 2024.

For example, on September 1, 2024, Team Leonardo was responsible for 2,717 orders.

# Step 2: Upload the CSV file to CloudZero

The next step is to create the unit cost telemetry stream by uploading the CSV file to CloudZero.

Log in to CloudZero and navigate to [**Settings** > **Telemetry Streams**](https://app.cloudzero.com/settings/telemetry), then select **Create New Stream **>** New Unit Cost Stream**.

<Image align="center" alt="Select Create New Stream > New Unit Cost Stream" border={true} src="https://downloads.cloudzero.com/documentation/resources/telemetry-csv-create-new-unit-cost-stream.png" className="border" />

Enter a stream name. For this example, use the name `engineering-team-orders`. Be aware that you cannot change the name after creating the stream, so ensure it is correct. If the name is not correct, you must delete the stream and create a new one with the correct name.

Next, enter the stream description: `Number of orders per engineering team per day`. You can change this later from the stream details page, if needed.

In the **Upload CSV** section, set the **Granularity**. A telemetry stream's granularity determines how you track data changes over a period of time. Because the goal is to track changes between orders from day to day, choose **Daily**, which is the default.

Next, select the [`example_data.csv`](https://downloads.cloudzero.com/documentation/resources/example_data.csv) file or drag and drop it into the **Upload CSV File** field. Note that the maximum file size is 3MB.

<Image align="center" alt="Select or drag and drop a CSV file" border={true} src="https://downloads.cloudzero.com/documentation/resources/unit-cost-tutorial-upload-csv.png" className="border" />

In the **Timestamp** section, select **Date** from the drop-down menu. This uses the `Date` column in the CSV file to set the date for each record in the telemetry stream.

In the **Unit value** section, select **Number of Orders** from the drop-down menu. This uses the `Number of Orders` column to set the unit value for each record in the telemetry stream, the number of orders per engineering team per day.

Set the **Target Dimension (Optional)** drop-down selector to the `Engineering Team` Custom Dimension you created as a prerequisite to this tutorial. This associates each engineering team with its number of orders per day, which allows you to allocate cloud cost per order by the Engineering Team dimension.

Set the **Dimension Element** drop-down selector to the column containing each element (team name) in your Dimension. This is the `Engineering Team` column in the sample CSV file. The column name does not need to match the dimension, You can name the column anything you like; however, it is the same as the Dimension name in this example for clarity.

After you configure the unit cost telemetry stream as described, the stream creation page should look like this:

<Image align="center" alt="Review the unit cost telemetry stream configuration" border={true} src="https://downloads.cloudzero.com/documentation/resources/unit-cost-tutorial-stream-configuration.png" className="border" />

Review the **CSV Reference Table** to make sure it looks as you expect it to:

<Image align="center" alt="Review the CSV Reference Table" border={true} src="https://downloads.cloudzero.com/documentation/resources/unit-cost-tutorial-csv-reference-table.png" className="border" />

Finally, click the **Save** button:

<Image align="center" alt="Click the Save button" border={true} src="https://downloads.cloudzero.com/documentation/resources/unit-cost-tutorial-create-stream-button.png" className="border" />

CloudZero redirects you to the [Telemetry Streams](https://app.cloudzero.com/telemetry) page and creates a unit cost telemetry stream according to your specifications.

<Image align="center" alt="The Telemetry Streams page shows the new unit cost telemetry stream" border={true} src="https://downloads.cloudzero.com/documentation/resources/unit-cost-tutorial-created-stream-status.png" className="border" />

Now, select the newly created stream to view its details page.

It can take up to 24 hours for CloudZero to ingest the data for a new telemetry stream, depending on the size of data. Smaller files can be ingested more quickly. While CloudZero processes the data, the details page will look as follows, with the **Status** displayed as `Pending`:

<Image align="center" alt="The Telemetry Streams page shows a unit cost stream in Pending status" border={true} src="https://downloads.cloudzero.com/documentation/resources/unit-cost-tutorial-details-page-pending.png" className="border" />

In addition, you can see the following information on the details page:

* Stream name and description
* Type of stream (`Metric`)
* Granularity (`Daily`)
* Source (`CSV`)
* Targeted dimensions (`Engineering Team`)
* Activity graph
* Last request timestamp
* Start date timestamp
* Recent errors

After CloudZero has finished ingesting the initial stream data, you can hover over the activity graph to see the number of records, requests, and errors processed per day:

<Image align="center" alt="The activity graph shows records processed per day" border={true} width="400px" src="https://downloads.cloudzero.com/documentation/resources/unit-cost-tutorial-activity-graph.png" className="border" />

# Step 3: Create a Dashboard

When the stream's ingest status is shown as **Available**, you can create an Analytics dashboard by navigating to [Analytics](https://app.cloudzero.com/analytics/dashboards) and selecting **Create Dashboard**.

Enter the name **Cost Per Order Per Engineering Team**, and set the visibility to either public (viewable by everyone in your organization) or private.

On the empty Dashboard, click the **Add** button, and then select **Visualization** from the drop-down menu.

In the **Choose an Explore** window, select **CloudZero Billing Data** from the list on the left, underneath your organization ID:

<Image align="center" alt="Select CloudZero Billing Data" border={true} src="https://downloads.cloudzero.com/documentation/resources/unit-cost-tutorial-analytics-choose-explore.png" className="border" />

Replace `Untitled` with the name you plan to use for your visualization: `Cost Per Order Per Engineering Team Per Day`.

Next, select the desired Dimensions and measures to visualize them. Our goal is to show the unit cost per order per engineering team, so expand the field list and select the following fields:

* **Cost Types & Usage > Real Cost**
* **Custom Dimensions > Engineering Team**
* **Unit Metrics > Engineering Team Orders**

Then select **Add calculation**:

<Image align="center" alt="Select Add calculation" border={true} src="https://downloads.cloudzero.com/documentation/resources/unit-cost-tutorial-analytics-add-calculation.png" className="border" />

In **Create table calculation** modal, define the custom expression to calculate the cost per order by engineering team, so you can display it in the visualization. To do this, you instruct CloudZero to divide the total cloud cost by the unit cost, as follows:

1. In the **Expression** field, start typing `base_billing_data.real_cost` and select the **Real Cost $\{base_billing_data.real_cost}** row that appears in the drop-down menu.
2. Add a `/` to indicate division.
3. Start typing the name of the unit cost telemetry stream, `engineering_team_orders`, and select the **engineering_team_orders_12345678901234567890123456789012_unit_metric.metric** dimension that appears in the drop-down menu. Note that the hyphens in the original telemetry stream name are replaced by underscores, so you must use underscores when you type the stream name.)
4. Set **Format** to **U.S. Dollars** and **Decimals** to **2**.
5. Enter a name in the **Name** field.

The expression should look like the following, though your telemetry stream name will be followed by a different ID. This is the expression in the Edit table calculation form shown in the screen image.

```
${base_billing_data.real_cost}/${engineering_team_orders_12345678901234567890123456789012_unit_metric.metric}
```

<Image align="center" alt="The custom expression for the table calculation" border={true} src="https://downloads.cloudzero.com/documentation/resources/unit-cost-tutorial-analytics-custom-expression.png" className="border" />

Click **Save** to save the custom expression.

In the visualization editor, select the column icon from the **Visualization** bar to display the chart as a series of columns:

<Image align="center" alt="Select the column icon" border={true} src="https://downloads.cloudzero.com/documentation/resources/unit-cost-tutorial-analytics-chart-symbol.png" className="border" />

For the chart to be most useful, you can configure it to display only the unit cost and the engineering team. Hide the **Unit Metric Engineering Team Orders** and **Cost Types & Usage Real Cost** columns from the visualization by selecting the **cog** icon next to each one's name and selecting **Hide this field in visualization**:

<Image align="center" alt="Select the cog icon to hide a column" border={true} src="https://downloads.cloudzero.com/documentation/resources/unit-cost-tutorial-analytics-hide-column.png" className="border" />

Finally, click **Save**. The new chart appears on your dashboard:

<Image align="center" alt="The dashboard displays the unit cost per order per engineering team as a chart" border={true} src="https://downloads.cloudzero.com/documentation/resources/unit-cost-tutorial-analytics-finished-chart.png" className="border" />

If you like, you can add more visualizations to further customize your dashboard. When you are done, click **Save** to save the Dashboard.

# Next steps

If you need to add new data or update existing data in your telemetry stream, you can [upload another CSV file](/docs/csv-import-telemetry#update-the-unit-cost-stream). For example, you might decide to add order data for October 2024. Alternatively, you can [send data to the CloudZero API](https://docs.cloudzero.com/reference/summetrictelemetry).

To learn more about unit cost metrics, see the following documentation:

* [What Is Cloud Unit Economics (CUE)? A Comprehensive And, More Importantly, Fun Guide](https://www.cloudzero.com/guide/cloud-unit-economics/)
* [How to Create a Unit Cost or Allocation Telemetry Stream by Uploading a CSV](/docs/csv-import-telemetry)
* [Dimensions](/docs/dimensions)
* [Unit Cost Analytics](/docs/unit-cost-analytics)
* [Creating a Dashboard](/docs/edit-dashboard#creating-a-dashboard)
