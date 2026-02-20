---
title: Notifications
category: features
createdAt: '2020-02-13T19:39:06.749Z'
hidden: false
slug: notifications
updatedAt: '2025-07-21'
---
A key benefit of the CloudZero platform is the ability to maintain a powerful normalized data model of your cost infrastructure, create predictive models of its future behavior, and send you Notifications when CloudZero believes that something needs your attention. CloudZero provides global Notifications and Notifications based on Views.

CloudZero [Views](/docs/views) help decentralize cost management in your engineering organization by providing targeted cost visibility to individual teams. Each View includes a Connection to an email, a Slack channel, or both, to provide Notifications.

To receive notifications from Views, you must set up notifications, following the steps in [Create Views](/docs/views#create-views). If you need to update your notification settings, follow the steps in [Edit Views](/docs/views#edit-views).

You can set up notifications to be sent to two channels, Slack and email. To receive notifications on Slack, you must set up a [Slack integration](https://docs.cloudzero.com/docs/enabling-slack-integration).  CloudZero suggests that when you specify an email, you use an email alias, such as `feature_team@yourcompany.com`, to manage the recipient group. To ensure you receive notification emails, you must allow emails from `cloudzero.com` and `hello.cloudzero.com`.

When your configuration is complete, you will receive the following types of notifications:

* **Weekly Updates:** Get your cost update every Monday for the last seven days, showing you the biggest changes week over week. Normally these notifications are sent on Tuesday.
* **Monthly Updates:** Get your cost update at the end of the month, showing you the biggest changes month over month. Normally these notifications are sent on the third or fourth day of the month.
* **Budget Notifications:** Get a Notification for each View if the spend exceeds the configured threshold, 80 or 100%.
* **Anomaly Alerts:** Get an alert when CloudZero detects unexpected spend during billing ingest, up to three times a day. CloudZero provides granular details about the services and accounts that seem to be responsible. For more information, see [How Anomaly Detection](/docs/anomaly-detection#how-anomaly-detection-works) works.
