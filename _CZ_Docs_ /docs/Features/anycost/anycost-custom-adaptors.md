---
title: Creating AnyCost Custom Adaptors
category: features
createdAt: '2022-08-10'
hidden: false
slug: anycost-custom-adaptors
updatedAt: '2024-09-10'
---
An Adaptor is a piece of code that allows CloudZero to process cost data from any provider. You must write the Adaptor code yourself, and you can use any programming language. The Adaptor should take the following actions:

* Automatically retrieve cost data from any provider.
* Translate the cost data to [Common Bill Format](/docs/anycost-common-bill-format-cbf) (CBF) for CloudZero ingestion.
* Transfer the cost data to CloudZero:
  * [AnyCost Bucket Adaptors](/docs/anycost-bucket-getting-started) upload a gzipped CSV file of CBF data to an Amazon S3 bucket.
  * [AnyCost Stream Adaptors](/docs/anycost-stream-getting-started) send a JSON body of CBF data to the CloudZero AnyCost API.

After you write your Adaptor, you can create the AnyCost Connection in the CloudZero UI, and CloudZero ingests the cost data. See the following documentation for more details:

* [Connect an AnyCost Bucket Adaptor](/docs/anycost-bucket-getting-started)
* [Connect an AnyCost Stream Adaptor](/docs/anycost-stream-getting-started)

# Guidelines for writing code for an AnyCost Adaptor

AnyCost Adaptors give you the freedom of creating your own code to format data from any provider. This data can then be ingested into the CloudZero platform for analysis and reporting. The development of these adaptors is largely up to you, but there are some very specific guidelines you must  follow to ensure a smooth setup with the CloudZero infrastructure.

First, you must coordinate a way to receive cost data from your vendor, whether it is through APIs or generated exports.

Second, you must write the code that will translate that data into the CloudZero [Common Bill Format (CBF)](/docs/anycost-common-bill-format-cbf). CBF is the CloudZero standard file format for cost data ingestion, and it is the required format for successful ingestion of cost data into the CloudZero platform.

## Adaptor requirements

When writing an Adaptor, you must do the following:

* Convert provider cost data into the CloudZero Common Bill Format.
* Preserve information whenever possible.
  * Example: if a provider gives you hourly data, do not aggregate that data up to daily.
  * Example: if a provider gives you precise information about a charge, attempt to pass all of that information along into the Common Bill Format (CBF).
* Process data by month.
  * Each report update in a given month is cumulative.
  * Adaptors must include all billing data for a given month to date.
* Ensure that `cost/cost` and `cost/discounted_cost` sum to the same total
* AnyCost Bucket Adaptors only: Write cost data files to a folder in the S3 bucket. Do not upload the files into the root of the bucket.

## Adaptor recommendations

When writing an Adaptor, CloudZero recommends that you do the following:

* Amortize to hourly.
  * Data is viewable in the platform according to the lowest amortization supplied.
  * Data supplied hourly can be aggregated to hourly and up (for example, monthly).
  * Note: this rule can be skipped for non-usage based line items (for example, Taxes).
* Include taxes.
* Handle Discounts and Committed Use.
* Allow ingesting back data.
* Minimize the frequency of drops without clear business value,. Tthere is a cost to processing new data drops; do not drop data more often than the provider is giving significant new information.
* Work with cost data using appropriate data types in your programming language (for example, decimal.Decimal instead of float in Python).
* Do not populate the `bill/invoice_id` field until the provider has closed the invoice for the month that is being processed.

# Maintaining your AnyCost data

## How to DELETE a record or records

CloudZero loads data cumulatively, so each data drop for any given billing period replaces what was previously in the CloudZero platform.

To delete or remove data from CloudZero for a given billing period, send CloudZero a new data drop for that period that contains all records, minus the ones you want to remove.

## How to DELETE an entire billing period

To delete data for an entire billing period, send CloudZero an empty data drop, and because it replaces what is currently in the system, your data for that period will be removed.

<Callout icon="ℹ️" theme="info">
  An empty data drop is one that contains a manifest file with the appropriate billing data information and that points to a CSV with headers and no rows.
</Callout>

## How to UPDATE existing data

To update data already in the CloudZero system, send the edited data along with the rest of the data for that billing period. CloudZero replaces whatever is currently in the system with the data that is sent.

CloudZero loads cumulatively, so what you send for any particular billing period will entirely replace what is already there. Therefore, ensure the data drop for the rows you want to edit contains all the data for that billing period to avoid losing data.
