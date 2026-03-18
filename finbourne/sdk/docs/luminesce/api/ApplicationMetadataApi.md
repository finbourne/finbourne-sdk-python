# luminesce.ApplicationMetadataApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_services_as_access_controlled_resources**](ApplicationMetadataApi.md#get_services_as_access_controlled_resources) | **GET** /honeycomb/api/metadata/access/resources | GetServicesAsAccessControlledResources: Get resources available for access control


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.luminesce.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.luminesce.api.application_metadata_api import ApplicationMetadataApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(ApplicationMetadataApi)
```

---

# **get_services_as_access_controlled_resources**
> ResourceListOfAccessControlledResource getServicesAsAccessControlledResources = get_services_as_access_controlled_resources()

GetServicesAsAccessControlledResources: Get resources available for access control

 Get the comprehensive set of resources that are available for access control.  The following LuminesceSql is executed to return this information,  which is then packaged up as AccessControlledResource:  ```sql select     Name,     min(coalesce(Description, Name) || ' (' || Type || ')') as Description from     Sys.Registration where     Type in ('DirectProvider', 'DataProvider')     and     ShowAll = true group by 1 order by 1     ```  The following error codes are to be anticipated with standard Problem Detail reports: - 401 Unauthorized - 403 Forbidden 

### Example

```python
api_instance = api_client_factory.build(ApplicationMetadataApi)
api_response = api_instance.get_services_as_access_controlled_resources()
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

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

