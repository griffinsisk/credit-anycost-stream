---
title: Sorting
deprecated: false
hidden: false
metadata:
  robots: index
---
Endpoints that support returning lots of data, usually but not always GETing a List of Resources, may support sorting.

If the endpoint supports sorting, it will return a `”sorting”` root key in the response:

```
"sorting": {
  "available": <list of sortable properties>,
  "current": <list of objects describing current sorting>,
  "ordering": <list of available sort orders, usually just "asc" and "desc">
}
```

This should be present in every response from sortable APIs, even if the user has not asked for sorting. For example, if I list all `insights` via `GET https://api.cloudzero.com/v2/insights`, I should see a response like:

```
"insights": [...],
"sorting": {
  "available": ["category", "cost_impact", "effort", "last_updated", "status", "title"],
  "current": [
    {
      "sort_key": "status",
      "sort_order": "asc"
    }
  ],
  "ordering": ["asc", "desc"],
}
```

A client controls the sorting of items via the `sort_key` and `sort_order` parameters:

```
GET https://api.cloudzero.com/v2/insights?sort_key=last_updated&sort_order=asc
```