---
title: Budgets
category: features
createdAt: '2022-03-30T14:34:33.610Z'
hidden: false
slug: budgets
updatedAt: '2022-03-30T18:37:01.407Z'
---
Budgets enable you to track spend against important business metrics and optionally notify the right people when something goes off track.

Each Budget includes:

* A link to a [View](doc:views), which determines the spend tracked by the Budget and the teams notified.
* A name that is unique within each View.
* A set of planned limits that associate a month with an amount of spend.
* Optionally, a set of alerts that determine the when to notify your teams.

If you have the necessary permissions, you have access to your organization’s Budgets at [https://app.cloudzero.com/budgets](https://app.cloudzero.com/budgets).

When the Budgets page opens, you will see that the page as these main areas:

* Left column containing a list of Budgets grouped by the View they belong to.
* Sidebar on the right containing a detailed view of a given budget for the currently selected View.

# Select a View

To change the active View in the right sidebar, click on the **box** in the **Budget Listing** that represents the **View** containing the Budgets you are interested in.

## Select a Budget

After you select a **View** in the **Budget Listing** in the left column, the View populates the right sidebar. By default, the first budget represented under the View will be the one selected. You can switch budgets using the **budget selector** at the top of the right sidebar, under the View name.

## Share Views and Budgets

After you have selected the View and Budget you wish to share, copy the URL of the page and send it to anyone with whom you need to share it.

# Create a Budget

To create a Budget, you must generate a CloudZero Budget Form. You can begin generating your Budget Form from different places on the Budgets page:

* Click the **Edit Download Budgets** button at the top of the page, OR
* Click the **Set Budget for this View** button under a View with no Budgets.
  After you select a View with no Budgets, click the **Set a Budget** button in the right sidebar.

Either action opens a modal where CloudZero collects some basic information about your Budget, including:

* The **Views** for which you would like to add or update Budgets.
* Whether you want to add or update a **Budget**, **forecast**, or both for each View.
  Note that forecasts behave just like budgets. Their purpose is to allow you to track your projections separately from your plans.
* **Start Month** and **End Month** for the Budgets you wish to add or update.
  Note you are limited to editing two years of Budgets at a time.

When your form is complete, click the **Download CSV** button, which triggers a download of your new Budget Form.

# Update a Budget

The Budget Form is generated as a CSV (comma separated value) spreadsheet. You can open it with any common spreadsheet tool (Microsoft Excel, Apple Numbers, Google Sheets, and so on).

When you download the spreadsheet, the Budget Form is already properly formatted for you with a table that has Views and Budgets listed vertically on the left, and the months listed horizontally as column headers across the form.

To update your budgets, put in the dollar amount that you wish to track against for each month in the row corresponding to the budget you wish to update. Do not edit any cells in the spreadsheet other than those in the table.

To set an alert to receive a Notification when the budget reaches 80% or 100% of spend enter **Y** in the appropriate cell as shown above. Set to **N** to turn off Notifications for that budget. Budget alerts will use the Notification channel set in the View settings.

<Image align="center" alt="Set Budget Alerts" border={false} src="https://downloads.cloudzero.com/documentation/resources/budgets-csv-example.png" />

When you are happy with your Budgets, save your Budget Form as a CSV file.

# Upload a CloudZero Budget Form

When you have completed filling out your Budget Form, return to the CloudZero app and on the Budgets, page click the **Upload Budgets** button at the top of the page. This opens a modal containing a drag and drop interface for uploading your Budget Form CSV file. You can also click into the box to use a file explorer selection interface.

When your file is selected, CloudZero will validate it and create your Budgets. If your document is invalid, CloudZero will let you know which row the error occurred in.

# Delete a Budget

To delete a Budget, select the Budget you intend to delete, click the vertical three-dot menu, and select and confirm **Delete Budget**.

<Image align="center" alt="Delete Budget" border={true} width="2848" src="https://files.readme.io/885f222-budget_delete.png" className="border" />
