---
title: Sample Python Script for Updating CostFormation Definition Language
category: features
createdAt: '2024-01-23T21:07:34.097Z'
hidden: false
slug: sample-python-costformation-script
updatedAt: '2024-01-23T21:07:34.097Z'
---
CloudZero provides a standard [REST API](https://docs.cloudzero.com/reference/getcostformationdefinitionversions) that customers can use to update their own dimensions. The following section contains an example Python script for programmatically making dimension updates, which could be a helpful reference or starting point.

```python
import os
import requests
import yaml  # pyyaml, https://pyyaml.org/wiki/PyYAMLDocumentation
from yaml import Loader


url = 'https://api.cloudzero.com/v2/costformation/definition/versions'

file_path = 'path/for/local/costformation_file.yaml'
use_etag = True
validate_only = False
use_test_key = False

headers = {
    'Authorization': os.environ['API_KEY'],
    **({'cloudzero-test-key': f'script-test'} if use_test_key else {})
}


def get_current_costformation(headers):
    response = requests.request('get', f'{url}/latest', headers=headers)
    download_url = response.json()['version']['uri']
    download_response = requests.request('get', download_url)
    return yaml.load(download_response.text, Loader), response.headers.get('ETag')


def apply_updates(cf):
    ### Update costformation object here. ###
    # Ex. cf['Dimensions']['SomeDimension']['Name'] = 'New Name'

    with open(file_path, 'w') as stream:
        yaml.dump(cf, stream, sort_keys=False)


def publish_costformation(headers):
    params = {'validate_only': validate_only}
    with open(file_path, 'rb') as file:
        files = {'file': file}
        request_kwargs = {'params': params, 'files': files}
        response = requests.request('post', url, headers=headers, **request_kwargs)
        print(response.json())


cf, etag = get_current_costformation(headers)
apply_updates(cf)

if use_etag:
    headers['If-Match'] = etag

publish_costformation(headers)
```

The script can be used as-is with a few small changes

* Set your API key. See [Authorization](https://docs.cloudzero.com/reference/authorization) in the API reference for more information.
* Set the `file_path` for local file saves.
* Add the desired update logic to `apply_updates`.

There are a few optional boolean fields at the top that can be changed: `use_etag`, `validate_only`, `use_test_key`.

For an explanation of test keys, see [Testing](https://docs.cloudzero.com/reference/testing) in the API reference.

The POST endpoint supports an optional `If-Match` header, for the `ETag` value returned by the GET endpoint. If included, a POST request will fail if the latest CostFormation version does not match the included `ETag` value. You may or may not wish to include the header for a given workflow, depending on which source of updates should be the source of truth.
