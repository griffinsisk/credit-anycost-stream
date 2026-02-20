---
title: Testing
deprecated: false
hidden: false
metadata:
  robots: index
---
You can use the CloudZero API V2 in test mode, which does not affect your live data. You enable this via the `cloudzero-test-key` header.

If a client passes a value for the `cloudzero-test-key` header, then all subsequent requests within 1 Hour with the same `cloudzero-test-key` value will honor the resource state. After 1 Hour all resources created with a given `cloudzero-test-key` header are purged from the system.