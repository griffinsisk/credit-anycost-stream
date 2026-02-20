---
title: AnyCost
category: features
createdAt: '2022-08-03'
hidden: false
slug: anycost
updatedAt: '2024-09-10T14:34:33.610Z'
---
With the CloudZero AnyCost framework, you can ingest cost data from any source and automate the processing of that data. Using the CloudZero tools, you can send cost data from different vendors to CloudZero on the schedule you prefer. Then you can register a new Billing Connection that automatically detects, ingests, and integrates that data into the CloudZero platform.

AnyCost uses CloudZero's Common Bill Format (CBF), a standard data model to ingest cost data from any source. CBF accommodates many types of cost data, including taxes, discounts, credits, and more. For details, see [Common Bill Format](/docs/anycost-common-bill-format-cbf).

# Adaptors

To ingest any vendor's cost data, you must [create an Adaptor](/docs/anycost-custom-adaptors). These Adaptors are code that run in your own environments, translate a single vendor's cost data into the Common Bill Format, and transfer the data to CloudZero on an automated schedule.

For example, if a vendor makes cost data available only once a day, you will likely transfer data to CloudZero only once every day. However, some vendors have Billing or Cost APIs that provide cost data on a more frequent basis, and for those you may decide to transfer cost data every eight hours or even hourly.

If you have five vendors whose cost data you want CloudZero to ingest, you will need to create five AnyCost Adaptors, one per vendor.

# Adaptor Types

CloudZero supports two types of AnyCost Adaptors:

* An [**AnyCost Bucket Adaptor**](/docs/anycost-bucket-getting-started) uploads cost data to an AWS S3 bucket.
* An [**AnyCost Stream Adaptor**](/docs/anycost-stream-getting-started) sends cost data directly to the CloudZero REST API.

To help you choose the AnyCost Adaptor type that you need to create, refer to the following table outlining the key differences:

| **Attribute**                 | **AnyCost Bucket Adaptor**                                                      | **AnyCost Stream Adaptor**                                              |
| ----------------------------- | ------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Method of transmitting data   | Upload a gzipped CSV file of cost data to S3                                    | Send a JSON request body with records of cost data to the CloudZero API |
| Required cloud infrastructure | Amazon Web Services S3 bucket                                                   | None                                                                    |
| Maximum size of cost data     | No maximum                                                                      | Currently, 5MB request body (uncompressed)                              |
| JSON manifest required        | Yes                                                                             | No                                                                      |
| Required actions              | Create manifest, convert raw data to CBF-formatted file, send file to CloudZero | Convert raw data to CBF, send CBF to CloudZero                          |
| Supported cost source         | Any                                                                             | Any                                                                     |

CloudZero recommends that you create an AnyCost Bucket Adaptor if you use AWS and need to transfer large volumes of cost data without size limitations.

If your cost data fits within a 5MB JSON request body, consider creating an AnyCost Stream Adaptor for simpler implementation. AnyCost Stream Adaptors are cloud-agnostic.

# Billing Connections

Before you can start transferring cost data to CloudZero, you must [register the Adaptor as a Billing Connection in the CloudZero UI](/docs/connections-custom#/). The Billing Connection will begin to ingest your custom cost data.

Billing Connections report the health and status of the automated ingestion process and  indicate if there are issues with the Common Bill Format syntax or transmission of data.
