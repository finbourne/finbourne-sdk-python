# lusid.StagingRuleSetApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_staging_rule_set**](StagingRuleSetApi.md#create_staging_rule_set) | **POST** /api/api/stagingrulesets/{entityType} | CreateStagingRuleSet: Create a StagingRuleSet
[**delete_staging_rule_set**](StagingRuleSetApi.md#delete_staging_rule_set) | **DELETE** /api/api/stagingrulesets/{entityType} | DeleteStagingRuleSet: Delete a StagingRuleSet
[**get_staging_rule_set**](StagingRuleSetApi.md#get_staging_rule_set) | **GET** /api/api/stagingrulesets/{entityType} | GetStagingRuleSet: Get a StagingRuleSet
[**list_staging_rule_sets**](StagingRuleSetApi.md#list_staging_rule_sets) | **GET** /api/api/stagingrulesets | ListStagingRuleSets: List StagingRuleSets
[**update_staging_rule_set**](StagingRuleSetApi.md#update_staging_rule_set) | **PUT** /api/api/stagingrulesets/{entityType} | UpdateStagingRuleSet: Update a StagingRuleSet


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.staging_rule_set_api import StagingRuleSetApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(StagingRuleSetApi)
```

---

# **create_staging_rule_set**
> StagingRuleSet createStagingRuleSet = create_staging_rule_set(entity_type, create_staging_rule_set_request)

CreateStagingRuleSet: Create a StagingRuleSet

Create a new staging rule set.

### Example

```python
api_instance = api_client_factory.build(StagingRuleSetApi)
entity_type = 'entity_type_example' # str
create_staging_rule_set_request = CreateStagingRuleSetRequest()
api_response = api_instance.create_staging_rule_set(entity_type, create_staging_rule_set_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| The entity type for which to create the staging rule set. | [required] 
 **create_staging_rule_set_request** | [**CreateStagingRuleSetRequest**](CreateStagingRuleSetRequest.md)| Request to create a staging rule set. | [required] 

### Return type

[**StagingRuleSet**](StagingRuleSet.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created staging rule set |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_staging_rule_set**
> DeletedEntityResponse deleteStagingRuleSet = delete_staging_rule_set(entity_type)

DeleteStagingRuleSet: Delete a StagingRuleSet

Delete a staging rule set of a specific entity type. Deletion will be valid from the staging rule set's creation datetime.  This means that the staging rule set will no longer exist at any effective datetime from the asAt datetime of deletion.

### Example

```python
api_instance = api_client_factory.build(StagingRuleSetApi)
entity_type = 'entity_type_example' # str
api_response = api_instance.delete_staging_rule_set(entity_type)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| The entity type for which to delete the staging rule set. | [required] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response from deleting staging rule set |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_staging_rule_set**
> StagingRuleSet getStagingRuleSet = get_staging_rule_set(entity_type, as_at=as_at)

GetStagingRuleSet: Get a StagingRuleSet

Get the staging rule set for the given entity type at the specific asAt time.

### Example

```python
api_instance = api_client_factory.build(StagingRuleSetApi)
entity_type = 'entity_type_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_staging_rule_set(entity_type, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| The entity type for which to retrieve the staging rule set. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the staging rule set. Defaults to return the latest              version of the staging rule set if not specified. | [optional] 

### Return type

[**StagingRuleSet**](StagingRuleSet.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested staging rule set |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_staging_rule_sets**
> PagedResourceListOfStagingRuleSet listStagingRuleSets = list_staging_rule_sets(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter)

ListStagingRuleSets: List StagingRuleSets

List all the staging rule sets matching particular criteria.

### Example

```python
api_instance = api_client_factory.build(StagingRuleSetApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
api_response = api_instance.list_staging_rule_sets(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to retrieve the staging rule sets. Defaults to return the latest              version of the staging rule sets if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing staging rule sets from a previous call to list              staging rule sets. This value is returned from the previous call. If a pagination token is provided the sortBy,              filter, effectiveAt, and asAt fields must not have changed since the original request. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**PagedResourceListOfStagingRuleSet**](PagedResourceListOfStagingRuleSet.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of staging rule sets |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_staging_rule_set**
> StagingRuleSet updateStagingRuleSet = update_staging_rule_set(entity_type, update_staging_rule_set_request)

UpdateStagingRuleSet: Update a StagingRuleSet

Update an existing staging rule set.

### Example

```python
api_instance = api_client_factory.build(StagingRuleSetApi)
entity_type = 'entity_type_example' # str
update_staging_rule_set_request = UpdateStagingRuleSetRequest()
api_response = api_instance.update_staging_rule_set(entity_type, update_staging_rule_set_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| The entity type for which to update the staging rule set. | [required] 
 **update_staging_rule_set_request** | [**UpdateStagingRuleSetRequest**](UpdateStagingRuleSetRequest.md)| Request to update a staging rule set. | [required] 

### Return type

[**StagingRuleSet**](StagingRuleSet.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated staging rule set |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

