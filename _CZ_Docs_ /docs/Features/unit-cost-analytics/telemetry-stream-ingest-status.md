---
title: Telemetry Stream Ingest Status
category: features
createdAt: '2022-01-12T19:40:03.416Z'
hidden: false
slug: telemetry-stream-ingest-status
updatedAt: '2022-01-12T19:47:59.644Z'
---
The Telemetry Streams [page](https://app.cloudzero.com/telemetry) in the CloudZero platform includes an Ingest Status column that describes the current state of each stream, the type of stream, and whether the stream is available when you are authoring Dimensions. Every possible status is listed on this page along with an explanation of what it means.

# Loading

This status means that a new telemetry stream has received records and been created, but has not yet been fully ingested. The ingest process typically completes within eight hours of the initial stream creation.

# Available

An `Available` stream is healthy and available for use when authoring Allocation Dimensions.

# Invalid

A stream is marked as `Invalid` when it targets one or more invalid Dimensions. A Dimension will be invalid if it gets deleted or enters a bad state. To determine the exact cause of the issue, CloudZero recommends reviewing your CostFormation definitions.

The Telemetry Streams page will underline any invalid Dimensions under the `Target` column.

<Image align="center" alt="Invalid Dimension underlined in the Target column" border={true} width="355" src="https://files.readme.io/0a6258f-Screen_Shot_2022-01-12_at_11.47.18_AM.png" className="border" />

New telemetry records sent to an invalid stream will still be received and processed, but the stream will be unavailable in the product until the Ingest Status returns to `Available`.
