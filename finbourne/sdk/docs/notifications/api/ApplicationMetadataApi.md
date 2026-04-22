# notifications.ApplicationMetadataApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_access_controlled_resources**](ApplicationMetadataApi.md#list_access_controlled_resources) | **GET** /notification/api/metadata/access/resources | ListAccessControlledResources: Get resources available for access control


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.notifications.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.notifications.api.application_metadata_api import ApplicationMetadataApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(ApplicationMetadataApi)
```

---

# **list_access_controlled_resources**
> ResourceListOfAccessControlledResource listAccessControlledResources = list_access_controlled_resources()

ListAccessControlledResources: Get resources available for access control

Get the comprehensive set of resources that are available for access control

### Example

```python
api_instance = api_client_factory.build(ApplicationMetadataApi)
api_response = api_instance.list_access_controlled_resources()
pprint(api_response)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResourceListOfAccessControlledResource**](ResourceListOfAccessControlledResource.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

