# drive.SearchApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search**](SearchApi.md#search) | **POST** /drive/api/search | [EARLY ACCESS] Search: Search for a file or folder with a given name and path


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.drive.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.drive.api.search_api import SearchApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(SearchApi)
```

---

# **search**
> PagedResourceListOfStorageObject search = search(search_body, page=page, sort_by=sort_by, limit=limit, filter=filter)

[EARLY ACCESS] Search: Search for a file or folder with a given name and path

### Example

```python
api_instance = api_client_factory.build(SearchApi)
search_body = SearchBody()
page = 'page_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
limit = 56 # int (optional)
filter = '' # str (optional)
api_response = api_instance.search(search_body, page=page, sort_by=sort_by, limit=limit, filter=filter)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_body** | [**SearchBody**](SearchBody.md)| Search parameters | [required] 
 **page** | **str**|  | [optional] 
 **sort_by** | [**List[str]**](str.md)|  | [optional] 
 **limit** | **int**|  | [optional] 
 **filter** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**PagedResourceListOfStorageObject**](PagedResourceListOfStorageObject.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

