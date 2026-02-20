---
title: Organization Management
category: features
hidden: false
slug: organization-management
---
Based on their responsibilities, some Customers and Managed Service Providers (MSPs) manage the configuration and usage of multiple CloudZero organizations.

To support these activities, CloudZero provides the capability to provision and manage several accounts from one centralized location through the Organization Management feature.

<Callout icon="ℹ️" theme="info">
  Organization Management must be enabled by a CloudZero account manager. If you are interested in this capability, contact your FinOps Account Manager.
</Callout>

# Organization Management terminology

The following definitions help you understand how to use Organization Management to provision and manage multiple accounts in CloudZero.

* **Standalone Organization**: A single, self-managed customer organization.
* **Primary Organization**: The centralized organization (likely an MSP or controlling entity) that creates and manages Tenant Organizations.
* **Tenant Organization**: An organization which is being managed by a Primary Organization.
* **Organization Group**: The collective group of Tenant Organizations being managed by a Primary Organization.

# Create Organization Group

After Organization Management has been enabled by a CloudZero account manager, you can create the Organization Group under which you will add the Tenant Organizations you will be managing.

To create an Organization Group:

1. Be sure you have been assigned an Organization role in CloudZero for your account.

2. Then select **Settings** > **Organization Management** to navigate to the Organization Management screen.

3. When the screen opens, click the **Create Organization Group** button.

   <Image align="center" alt="Create Organization Group" border={true} src="https://downloads.cloudzero.com/documentation/resources/Org-Mgt-create-org-group-2025-07-11.jpg" className="border" />

4. In the pop-up window that opens, in response to the prompt **Do you want to create a new organization group?**, click **Create** to create an Organization Group

If you click **Cancel**,  you will return to the Organization Management screen.

# Add existing organization to an Organization Group

If your customer, subsidiary, or account that requires management already exists in CloudZero, you must ask your counterpart in that organization for their specific Organization ID before you proceed.

To find the Organization ID, your counterpart must navigate to **Settings** > **Overview** and  **click to copy Organization ID**.

<Image align="center" alt="Copy org ID" border={true} src="https://downloads.cloudzero.com/documentation/resources/Settings-ovw-copy-org-id-cropd-2025-07-11.jpg" className="border" />

When you have the Organization ID, follow these steps to add an existing Tenant Organization to your Organization Group:

1. Navigate to **Settings** > **Organization Management** and click **Invite Tenant**.

<Image align="center" alt="Invite Tenant" border={true} src="https://downloads.cloudzero.com/documentation/resources/Org-Mgt-invite-tenant-2025-07-11.jpg" className="border" />

2. In the pop-up window that opens, in response to the prompt **Enter the organization id of the tenant you want to invite**, paste in the Tenant Organization ID for the relevant account and click the **Invite Tenant** button.

Your counterpart in the new Tenant Organization will receive a notification that says **You have a pending invitation from `Managing Company` to join their organization group and must select Accept or Decline**.

Note that any user with the necessary permissions in the Tenant Organization can accept or decline this invitation.

While the invitation is pending, the Tenant Organization appears on the **Invitations** tab of the Organization Management screen.

<Image align="center" alt="Invitations pending" border={true} src="https://downloads.cloudzero.com/documentation/resources/Org-Mgt-invitations-pending-blur-2025-07-11.jpg" className="border" />

After your counterpart has accepted, you will see the new Tenant Organization in the list of accounts on the **Tenants** tab of the Organization Management screen.

<Image align="center" alt="Organization Management screen after acceptance" border={true} src="https://downloads.cloudzero.com/documentation/resources/Org-Mgt-accepted-org-blur-2025-07-11.jpg" className="border" />

# Add new Tenant Organization to Organization Group

If your customer, subsidiary, or account that requires management does not already exist in CloudZero, you must add this account to the platform. Follow these steps to add a new Tenant Organization to your Organization Group:

1. Select **Settings** > **Organization** **Management** and on the Organization Management screen, click **Create Tenant Organization**.

<Image align="center" alt="Create Organization Group" border={false} src="https://downloads.cloudzero.com/documentation/resources/Org-Mgt-popup-create-tenant-enabled-2025-07-11.jpg" />

3. In the popup window that opens, in response to the prompt **Enter a name for your new tenant**, enter the name of the Tenant Organization you wish to create.
4. Select the **Is Enabled** check box to indicate the Tenant Organization should be enabled immediately.
   Note that until an organization is enabled, you will not be able to ingest any cloud cost information.
5. Click the **Create** button to create the Tenant Organization and add it to your Organization Group.

The new Tenant Organization appears in the list of accounts on the Tenants tab of the Organization Management screen.

# Manage user access to Tenant Organizations

You are likely to want only certain users from the Primary Organization to have access to certain Tenant Organizations.

For example, if you have project-based team assignments for specific accounts, you will want people on only the relevant project teams to have access to the Tenant Organizations for those customers. Follow these steps to manage access by Primary Organization users to Tenant Organizations:

1. Select **Settings** > **Organization Management** and on the Organization Management screen, click the Tenant Organization to which you want to assign users.
2. When the Tenant Detail screen opens showing the name of the organization and its status, in the lower panel, click the **Manage Access** button.
3. In the pop-up window that opens, if needed, search for users and on the list of users,  use the checkbox to select each user from the Primary Organization who needs access to the Tenant Organization.
4. Click the **Apply** button to grant these users access to the Tenant Organization or **Cancel** to go back to the Organization Management screen.

# Switch to a different Tenant Organization

Primary Organization users sign in to CloudZero through their Primary Organization.

After logging in, a Primary Organization user can click the tenant switcher drop-down arrow in the upper left corner of the Organization Management screen to search for and select a different Tenant Organization and switch to that organization.

Each user sees only the Tenant Organizations that the user has access to manage.

Users belonging to a Tenant Organization will log directly into that organization, and will not be able to see any other Tenant Organization data or any data relating to the Primary Organization.

# Disable a Tenant Organization

Disabling a tenant organization will prevent users from that tenant from logging in, and will pause all billing and ingestion of metrics. Follow these steps to disable a Tenant Organization:

1. Navigate to **Settings** > **Organization Management** and on the Organization Management screen, click the Tenant Organization to disable.
2. On the Tenant Detail screen, slide the Organization status toggle to disable the tenant organization.

<Callout icon="ℹ️" theme="info">
  You can re-enable the Tenant Organization from the Tenant Detail screen.
</Callout>

# Remove a Tenant Organization

Before you can remove a Tenant Organization you must remove all users who have access to the tenant. To do this, navigate to the Organization Management screen, select the Tenant Organization, and on the Tenant Detail screen, click the **Manage Access** button and deselect the users. For more details, see the section [Manage User Access to Tenant Organizations](#manage-user-access-to-tenant-organizations).

1. After all users have been removed, the **Remove Tenant** button becomes available; click the button.
2. In the **Remove `tenantname`** pop-up window that opens, in response to the prompt:
   **Are you sure you want to remove this tenant?**, type the `tenantname` as displayed in the popup to confirm.
3. Click the **Remove** button in the pop-up window to remove that Tenant Organization from your Organization Group.

# Delete an Organization Group

If you no longer need to manage Tenant Organizations, you can delete your Organization Group.

To do this, you must remove all the Tenant Organizations that are assigned to your Organization Group by following the instructions in the section [Remove Tenant Organization](#remove-tenant-organization).

Then follow these steps to delete your Organization Group:

1. Select **Settings** > **Organization Management**, and on the Organization Management screen, click the **Delete Organization Group** button.
2. In the pop-up window that opens, in response to the prompt **Do you want to delete this organization group?**, click the **Delete** button.
