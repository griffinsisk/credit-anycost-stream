---
title: Idempotency
deprecated: false
hidden: false
metadata:
  robots: index
---
The CloudZero API V2 supports Idempotency via `cloudzero-idempotency-key` header. If a client passes the same value for the `cloudzero-idempotency-key` header for a possibly non-idempotent operation (e.g. PATCH), we will ensure that the operation is Idempotent by caching the response of the first request to the resource with that value for `cloudzero-idempotency-key`. The resource will return the same response, headers, status codes ... warts and all.

Currently, the `cloudzero-idempotency-key` applies to the HTTP *Path* and *Method* and is checked *before* any other code runs. This means a client will receive the same response to all subsequent requests to the same resource endpoint for the same `cloudzero-idempotency-key` value.