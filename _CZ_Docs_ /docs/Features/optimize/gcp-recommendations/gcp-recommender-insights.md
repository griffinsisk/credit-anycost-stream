---
title: Supported GCP Recommenders
category: features
createdAt: '2024-07-18T12:44:28.000Z'
hidden: false
slug: gcp-recommender-insights
updatedAt: '2024-07-18T12:44:28.000Z'
---
CloudZero supports ingestion of GCP Recommender data, which includes insights and recommendations to optimize resource usage. Insights identify issues such as overpayments for reserved instances, while recommendations suggest corrective actions, like modifying your reservation plan.

<Callout icon="ℹ️">
  To ingest GCP Recommender data, set up a [GCP Billing connection](/docs/connections-gcp-billing) first, and then set up a [GCP Recommender connection](/docs/connections-gcp-recommender).
</Callout>

The following Recommenders are supported:

* [Change Over-Provisioned SQL Instance](https://cloud.google.com/sql/docs/mysql/recommender-sql-overprovisioned)
* [Delete Idle Address Recommender](https://cloud.google.com/compute/docs/viewing-and-applying-idle-resources-recommendations)
* [Delete Idle Disk Recommender](https://cloud.google.com/compute/docs/viewing-and-applying-idle-resources-recommendations)
* [Delete Idle Image Recommender](https://cloud.google.com/compute/docs/viewing-and-applying-idle-resources-recommendations)
* [Snapshot and Delete Idle Provisioned Disks](https://cloud.google.com/compute/docs/viewing-and-applying-idle-resources-recommendations)
* [Stop Idle VM Instances Recommender](https://cloud.google.com/compute/docs/instances/idle-vm-recommendations-overview)
* [VM Machine Type Recommender](https://cloud.google.com/compute/docs/instances/apply-machine-type-recommendations-for-instances)
