---
title: Post telemetry records
excerpt: >-
  Allocation telemetry provides additional information that the CloudZero system
  can use to split your cloud cost data through custom allocation dimensions. In
  this way, you can gain further insights into the costs of your multi-tenant
  systems, shared infrastructure, and more.


  The `telemetry_stream_name` sent to this API can be used in the `Streams`
  parameter of an `AllocateByStreams`

  custom dimension (see
  https://docs.cloudzero.com/docs/allocation-short-form-rules#allocatebystreams-short-form-rule)



  **Note**: This endpoint is the legacy version of
  `/unit-cost/v1/telemetry/allocation/{telemetry_stream_name}/sum`. It is
  functionally identical, but predates the operational path parameter concept.
api:
  file: telemetry.yaml
  operationId: postAllocationTelemetry
hidden: false
---