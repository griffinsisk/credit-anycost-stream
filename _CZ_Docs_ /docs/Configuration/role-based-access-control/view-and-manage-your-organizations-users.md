---
title: View and Manage your Organization’s Users
deprecated: false
hidden: false
metadata:
  robots: index
---
If you have the appropriate permissions to manage other users, you can view a list of all users in your organization on the [Users](https://app.cloudzero.com/settings/users) page.

To open this page, navigate to **Settings** > **Users tile** or use the **Settings** > **Users** option in the left navigation.

The Users page **lists the users** in your organization and includes the following information for each user:

* Email address
* Roles that the user has been assigned

If you want to delete a user from CloudZero, select the **trash can icon** next to the user's information:

# How to invite new users to CloudZero

CloudZero provides two ways to onboard new users into the application. One is manual and the other is by using Just-in-Time (JIT) provisioning through your connected SSO portal.

## Manual onboarding of new users

To invite someone to join your CloudZero organization, on the Users page, click the **Invite User** button.

In the form that opens, enter the user's email address and click **Invite User**. Be sure to enter an email address that matches the email domain your organization was set up with.

For example, if your organization's domain is linked to `@cloudzero.com`, a new user must have an email address ending in `@cloudzero.com`. When the user accepts the invitation, the user will automatically join your organization. Until users accept the invitation, they will be **Pending users** and cannot be assigned to any Roles or perform any actions in CloudZero. To see the acceptance status of user invitations, select the **History** tab of the **Users** page.

New users will be assigned automatically to the DEFAULT Role configured for your Organization.

<Image align="center" alt="Invite user form" border={true} width="500px" src="https://files.readme.io/ea118f4c5862d8665bf7942a02d8d07b7758e084a4b9c6a3927d727e193e97b0-invite-user-form.jpg" className="border" />

## Just-in-time (JIT) onboarding of new users through SSO

If you are using SSO to manage access to the CloudZero application, you will be able to take advantage of Just-in-Time provisioning.

When a user is assigned to the CloudZero application in your SSO provider and logs in for the first time, CloudZero will auto-provision the account for that user.

New users will be automatically assigned to the DEFAULT Role configured for your organization unless specific groups claims are also configured and passed to CloudZero through the SSO provider.

# Roles

CloudZero allows you to manage user access to your organization’s data and control a user’s permissions through the Roles feature.

For details on how to configure and manage Roles, see [View and Manage Roles](/docs/view-and-manage-roles).
