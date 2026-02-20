---
title: Standard Storage Class Exceeds Target Threshold
category: features
createdAt: '2023-07-19T13:00:00.000Z'
hidden: false
slug: excessive-gcp-standard-storage-usage
updatedAt: '2023-07-19T13:00:00.000Z'
---
This Recommendation focuses on optimizing GCP Cloud Storage classes based on spend. Standard class is the default and most expensive storage tier, ideally used for frequently accessed data. The threshold for Standard storage spend is 50%; additional spend over that can indicate that storage is not optimized. Moving data that is not frequently accessed to lower Storage classes can result in savings.

**Threshold**: This Recommendation is created if the total real cost spend on Standard storage class exceeds 50% of the total real cost for all GCP Cloud Storage and is at least $500. When the total spend for storage in Standard class falls below 50%, the Recommendation will automatically be closed.

GCP has three other storage classes that should be considered for less frequently accessed data:

**Nearline**: Ideal for data you plan to read or modify on average once per month or less.
Note: Data can be continuously added but should only be accessed monthly

**Coldline**: Ideal for data you plan to read or modify at most once a quarter.

**Archival**: Ideal for data that you plan to access less than once a year such as archived data, disaster recovery data, and so on

GCP also has Autoclass, a service that automatically transitions objects in your bucket to appropriate storage classes based on each object's access pattern. This is a great option for data that may have changing patterns.

Pricing costs for each storage class in each region can be found [in the Google Cloud documentation](https://cloud.google.com/storage/pricing).

The 90-day cost graph shows the daily total spend for all GCP Cloud Storage resources with Standard Storage class and highlights the top five resources with the highest spend to consider optimizing.
