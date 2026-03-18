# lusid.CutLabelDefinitionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cut_label_definition**](CutLabelDefinitionsApi.md#create_cut_label_definition) | **POST** /api/api/systemconfiguration/cutlabels | CreateCutLabelDefinition: Create a Cut Label
[**delete_cut_label_definition**](CutLabelDefinitionsApi.md#delete_cut_label_definition) | **DELETE** /api/api/systemconfiguration/cutlabels/{code} | DeleteCutLabelDefinition: Delete a Cut Label
[**get_cut_label_definition**](CutLabelDefinitionsApi.md#get_cut_label_definition) | **GET** /api/api/systemconfiguration/cutlabels/{code} | GetCutLabelDefinition: Get a Cut Label
[**list_cut_label_definitions**](CutLabelDefinitionsApi.md#list_cut_label_definitions) | **GET** /api/api/systemconfiguration/cutlabels | ListCutLabelDefinitions: List Existing Cut Labels
[**update_cut_label_definition**](CutLabelDefinitionsApi.md#update_cut_label_definition) | **PUT** /api/api/systemconfiguration/cutlabels/{code} | UpdateCutLabelDefinition: Update a Cut Label


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.cut_label_definitions_api import CutLabelDefinitionsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(CutLabelDefinitionsApi)
```

---

# **create_cut_label_definition**
> CutLabelDefinition createCutLabelDefinition = create_cut_label_definition(create_cut_label_definition_request=create_cut_label_definition_request)

CreateCutLabelDefinition: Create a Cut Label

Create a Cut Label valid in all scopes

### Example

```python
api_instance = api_client_factory.build(CutLabelDefinitionsApi)
create_cut_label_definition_request = CreateCutLabelDefinitionRequest()
api_response = api_instance.create_cut_label_definition(create_cut_label_definition_request=create_cut_label_definition_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_cut_label_definition_request** | [**CreateCutLabelDefinitionRequest**](CreateCutLabelDefinitionRequest.md)| The cut label definition | [optional] 

### Return type

[**CutLabelDefinition**](CutLabelDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created cut label |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_cut_label_definition**
> datetime deleteCutLabelDefinition = delete_cut_label_definition(code)

DeleteCutLabelDefinition: Delete a Cut Label

Delete a specified cut label

### Example

```python
api_instance = api_client_factory.build(CutLabelDefinitionsApi)
code = 'code_example' # str
api_response = api_instance.delete_cut_label_definition(code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The Code of the Cut Label that is being Deleted | [required] 

### Return type

**datetime**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The time of deletion |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_cut_label_definition**
> CutLabelDefinition getCutLabelDefinition = get_cut_label_definition(code, as_at=as_at)

GetCutLabelDefinition: Get a Cut Label

Get a specified cut label at a given time

### Example

```python
api_instance = api_client_factory.build(CutLabelDefinitionsApi)
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_cut_label_definition(code, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The Code of the Cut Label that is being queried | [required] 
 **as_at** | **datetime**| The time at which to get the Cut Label | [optional] 

### Return type

[**CutLabelDefinition**](CutLabelDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested cut label |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_cut_label_definitions**
> PagedResourceListOfCutLabelDefinition listCutLabelDefinitions = list_cut_label_definitions(as_at=as_at, sort_by=sort_by, limit=limit, filter=filter, page=page)

ListCutLabelDefinitions: List Existing Cut Labels

List all the Cut Label Definitions that are valid at the given AsAt time

### Example

```python
api_instance = api_client_factory.build(CutLabelDefinitionsApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
page = 'page_example' # str (optional)
api_response = api_instance.list_cut_label_definitions(as_at=as_at, sort_by=sort_by, limit=limit, filter=filter, page=page)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| Optional. The As At time at which listed Cut Labels are valid | [optional] 
 **sort_by** | [**List[str]**](str.md)| Optional. Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set.              For example, to filter on code, use \&quot;code eq &#39;string&#39;\&quot;              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **page** | **str**| The pagination token to use to continue listing cut labels from a previous call This value is returned from the previous call.  If a pagination token is provided the sortBy, filter, and asAt fields  must not have changed since the original request. | [optional] 

### Return type

[**PagedResourceListOfCutLabelDefinition**](PagedResourceListOfCutLabelDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of cut labels |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_cut_label_definition**
> CutLabelDefinition updateCutLabelDefinition = update_cut_label_definition(code, update_cut_label_definition_request=update_cut_label_definition_request)

UpdateCutLabelDefinition: Update a Cut Label

Update a specified cut label

### Example

```python
api_instance = api_client_factory.build(CutLabelDefinitionsApi)
code = 'code_example' # str
update_cut_label_definition_request = UpdateCutLabelDefinitionRequest()
api_response = api_instance.update_cut_label_definition(code, update_cut_label_definition_request=update_cut_label_definition_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The Code of the Cut Label that is being updated | [required] 
 **update_cut_label_definition_request** | [**UpdateCutLabelDefinitionRequest**](UpdateCutLabelDefinitionRequest.md)| The cut label update definition | [optional] 

### Return type

[**CutLabelDefinition**](CutLabelDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated cut label |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

