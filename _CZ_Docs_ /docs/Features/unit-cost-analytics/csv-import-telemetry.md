---
title: Telemetry Stream CSV Import
category: features
createdAt: '2024-09-12T19:40:03.416Z'
hidden: false
slug: csv-import-telemetry
updatedAt: '2025-01-27T19:40:03.416Z'
---
A telemetry stream provides CloudZero with cloud usage data to help you ensure your business is maximizing profit when delivering cloud-based services. CloudZero allows you to create and update a **unit cost metric** or **allocation** telemetry stream through the user interface by uploading a CSV file with telemetry data. This can be a convenient alternative to sending telemetry stream data to the [CloudZero API](https://docs.cloudzero.com/reference/summetrictelemetry).

<Image align="center" alt="Telemetry Streams page listing existing unit cost metric and allocation streams" border={true} src="https://downloads.cloudzero.com/documentation/resources/telemetry-csv-streams-page.png" className="border" />

<Callout icon="📘" theme="info">
  The maximum CSV file size is 3MB.
</Callout>

# Unit Cost Metric versus Allocation

When you create a telemetry stream, it is important to understand the difference between a [**unit cost metric**](#unit-cost-metric-overview) and an [**allocation**](#allocation-overview), and when it is appropriate to use each one.

## Unit Cost Metric overview

A [unit cost metric](#create-a-unit-cost-metric-telemetry-stream-in-the-cloudzero-ui) is a measurement of how efficiently your company is operating in the cloud, calculated as cloud cost divided by unit of demand. You can choose the unit of demand that is appropriate to track for your business. For example, if you are a food delivery platform, your unit of demand might be the `number of orders processed`. The unit cost metric, then, is your `cost per order`.

Tracking unit cost metrics helps you gauge whether your business is operating efficiently. Even if your total cloud costs increase, a decreased unit cost metric indicates that your business is scaling efficiently, because you are spending less money to process each transaction.

You can associate a unit cost metric with the cost data for a particular dimension, such as products your company sells. This allows you to further refine your analysis by determining `cost per order per product`, for example.

## Allocation overview

In contrast, an [allocation](#create-an-allocation-telemetry-stream-in-the-cloudzero-ui) is a way to split cloud costs into new categories based on actual usage. For example, if you have an AWS RDS database that is shared across engineering teams, you can create an allocation that assigns the actual number of RDS writes to a given team name. You could then reference one or more allocation streams directly in your [CostFormation definitions](/docs/costformation-definition-language-guide#adding-allocations) as a source of data when crafting Custom Dimensions. Each element name defined in your stream, in this case, an engineering team's name, corresponds to an element that exists within the Dimension. In this example, Team Alpha is an element in the Engineering Team Dimension.

You can associate an allocation with an additional Dimension's cost data. For example, you might want to see each engineering team's RDS usage split across a Product Dimension. This allows you to determine how much money each team is spending on RDS to develop each of your company's products, for example.

<Callout icon="ℹ️" theme="info">
  To learn how unit cost metrics and allocations can help you manage cloud costs more efficiently, see [What Is Cloud Unit Economics (CUE)? A Comprehensive And, More Importantly, Fun Guide](https://www.cloudzero.com/guide/cloud-unit-economics/).
</Callout>

# Create a Unit Cost Metric Telemetry Stream in the CloudZero UI

A unit cost metric telemetry stream sends CloudZero the data required to calculate a unit cost metric for your organization. For example, you can use the CloudZero UI to upload a CSV file that lists your number of orders per day or per month. After you create a unit cost metric stream, you can create [Analytics dashboards](/docs/edit-dashboard) to track your unit cost metrics over time.

## Upload the Unit Cost Metric CSV file

Include the following data in each row of the CSV file you intend to upload:

* Required: Timestamp in any format. For example, `2024-09-01` or `2024-09-01T12:00:00Z`.
* Required:  Unit value. Must be greater than 0. For example, `200` to represent the number of orders for that day or month.
* Optional: Up to five dimension elements (one per column). This allows you to associate additional cost data with the unit cost metric you create. For example, if you provide an `Engineering Team` column, you can associate each engineering team value in the column with the `cost per order` in order to calculate the `cost per order per engineering team`.

The first row of the CSV file should list the column names, and you can use any names you like.

To create a unit cost metric telemetry stream by uploading a CSV to the CloudZero UI:

1. Navigate to [**Settings** > **Telemetry Streams**](https://app.cloudzero.com/settings/telemetry).

2. Select **Create New Stream** > **New Unit Cost Metric Stream**.

   <Image align="center" alt="Select Create New Stream > New Unit Cost Metric Stream" border={true} src="https://downloads.cloudzero.com/documentation/resources/telemetry-csv-create-new-unit-cost-stream-1.png" className="border" />

3. Enter a stream **Name**, such as `engineering-team-orders`. You cannot change this value after you create the stream. The name can include up to 256 letters, digits, underscores, periods, or hyphens in any combination.

4. Optionally, enter a **Description** for the stream.

5. Set **Granularity** of data in the stream to **Daily** (default) or **Monthly**. You cannot change this setting after you create the stream.

   Granularity determines the time period used to track data changes:

   * Daily granularity lets you track how unit values change from day to day.
   * Monthly granularity lets you track how unit values change from month to month.

   Any data provided at a finer level of granularity will be aggregated. For example, if you provide hourly data but choose **Daily**, all of the hourly values for a given metric will be combined into a single value for the day.

6. Optionally, check the **Fill gaps in time?** box to allow CloudZero to add data for missing timestamps based on data for the preceding timestamp. The added data will appear in Analytics and the Explorer.

   With this setting enabled, if your stream's granularity is set to monthly and you provide data for January, February, and April but _not March_, for example, CloudZero uses the value of the preceding timestamp to fill in the missing month:

   * January: 20
   * February: 23
   * _March: 23 (value copied from February)_
   * April: 25

   Likewise, if your stream's granularity is set to daily and you provide data for July 1, 2, and 5, CloudZero creates timestamps for July 3 and 4 using the value from July 2:

   * July 1: 150
   * July 2: 100
   * _July 3: 100 (value copied from July 2)_
   * _July 4: 100 (value copied from July 2)_
   * July 5: 75

7. In the **Upload CSV File** section, select your CSV file or drag and drop the file into the field. You can replace the CSV file with a new one at any point before creating the stream. The maximum file size is 3MB.

   <Image align="center" alt="Select or drag and drop a CSV file" border={true} src="https://downloads.cloudzero.com/documentation/resources/telemetry-csv-select-file-2.png" className="border" />

8. Select the **Timestamp** drop-down menu to choose the timestamps column from your CSV file.

9. Select the **Unit value** drop-down menu to choose the unit values column from your CSV file.

10. Optionally, select a target Dimension from the **Target Dimension (Optional)** drop-down menu. This menu displays all of your organization's Dimensions, including CloudZero-defined and user-defined Dimensions.

    Selecting a target Dimension enables you to associate the metric with cost data from a specific Dimension so you can determine the cost per unit per Dimension element. For example, you can select an `Engineering Team` Dimension to calculate `cost per order per engineering team`.

    1. If you selected a target Dimension, you must select an elements column in your CSV from the **Dimension Element** drop-down menu. This column provides the values that correspond to the target Dimension. For example, if your CSV file has a `Team` column that includes a value such as `Team Alpha` or `Team Beta` for each row, select the `Team` column from this drop-down menu.
    2. Optionally, select the **+** (plus sign) beneath the first target Dimension to add more target Dimensions and elements. Any CSV columns not mapped to a Dimension will be ignored when the stream is created.

       Note that you cannot change the target dimensions after you create the stream.

       <Image align="center" alt="Select a target dimension and then an element column" border={true} src="https://downloads.cloudzero.com/documentation/resources/telemetry-csv-unit-metric-dimensions-1.png" className="border" />

11. Ensure the **CSV Reference Table** shows your data as you expect it and that there are no errors displayed.

    <Image align="center" alt="Review the CSV Reference Table" border={true} src="https://downloads.cloudzero.com/documentation/resources/telemetry-csv-import-reference-table.png" className="border" />

    If there is an error message, such as a type mismatch, you can select an invalid value in the CSV Reference Table and type in a new value. You can also reassign columns or upload a new CSV file.

12. Optionally, select **Export to CSV** to download a copy of the data in the CSV Reference Table. This is useful if you have manually edited any cell values to resolve errors and want to download a CSV file that includes the updated data.

13. Select **Save**.

After CloudZero creates your stream, you are redirected to the [Telemetry Streams](https://app.cloudzero.com/settings/telemetry) page, where you can see your new unit cost metric stream in the table. Its status will change from **Pending** to **Available** after CloudZero ingests the data.

Note that it can take up to 24 hours for CloudZero to ingest the data from a new stream.

<Image align="center" alt="The Telemetry Streams page shows the unit cost metric stream you created" border={true} src="https://downloads.cloudzero.com/documentation/resources/telemetry-csv-list-streams.png" className="border" />

## View the Unit Cost Metric Stream details

From the [Telemetry Streams](https://app.cloudzero.com/settings/telemetry) page, you can select the name of a unit cost metric stream to view its details page, where you can take the following actions:

* [Add and/or replace records by uploading another CSV file](#update-the-unit-cost-metric-stream)
* Update the stream description
* Delete the stream
* Download a CSV file of recent records (the last seven days)
* View information about the stream, including:
  * Stream type (`Unit Cost Metric`)
  * Granularity of data (`Daily` or `Monthly`)
  * Status (`Pending` or `Available`)
  * Source (`CSV` and/or `API`)
  * Targeted dimensions
  * Activity of records ingestion
  * An [example of a payload](#view-example-unit-cost-metric-api-payload) you can send to the CloudZero API (streams with target dimensions only)

<Image align="center" alt="The unit cost metric stream details page" border={true} src="https://downloads.cloudzero.com/documentation/resources/telemetry-csv-unit-metric-details-page-2.png" className="border" />

## View example Unit Cost Metric API payload

If you configured the unit cost metric stream with one or more target Dimensions, you can view a sample API payload by selecting the **API Example** button near the **Targeted Dimensions** list.

<Image align="center" alt="Select API Example to view a sample API payload for your unit cost metric stream" border={true} width="400px" src="https://downloads.cloudzero.com/documentation/resources/telemetry-csv-unit-cost-api-example-button-1.png" className="border" />

The API example includes the following information:

* The API URL of your unit cost metric stream, for example: `https://api.cloudzero.com/unit-cost/v1/telemetry/metric/{your-unit-cost-stream-name}`. To post records to your stream using a specific type of operation, append the following paths to your API URL:
  * [/sum](https://docs.cloudzero.com/reference/summetrictelemetry)
  * [/replace](https://docs.cloudzero.com/reference/replacemetrictelemetry)
  * [/delete](https://docs.cloudzero.com/reference/deletemetrictelemetry)
* A sample payload for the predecing operations, pre-filled with your granularity settings and associated costs (target Dimensions). For example:

  ```json
  {
      "records": [
          {
              "timestamp": "<your timestamp here>",
              "value": "<number greater than 0>",
              "associated_cost": {
                  "custom:Engineering Team": "<your value here>"
              }
          }
      ]
  }
  ```

<Image align="center" alt="The API URL and a sample payload customized for your unit cost metric stream" border={false} width="400px" src="https://downloads.cloudzero.com/documentation/resources/telemetry-csv-unit-cost-api-example-2.png" />

## Update the Unit Cost Metric Stream

You can update the unit cost metric stream by uploading a new CSV file. The CSV file adds new records or replaces existing ones based on the record date:

* If a record in the CSV file has the same data as an existing record _except for the unit value_, the CSV record will replace (overwrite) the existing record.
* If a record in the CSV file has data that does not match any existing records, the CSV record will be added as a new entry.

To add and or replace records in a unit cost metric stream:

1. From the [Telemetry Streams](https://app.cloudzero.com/settings/telemetry) page, select the name of the unit cost metric stream you want to update.

2. Optionally, update the stream **Description**.

3. Optionally, check the **Fill gaps in time?** box to allow CloudZero to add data for missing timestamps based on data for the preceding timestamp.

4. In the **Upload CSV** section, select your CSV file or drag and drop the file into the field. You can replace the CSV file with a new one at any point before you select **Update**.

   <Image align="center" alt="Select or drag and drop a CSV file to update stream records" border={true} src="https://downloads.cloudzero.com/documentation/resources/telemetry-csv-update-records-from-details-page-2.png" className="border" />

5. Select the **Timestamps** drop-down menu to choose the timestamps column from your CSV file.

6. Select the **Unit value** drop-down menu to choose the unit values column from your CSV file.

7. If you selected a target Dimension when you created the stream, select the corresponding elements column in your CSV file from the **Dimension Element** drop-down menu.

   <Image align="center" alt="Select an elements column from the drop-down menu" border={true} src="https://downloads.cloudzero.com/documentation/resources/telemetry-csv-unit-metric-update-records-1.png" className="border" />

8. Ensure the **CSV Reference Table** shows your data as you expect it and that there are no errors displayed.

   If there is an error message, such as a type mismatch, you can select an invalid value in the CSV Reference Table and type in a new value. You can also remap columns or upload a new CSV file.

9. Optionally, select **Export to CSV** to download a copy of the data in the CSV Reference Table. This is useful if you have manually edited any cell values to resolve errors and want to download a CSV that includes the updated data.

10. Select **Update**.

CloudZero displays a message stating how many records it successfully updated. The updated records appear in CloudZero after the next data ingest.

# Create an Allocation Telemetry Stream in the CloudZero UI

An **allocation telemetry stream** sends CloudZero the data required to calculate an allocation. For example, you can use the CloudZero UI to upload a CSV file that lists the number of RDS writes per day or per month for each engineering team. After you create an allocation stream, you can create a custom dimension from it using [CostFormation](/docs/costformation-definition-language-guide#adding-allocations).

## Upload the Allocation CSV File

Include the following data in each row of the CSV you intend to upload:

* Required: Timestamp in any format. For example, `2024-09-01` or `2024-09-01T12:00:00Z`.
* Required: Allocation value. Must be greater than 0. For example, `1000` to represent the number of RDS writes for that day or month.
* Required: Element name. For example, `Team Alpha` to associate the number of RDS writes per day with the Alpha engineering team.
* Optional: Up to five dimension elements (one per column). This allows you to associate additional data sources with the allocation. For example, if you provide a `Product` column, you can associate each product in the column with the number of RDS writes per team in order to calculate the number of RDS writes per team per product.

The first row of the CSV file should list the column names, and you can use any names you like.

To create an allocation telemetry stream by uploading a CSV file to the CloudZero UI:

1. Navigate to [**Settings** > **Telemetry Streams**](https://app.cloudzero.com/settings/telemetry).

2. Select **Create New Stream** > **New Allocation Stream**.

   <Image align="center" alt="Select Create New Stream > New Allocation Stream" border={true} src="https://downloads.cloudzero.com/documentation/resources/telemetry-csv-create-new-allocation-stream-1.png" className="border" />

3. Enter a stream **Name**, such as `rds-writes-by-team`. You cannot change this value after you create the stream. The name can include up to 256 letters, digits, underscores, periods, or hyphens in any combination.

4. Optionally, enter a **Description** for the stream.

5. Set **Granularity** of data in the stream to **Hourly**, **Daily** (default), or **Monthly**. You cannot change this value after you create the stream.

   Granularity determines the time period used to track data changes:

   * Hourly granularity lets you track how allocation values change from hour to hour.
   * Daily granularity lets you track how allocation values change from day to day.
   * Monthly granularity lets you track how allocation values change from month to month.

   Any data provided at a finer level of granularity will be aggregated. For example, if you provide hourly data but choose **Daily**, all of the hourly values for a given element will be combined into a single value for the day.

6. Optionally, check the **Fill gaps in time?** box to allow CloudZero to add data for missing timestamps based on data for the preceding timestamp. The added data will appear in Analytics and Explorer.

   With this setting enabled, if your stream's granularity is set to monthly and you provide data for January, February, and April but _not March_, for example, CloudZero uses the value of the preceding timestamp to fill in the missing month:

   * January: 20
   * February: 23
   * _March: 23 (value copied from February)_
   * April: 25

   Likewise, if your stream's granularity is set to daily and you provide data for July 1, 2, and 5, CloudZero creates timestamps for July 3 and 4 using the value from July 2:

   * July 1: 150
   * July 2: 100
   * _July 3: 100 (value copied from July 2)_
   * _July 4: 100 (value copied from July 2)_
   * July 5: 75

7. In the **Upload CSV File** section, select your CSV file or drag and drop the file into the field. You can replace the CSV file with a new one at any point before creating the stream. The maximum file size is 3MB.

   <Image align="center" alt="Select or drag and drop a CSV file" border={true} src="https://downloads.cloudzero.com/documentation/resources/telemetry-csv-allocation-select-file-2.png" className="border" />

8. Select the **Timestamp** drop-down menu to choose the timestamps column from your CSV.

9. Select the **Allocation value** drop-down menu to choose the allocation values column from your CSV.

10. Select the **Element name** drop-down menu to choose the element names column from your CSV. If you use the allocation stream to [create a Dimension](/docs/costformation-definition-language-guide#defining-a-custom-dimension) later, these values become the element names in the dimension.

11. Optionally, select a target dimension from the **Target Dimension (Optional)** drop-down menu. This menu displays all of your organization's dimensions, including CloudZero-defined and user-defined Dimensions.

    Selecting a target Dimension enables you to associate the allocation with cost data from an existing Dimension so you can group the allocated usage by each element in the selected Dimension. For example, you can select the `Product` Dimension to calculate `number of RDS writes per engineering team per product`.

    1. If you selected a target Dimension, you must select an elements column in your CSV file from the **Dimension Element** drop-down menu. This column provides the values that correspond to the target dimension. For example, if your CSV file has a `Product` column that includes a value such as `Analytics` or `AI Solutions` for each row, select the `Product` column from this drop-down.
    2. Optionally, select the **+** (plus sign) beneath the first target dimension to add more target Dimensions and elements. Any CSV columns not mapped to a Dimension will be ignored when the stream is created.

       Note that you cannot change the target Dimensions after you create the stream.

       <Image align="center" alt="Select a target Dimension and then an element column" border={true} src="https://downloads.cloudzero.com/documentation/resources/telemetry-csv-allocation-dimensions-1.png" className="border" />

12. Ensure the **CSV Reference Table** shows your data as you expect it and that there are no errors displayed.

    <Image align="center" alt="Review the CSV Reference Table" border={true} src="https://downloads.cloudzero.com/documentation/resources/telemetry-csv-import-reference-table.png" className="border" />

    If there is an error message, such as a type mismatch, you can select an invalid value in the CSV Reference Table and type in a new value. You can also remap columns or upload a new CSV file.

13. Optionally, select **Export to CSV** to download a copy of the data in the CSV Reference Table. This is useful if you have manually edited any cell values to resolve errors and want to download a CSV that includes the updated data.

14. Select **Save**.

After CloudZero creates your stream, you are redirected to the [Telemetry Streams](https://app.cloudzero.com/settings/telemetry) page, where you can see your new allocation stream in the table.Its status will change from **Pending** to **Available** after CloudZero ingests the data.

Note that it can take up to 24 hours for CloudZero to ingest the data from a new stream.

<Image align="center" alt="The Telemetry Streams page shows the allocation stream you created" border={true} src="https://downloads.cloudzero.com/documentation/resources/telemetry-csv-list-allocation-streams.png" className="border" />

## View the Allocation Stream Details

From the [Telemetry Streams](https://app.cloudzero.com/settings/telemetry) page, you can select the name of an allocation stream to view its details page, where you can take the following actions:

* [Add and/or replace records by uploading another CSV file](#update-the-allocation-stream)
* Update the stream description
* Delete the stream
* Download a CSV file of recent records (the last 7 days)
* View information about the stream, including:
  * Stream type (`Allocation`)
  * Granularity of data (`Daily`, `Hourly`, or `Monthly`)
  * Status (`Pending` or `Available`)
  * Source (`CSV` and/or `API`)
  * Targeted dimensions
  * Activity of records ingestion
  * An [example of a payload](#view-example-allocation-api-payload) you can send to the CloudZero API (streams with target dimensions only)

<Image align="center" alt="The allocation stream details page" border={true} src="https://downloads.cloudzero.com/documentation/resources/telemetry-csv-allocation-details-page-2.png" className="border" />

## View example Allocation API payload

If you configured the allocation stream with one or more target Dimensions, you can view a sample API payload by selecting the **API Example** button near the **Targeted Dimensions** list.

<Image align="center" alt="Select API Example to view a sample API payload for your allocation stream" border={true} width="400px" src="https://downloads.cloudzero.com/documentation/resources/telemetry-csv-allocation-api-example-button-1.png" className="border" />

The API example includes the following information:

* The base API URL of your allocation stream, for example: `https://api.cloudzero.com/unit-cost/v1/telemetry/allocation/{your-allocation-stream-name}`. To post records to your stream using a specific type of operation, append the following paths to your API URL:
  * [/sum](https://docs.cloudzero.com/reference/sumallocationtelemetry)
  * [/replace](https://docs.cloudzero.com/reference/replaceallocationtelemetry)
  * [/delete](https://docs.cloudzero.com/reference/deleteallocationtelemetry)
* A sample payload for the preceding operations, pre-filled with your granularity settings and filters (target dimensions). For example:

  ```json
  {
      "records": [
          {
              "timestamp": "<your timestamp here>",
              "granularity": "DAILY",
              "value": "<number greater than 0>",
              "filter": {
                  "custom:Product": [
                      "<your value here>"
                  ]
              },
              "element_name": "<your element_name here>"
          }
      ]
  }
  ```

<Image align="center" alt="The API URL and a sample payload customized for your allocation stream" border={true} width="400px" src="https://downloads.cloudzero.com/documentation/resources/telemetry-csv-allocation-api-example-2.png" className="border" />

## Update the Allocation Stream

You can update the allocation stream by uploading a new CSV file. The CSV file adds new records or replaces existing ones based on the record date:

* If a record in the CSV file has the same data as an existing record _except for the allocation value_, the CSV record will replace (overwrite) the existing record.
* If a record in the CSV file has data that does not match any existing records, the CSV record will be added as a new entry.

To add and or replace records in an allocation stream:

1. From the [Telemetry Streams](https://app.cloudzero.com/settings/telemetry) page, select the name of the allocation stream you want to update.

2. Optionally, update the stream **Description**.

3. Optionally, check the **Fill gaps in time?** box to allow CloudZero to add data for missing timestamps based on data for the preceding timestamp.

4. In the **Upload CSV file** section, select your CSV file or drag and drop the file into the field. You can replace the CSV with a new one at any point before you select **Update**.

   <Image align="center" alt="Select or drag and drop a CSV file to update stream records" border={true} src="https://downloads.cloudzero.com/documentation/resources/telemetry-csv-update-allocation-records-from-details-page-2.png" className="border" />

5. Select the **Timestamp** drop-down menu to choose the timestamps column from your CSV.

6. Select the **Allocation Value** drop-down menu to choose the allocation values column from your CSV file.

7. Select the **Element name** drop-down menu to choose the element names column from your CSV file.

8. If you selected a target Dimension when you created the stream, select the corresponding elements column in your CSV file from the drop-down menu.

   <Image align="center" alt="Select an elements column from the drop-down menu" border={true} src="https://downloads.cloudzero.com/documentation/resources/telemetry-csv-allocation-update-records-1.png" className="border" />

9. Ensure the **CSV Reference Table** shows your data as you expect it and that there are no errors displayed.

   If there is an error message, such as a type mismatch, you can select an invalid value in the CSV Reference Table and type in a new value. You can also remap columns or upload a new CSV file.

10. Optionally, select **Export to CSV** to download a copy of the data in the CSV Reference Table. This is useful if you have manually edited any cell values to resolve errors and want to download a CSV that includes the updated data.

11. Select **Update**.

CloudZero displays a message stating how many records it successfully updated. The updated records appear in CloudZero after the next data ingest.

# Delete a Telemetry Stream

To delete a unit cost metric or allocation telemetry stream through the [Telemetry Streams](https://app.cloudzero.com/settings/telemetry) page:

1. Select the three-dot icon in the **Actions** column for the stream you intend to delete.
2. Click the **Delete Telemetry Stream** button.
3. Type the name of the stream into the dialog box.
4. Select **Delete**.

<Image align="center" alt="Select the three-dot icon to display the Actions menu" border={true} src="https://downloads.cloudzero.com/documentation/resources/telemetry-csv-delete-stream-actions-icon.png" className="border" />

To delete a telemetry stream through the stream's details page:

1. Click the **Delete Stream** button.
2. Type the name of the stream into the dialog box.
3. Select **Delete**.

CloudZero completes the stream deletion within one hour.
