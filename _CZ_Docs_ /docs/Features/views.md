---
title: Views
category: features
createdAt: '2020-04-14T01:50:43.146Z'
hidden: false
slug: views
updatedAt: '2024-11-06T16:38:31.562Z'
---
Views help decentralize cost management in your engineering organization by providing targeted cost visibility to individual teams. An example of the Views page follows, listing available **Views** for a **team** and showing the **Name**, **Group By (Principal Dimension)**, **Filters**, and **Connections** for the selected View.

<Image align="center" alt="List of Views on the Views page" border={true} src="https://downloads.cloudzero.com/documentation/resources/views-page-list.png" className="border" />

Each View includes the following:

* A **Principal Dimension** to group costs by
* At least one **Filter** to filter costs by
* A Slack and/or email **Connection** (notification channel)

After a View has been defined, CloudZero automatically monitors costs and anomalies corresponding to the View's **Principal Dimension**, filtered by the View's **Filters**. CloudZero then sends [Notifications](/docs/notifications) to the defined **Connections**.

<Callout icon="ℹ️" theme="info">
  View Notifications are sent to email addresses, a Slack channel, or both.

  You can enter multiple email addresses to receive notifications, or use an email alias, such as `feature_team@yourcompany.com`, to manage the recipient group. To ensure you receive notification emails, you must allow emails from `cloudzero.com` and `hello.cloudzero.com`.

  For details concerning the Notifications sent and their frequency, see the [Notifications](/docs/notifications) page.

  CloudZero provides global Notifications as well as Notifications from Views.
</Callout>

# Global Views

By default, every organization has a Global View that is mapped to the entirety of your cloud spend.

<Image align="center" alt="Global View highlighted on the Views page" border={true} src="https://downloads.cloudzero.com/documentation/resources/views-page-global-view.png" className="border" />

The **Principal Dimension** of the Global View determines how CloudZero displays your data in other parts of the platform, such as [weekly and monthly trend Notifications](/docs/notifications) and the [CloudZero Dashboard](https://app.cloudzero.com/dashboard).

You can change the **Principal Dimension** of the Global View to the Dimension most relevant to you, such as `Service`, `Product`, `Customer`, and so on. However, because the Global View includes all cloud costs, you cannot assign **Filters** to it.

You can also edit the Global View **Connections** to change where organization-wide Notifications and Anomalies are delivered.

# Examine Views

Users with the necessary permissions can examine their organization's Views by navigating to the [Views page](https://app.cloudzero.com/team-views) in CloudZero.

Select a View to display its details:

* Name
* Group By (Principal Dimension)
* Filters
* Connections

<Image align="center" alt="Engineering Team Leonardo View selected showing its details" border={true} src="https://downloads.cloudzero.com/documentation/resources/views-page-view-details.png" className="border" />

# Create Views

You can create additional Views to deliver cost Notifications for a subset of your cost to the teams responsible for those costs.

To create a new View, navigate to [Settings > Views](https://app.cloudzero.com/team-views) and select **Create View** at the top right of the page.

<Image align="center" alt="Select the Create View button to create a new View" border={true} src="https://downloads.cloudzero.com/documentation/resources/views-page-create-view.png" className="border" />

The **Create a View** form opens.

<Image align="center" border={true} width="500px" src="https://files.readme.io/8bd242e42ac88f33c418d136ba715f3573382eea2d12532888dbfac142f5b3f9-views-create-view-1.png" className="border" />

Follow these steps to complete the form:

1. Enter a **View Name**.

2. **Select a Dimension to filter on** from the **Filters** drop-down menu. For example, you could choose to filter costs by a custom `Engineering Team` Dimension.

   <Callout icon="ℹ️" theme="info">
     Views do not support filtering by Resource or Resource Summary.
   </Callout>

3. Select one or more elements to add to your filter from the **Select elements to add to your filter** drop-down menu. For example, if you selected the `Engineering Team` dimension, you could select the `Team Alpha` element to show only costs associated with the engineering team Alpha.

4. Repeat steps 3 and 4 as needed to add any number of Dimensions and elements you wish to further refine the View.

5. Select a Dimension to group costs by from the **Group by (Principal Dimension)** drop-down menu. The principal Dimension determines how CloudZero displays data in the Explorer when the View is selected.

   Toggle the **View Anomalies** setting (shown following these steps) to enable or disable anomaly detection for this View (enabled by default).

6. If you enabled anomaly detection, set the threshold (scroll down on the form) to either **Automatic** or **Manual**:
   * **Automatic:** CloudZero automatically sets the threshold for identifying anomalies based on this View's spend:

     | 30 Day Spend                            | Threshold |
     | --------------------------------------- | --------- |
     | Less than or equal to $100.00           | $5.00     |
     | Between $100.00 and $1,000.00           | $10.00    |
     | Between $1,000.00 and $10,000.00        | $25.00    |
     | Between $10,000.00 and $50,000.00       | $75.00    |
     | Between $50,000.00 and $250,000.00      | $100.00   |
     | Between $250,000.00 and $1,000,000.00   | $150.00   |
     | Between $1,000,000.00 and $5,000,000.00 | $250.00   |
     | Greater than $5,000,000.00              | $500.00   |

   * **Manual:** You define the threshold for identifying anomalies based on this View's spend. If you select **Manual**, enter a percentage of the average daily spend over the last 30 days. For example, `50` would trigger an anomaly if total daily spend for the View increases by 50% (such as increasing from $1,000 to $1,500).

7. In the **Notification Channel** section (shown following these steps), select at least one Notification channel:
   * **Slack Channel ID:** Enter the ID of the Slack channel that CloudZero should send Notifications to. You must connect CloudZero to Slack first. For details, see [Enabling Slack Integration](/docs/enabling-slack-integration). You can specify only one Slack channel.
   * **Email Address:** Enter the email address or addresses that CloudZero should send Notifications to. You can use an email alias, such as `feature_team@yourcompany.com`, to manage a recipient group. To ensure you receive notification emails, you must allow emails from cloudzero.com and hello.cloudzero.com.

8. Select **Save**.

CloudZero starts watching the specified set of features and sends cost updates and anomalies to the selected Slack channel and email address or addresses.

# Edit Views

To modify the name, filters, or notification channels of a View:

1. Navigate to [Settings > Views](https://app.cloudzero.com/team-views) and select the `...` (three dot) overflow menu on the View you want to edit.
2. Select **Edit**.
3. Change the View settings as needed.
4. Select **Save**.

# Edit the Global View

CloudZero allows you to edit the Global View as follows:

* Change the principal dimension that all costs are grouped by.
* Enable or disable View anomalies.
* Change the anomaly threshold, if enabled.
* Configure notification channels.

<Callout icon="ℹ️" theme="info">
  You cannot assign filters to the Global View.
</Callout>

# Delete Views

To delete a View:

1. Navigate to [Settings > Views](https://app.cloudzero.com/team-views) and select the `...` (three dot) overflow menu on the View you want to delete.
2. Select **Delete**.

CloudZero immediately deletes the View. No confirmation is required.

# Explore Views

You can see the cost and trends of a particular view [within the Explorer](/docs/explorer#selecting-a-view).
