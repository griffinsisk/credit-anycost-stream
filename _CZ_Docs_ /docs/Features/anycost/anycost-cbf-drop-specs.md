---
title: Configuring AnyCost Bucket File Drops
category: features
createdAt: '2022-08-17'
hidden: false
slug: anycost-cbf-drop-specs
updatedAt: ''
---
An AnyCost Bucket Adaptor sends Common Bill Format (CBF) cost data to CloudZero by uploading the data to an Amazon S3 bucket in your AWS account. This is called a file drop, and it must include the following two files:

* A gzipped CSV containing CBF data:
  * Encoded in UTF-8
  * Limited to a maximum of 1 million rows
* A JSON manifest file

# Files uploaded in a file drop

The Adaptor uploads these files to the following paths in the S3 bucket:

```
<root_path>/<billing_data_id>/<drop_id>/<data_file>.csv.gz
<root_path>/<billing_data_id>/manifest.json
```

The following explains this code:

`<root_path>`is a folder within the S3 Bucket where your adaptor will write data. This must be a folder and cannot be the root of the S3 Bucket.

`<billing_data_id>` represents an “atom” of billing data which will be added, removed, or updated as a complete unit.  It must represent a single month of billing data and be formatted as the first day of a month to the first day of the next month: `YYYYMMDD-YYYMMDD`.  For example, the billing data ID for the month of May 2022 would be: `20220501-20220601`. This limitation on the billing data ID (monthly granularity and specific format) may change in future versions.

`<drop_id>` is a unique identifier under which is a complete set of data for this `<billing_data_id>`.  Only one `<drop_id>` needs to exist.  If there is more than one, the current drop ID is indicated by the `manifest.json`.  This is useful for versioning.

When new data is available for this `<billing_data_id>` it should be added under a new `<drop_id>` and the `manifest.json` updated.  The old `<drop_id>` can then be removed or kept in case it is necessary to “revert”.  To remove all data associated with a `<billing_data_id>`, create an empty `<drop_id>` and point the manifest to that.

Although the `<drop_id>` may be any unique identifier, the best practice is to use a timestamp formatted to remove any special characters.  This makes it easy to see when billing drops were delivered and may be helpful for debugging.

For example, a new billing drop created on May 19, 2022 at 3:45:16PM UTC would have a drop ID of `20220519T154516Z`

<Callout icon="ℹ️" theme="info">
  IMPORTANT: CloudZero ingests cumulatively for each billing period indicated in a data drop. That is, all data for the time period provided in the `<billing_data_id>` replaces all existing data in the platform.

  With that in mind, ensure that your drops contain all the data for a given time period. If your provider supplies only incremental data drops (for example., each day you get that day's data, and not previous days' data), adaptors must include code that copies all of the previous data for the billing period into every data drop. Otherwise, you will lose all previous days in a billing period with each drop made.

  NOTE: Empty data drops will effectively remove all billing data for the supplied period. An empty drop is one containing a `<manifest.json>` file that points to a CSV file with headers and no rows.
</Callout>

`data_file>`.csv.gz represents zero or more gzipped [Common Bill Format (CBF)](/docs/anycost-common-bill-format-cbf) CSV files which contain the data for this `<billing_data_id>`.

manifest.json is the file that includes metadata about the current contents under the `<billing_data_id>` including the version and pointer to the current `<drop_id>`.  A change to the `manifest.json` file indicates the data under this `<billing_data_id>` should be re-ingested and completely replace any prior instance of data with the same `<billing_data_id>`.

<Callout icon="ℹ️" theme="info">
  Data will not be re-ingested unless the `manifest.json` is updated.
</Callout>

The following is an example of a manifest file:

```
{
  "version": "1.3.0",
  "current_drop_id":"YYYYMMDDTHHMMSSZ"
}
```

# CBF Drop example

The following is a simple example for a fake cloud provider “Simple Cloud”.  This example may also be [downloaded](https://downloads.cloudzero.com/generic_billing_format_examples/simple_cloud_billing_example.zip) for reference.

## Folder Structure

* simple_cloud/
  * 20220301-20220401/
    * 20220314T100216Z/
      * data_export-0001.csv.gz
    * 20220317T171218Z/
      * data_export-0001.csv.gz
    * manifest.json

`simple_cloud` is the `<root_path>` of the Billing Connection.  A single billing period is represented with data for the month of March.  The `<billing_data_id>` is `20220301-20220401`.  The folders under the `<billing_data_id>` are for different data drops.  Each one contains all the data for March at the time it was created.  A timestamp is used for the `<drop_id>`. This is not a requirement, but a useful convention.  In this example each file drop contains only a single gzipped CSV file; however for larger billing drops, there may be many files.

## &#x20;Manifest

The `manifest.json` file contains:

```
{
  "version": "1.3.0",
  "current_drop_id": "20220317T171218Z"
}
```

The `manifest.json` file references the `current_drop_id` which is `20220317T171218Z`.  The data under this `<drop_id>` contains all the data from the billing drop which occurred on March 14th (`20220314T100216Z`) plus any additional data from between the 14th and 17th. The billing drop from the 14th (`20220314T100216Z`) is no longer needed, but is kept for historical auditing purposes. If necessary, you could  “revert” to the prior billing drop (for period represented by the billing data ID `20220301-20220401`) by updating the manifest to reference `20220314T100216Z`.
