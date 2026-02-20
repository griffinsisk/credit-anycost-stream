---
title: Getting Started with the Toolkit
category: features
createdAt: '2021-07-28T14:06:49.070Z'
hidden: false
slug: getting-started-2
updatedAt: '2021-07-30T19:35:55.783Z'
---
If you have not yet installed VS Code, navigate to the [VS Code website](https://code.visualstudio.com) and install the latest version (`v1.57.1` or higher).

# Install the CostFormation Toolkit Extension

After VS Code is installed, you can install the [CostFormation Toolkit](https://docs.cloudzero.com/docs/vscode-costformation-extension) extension. Select the **Extensions** icon in VS Code and search the extension marketplace for `CloudZero`. Then, select **Install**.

<Image align="center" alt="Seach for CloudZero in the marketplace" border="#000000" width="1258" src="https://files.readme.io/bf8a387-Extension-Install.png" className="border" />

# Connect to the CloudZero Platform

For many of the features to work, you must be authenticated with the CloudZero platform and have the necessary permissions for your organization. To log in, open the VS Code command palette (⇧⌘P/Ctrl-Shift-P) and select the command **CloudZero: Authenticate With the CloudZero Platform**.

<Image align="center" alt="Select the command to authenticate" border="#000000" width="2044" src="https://files.readme.io/56c70af-Authenticate.png" className="border" />

Your default browser opens the CloudZero login page, where you can enter your credentials.

<Image alt="Log in to CloudZero in your browser" border={false} src="https://downloads.cloudzero.com/documentation/resources/cloudzero-login-screen.png" />

After your credentials have been authenticated, you are redirected to a page displaying a success message confirming you have logged in and prompting you to close the tab and return to VS Code.

<Image align="center" alt="&#x22;Success! You have successfully logged into CloudZero. You can close this browser tab and return to VS Code.&#x22;" border={true} src="https://downloads.cloudzero.com/documentation/resources/vscode-auth-login-success.png" className="border" />

You can close the page and return to VS Code, where you will see a notification confirming that you are logged in to CloudZero:

<Image alt="&#x22;CloudZero: You are logged in as username!&#x22;" border={false} src="https://downloads.cloudzero.com/documentation/resources/vscode-auth-login-success-notification.png" />

# Create a new Definitions file

If your organization does not already have any custom Dimensions, you can begin to define new custom definitions by opening a new file and saving it. When you are prompted for the filename, you can name the file anything you like, but the extension of the file must be `.cz.yaml`.

For example: `our-definitions.cz.yaml`

# Download the latest definitions

If your organization already has custom definitions, you can download them and save them locally. Open the VS Code command palette (⇧⌘P/Ctrl-Shift-P) and select the command **CloudZero: Download Latest CostFormation**.

<Image align="center" alt="Select the download latest command" border="#000000" width="2058" src="https://files.readme.io/b5b7258-DownloadLatest.png" className="border" />

The VS Code Save dialog opens. Enter a name for your file and click **Save**.

<Callout icon="ℹ️" theme="info">
  The file extension must be `.cz.yaml`. If you do not specify an extension, `.cz.yaml` is automatically appended to the filename.
</Callout>

# Create your first Custom Dimensions

If you have not defined a CostFormation template previously and want to see an example that can be modified to your needs, examine the built-in examples: **Static Grouping**, **Dynamic Grouping**, **Even Allocation**, and **Proportional Allocation**. The following examples are shown:

* **Static Grouping**: Shows how to create rules that use statically named elements.
* **Dynamic Grouping**: Shows how to create a rule that will generate dynamically named elements using the source data.

These examples are part of the autocomplete feature. To add one of the examples to your definitions file, start typing the word `example` and you will see the examples, as illustrated for two of the examples:

<Image align="center" alt="Select an example" border="#242726" width="2740" src="https://files.readme.io/7c26d16-Screen_Shot_2021-07-28_at_11.01.22_AM.png" className="border" />

Select one of the examples to enter it into your file. Your cursor is placed in the first customizable area, which is the dimension `Id`. You can replace this with your own ID. Press the `Tab` key to advance to other fields that you can customize.

<Image align="center" alt="Next field you can customize, Name" border="#232523" width="3462" src="https://files.readme.io/3134b05-Screen_Shot_2021-07-28_at_11.05.05_AM.png" className="border" />

<Callout icon="ℹ️" theme="info">
  Although the two methods of grouping elements are shown as separate examples, these types of rules can be combined to create a dimension with both statically and dynamically named elements.

  These example templates are intended to be used in an empty file. Thus they contain the root element,  `Dimensions`, of a definitions file. If you add both examples, you will need to delete one of those lines.
</Callout>

# Troubleshooting the CostFormation Toolkit Extension

If your organization has recently enabled seamless SSO login and you attempt to authenticate the CloudZero CostFormation Toolkit extension, your browser may display the following error message:

**Oops, something went wrong**

**There could be a misconfiguration in the system or a service outage. We track these errors automatically, but if the problem persists feel free to contact us.**

**Please try again.**

To re-authenticate with CloudZero after your organization has enabled seamless SSO login, complete the following steps:

1. Update to the latest version of the [extension](https://marketplace.visualstudio.com/items?itemName=cloudzero.costformation-toolkit) (`v1.0.9` or higher).

2. Refresh VS Code by navigating to **View** > **Command Palette...** and selecting **Developer: Reload Window**.

3. Navigate to **Settings** > **Extensions** > **CloudZero CostFormation**.

4. In the **General: Auth URL** drop-down menu, select `https://auth.cloudzero.com`.

   <Image alt="Select https://auth.cloudzero.com from the CloudZero extension Auth URL settings" border={false} src="https://downloads.cloudzero.com/documentation/resources/vscode-auth-login-setting.png" />

5. Navigate to **View** > **Command Palette...** and select **Authenticate With the CloudZero Platform**.

6. Follow the remaining steps in [authentication](/docs/authentication#/).

<br />
