# insights.LogMetadataApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_queryable_fields**](LogMetadataApi.md#list_queryable_fields) | **GET** /insights/api/metadata/logs | [EARLY ACCESS] ListQueryableFields: List the queryable fields for every supported log type.


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.insights.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.insights.api.log_metadata_api import LogMetadataApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(LogMetadataApi)
```

---

# **list_queryable_fields**
> ResourceListOfQueryableLogType listQueryableFields = list_queryable_fields()

[EARLY ACCESS] ListQueryableFields: List the queryable fields for every supported log type.

Returns, for each log type, the fields that can be selected and/or filtered, their data types, and the comparator operations available for each filterable field. Intended to power a UI that advertises the correct comparators for a chosen field.

### Example

```python
api_instance = api_client_factory.build(LogMetadataApi)
api_response = api_instance.list_queryable_fields()
pprint(api_response)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResourceListOfQueryableLogType**](../model/ResourceListOfQueryableLogType.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

