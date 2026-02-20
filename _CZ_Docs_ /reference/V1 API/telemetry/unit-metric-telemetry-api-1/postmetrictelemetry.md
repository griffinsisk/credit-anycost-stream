---
title: Post metrics records
excerpt: >
  A new public endpoint is available to send CloudZero Unit Metric telemetry
  data. This endpoint allows you to send Unit Metric data that will
  automatically be available in the CloudZero Analytics platform after the next
  data ingest.


  **Note**: This endpoint is the legacy version of
  `/unit-cost/v1/telemetry/metric/{metric_name}/sum`. It is functionally
  identical, but predates the operational path parameter concept.
api:
  file: telemetry.yaml
  operationId: postMetricTelemetry
hidden: false
---