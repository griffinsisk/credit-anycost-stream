---
title: Slack Integration
category: getting-started
createdAt: '2020-02-13T19:39:06.151Z'
hidden: false
slug: enabling-slack-integration
updatedAt: '2021-09-10T16:13:20.887Z'
---
Through [Notifications](/docs/notifications) CloudZero pushes information to you about things happening in your environment. These notifications can be configured with Slack to route alerts to different channels based on filters, for example, by Dimensions, tags, or accounts. To enable this functionality, you must first connect CloudZero with your Slack workspace.

# Connect CloudZero to your Slack workspace

1. Navigate to the [App Integrations page](https://app.cloudzero.com/organization/app-integrations).
2. Select **Add to Slack**. This will launch Slack and prompt for authorization. This may require a workspace admin to approve the request.

<Image align="center" alt="App Integrations page with Add to Slack button" className="border" border={true} src="https://downloads.cloudzero.com/documentation/resources/add-to-slack.png" />

# Select a Slack channel for notifications

Every organization has a [Global View](/docs/views#/create-views) that will report on all of the cloud spend across your entire organization.  CloudZero administrators in your organization can change the Slack channel that those notifications are delivered to by editing the Global View.

To add a Slack channel to receive Notifications, you must enter a Slack Channel ID. You can find a channel ID by going to the channel, clicking on the name of the channel in the top left corner, scrolling down to the bottom of the About tab (this is the default tab), and copying the channel ID.

<Image align="center" alt="Slack Channel ID location" className="border" border={true} src="https://downloads.cloudzero.com/documentation/resources/channel-id-location.png" />

# Send messages to a private Slack channel

If you want CloudZero to deliver notifications to a private Slack channel, you must invite the CloudZero app into that channel. To invite CloudZero to a private channel, open the channel in Slack and type `/invite @CloudZero`.
