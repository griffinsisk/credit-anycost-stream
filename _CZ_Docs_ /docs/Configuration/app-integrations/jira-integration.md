---
title: Jira Integration
category: features
createdAt: '2025-03-17T19:39:06.151Z'
hidden: false
slug: jira-integration
updatedAt: '2025-03-17T19:39:06.151Z'
---
CloudZero offers an app integration with [Jira](https://www.atlassian.com/software/jira) so you can create [Work Items](https://community.atlassian.com/forums/Jira-articles/It-s-here-Work-is-the-new-collective-term-for-all-items-you/ba-p/2954892) from Optimize Recommendations and Anomalies, helping your team to track and resolve cloud cost issues faster.

After you create a Work Item linked to a Recommendation or an Anomaly, you can view the Jira status from within CloudZero.

<Callout icon="ℹ️" theme="info">
  CloudZero integrates only with [Jira Cloud](https://www.atlassian.com/software/jira). Integration with [Jira Data Center](https://www.atlassian.com/enterprise/data-center/jira) and [Jira Service Management](https://www.atlassian.com/software/jira/service-management) is not supported.
</Callout>

# Connect to Jira

Only users with the necessary permissions can configure app integrations in CloudZero. For information about how to manage permissions, see [Role-based Access Control](/docs/role-based-access-control).

<Callout icon="ℹ️" theme="info">
  CloudZero recommends that you [create a Jira user](https://support.atlassian.com/jira-cloud-administration/docs/create-edit-and-delete-users/) to file Work Items on behalf of CloudZero. You can treat the user like a service account, You must be able to log in to Jira with this account so you can authenticate the integration.

  If you create a Jira user, do the following:

  * Assign the **User** [project role](https://www.atlassian.com/software/jira/guides/permissions/overview#what-are-users-and-groups) to the user.
  * Give the user access to the necessary projects.
  * Log in to Jira as the user.
</Callout>

To set up a Jira app integration:

1. Ensure you are logged in to Jira with the appropriate user account.

2. In CloudZero, navigate to [**Settings** > **App Integrations**](https://app.cloudzero.com/organization/app-integrations) and select **Connect Jira**:

   <Image align="center" alt="Select Connect Jira on the App Integrations page" border={true} src="https://downloads.cloudzero.com/documentation/resources/jira-integration-connect-new.png" className="border" />

3. In response to the message requesting access to your Atlassian account, click the **Accept** button to grant CloudZero's Jira integration the [required permissions](#required-access-scopes-in-jira):

   <Image align="center" alt="Select Accept to grant CloudZero's Jira integration the required permissions" border={true} width="500px" src="https://downloads.cloudzero.com/documentation/resources/jira-integration-authenticate.png" className="border" />

4. In the CloudZero UI, ensure that your Jira instance is correct and select **Confirm Instance** to complete the app integration connection:

   <Image align="center" alt="Select Confirm Instance" border={true} src="https://downloads.cloudzero.com/documentation/resources/jira-integration-confirm-instance.png" className="border" />

The [App Integrations](https://app.cloudzero.com/organization/app-integrations) page shows you that CloudZero is connected to Jira:

<Image align="center" alt="A successfully connected Jira integration in CloudZero" border={true} src="https://downloads.cloudzero.com/documentation/resources/jira-integration-connected.png" className="border" />

The **Created by** field shows the name of the CloudZero user who set up the integration inside CloudZero.

You can now [create Jira Work Items](/docs/jira-integration#/create-jira-work-item) from CloudZero Recommendations or Anomalies.

# Disconnect Jira

To disconnect the Jira app integration, navigate to [**Settings** > **App Integrations**](https://app.cloudzero.com/organization/app-integrations) and select **Disconnect Jira**:

<Image align="center" alt="The Jira integration Disconnect button" border={true} src="https://downloads.cloudzero.com/documentation/resources/jira-integration-disconnect.png" className="border" />

After disconnecting Jira from CloudZero, Work Items created from Optimize or Anomalies remain in Jira. However, you will no longer be able to create new Work Items from Optimize or Anomalies, and any status changes on existing Work Items will not be reflected in CloudZero.

# Create Jira Work Item

After the Jira integration is enabled, users who have access to Optimize and Anomalies in CloudZero can create or unlink a Jira Work Item without needing to log in to Jira.

<Callout icon="ℹ️" theme="info">
  A single Jira Work Item corresponds to a single Anomaly. Only one Work Item may be linked to an Anomaly at a time. You can connect a Jira Work Item to one or more Recommendations. However, only one Work Item may be linked to a particular Recommendation at any one time.

  To enter the **Team Name** in the form to create a Jira Work Item, you must enter the `Team UUID`. Due to limitations of JIRA's API, CloudZero is unable to query for Team Names. To retrieve the `Team UUID`, go to your Team page in JIRA and copy the ending `UUID `embedded in the URL.
</Callout>

## Create Jira Work Item from a Recommendation

To create a Jira Work Item from a Recommendation:

1. Navigate to the **[Optimize](https://app.cloudzero.com/optimize/overview)** page in the CloudZero app.

2. Open the **Recommendations** tab.

3. Select one or more **Recommendations**.

4. In the panel that opens above the table of **Recommendations**, select **Create Jira Work Item**.

5. Review any notification that opens about existing connections to a Jira Work Item.

6. When the form opens to create a Work Item, complete the form to align with your Jira requirements and click the button to **Create the Work Item**.

7. After you create a Work Item, click the **Recommendation** and look for the link to the Work Item in the **Integrations** section of the **Recommendations** **detail** panel. Click the **Work Item** to view it in Jira.

## Create Jira Work Item from an Anomaly

1. Navigate to the **[Anomalies](https://app.cloudzero.com/anomalies)** page in the CloudZero app.
2. Select any one **Anomaly**.
3. At the bottom right of the **Anomaly detail** panel that opens, in the **Integrations** section, review any Jira Work Item already created or select **Create Jira Work Item**.
4. When the form opens to create a Work Item, complete the form to align with your Jira requirements and click the button to **Create the Work Item**.

# Unlink Jira Work Item

You can unlink a Work Item from a Recommendation or an Anomaly. After you unlink a Work Item, it will still exist in Jira, but it will not be shown with the Recommendation or Anomaly details in CloudZero.

To unlink a Work Item from a Recommendation or an Anomaly, navigate to the Recommendation or Anomaly detail in CloudZero and select **Unlink** in the **Integrations** section.

After a Work Item is unlinked from the Recommendation or Anomaly, you can choose to [create a new Work iItem](/docs/jira-integration#/create-jira-work-item) that will be linked to the Recommendation or Anomaly.

# Required Jira access scopes

During the setup process, you must agree to grant CloudZero the following access [scopes](https://developer.atlassian.com/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/#classic-scopes) in Jira:

* `Manage: jira-webhook`. Fetch, register, refresh, and delete dynamically declared Jira webhooks.
* `View: jira-user, jira-work`.
  * View user information in Jira that the user has access to, including usernames, email addresses, and avatars.
  * Read Jira project and work type data, and search for Work Items and objects associated with Work Items like attachments and worklogs.
* `Update: jira-work`. Create and edit Work Items in Jira, post comments as the user, create worklogs, and delete work items.

Note that CloudZero cannot delete Jira Work Items and does not request the `delete` permission.
