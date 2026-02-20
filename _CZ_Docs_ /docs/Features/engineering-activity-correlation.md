---
title: Engineering Events
category: features
createdAt: '2020-02-28T14:11:56.873Z'
hidden: false
slug: engineering-activity-correlation
updatedAt: '2022-05-03T15:17:07.598Z'
---
CloudZero allows you to correlate activities in your engineering systems, such as source control, CI/CD, configuration management, and so on, with your cloud costs.

To use Engineering Events, you must navigate to **Settings** > **API Keys** and on the [API Keys page](https://app.cloudzero.com/organization/api-keys), generate or copy your API Key to use in sending your events to the CloudZero platform.

# Integrate with the Events API

When you have an API key, you can have your engineering system send relevant events to the CloudZero system by using the [Events API](/reference/postevent#/versions).

Users typically integrate their continuous integration system first.  To do this, select a branch or repo with an active feature that has an impact on cost and set that feature up to send events to CloudZero for any cloud deployment.  In the future, if you see a cost anomaly or a cost decrease, you will be able to see the pattern of deployments to production to look for correlations.

<Callout icon="ℹ️" theme="info">
  Only the title and source in the data event payload are required. Many customers find it useful to also add a link (an `http` string to the build), and at least one of the filter values. You do not need to fill in all of the filter values, only whatever is easiest based on how you store and deploy your code.
</Callout>

# View Events

After you have sent at least one Event to the CloudZero system, you can view your Events in the Explorer.

When you are looking at hourly granularities in a seven-day or less view, you will see each event as a black line on the chart. Clicking on any of those lines will display the events slide-out on the right and allow you to view the details of that event.

When you are viewing granularities larger than hourly, such as daily, events will be aggregated up and shown as circles under the graph. Clicking on any of the circles will zoom in to that day on the graph.
