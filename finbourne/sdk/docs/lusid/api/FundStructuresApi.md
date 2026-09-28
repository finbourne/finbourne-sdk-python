# lusid.FundStructuresApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_fund_structure_member**](FundStructuresApi.md#add_fund_structure_member) | **POST** /api/api/fundstructures/{scope}/{code}/members | [EXPERIMENTAL] AddFundStructureMember: Add a member to a Fund Structure.
[**create_fund_structure**](FundStructuresApi.md#create_fund_structure) | **POST** /api/api/fundstructures/{scope} | [EXPERIMENTAL] CreateFundStructure: Create a Fund Structure.
[**delete_fund_structure**](FundStructuresApi.md#delete_fund_structure) | **DELETE** /api/api/fundstructures/{scope}/{code} | [EXPERIMENTAL] DeleteFundStructure: Delete a Fund Structure.
[**get_fund_structure**](FundStructuresApi.md#get_fund_structure) | **GET** /api/api/fundstructures/{scope}/{code} | [EXPERIMENTAL] GetFundStructure: Get a Fund Structure.
[**list_fund_structures**](FundStructuresApi.md#list_fund_structures) | **GET** /api/api/fundstructures | [EXPERIMENTAL] ListFundStructures: List Fund Structures.
[**remove_fund_structure_member**](FundStructuresApi.md#remove_fund_structure_member) | **DELETE** /api/api/fundstructures/{scope}/{code}/members/{nodeCode} | [EXPERIMENTAL] RemoveFundStructureMember: Remove a member from a Fund Structure.
[**upsert_fund_structure**](FundStructuresApi.md#upsert_fund_structure) | **PUT** /api/api/fundstructures/{scope}/{code} | [EXPERIMENTAL] UpsertFundStructure: Upsert a Fund Structure.


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

# **add_fund_structure_member**
> FundStructure addFundStructureMember = add_fund_structure_member(scope, code, fund_structure_member_request, effective_at=effective_at)

[EXPERIMENTAL] AddFundStructureMember: Add a member to a Fund Structure.

Add a node and the links that join it to existing members, from an effective datetime. The result is a new  bitemporal version of the structure. The change applies to the version in force at that datetime; if a  later version of the structure already exists the request is rejected, since the member would otherwise  drop out when that version begins. Upsert the full definition for each affected version in that case.

### Example

```python
api_instance = api_client_factory.build(FundStructuresApi)
scope = 'scope_example' # str
code = 'code_example' # str
fund_structure_member_request = FundStructureMemberRequest()
effective_at = 'effective_at_example' # str (optional)
api_response = api_instance.add_fund_structure_member(scope, code, fund_structure_member_request, effective_at=effective_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund Structure. | [required] 
 **code** | **str**| The code of the Fund Structure. Together with the scope this uniquely identifies the Fund Structure. | [required] 
 **fund_structure_member_request** | [**FundStructureMemberRequest**](../model/FundStructureMemberRequest.md)| The node to add and the links joining it to existing members. | [required] 
 **effective_at** | **str**| The effective datetime or cut label from which the member is part of the structure. Defaults to the current LUSID system datetime if not specified. | [optional] 

### Return type

[**FundStructure**](../model/FundStructure.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Fund Structure with the member added. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

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

# **delete_fund_structure**
> DeletedEntityResponse deleteFundStructure = delete_fund_structure(scope, code, effective_at=effective_at)

[EXPERIMENTAL] DeleteFundStructure: Delete a Fund Structure.

Delete a Fund Structure from the given effective datetime. It remains retrievable at earlier effective datetimes.

### Example

```python
api_instance = api_client_factory.build(FundStructuresApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
api_response = api_instance.delete_fund_structure(scope, code, effective_at=effective_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund Structure to be deleted. | [required] 
 **code** | **str**| The code of the Fund Structure to be deleted. Together with the scope this uniquely identifies the Fund Structure. | [required] 
 **effective_at** | **str**| The effective datetime or cut label from which the Fund Structure is deleted. Defaults to the current LUSID system datetime if not specified. | [optional] 

### Return type

[**DeletedEntityResponse**](../model/DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the Fund Structure was deleted. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_fund_structure**
> FundStructure getFundStructure = get_fund_structure(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)

[EXPERIMENTAL] GetFundStructure: Get a Fund Structure.

Retrieve the definition of a particular Fund Structure at an effective and asAt datetime, including its nodes,  edges, allocation groups and the funds its nodes refer to.

### Example

```python
api_instance = api_client_factory.build(FundStructuresApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.get_fund_structure(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund Structure. | [required] 
 **code** | **str**| The code of the Fund Structure. Together with the scope this uniquely identifies the Fund Structure. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the Fund Structure. Defaults to the current LUSID system datetime if not specified. | [optional] 
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
> PagedResourceListOfFundStructure listFundStructures = list_fund_structures(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)

[EXPERIMENTAL] ListFundStructures: List Fund Structures.

List all the Fund Structures matching the given criteria.

### Example

```python
api_instance = api_client_factory.build(FundStructuresApi)
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.list_fund_structures(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effective datetime or cut label at which to list the Fund Structures. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list Fund Structures. Defaults to returning the latest version of each Fund Structure if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Fund Structures; this value is returned from the previous call. If a pagination token is provided, the filter and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. For example, to filter on the Fund Structure code, specify \&quot;id.Code eq &#39;Structure1&#39;\&quot;. For more information about filtering results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. | [optional] 
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

---

# **remove_fund_structure_member**
> FundStructure removeFundStructureMember = remove_fund_structure_member(scope, code, node_code, effective_at=effective_at)

[EXPERIMENTAL] RemoveFundStructureMember: Remove a member from a Fund Structure.

Remove a node and every link that touches it, from an effective datetime. The result is a new bitemporal  version of the structure. The change applies to the version in force at that datetime; if a later version  of the structure already exists the request is rejected, since the member would otherwise reappear when  that version begins. Upsert the full definition for each affected version in that case.

### Example

```python
api_instance = api_client_factory.build(FundStructuresApi)
scope = 'scope_example' # str
code = 'code_example' # str
node_code = 'node_code_example' # str
effective_at = 'effective_at_example' # str (optional)
api_response = api_instance.remove_fund_structure_member(scope, code, node_code, effective_at=effective_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund Structure. | [required] 
 **code** | **str**| The code of the Fund Structure. Together with the scope this uniquely identifies the Fund Structure. | [required] 
 **node_code** | **str**| The node code of the member to remove. | [required] 
 **effective_at** | **str**| The effective datetime or cut label from which the member is no longer part of the structure. Defaults to the current LUSID system datetime if not specified. | [optional] 

### Return type

[**FundStructure**](../model/FundStructure.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Fund Structure with the member removed. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_fund_structure**
> FundStructure upsertFundStructure = upsert_fund_structure(scope, code, fund_structure_request)

[EXPERIMENTAL] UpsertFundStructure: Upsert a Fund Structure.

Create or replace the full definition of a Fund Structure from an effective datetime. A change to the  definition becomes a new bitemporal version: the structure as it was declared at earlier effective datetimes,  and as of earlier asAt datetimes, remains retrievable.

### Example

```python
api_instance = api_client_factory.build(FundStructuresApi)
scope = 'scope_example' # str
code = 'code_example' # str
fund_structure_request = FundStructureRequest()
api_response = api_instance.upsert_fund_structure(scope, code, fund_structure_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund Structure. | [required] 
 **code** | **str**| The code of the Fund Structure. Together with the scope this uniquely identifies the Fund Structure, and must match the code in the request body. | [required] 
 **fund_structure_request** | [**FundStructureRequest**](../model/FundStructureRequest.md)| The full definition of the Fund Structure from the effective datetime in the request, or the current LUSID system datetime if not specified. | [required] 

### Return type

[**FundStructure**](../model/FundStructure.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Fund Structure as it stands from the effective datetime. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

