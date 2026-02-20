---
title: View and Manage Roles
deprecated: false
hidden: false
metadata:
  robots: index
---
Roles are the means within CloudZero through which you control access to cost and usage data and assign granular user permissions. You can assign users one or many Roles to align users with your business needs.

The [Roles](https://app.cloudzero.com/settings/roles) page lists the Roles configured for your organization. To open the Roles page, navigate to **Settings** > **Roles**. For each Role, the page shows the **Name**, **Description**, access **Filters**, date and time **Created At** and **Last Updated**, user **Last Updated By**, and the number of **Users** who have the Role.

If you have the appropriate permissions, from the [Roles](https://app.cloudzero.com/settings/roles) page you can can create Roles, assign access rules to each Role, configure the granular permissions assigned to each Role, and add users to one or more Roles to provide the level of access each user should have in the platform.

<Callout icon="ℹ️" theme="info">
  Any new users onboarded to your account will be added to the DEFAULT Role for your organization. When your organization is created, the DEFAULT Role is assigned FULL ACCESS to all data and has all permissions enabled. This persists unless you modify the DEFAULT role settings. For details, see the section titled [Change a Role’s Data Access Level or Cost Type](/docs/view-and-manage-roles#/change-a-roles-data-access-level-or-cost-type).
</Callout>

# Permissions in Roles

To see the permissions for any Role, click that Role on the Roles page to open the Role Details screen, showing the date and time last updated and the user who made the update, followed by the **Basic Information**: the **Name** and **Description**:

<Image align="center" alt="Role details for full access role" border={true} src="https://files.readme.io/0ecada671016959b9ff0f172cec26449efb24bfdb84f210973164d242b2657a2-02-full-access-role.jpg" className="border" />

## Data Access Controls in Roles

You can configure a Role to provide one of three types of **Data Access Control**:

* **[Full Access](/docs/view-and-manage-roles#/full-access-permissions)**: Users have access to all of your organization's spend data and can view all [cost types](/docs/user-groups#access-to-cost-types).
* **[Limited Access](/docs/view-and-manage-roles#/limited-access-permissions)**: Users have limited access to spend data based on dimensional filters and selected [cost types](/docs/user-groups#access-to-cost-types).
* **[No Access](/docs/view-and-manage-roles#/no-access-permissions)**: Users have no access to spend data.

### Full Access permissions

A user assigned to a Role with **Full Access** configured is granted access to all of their organization's spend data in CloudZero, including the following features:

* Explorer
* Analytics
* Legacy Dashboards
* Optimize
* Anomalies
* Budgets
* Dimensions Diagram

Users with **Full Access** Roles can view spend data for all [cost types](/docs/view-and-manage-roles#access-to-cost-types-in-roles).

### Limited Access Permissions

A user assigned to a Role with **Limited Access** configured can view spend data as allowed by selected filters. When a Limited Access Role is created, you must add at least one filter with the Dimension the organization wants users to be able to access.

<Image align="center" alt="Limited access role fields" border={true} src="https://files.readme.io/c5f2a0627955c4f1283283c00e6b31b831a473ec7a51463e8f4d20c9505bddd7-03-limited-access-role.jpg" className="border" />

Users with a **Limited Access** Role have access to spend data as follows:

* Explorer: Spend data is filtered by the Role's access to Dimensions.
* Analytics: Spend data in Dashboards is filtered by the Role's access to Dimensions.
* Legacy Dashboards: No access.
* Optimize: Recommendations are filtered by the Role's access to Dimensions.
* Anomalies: Recommendations are filtered by the Role's access to Dimensions.
* Budgets: No access.
* Dimensions Diagram: No access.

Users in a **Limited Access** Role can view only the [cost types](/docs/view-and-manage-roles#access-to-cost-types-in-roles) selected for the Role. All other cost types are hidden from Limited Access users in the [Explorer](/docs/explorer) and [Analytics](/docs/analytics).

### No Access Permissions

A user assigned to a Role with **No Access** configured cannot view any of their organization's spend data or access platform features in CloudZero.

These users can be granted permission to manage the various settings within the CloudZero platform, making this level of access appropriate for use cases like service accounts or ops accounts who need to manage the platform but do not need to view any spend data.

Because users in **No Access** Roles cannot view spend data; they do not have access to any [cost types](/docs/view-and-manage-roles#access-to-cost-types-in-roles).

## Access to Cost Types in Roles

Access to different cost types in the [Explorer](/docs/explorer) and [Analytics](/docs/analytics) is also configured at the Role level.

* No Access: Cannot view any cost types.
* Limited Access: Can view one or more of these cost types, as selected:
  * [Amortized Cost](/docs/explorer#amortized-cost)
  * [Billed Cost](/docs/explorer#billed-cost)
  * [Discounted Amortized Cost](/docs/explorer#discounted-amortized-cost)
  * [Discounted Cost](/docs/explorer#discounted-cost)
  * [Invoiced Amortized Cost](/docs/explorer#invoiced-amortized-cost)
  * [On Demand Cost](/docs/explorer#on-demand-cost)
  * [Real Cost](/docs/explorer#real-cost)
  * Usage Amount if enabled by a FinOps Account Manager for your account
* Full Access: Can view all cost types.

When a **Limited Access** Role does not grant access to specific cost types, access to the Explorer and Analytics is affected as follows:

* Explorer: The cost type selector will not show users cost types they do not have access to. If users attempt to go to an Explorer page that uses a restricted cost type, such as through a previously saved link, they will see an **Access Denied** error.
* Analytics: All cost types will be shown when the user is authoring Dashboards and in the cost type selector, if it is used on a Dashboard. In addition, all Dashboards will be accessible, even if they reference disallowed cost types. However, the value shown for any cost type the user does not have access to will always be $0.

In addition, **Limited Access** and **Full Access** Roles allow setting a default cost type for users assigned to the Role. In the Explorer, users can select from the **Cost Type** drop-down list to [change the displayed Cost Type](/docs/explorer#cost-types) to another type they have access to.

<Image align="center" alt="Cost type selector" border={true} src="https://files.readme.io/c31eef0b68a144c686b3fe02795307f2a96239b3d530c50d7274ae168d0316e7-04-role-cost-type-selector.jpg" className="border" />

For more information about cost types, see the [Cost Types documentation](/docs/explorer#cost-types).

## Granular permissions configuration

Each Role can be configured to provide granular permissions to different areas of the CloudZero application. For example, a Role can be configured to allow users to view but not edit budget details, or to create and modify cloud connections but not manage SSO settings.

To expand the permissions selector, click **+ Edit Permissions**.

Each permission that can be toggled on or off is logically grouped into categories that align with functionality than end users see throughout the application.

In the permissions selector, click the **>** symbol next to the category with the permissions you want to change to expand the list of permissions and toggle them on or off for the Role. As an example, the API Key Settings to view, create and modify, and delete API keys are shown in this image:

<Image align="center" alt="Role API keys" border={true} src="https://files.readme.io/97c9d1c51be21f1998b6e7e48326528bfd671d86fb8e875f6c3490458e25f925-05-role-api-keys.jpg" className="border" />

There are logical dependencies between toggles for each category. For example, if you wish to grant a Role permission to **Delete API Keys**, the system will automatically enable the capability to **View** and **Create/Modify API Keys** as well.

There are several permissions that must be assigned to a Role in order for the CloudZero application to function. These permissions are considered system-level permissions and are not visible to users to toggle on or off.

# How CloudZero handles multiple role assignments

If a user is assigned multiple Roles, then CloudZero will examine both the Data Access Controls and Permissions provided in each Role, and combine them into a consolidated experience for the user. This is referred to as a `union` of access and permissions.

This union is a key concept to apply when you are configuring permissions for users, to ensure you know what users will be able to see and do within CloudZero if they are assigned to multiple Roles.

The following examples provide an overview of various potential Role combinations and the outcome that is experienced by end users when they log into the system.

| Data Access union example                                                                                                                                                                                              | Outcome                                                                                         |
| :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------- |
| You are assigned one Role with **No Access** and another Role with **Full Access**.                                                                                                                                    | You have full access to all spend data.                                                         |
| You are assigned a Role with **No Access** and another Role with **Limited Access** to show only data relevant to `Team Donatello`.                                                                                    | You have access to the data granted by the **Limited Access** Role for `Team Donatello`.        |
| You are assigned to two Roles, both of which have **Limited Access**. One Role has spend data filtered to the `Team Donatello` Dimension; the other Role has spend data filtered to the `Team Michelangelo` Dimension. | You have access to spend data for both the `Team Donatello` and `Team Michelangelo` Dimensions. |

| Permissions union example                                                                                                                                                                                                                                          | Outcome                                                                                      |
| :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------- |
| You are assigned a Role which only has permission to **view** SSO Settings.                                                                                                                                                                                        | You have access to **view** SSO Settings                                                     |
| You are assigned a Role which only has permission to **view** SSO Settings.  You are assigned another Role which has permission to **modify** and **delete** SSO Settings.                                                                                         | You have access to **view**, **modify**, and **delete** SSO Settings.                        |
| You are assigned a Role which has permission to **view** Telemetry Stream Details. You are assigned another Role which has permission to **modify** Telemetry Stream Details. You are assigned a Role which has permission to **delete** Telemetry Stream Details. | You have access to **view**, **modify**, and **delete** Telemetry Stream Detail information. |

If a user is assigned to multiple roles, on the User Details page, you can view the combined permission set that the union logic grants the user. Follow these steps to see the combined permissions information for a user:

1. Navigate to **Settings** > **Users**.
2. Click the **pencil icon** on the row of the users whose permissions you want to view.
3. When the drawer expands showing the list of roles that user is assigned, click **User Permissions** tab.

# Manage Roles

If you have the appropriate permissions to manage Roles, you can take the following actions:

* [Create a Role](/docs/view-and-manage-roles#create-role).
  * [Configure Role with Full Access to data](/docs/view-and-manage-roles#/configure-role-with-full-access-to-data)
  * [Configure Role with No Access to data](/docs/view-and-manage-roles#configure-role-with-no-access-to-data)
  * [Configure Limited Access Role](/docs/view-and-manage-roles#configure-limited-access-role)
  * [Configure Role with Granular Permissions](/docs/view-and-manage-roles#configure-role-with-granular-permissions)
* [Add users to a Role through the Role Settings page](/docs/view-and-manage-roles#add-users-to-a-role-through-the-role-settings-page).
* [Add Users to a Role through the User Settings page](/docs/view-and-manage-roles#add-users-to-a-role-through-the-user-settings-page).
* [Remove users from a Role through the Role Settings page](/docs/view-and-manage-roles#remove-users-from-a-role-through-the-role-settings-page).
* [Move users to another Role](/docs/view-and-manage-roles#/move-users-to-another-role).
* [Change a Role’s data access level or cost type access](/docs/view-and-manage-roles#/change-a-roles-data-access-level-or-cost-type).
* [Delete a Role](/docs/view-and-manage-roles#delete-a-role).

## Create Role

The steps to create a Role vary depending on the type of Role you are creating. Some Roles will have more steps than others. The steps are broken down logically here for each scenario.

### Configure Role with Full Access to data

To create a Role with Full Access to data:

1. Navigate to **Settings** > **Roles**.
2. Click **Add New Role**.
3. Enter a Role **Name**.
4. Optionally, enter a Role **Description**.
5. Set the **Data Access Control** level to **Full Access**.
6. Select a default **Cost Type View** from the drop-down list.
7. Click **Create Role**.

The following image shows an example configuration of a **Full Access** Role with the default **Cost View** set to **Real Cost**:

<Image align="center" alt="Full access role for Real Cost" border={true} width="500px" src="https://files.readme.io/4b6f5d17b1416638f7fd19627392864a2cbc59280421f45256c2f0b2ae5d6806-06-full-access-real-cost-role.jpg" className="border" />

After you save the Role, the Role details page for the new Role opens. You can then add users to the Role and make other changes. For details, see [Add Users to a Role through the Role Settings page](/docs/view-and-manage-roles#add-users-to-a-role-through-the-role-settings-page) and [Add Users to a Role through the User Settings page](/docs/view-and-manage-roles#add-users-to-a-role-through-the-user-settings-page).

### Configure Role with No Access to data

To create a Role with No Access to data:

1. Navigate to **Settings** > **Roles**.
2. Click **Add Role**.
3. Enter a Role **Name**.
4. Optionally, enter a Role **Description**.
5. Set the **Data Access Control** level to **No Access**.
6. Click **Create Role**.

The following image shows an example configuration of a **No Access** Role.

<Image align="center" alt="No Access role configuration" border={true} width="600px" src="https://files.readme.io/ffee6d95a78634bdaaeab0e0fd1e553622d712de3a369c25d8927726f684ea4a-07-no-access-role.jpg" className="border" />

After you save the Role, the Role details page for the new Role opens. You can then add users to the Role and make other changes. For details, see [Add Users to a Role through the Role Settings page](/docs/view-and-manage-roles#add-users-to-a-role-through-the-role-settings-page) and [Add Users to a Role through the User Settings page](/docs/view-and-manage-roles#add-users-to-a-role-through-the-user-settings-page).

### Configure Limited Access Role

A Limited Access Role grants access to at least one filter and at least one Cost Type. To create a Role with Limited Access:

1. Navigate to **Settings** > **Roles**.
2. Click **Add Role**.
3. Enter a Role **Name**.
4. Optionally, enter a Role **Description**.
5. Set the **Data Access Control** level to **Limited Access**.
6. Click **Add Filter**.
7. Select the Dimension you want to filter on, for example, `Cloud Provider`.
8. Select one or more Dimension values, for example, `Azure`. By default, the Boolean operator is set to `is`, which means the filter allows access to the selected values. Toggle this to `except` to disallow access to the selected values. For example, if you want to prevent a Role from viewing certain Azure subscriptions, toggle `Except` and then select the Azure subscriptions the Role should not have access to.

<Image align="center" alt="Add filter for Limited Access Role" border={true} src="https://files.readme.io/2e1329649d8f0ca6781f7fbc2eae9d943d956b319399f58b4efb79d737506e9b-08-limited-access-add-filter.jpg" className="border" />

9. Optionally, filter on additional Dimensions by selecting **Add Another Filter**. All filters will be applied to the Role's access.
10. Click **Apply** to save the filter configuration.
11. Select the **Cost Types** you want users to see in the Explorer and Analytics.
    By default, all cost types are selected. You can deselect a cost type by clicking the **X** next to it, or remove all cost types by clicking **Clear All**. Cost types that are not selected will be hidden from users in the Explorer and Analytics.

<Image align="center" alt="LImited access role configuration" border={true} width="700px" src="https://files.readme.io/6d982d6eaddbeca3d7020a189ed40873e5a6537f3b97b3a826e21299233b4b41-09-limited-access-role-form.jpg" className="border" />

12. Select a **Default Cost View** from the drop-down list. For information about each cost type, see the [Cost Types](/docs/explorer#cost-types) documentation.
13. Click **Create Role**.

The following image shows an example configuration of a Limited Access Role that grants access only to data where the cloud provider is AWS. The Role also grants access to all cost types, with a default cost type of **Real Cost**:

<Image align="center" alt="Limited Access to AWS cloud provider" border={true} src="https://files.readme.io/86bf3e1701d82127bcae6b8df8c0164cc04b68c268c629a767b2831cd9a0ca97-10-limited-access-cost-types.png" className="border" />

After you create a Limited Access Role, the filters typically take effect within one to two hours. However, in some cases, it may take up to 24 hours. While CloudZero processes the filters, you will see an icon with circular arrows next to the Role **Name** on the Roles page, and next to the **Data Access** heading on the Role detail page.

### Configure Role with Granular Permissions

1. Navigate to **Settings** > **Roles**.
2. Click **Add New Role**.
3. Enter a Role **Name**.
4. Enter a Role **Description**.
5. Click **Edit Permissions**.
6. Review the list of permissions in the side bar panel that appears and determine what is applicable to the needs of this Role.
7. Toggle on each permission that you need enabled for this Role. Make sure any permissions not needed for this Role are toggled off.
8. Click **Save Permissions**.
9. Click **Create Role**.

Changes made to permissions assigned to a particular Role are effective immediately upon the Role successfully updating. The following image shows an example of granular permissions you can configure for each Role in CloudZero, with two categories expanded to show the toggles for each permission and all permissions available for some categories, but only a certain number for other categories:

<Image align="center" alt="Role permissions list" border={true} src="https://files.readme.io/02f954e3c8a33fa8113a15bce5f403dcf4cbb05508f318221eccca8266a90e44-11-roles-permission-list.jpg" className="border" />

## Add Users to a Role through the Role Settings page

Follow these steps to add users to an existing Role through the Role Settings:

1. Navigate to **Settings** > **Roles**.
2. Select the **Role** you plan to add users to.
3. Click + **Add Users**.
4. Select the users you would like to add to the Role.
5. Click **Add to Role**.

<Image align="center" alt="User search" border={true} src="https://files.readme.io/7e37d6860819a0afbe0b9aa4693cd690dbedeefc942c6ac08e9c4d88e7e93ec0-12-roles-users-search.jpg" className="border" />

## Add Users to a Role through the User Settings page

Follow these steps to add users to an existing Role through the User Settings:

1. Navigate to **Settings** > **Users**.
2. Click the **pencil icon** in the row of the user you want to add.
3. When the drawer expands showing the list of roles that user is assigned, check or uncheck each role that needs to be applied to the user.
4. Click **Save Changes**.

## Remove Users from a Role through the Role Settings page

Follow these steps to remove individual users from a Role:

1. Navigate to **Settings** > **Roles**.
2. Select the Role you plan to edit.
3. Find the user you wish to remove and click the **remove icon** (circle with a line inside) in the **Actions** column.
4. Click **Remove** to confirm you want to remove the user from the Role.

Users must remain in at least one Role. If the user you are attempting to remove is not in another Role, you will see an error message that the user cannot be removed from the current Role.

## Move Users to another Role

Follow these steps to move users from the current Role to another Role:

1. Navigate to **Settings** > **Roles**.
2. Select the Role you plan to edit.
3. Click **Move Users**.

<Image align="center" alt="Move user" border={true} src="https://files.readme.io/aa1b3bec87f34be2d80d9d8292e3db094224df773a4bd942c5deecea890161d6-14-move-user.png" className="border" />

4. Select the Role you want to move the user(s) to.
5. Select the user(s) you want to move.
6. Click **Move to Role**.

## Change a Role’s Data Access Level or Cost Type

Follow these steps to change a Role's level of Data Access Control, Cost Type View, and default Cost Type:

1. Navigate to **Settings** > **Roles**.
2. Select the Role you plan to edit.
3. Select the desired level of **Data Access Control**: **Limited Access**, **Full Access**, or **No Access**.
4. For a Limited Access Role, add at least one **filter** and **Cost Type**. For details, see the steps to create a filter in the section [Configure Limited Access Role](/docs/view-and-manage-roles#configure-limited-access-role).
5. For Full Access and Limited Access Roles, select a default **[Cost Type](/docs/view-and-manage-roles#access-to-cost-types-in-roles)**.
6. Click **Update Role**.

For example, the Default Role grants Full Access by default, but you can choose to change the **Data Access Control** level of the Default Role to **No Access** so new users have no permissions until you move them or add them to another Role.

## Delete a Role

If you have the appropriate permissions, you can delete a Role, but all Role members must be moved to another Role first.

1. Navigate to **Settings** > **Roles**.
2. Select the Role you plan to edit.
3. Remove all users or move all users to another Role. For details, see the sections [Remove Users from a Role through the Role Settings page](/docs/view-and-manage-roles#remove-users-from-a-role-through-the-role-settings-page) and [Move Users to another Role](/docs/view-and-manage-roles#/move-users-to-another-role).
4. After the Role's users are removed or moved, click **Delete**. A confirmation message indicates that the role has been successfully deleted.

<br />
