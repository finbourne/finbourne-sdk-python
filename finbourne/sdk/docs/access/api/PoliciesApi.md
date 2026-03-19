# access.PoliciesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_to_policy_collection**](PoliciesApi.md#add_to_policy_collection) | **POST** /access/api/policycollections/{code}/add | AddToPolicyCollection: Add To PolicyCollection
[**create_policy**](PoliciesApi.md#create_policy) | **POST** /access/api/policies | CreatePolicy: Create Policy
[**create_policy_collection**](PoliciesApi.md#create_policy_collection) | **POST** /access/api/policycollections | CreatePolicyCollection: Create PolicyCollection
[**delete_policy**](PoliciesApi.md#delete_policy) | **DELETE** /access/api/policies/{code} | DeletePolicy: Delete Policy
[**delete_policy_collection**](PoliciesApi.md#delete_policy_collection) | **DELETE** /access/api/policycollections/{code} | DeletePolicyCollection: Delete PolicyCollection
[**evaluate**](PoliciesApi.md#evaluate) | **POST** /access/api/me | Evaluate: Run one or more evaluations
[**get_own_policies**](PoliciesApi.md#get_own_policies) | **GET** /access/api/me | GetOwnPolicies: Get policies of requesting user
[**get_policy**](PoliciesApi.md#get_policy) | **GET** /access/api/policies/{code} | GetPolicy: Get Policy
[**get_policy_collection**](PoliciesApi.md#get_policy_collection) | **GET** /access/api/policycollections/{code} | GetPolicyCollection: Get PolicyCollection
[**list_policies**](PoliciesApi.md#list_policies) | **GET** /access/api/policies | ListPolicies: List Policies
[**list_policy_collections**](PoliciesApi.md#list_policy_collections) | **GET** /access/api/policycollections | ListPolicyCollections: List PolicyCollections
[**page_policies**](PoliciesApi.md#page_policies) | **GET** /access/api/policies/page | PagePolicies: Page Policies
[**page_policy_collections**](PoliciesApi.md#page_policy_collections) | **GET** /access/api/policycollections/page | PagePolicyCollections: Page PolicyCollections
[**remove_from_policy_collection**](PoliciesApi.md#remove_from_policy_collection) | **POST** /access/api/policycollections/{code}/remove | RemoveFromPolicyCollection: Remove From PolicyCollection
[**update_policy**](PoliciesApi.md#update_policy) | **PUT** /access/api/policies/{code} | UpdatePolicy: Update Policy
[**update_policy_collection**](PoliciesApi.md#update_policy_collection) | **PUT** /access/api/policycollections/{code} | UpdatePolicyCollection: Update PolicyCollection


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.access.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.access.api.policies_api import PoliciesApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(PoliciesApi)
```

---

# **add_to_policy_collection**
> PolicyCollectionResponse addToPolicyCollection = add_to_policy_collection(code, add_to_policy_collection_request, scope=scope)

AddToPolicyCollection: Add To PolicyCollection

Add Policies and/or PolicyCollections to a PolicyCollection

### Example

```python
api_instance = api_client_factory.build(PoliciesApi)
code = 'code_example' # str
add_to_policy_collection_request = AddToPolicyCollectionRequest()
scope = 'scope_example' # str (optional)
api_response = api_instance.add_to_policy_collection(code, add_to_policy_collection_request, scope=scope)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code of the PolicyCollection | [required] 
 **add_to_policy_collection_request** | [**AddToPolicyCollectionRequest**](AddToPolicyCollectionRequest.md)| Ids of the PolicyCollections and/or Policies to add to the PolicyCollection | [required] 
 **scope** | **str**| Optional. Will use the default scope if not provided. The scope of the PolicyCollection | [optional] 

### Return type

[**PolicyCollectionResponse**](PolicyCollectionResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated PolicyCollection |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **create_policy**
> PolicyResponse createPolicy = create_policy(policy_creation_request)

CreatePolicy: Create Policy

Creates a Policy

### Example

```python
api_instance = api_client_factory.build(PoliciesApi)
policy_creation_request = PolicyCreationRequest()
api_response = api_instance.create_policy(policy_creation_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_creation_request** | [**PolicyCreationRequest**](PolicyCreationRequest.md)| The definition of the Policy | [required] 

### Return type

[**PolicyResponse**](PolicyResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created policy |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **create_policy_collection**
> PolicyCollectionResponse createPolicyCollection = create_policy_collection(policy_collection_creation_request)

CreatePolicyCollection: Create PolicyCollection

Creates a PolicyCollection

### Example

```python
api_instance = api_client_factory.build(PoliciesApi)
policy_collection_creation_request = PolicyCollectionCreationRequest()
api_response = api_instance.create_policy_collection(policy_collection_creation_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_collection_creation_request** | [**PolicyCollectionCreationRequest**](PolicyCollectionCreationRequest.md)| The definition of the PolicyCollection | [required] 

### Return type

[**PolicyCollectionResponse**](PolicyCollectionResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created PolicyCollection |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_policy**
> deletePolicy = delete_policy(code, scope=scope)

DeletePolicy: Delete Policy

Deletes an identified Policy

### Example

```python
api_instance = api_client_factory.build(PoliciesApi)
code = 'code_example' # str
scope = 'scope_example' # str (optional)
api_instance.delete_policy(code, scope=scope)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code of the Policy | [required] 
 **scope** | **str**| Optional. Will use the default scope if not provided. The scope of the Policy | [optional] 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_policy_collection**
> deletePolicyCollection = delete_policy_collection(code, scope=scope)

DeletePolicyCollection: Delete PolicyCollection

Deletes an identified PolicyCollection

### Example

```python
api_instance = api_client_factory.build(PoliciesApi)
code = 'code_example' # str
scope = 'scope_example' # str (optional)
api_instance.delete_policy_collection(code, scope=scope)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code of the PolicyCollection | [required] 
 **scope** | **str**| Optional. Will use the default scope if not provided. The scope of the PolicyCollection | [optional] 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **evaluate**
> Dict[str, EvaluationResponse] evaluate = evaluate(request_body, applications=applications)

Evaluate: Run one or more evaluations

Given a dictionary of evaluation requests (keyed by any arbitrary correlation identifier), each will be evaluated according to the current user's policies (deduced from the provided OAuth token).

### Example

```python
api_instance = api_client_factory.build(PoliciesApi)
request_body = {"data-access-page-evaluation":{"request":{"action":{"entityCode":"WebSitePage","scope":"FINBOURNE","activity":"SeeAdminControls"},"toEffectiveDate":"2018-12-08T13:30:00.0000000+00:00","toAsAt":"2018-12-31T11:00:00.0000000+00:00"},"resource":{"id":{"scope":"FINBOURNE","code":"DataAccessPage"},"metadata":{"RequiredLicence":[{"provider":"WebsiteAccess","value":"FINBOURNE"}]}}}} # Dict[str, EvaluationRequest]
applications = ['applications_example'] # List[str] (optional)
api_response = api_instance.evaluate(request_body, applications=applications)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, EvaluationRequest]**](EvaluationRequest.md)| A dictionary of evaluations, keyed using any arbitrary correlation id (it will be returned with the response for that evaluation). | [required] 
 **applications** | [**List[str]**](str.md)| Optional. The application type of the roles and policies to use when evaluating. | [optional] 

### Return type

[**Dict[str, EvaluationResponse]**](EvaluationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Run an evaluation against the current user&#39;s entitlements |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_own_policies**
> List[AttachedPolicyDefinitionResponse] getOwnPolicies = get_own_policies(applications=applications)

GetOwnPolicies: Get policies of requesting user

Gets all Policies for the current user

### Example

```python
api_instance = api_client_factory.build(PoliciesApi)
applications = ['applications_example'] # List[str] (optional)
api_response = api_instance.get_own_policies(applications=applications)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applications** | [**List[str]**](str.md)| Optional. Filter on the applications that the policies apply to | [optional] 

### Return type

[**List[AttachedPolicyDefinitionResponse]**](AttachedPolicyDefinitionResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get policies and licences of current user |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_policy**
> PolicyResponse getPolicy = get_policy(code, scope=scope, as_at=as_at)

GetPolicy: Get Policy

Gets an identified Policy

### Example

```python
api_instance = api_client_factory.build(PoliciesApi)
code = 'code_example' # str
scope = 'scope_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_policy(code, scope=scope, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code of the Policy | [required] 
 **scope** | **str**| Optional. Will use the default scope if not provided. The scope of the Policy | [optional] 
 **as_at** | **datetime**| Optional. The AsAt date and time at which to retrieve the Policy. Defaults to returning the latest version | [optional] 

### Return type

[**PolicyResponse**](PolicyResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a specific Policy |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_policy_collection**
> PolicyCollectionResponse getPolicyCollection = get_policy_collection(code, scope=scope)

GetPolicyCollection: Get PolicyCollection

Gets an identified PolicyCollection

### Example

```python
api_instance = api_client_factory.build(PoliciesApi)
code = 'code_example' # str
scope = 'scope_example' # str (optional)
api_response = api_instance.get_policy_collection(code, scope=scope)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code of the PolicyCollection | [required] 
 **scope** | **str**| Optional. Will use the default scope if not provided. The scope of the PolicyCollection | [optional] 

### Return type

[**PolicyCollectionResponse**](PolicyCollectionResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Requested PolicyCollection |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_policies**
> List[PolicyResponse] listPolicies = list_policies(scope=scope)

ListPolicies: List Policies

Gets all Policies in a scope. For pagination support, use PagePolicies.

### Example

```python
api_instance = api_client_factory.build(PoliciesApi)
scope = 'scope_example' # str (optional)
api_response = api_instance.list_policies(scope=scope)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Optional. Will use the default scope if not provided. The requested scope | [optional] 

### Return type

[**List[PolicyResponse]**](PolicyResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List Policies |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_policy_collections**
> List[PolicyCollectionResponse] listPolicyCollections = list_policy_collections(scope=scope)

ListPolicyCollections: List PolicyCollections

Gets all PolicyCollections in a scope. For pagination support, use PagePolicyCollections

### Example

```python
api_instance = api_client_factory.build(PoliciesApi)
scope = 'scope_example' # str (optional)
api_response = api_instance.list_policy_collections(scope=scope)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Optional. Will use the default scope if not provided. The requested scope | [optional] 

### Return type

[**List[PolicyCollectionResponse]**](PolicyCollectionResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Requested list of PolicyCollections |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **page_policies**
> ResourceListOfPolicyResponse pagePolicies = page_policies(sort_by=sort_by, limit=limit, filter=filter, page=page)

PagePolicies: Page Policies

Gets all Policies with pagination support.

### Example

```python
api_instance = api_client_factory.build(PoliciesApi)
sort_by = 'sort_by_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
page = 'page_example' # str (optional)
api_response = api_instance.page_policies(sort_by=sort_by, limit=limit, filter=filter, page=page)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort_by** | **str**| Optional. Order the results by these fields. Use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **limit** | **int**| Optional. 2000 if not provided. When paginating, limit the number of returned results to this many | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set | [optional] 
 **page** | **str**| Optional. Paging token returned from a previous result | [optional] 

### Return type

[**ResourceListOfPolicyResponse**](ResourceListOfPolicyResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Requested list of Policies |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **page_policy_collections**
> ResourceListOfPolicyCollectionResponse pagePolicyCollections = page_policy_collections(sort_by=sort_by, limit=limit, filter=filter, page=page)

PagePolicyCollections: Page PolicyCollections

Gets all PolicyCollections with pagination support.

### Example

```python
api_instance = api_client_factory.build(PoliciesApi)
sort_by = 'sort_by_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
page = 'page_example' # str (optional)
api_response = api_instance.page_policy_collections(sort_by=sort_by, limit=limit, filter=filter, page=page)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort_by** | **str**| Optional. Order the results by these fields. Use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **limit** | **int**| Optional. 2000 if not provided. When paginating, limit the number of returned results to this many | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set | [optional] 
 **page** | **str**| Optional. Paging token returned from a previous result | [optional] 

### Return type

[**ResourceListOfPolicyCollectionResponse**](ResourceListOfPolicyCollectionResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Requested list of PolicyCollections |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **remove_from_policy_collection**
> PolicyCollectionResponse removeFromPolicyCollection = remove_from_policy_collection(code, remove_from_policy_collection_request, scope=scope)

RemoveFromPolicyCollection: Remove From PolicyCollection

Remove Policies and/or PolicyCollections from a PolicyCollection

### Example

```python
api_instance = api_client_factory.build(PoliciesApi)
code = 'code_example' # str
remove_from_policy_collection_request = RemoveFromPolicyCollectionRequest()
scope = 'scope_example' # str (optional)
api_response = api_instance.remove_from_policy_collection(code, remove_from_policy_collection_request, scope=scope)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code of the PolicyCollection | [required] 
 **remove_from_policy_collection_request** | [**RemoveFromPolicyCollectionRequest**](RemoveFromPolicyCollectionRequest.md)| Ids of the PolicyCollections and/or Policies to remove from the PolicyCollection | [required] 
 **scope** | **str**| Optional. Will use the default scope if not provided. The scope of the PolicyCollection | [optional] 

### Return type

[**PolicyCollectionResponse**](PolicyCollectionResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated PolicyCollection |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_policy**
> PolicyResponse updatePolicy = update_policy(code, policy_update_request, scope=scope)

UpdatePolicy: Update Policy

Updates a Policy

### Example

```python
api_instance = api_client_factory.build(PoliciesApi)
code = 'code_example' # str
policy_update_request = PolicyUpdateRequest()
scope = 'scope_example' # str (optional)
api_response = api_instance.update_policy(code, policy_update_request, scope=scope)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code of the Policy | [required] 
 **policy_update_request** | [**PolicyUpdateRequest**](PolicyUpdateRequest.md)| The updated definition of the Policy | [required] 
 **scope** | **str**| Optional. Will use the default scope if not provided. The scope of the Policy | [optional] 

### Return type

[**PolicyResponse**](PolicyResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated policy |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_policy_collection**
> PolicyCollectionResponse updatePolicyCollection = update_policy_collection(code, policy_collection_update_request, scope=scope)

UpdatePolicyCollection: Update PolicyCollection

Updates a PolicyCollection

### Example

```python
api_instance = api_client_factory.build(PoliciesApi)
code = 'code_example' # str
policy_collection_update_request = PolicyCollectionUpdateRequest()
scope = 'scope_example' # str (optional)
api_response = api_instance.update_policy_collection(code, policy_collection_update_request, scope=scope)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code of the PolicyCollection | [required] 
 **policy_collection_update_request** | [**PolicyCollectionUpdateRequest**](PolicyCollectionUpdateRequest.md)| The updated definition of the PolicyCollection | [required] 
 **scope** | **str**| Optional. Will use the default scope if not provided. The scope of the PolicyCollection | [optional] 

### Return type

[**PolicyCollectionResponse**](PolicyCollectionResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated PolicyCollection |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

