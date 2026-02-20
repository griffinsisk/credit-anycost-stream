---
title: Anomaly Detection
category: features
hidden: false
slug: anomaly-detection
---
The Anomaly Detection feature uses your cloud billing data to detect and flag abnormal spend events down to an hourly granularity. To view a list of Anomalies, use the Anomalies link in the CloudZero main navigation.

You can preset thresholds to be alerted through Budgets and get Notifications of trends on a weekly basis. Anomaly Detection alerts the Slack channels and emails associated with a View about spikes in spend that have not been seen through historical trends. Unplanned and sudden spikes in spend can become costly if they go unnoticed. Anomaly Detection can help reduce and prevent unplanned expenses on events such as bugs in new deployments, tests that have been forgotten, and other unplanned and accidental situations.

# How Anomaly Detection works

Anomaly Detection is automatically enabled across your CloudZero account and all views using Real Cost data. For more details, see [Real Cost](doc:explorer#real-cost) in the Explorer. Anomaly Detection checks globally across the Cloud Provider Dimensions of `Accounts`, `Service`, and `Usage Family`. In addition for each View that is created, Anomaly Detection is enabled for that subset of data.

The Cost impact for detected Anomalies is the difference between what the model calculates the expected cost to be and what the cost actually is over the Anomaly period.

Anomaly Detection is enabled by default for all Views. You can disable Anomaly Detection for a specific View by editing the View. Toggle the View Anomalies switch to disable Anomaly Detection. For more information, see [editing Views](doc:views#edit-views).

<Image align="center" alt="Anomalies opt-out toggle" border={true} src="https://downloads.cloudzero.com/documentation/resources/anomalies-disable.png" className="border" />

# Anomaly Detection Thresholds

An Anomaly Threshold is the minimum amount that the spend must exceed to be considered an Anomaly.

By default, the automatic Anomaly Threshold is enabled to determine if anomalous spend is found globally or within any Views. To further refine the threshold for Views, you can set a manual threshold as a percentage of the View's daily spend.

<Callout icon="ℹ️" theme="info">
  In addition, Anomalies are generated against accounts, services, and product family. These cannot be turned off as they are not connected to the Global View. The notifications are sent to any user with the necessary permissions who has not disabled their email notifications, which also include weekly and monthly trend notifications. For more information, see [Anomaly Alerts](/docs/anomaly-detection#anomaly-alerts).
</Callout>

## Automatic Anomaly Threshold

Automatic thresholds look at a sliding scale based on the previous 30 days of spend. The following table outlines the default thresholds for various levels of spend in the 30-day window.

<Callout icon="ℹ️" theme="info">
  For Global Anomalies, the 30-day spend is total cloud spend. For View Anomalies, it is total View spend
</Callout>

|               30 Day Spend              | Threshold |
| :-------------------------------------: | :-------: |
|               \<= $100.00               |   $5.00   |
|      Between $100.00 and $1,000.00      |   $10.00  |
|     Between $1,000.00 and $10,000.00    |   $25.00  |
|    Between $10,000.00 and $50,000.00    |   $75.00  |
|    Between $50,000.00 and $250,000.00   |  $100.00  |
|  Between $250,000.00 and $1,000,000.00  |  $150.00  |
| Between $1,000,000.00 and $5,000,000.00 |  $250.00  |
|             > $5,000,000.00             |  $500.00  |

## Manual Anomaly Threshold

<Callout icon="ℹ️" theme="info">
  Setting a manual threshold is available only for View Anomalies. Global Anomalies use the automatic Anomaly Threshold.
</Callout>

You can set thresholds for each View manually to override the default thresholds. To edit thresholds, you must have the necessary permissions on your account. Set a manual threshold as follows:

1. Navigate to **Views** under the **Settings** tab in the left navigation.
2. On the View for which you want to adjust the threshold, click the three dots and then select **Edit**.
3. Scroll down to the **Threshold** section and select **Manual**.
   ![](https://downloads.cloudzero.com/documentation/resources/anomalies-thresholds-v2.png)
4. Enter a percentage of the View’s spend.
   This percentage represents a percentage of the average daily spend over the last 30 days, and is applied to the individual elements of the principal Dimension. An Anomaly will be triggered on an individual element if the spend increase over 24 hours is equal to or greater than the manual threshold. For example, a View with $1000 of daily spend set to 50% would have a threshold of $500. This would trigger an Anomaly if the spend for an individual element in the View's principal Dimension increases by $500 over 24 hours. However, if the Dimension is Teams, an Anomaly would be triggered if Team A increases from $300 to $800 (+$500 over a 24 hour period).
5. Click **Save**.

# View Anomalies

You can view Anomalies on the [CloudZero homepage](https://app.cloudzero.com) and from the top navigation, in the [Explorer](https://app.cloudzero.com/explorer), and in [Anomaly Alerts (Notifications)](https://docs-beta-cz.r/docs/anomaly-detection#anomaly-alerts).

## View Anomalies from the top navigation

When you select **Anomalies** from the top navigation, a list of your Anomalies opens.

When you click an **Anomaly**, a details page opens with an **Overview** and a **Comments** tab.

The **Overview** includes a graph, a **Description**, **Actions** to change the **Status** and select the level of **Effort**, `Low`, `Medium`, or `High`, and **Integrations**, for example, **Create Jira Work Item**.

A list of the affected **Resources** is also provided.

## View Anomalies on the homepage

The main Dashboard on the homepage provides an overview of the total number of Anomalies in the past 30 days and the total cost of detected Anomalies in the last 30 days. Click on an Anomaly next to the pie chart to open the details page for that Anomaly.

<Image align="center" alt="Anomalies homepage display" border={true} src="https://files.readme.io/1ab4800a17ae96dbb21288874a0b4d849c39dcec82758e5e14e3b22b508c0b93-2025-10-Anomalies-homepage-display.png" className="border" />

## View Anomalies in the Explorer

The Explorer view of Anomalies provides granular details about the Anomaly. To see Anomalies when you are in the Explorer, select **Anomalies & Events** and select the **Anomalies** tab.

When you select an Anomaly, it expands with more details.

Change your time granularity to **Hourly** when possible for a precise identification of when the Anomaly was detected.

<Image align="center" alt="Anomalies display in the Exlporer" border={true} width="600px" src="https://files.readme.io/fcb148580e0844303ceb254a20203c44e0a2ef1a9c2b92efce26861398768915-2025-10-Anomalies-Explorer-display.png" className="border" />

# API and Exports

You can export anomalies to a `CSV` format file using  the **Export as CSV** button on the Anomalies page or on the detail page for the Anomaly. Anomalies are also available through API at the [/v2/insights](https://docs.cloudzero.com/reference/getinsights) endpoint.

# Anomaly Alerts

By default Anomaly Detection alerts are sent by email to all Admin users in your organization and can be updated in the View settings for `Global View`. You can also create a view to deliver Notifications directly to relevant teams. For details, see [Creating Views](https://docs.cloudzero.com/docs/views#creating-views). The notifications can be delivered to an email address or Slack channel. To learn more about enabling Slack notifications, see [Slack Integration](https://docs.cloudzero.com/docs/enabling-slack-integration).

When an Anomaly is detected, a Notification will be sent once. The system will not continue to send Notifications on the specific Anomaly to prevent noise and spamming users.

<br />
