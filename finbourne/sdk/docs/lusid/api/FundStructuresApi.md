# lusid.FundStructuresApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_fund_structure**](FundStructuresApi.md#create_fund_structure) | **POST** /api/api/fundstructures/{scope} | [EXPERIMENTAL] CreateFundStructure: Create a Fund Structure.
[**get_fund_structure**](FundStructuresApi.md#get_fund_structure) | **GET** /api/api/fundstructures/{scope}/{code} | [EXPERIMENTAL] GetFundStructure: Get a Fund Structure.
[**list_fund_structures**](FundStructuresApi.md#list_fund_structures) | **GET** /api/api/fundstructures | [EXPERIMENTAL] ListFundStructures: List Fund Structures.


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.fund_structures_api import FundStructuresApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(FundStructuresApi)
```

---

# **create_fund_structure**
> FundStructure createFundStructure = create_fund_structure(scope, fund_structure_request)

[EXPERIMENTAL] CreateFundStructure: Create a Fund Structure.

Create a new Fund Structure Model. The scope and code of the Fund Structure are provided in the request body.

### Example

```python
api_instance = api_client_factory.build(FundStructuresApi)
scope = 'scope_example' # str
fund_structure_request = FundStructureRequest()
api_response = api_instance.create_fund_structure(scope, fund_structure_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund Structure. | [required] 
 **fund_structure_request** | [**FundStructureRequest**](../model/FundStructureRequest.md)| The definition of the Fund Structure. | [required] 

### Return type

[**FundStructure**](../model/FundStructure.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created Fund Structure. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_fund_structure**
> FundStructure getFundStructure = get_fund_structure(scope, code, as_at=as_at, property_keys=property_keys)

[EXPERIMENTAL] GetFundStructure: Get a Fund Structure.

Retrieve the definition of a particular Fund Structure, including its nodes, edges, and any inline fund definitions.

### Example

```python
api_instance = api_client_factory.build(FundStructuresApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.get_fund_structure(scope, code, as_at=as_at, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund Structure. | [required] 
 **code** | **str**| The code of the Fund Structure. Together with the scope this uniquely identifies the Fund Structure. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Fund Structure. Defaults to returning the latest version if not specified. | [optional] 
 **property_keys** | [**List[str]**](../model/str.md)| A list of property keys from the &#39;FundStructure&#39; domain to decorate onto the Fund Structure.              These must take the format {domain}/{scope}/{code}, for example &#39;FundStructure/Manager/Id&#39;. If no properties are specified, then no properties will be returned. | [optional] 

### Return type

[**FundStructure**](../model/FundStructure.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Fund Structure. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_fund_structures**
> PagedResourceListOfFundStructure listFundStructures = list_fund_structures(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)

[EXPERIMENTAL] ListFundStructures: List Fund Structures.

List all the Fund Structures matching the given criteria.

### Example

```python
api_instance = api_client_factory.build(FundStructuresApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.list_fund_structures(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list Fund Structures. Defaults to returning the latest version of each Fund Structure if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Fund Structures; this value is returned from the previous call. If a pagination token is provided, the filter and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. For example, to filter on the Fund Structure code, specify \&quot;id.Code eq &#39;Structure1&#39;\&quot;. For more information about filtering results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **sort_by** | [**List[str]**](../model/str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **property_keys** | [**List[str]**](../model/str.md)| A list of property keys from the &#39;FundStructure&#39; domain to decorate onto each Fund Structure.              These must take the format {domain}/{scope}/{code}, for example &#39;FundStructure/Manager/Id&#39;. | [optional] 

### Return type

[**PagedResourceListOfFundStructure**](../model/PagedResourceListOfFundStructure.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Fund Structures. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

