---
title: Filtering
deprecated: false
hidden: false
metadata:
  robots: index
---
Endpoints that support returning lots of data, usually but not always GETing a List of Resources, may support filtering.

If the endpoint supports filtering, it will return a `”filtering”` root key in the response:

```
"filtering": {
  "available": <list of filterable fields, their filterable values, and the types of these values >,
  "current": <list of objects describing current filtering>
}
```

This should be present in every response from filterable APIs, even if the user has not asked for filtering. For example, if I list all `insights` via `GET https://api.cloudzero.com/v2/insights`, I should see a response like:

```
"insights": [...],
"filtering": {
  "available": [
    {
      "field": "status",
      "valid_values": [
        "new",
        "in_progress",
        "on_hold",
        "addressed",
        "ignored"
      ],
      "valid_types": [
        "string"
      ]
    }
  ],
  "current": {
    "status": ["in_progress", "new"]
  }
}

```

A client controls the filtering of items via mapping the `field` key to a single `valid_values` parameter. These `field` key/value pairs are repeatable:

```
GET https://api.cloudzero.com/v2/insights?status=in_progress&status=new
```