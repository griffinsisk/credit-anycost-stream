---
title: Pagination
deprecated: false
hidden: false
metadata:
  robots: index
---
Endpoints that support returning lots of data, usually but not always GETing a List of Resources, support dual-cursor pagination.

If the endpoint supports pagination, it will return a `”pagination”` root key in the response:

```
"pagination": {
  "page_count": <number of total pages>,
  "item_count": <number of items in this response>,
  "total_count": <total number of items in all pages>,
  "cursor": {
    "next_cursor": <cursor parameter for next page>,
    "previous_cursor": <cursor parameter for previous page>,
    "has_next": <true if next_cursor>,
    "has_previous": <true if previous cursor>
  }
}
```

This should be present in every response from paginated APIs, even if the user has not asked for pagination or if all of the data fits into one response. For example, if I list all `insights` via `GET https://api.cloudzero.com/v2/insights` and I don’t have any, I would still get a response like:

```
{
  "pagination": {
    "page_count": 0,
    "item_count": 0,
    "total_count": 0,
    "cursor": {
      "next_cursor": null,
      "previous_cursor": null,
      "has_next": false,
      "has_previous": false
    }
  },
  "insights": []
}
```

A client controls the number of items per page via the `limit` parameter.

```
GET https://api.cloudzero.com/v2/insights?limit=5
```

might return

```
{
  "pagination": {
    "page_count": 3,
    "item_count": 5,
    "total_count": 15,
    "cursor": {
      "next_cursor": "H4sIAL1Fs2EC/yWKQQqAMAwEv1Jy9uqlnynBpFiMRJooiPh3o952ZvYC0+5l4RNyAkHzsm+EzgRD+pt24v5WtOmVcyMunU3liFdOFcU4vLS1efAYW2s1/uB+ANRxjWxiAAAA",
      "previous_cursor": null,
      "has_next": true,
      "has_previous": false
    }
  },
  "insights": [...]
}
```

The `next_cursor` and `previous_cursor` returned are opaque strings that can be used to grab the next and previous pages of data respectively. A client does so simply by passing the **_urlencoded _**value of `next_cursor` or `previous_cursor` via the `cursor` parameter:

> 🚧 URL Encoding Cursors
> 
> Remember to url encode the cursor before sending it up as a query parameter!
> 
> We do it this way to accommodate both Web Browser and Programmatic access.

```
GET https://api.cloudzero.com/v2/insights?cursor=H4sIAL1Fs2EC%2FyWKQQqAMAwEv1Jy9uqlnynBpFiMRJooiPh3o952ZvYC0%2B5l4RNyAkHzsm%2BEzgRD%2Bpt24v5WtOmVcyMunU3liFdOFcU4vLS1efAYW2s1%2FuB%2BANRxjWxiAAAA
```

might return

```
{
  "pagination": {
    "page_count": 3,
    "item_count": 5,
    "total_count": 15,
    "cursor": {
      "next_cursor": "H4sIAAFGs2EC/yWKQQqAMAwEv1Jy9qAHL/1MCTbFYiSSVEHEv5vibWdmHzDRlja6IQZgtJbOI2OjDEP4m2gm7RVt6XKtmZKSCV/+iqEgG7nnutfmPPuWUow6TOP7ASTguj9jAAAA",
      "previous_cursor": "H4sIAAFGs2EC/yWKQQqAMAwEv1Jy9uDFi58pwaRYjESaKIj4d1O87czsA6bN88Y3zAkEzfN5EDoTDOlv2ohbr2hLl2slzo1N5YrXnAqKcXipe/XgKbaWYtxhfD+RhfoRYgAAAA==",
      "has_next": true,
      "has_previous": true
    }
  },
  "insights": [...]
}
```