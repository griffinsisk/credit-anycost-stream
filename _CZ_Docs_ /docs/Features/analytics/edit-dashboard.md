---
title: Creating and Editing Dashboards
category: features
hidden: false
slug: edit-dashboard
---
CloudZero [Analytics](https://app.cloudzero.com/analytics/dashboards) provides customers with self-service cloud cost Analytics. Users with the necessary permissions can create and edit Dashboards to share with the rest of their organization. They can also [create folders for organizing Dashboards](/docs/edit-dashboard#manage-folders).

<Callout icon="ℹ️" theme="info">
  Analytics supports analysis of one year of data, to ensure an optimal user experience in building Dashboards. Additional data remains accessible through the Explorer.
</Callout>

# View Analytics

Select the **Analytics** link in the CloudZero top menu bar to view the [Analytics](https://app.cloudzero.com/analytics/folders/view) page:

<Image align="center" alt="The Analytics Page in CloudZero" border={true} src="https://downloads.cloudzero.com/documentation/resources/analytics-page-1.png" className="border" />

From the Analytics page, you can take the following actions:

* Select a quick filter to display a list of certain Dashboards:
  * [**All**](https://app.cloudzero.com/analytics/folders/view) Dashboards
  * Dashboards in your [**Private**](https://app.cloudzero.com/analytics/folders/private_folder/view) folder (if you have the necessary permissions)
  * Dashboards marked as [**Favorites**](https://app.cloudzero.com/analytics/folders/favorites/view)
  * [**Recent**](https://app.cloudzero.com/analytics/folders/recent/view) Dashboards (the five most recently viewed).
* Search all Dashboards in the organization.
* Search Dashboards within the current folder.
* Set a Dashboard as a favorite by selecting the **heart icon** next to its name.
* [Manage Dashboards](#manage-dashboards).
* [Manage folders](#manage-folders).

# Manage Dashboards

By default, Dashboards appear in the **Dashboards Home** on the [Analytics](https://app.cloudzero.com/analytics/dashboards) page. If you have the necessary permissions, you can take the following actions to manage Analytics Dashboards:

* [Create a Dashboard](/docs/edit-dashboard#create-dashboard)
* [Edit a Dashboard](https://docs.cloudzero.com/docs/edit-dashboard#edit-dashboard-content)
* [Copy a Dashboard](/docs/edit-dashboard#copy-dashboard)
* [Delete a Dashboard](/docs/edit-dashboard#delete-dashboard)

All user roles can view public Dashboards. If you have the necessary permissions, you can also view the private Dashboards you have have created.

## Create Dashboard

To create a Dashboard:

1. On the [Analytics](https://app.cloudzero.com/analytics/dashboards) page, click the **Create Dashboard** button:

   <Image align="center" alt="Create Dashboard button" border={true} src="https://downloads.cloudzero.com/documentation/resources/analytics-create-dashboard-button.png" className="border" />

2. Enter a Dashboard name.

   <Callout icon="ℹ️" theme="info">
     When you create a Dashboard, it will automatically inherit the visibility of the [folder](#manage-folders) you create it in.
   </Callout>

3. Click the **Create** button:

   <Image align="center" alt="Select the Create button to create a new dashboard" border={false} width="500px" src="https://downloads.cloudzero.com/documentation/resources/analytics-create-new-dashboard.png" />

4. On the new Dashboard page, select **Add** to add a tile to your Dashboard: visualization, text box, Markdown box, or button.

   <Image alt="Select Add to add a tile to your dashboard" border={false} src="https://downloads.cloudzero.com/documentation/resources/analytics-new-blank-dashboard.png" />

5. If you add a visualization tile, select **CloudZero Billing Data** as the source of cost data, called an `Explore`:

   <Image align="center" alt="Select CloudZero Billing Data" border={true} src="https://downloads.cloudzero.com/documentation/resources/analytics-dashboard-viz-cz-billing-data.png" className="border" />

6. Select the desired billing data fields to build your visualization.
   Use the search field to find a field or browse through the Dimension categories. Selecting a field will add it to the **In Use** tab and the **Data** section.

   <Image alt="Select billing data fields" border={false} src="https://downloads.cloudzero.com/documentation/resources/analytics-dashboard-select-fields.png" />

7. After selecting your data fields, select **Run** to see the data and the visualization populate. You can choose different fields and run the data again as needed.

   <Image alt="Select the Run button to explore the data" border={false} src="https://downloads.cloudzero.com/documentation/resources/analytics-dashboard-run-button.png" />

8. To pivot and group the data, hover over the data you would like to pivot on and click the **arrow icon**. Alternatively, if the data you want to pivot on is in the table in the Data section, you can click on the **icon** and select **Pivot**.

9. To add a filter, hover over the data you would like to filter on and click the **filter icon**. This will add the selected data to the **Filter** section on the right where you can determine how you want to filter. Note that the data you want to filter on does not need to be included in the Data section. For example, you can filter any visualization by date.

10. Enter the name of the visualization.

    <Image alt="Enter a name for the visualization" border={false} src="https://downloads.cloudzero.com/documentation/resources/analytics-dashboard-name-viz-tile.png" />

11. Click the **Save** button.

    <Image alt="Save the visualization tile" border={false} src="https://downloads.cloudzero.com/documentation/resources/analytics-dashboard-save-viz-tile.png" />

12. Optionally, adjust the size and location of the visualization tile, add more tiles, or both. For more information about creating Dashboard tiles, see the [Looker documentation](https://cloud.google.com/looker/docs/creating-user-defined-dashboards#adding_tiles_and_text_to_a_dashboard).

13. Select **Save** to save the Dashboard.

    <Image alt="Save the edited dashboard" border={false} src="https://downloads.cloudzero.com/documentation/resources/analytics-dashboard-save-edited-dashboard.png" />

## Edit Dashboard

If you have the necessary permissions, you can rename Dashboards you have created and [edit](#editing-dashboard-content) custom Dashboards anyone has created.

<Callout icon="ℹ️" theme="info">
  When you create a Dashboard, it will automatically inherit the visibility of the folder you create it in. You can change its visibility by [moving it into a folder](/docs/edit-dashboard#move-folder-or-dashboard) with a different visibility setting.
</Callout>

## Rename Dashboard

To rename a Dashboard:

1. On the [Analytics](https://app.cloudzero.com/analytics/dashboards) page, locate the Dashboard you plan to rename.

2. Select the three-dot icon in the **Actions** column.

   <Image align="center" alt="Select the Actions icon" border={true} src="https://downloads.cloudzero.com/documentation/resources/analytics-dashboard-actions-icon.png" className="border" />

3. Select **Configure Dashboard**.

4. Update the Dashboard name.

5. Select **Update**.

## Edit Dashboard content

To edit the content of a Dashboard:

1. On the [Analytics](https://app.cloudzero.com/analytics/dashboards) page, locate the Dashboard you plan to edit.

2. Select the three-dot icon in the **Actions** column.

   <Image align="center" alt="Select the Actions icon" border={true} src="https://downloads.cloudzero.com/documentation/resources/analytics-dashboard-actions-icon.png" className="border" />

3. Select **Edit Dashboard**.

4. Follow the instructions on [creating a Dashboard](#create-dashboard) to add, update, or remove tiles on your Dashboard. For more information about editing Dashboard tiles, see the [Looker documentation](https://cloud.google.com/looker/docs/editing-user-defined-dashboards#editing_tiles).

5. Select **Save** to save the Dashboard.

   <Image alt="Save the edited dashboard" border={false} src="https://downloads.cloudzero.com/documentation/resources/analytics-dashboard-save-edited-dashboard.png" />

You can also edit a Dashboard you are currently viewing. Select the three-dot icon and choose **Edit dashboard** from the drop-down menu.

<Image alt="Select the three-dot icon and select Edit dashboard" border={false} src="https://downloads.cloudzero.com/documentation/resources/analytics-dashboard-view-and-edit-dashboard.png" />

## Copy Dashboard

If you have the necessary permissions, you can copy a Dashboard and then edit it. For example, you can duplicate one of CloudZero's standard Dashboards or a custom Dashboard that you or someone else created.

To copy a Dashboard:

1. On the [Analytics](https://app.cloudzero.com/analytics/dashboards) page, locate the Dashboard you plan to copy.

2. Select the three-dot icon in the **Actions** column:

   <Image align="center" alt="Select the Actions icon" border={true} src="https://downloads.cloudzero.com/documentation/resources/analytics-dashboard-actions-icon.png" className="border" />

3. Select **Copy Dashboard**.
   CloudZero will immediately create a copy of the Dashboard and take you to it.

4. Optionally, follow the instructions on [creating a Dashboard](#create-dashboard) to add, update, or remove tiles in your Dashboard. For more information about editing Dashboard tiles, see the [Looker documentation](https://cloud.google.com/looker/docs/editing-user-defined-dashboards#editing_tiles).

5. Optionally, rename the Dashboard. By default, CloudZero uses the original Dashboard's name and adds `(copy)` at the end.

6. Select **Save** to save the edited copy of the Dashboard.

   <Image alt="Save the edited dashboard" border={false} src="https://downloads.cloudzero.com/documentation/resources/analytics-dashboard-save-edited-dashboard.png" />

## Delete Dashboard

If you have the necessary permissions, you can delete the Dashboards you have created.

<Callout icon="⚠️" theme="warn">
  If you delete a Dashboard by mistake, you must contact your CloudZero representative to restore it.
</Callout>

To delete a Dashboard:

1. On the [Analytics](https://app.cloudzero.com/analytics/dashboards) page, locate the Dashboard you plan to delete.

2. Select the three-dot icon in the **Actions** column.

   <Image alt="Select the Actions icon" border={false} src="https://downloads.cloudzero.com/documentation/resources/analytics-dashboard-actions-icon.png" />

3. Select **Delete Dashboard**.

4. In response to the prompt identifying the Dashboard to be deleted, click the **Delete** button to confirm deletion. Note that this will **immediately and permanently** delete your Dashboard.

<Image align="center" alt="Delete Dashboard" border={false} width="500px" src="https://files.readme.io/7f10e2ae36bfdc0632b20cb35548480a41ed7c44fb915424e5004e65e67c3ef7-analytics-dashboards-confirm-delete-dashboard-1.png" />

CloudZero deletes the Dashboard and reloads the page.

# Manage folders

If you have the necessary permissions, you can take the following actions to organize Dashboards into folders:

* [Create a folder](#creating-a-folder)
* [Configure a folder](#configuring-a-folder)
* [Delete a folder](#deleting-a-folder)
* [Move a folder or Dashboard](/docs/edit-dashboard#move-folder-or-dashboard)

All user roles can view public folders. If you have the necessary permissions, you can also view the private Dashboards you have created, which are stored in the **Private** folder.

## Create folder

You can create folders within folders, nested as deeply as needed.

Note that you cannot create folders inside the **Private** folder.

To create a folder:

1. On the [Analytics](https://app.cloudzero.com/analytics/dashboards) page, click the **Create Folder** button:

   <Image align="center" alt="Create Folder button" border={true} src="https://downloads.cloudzero.com/documentation/resources/analytics-folders-create-folder-1.png" className="border" />

2. Enter a folder name (100 characters maximum).

3. Set the folder's visibility by selecting one of the options listed.
   Note that you cannot create a new private folder. Use the existing [Private](https://app.cloudzero.com/analytics/folders/private_folder/view) folder instead. When you finish, click the **Create Folder** button. The visibility options are:

   * **Public**: visible to everyone in your organization.
   * **Roles**: visible only to users with specific Roles. Select the **Role** that will have access to the folder from the drop-down list.

CloudZero displays a **Folder created successfully** message when the folder is created.

## Configure folder

You can update a the name and visibility of a folder. Note that you cannot rename the **Private** folder or change its visibility.

To configure a folder:

1. On the [Analytics](https://app.cloudzero.com/analytics/dashboards) page, locate the folder you plan to configure.

2. Select the three-dot icon in the **Actions** column.

   <Image align="center" alt="Select the Actions icon" border={true} src="https://downloads.cloudzero.com/documentation/resources/analytics-folders-actions-icon-1.png" className="border" />

3. Select **Configure**.

4. Optionally, update the folder name (100 characters maximum).

5. Optionally, set the visibility for the folder by selecting the Roles that will have access to the folder. If no Roles are selected, the folder and its contents will be public for all users in the organization.

6. Select **Update**.

<Image align="center" alt="Configure folder form" border={false} width="500px" src="https://files.readme.io/da6f400bd8c89708ded7e19d2f92371f940bed5b60a795bc5eb83466a5bf60cc-analytics-folders-configure-folder-1.png" />

CloudZero displays a **Folder updated successfully** message when the update is done.

## Delete folder

A folder must be empty before you can delete it. Move or delete any Dashboards that are inside the folder first. Note that you cannot delete the **Private** folder.

To delete an empty folder:

1. On the [Analytics](https://app.cloudzero.com/analytics/dashboards) page, locate the folder you plan to delete.

2. Select the three-dot icon in the **Actions** column:

   <Image align="center" alt="Select the Actions icon" border={true} src="https://downloads.cloudzero.com/documentation/resources/analytics-folders-actions-icon-1.png" className="border" />

3. Select **Delete**.

4. Click the **Delete** button to confirm deletion. Note that this will **immediately and permanently** delete your folder.

CloudZero deletes the folder and returns you to the parent folder, or the Dashboards Home on the [Analytics](https://app.cloudzero.com/analytics/dashboards) page if there is no parent folder.

# Move folder or Dashboard

You can move Dashboards and folders. Moving a folder also moves all of its nested contents. Note that you cannot move folders into the **Private** folder.

To move a Dashboard or folder:

1. On the [Analytics](https://app.cloudzero.com/analytics/dashboards) page, locate the folder or Dashboard you plan to move.

2. Select the three-dot icon in the **Actions** column.

   <Image align="center" alt="Select the Actions icon" border={true} src="https://downloads.cloudzero.com/documentation/resources/analytics-folders-actions-icon-1.png" className="border" />

3. Select **Move**.

4. Select a destination folder and the **Move** button when it is available.

<Image align="center" alt="Move folder form" border={false} width="500px" src="https://files.readme.io/25638fc84790d92b993467818e135597d622f2d5c8036b47dfc323eb8e25cda2-analytics-folders-confirm-move-1.png" />

CloudZero moves the item into the selected folder.

# Change Dashboard visibility

Each Dashboard inherits the visibility settings of its parent folder. If you have the necessary permissions, you can change the visibility of a Dashboard by [moving it](/docs/edit-dashboard#move-folder-or-dashboard) into a different folder:

* To make a Dashboard private, move it into the [**Private**](https://app.cloudzero.com/analytics/folders/private_folder/view) folder.
* To make a Dashboard public, move it into any public folder or the [Dashboards Home](https://app.cloudzero.com/analytics/dashboards).
* To make a Dashboard accessible to a limited audience, move it into a folder that is only visible to specific Roles. You can [configure a folder](#configure-folder) to be visible to the Roles you select.

# Maximize Dashboard Performance

CloudZero recommends that you follow these guidelines when building Dashboards to maximize performance and usability:

**Set a default Dashboard usage date filter to include data only for the months you need**.
Fewer months means less data has to be processed to return your dashboard visualizations, which improves performance.

**Limit the number of tiles used in your dashboard**.
Each tile added to a dashboard impacts memory consumption and results in additional queries to fetch data, which can impact performance. Adding too many tiles to a dashboard can also result in an overwhelming experience for users, and make key information more difficult to find.

**Minimize the usage of pivot tables**.
Pivot tables consume more memory and result in more complex and less performant queries in loading data.

**Try to use tables instead of individual tiles for summary-level headers**.
This minimizes the number of queries needed to return data and improves overall Dashboard performance.

**Limit the number of rows and columns returned in visuals**.
Adding more rows and columns impacts ability of users to quickly analyze data on the Dashboard, and also has a negative performance impact on load times.
