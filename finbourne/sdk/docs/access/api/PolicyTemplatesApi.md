# access.PolicyTemplatesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_policy_template**](PolicyTemplatesApi.md#create_policy_template) | **POST** /access/api/policytemplates | [EXPERIMENTAL] CreatePolicyTemplate: Create a Policy Template
[**delete_policy_template**](PolicyTemplatesApi.md#delete_policy_template) | **DELETE** /access/api/policytemplates/{code} | [EXPERIMENTAL] DeletePolicyTemplate: Deleting a policy template
[**generate_policy_from_template**](PolicyTemplatesApi.md#generate_policy_from_template) | **POST** /access/api/policytemplates/$generatepolicy | [EXPERIMENTAL] GeneratePolicyFromTemplate: Generate policy from template
[**get_policy_template**](PolicyTemplatesApi.md#get_policy_template) | **GET** /access/api/policytemplates/{code} | [EXPERIMENTAL] GetPolicyTemplate: Retrieving one Policy Template
[**list_policy_templates**](PolicyTemplatesApi.md#list_policy_templates) | **GET** /access/api/policytemplates | [EXPERIMENTAL] ListPolicyTemplates: List Policy Templates
[**update_policy_template**](PolicyTemplatesApi.md#update_policy_template) | **PUT** /access/api/policytemplates/{code} | [EXPERIMENTAL] UpdatePolicyTemplate: Update a Policy Template


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.access.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.access.api.policy_templates_api import PolicyTemplatesApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(PolicyTemplatesApi)
```

---

# **create_policy_template**
> PolicyTemplateResponse createPolicyTemplate = create_policy_template(policy_template_creation_request)

[EXPERIMENTAL] CreatePolicyTemplate: Create a Policy Template

Creates a Policy Template

### Example

```python
api_instance = api_client_factory.build(PolicyTemplatesApi)
policy_template_creation_request = PolicyTemplateCreationRequest()
api_response = api_instance.create_policy_template(policy_template_creation_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_template_creation_request** | [**PolicyTemplateCreationRequest**](PolicyTemplateCreationRequest.md)| The definition of the policy template | [required] 

### Return type

[**PolicyTemplateResponse**](PolicyTemplateResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created Policy Template |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_policy_template**
> deletePolicyTemplate = delete_policy_template(code, scope=scope)

[EXPERIMENTAL] DeletePolicyTemplate: Deleting a policy template

Deletes an identified Policy Template

### Example

```python
api_instance = api_client_factory.build(PolicyTemplatesApi)
code = 'code_example' # str
scope = 'scope_example' # str (optional)
api_instance.delete_policy_template(code, scope=scope)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code of the Policy Template | [required] 
 **scope** | **str**| Optional. Will use the default scope if not provided. The scope of the Policy Template | [optional] 

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

# **generate_policy_from_template**
> GeneratedPolicyComponents generatePolicyFromTemplate = generate_policy_from_template(generate_policy_from_template_request, as_at=as_at)

[EXPERIMENTAL] GeneratePolicyFromTemplate: Generate policy from template

Generates policies from templates

### Example

```python
api_instance = api_client_factory.build(PolicyTemplatesApi)
generate_policy_from_template_request = GeneratePolicyFromTemplateRequest()
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.generate_policy_from_template(generate_policy_from_template_request, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_policy_from_template_request** | [**GeneratePolicyFromTemplateRequest**](GeneratePolicyFromTemplateRequest.md)| Definition of the generate request | [required] 
 **as_at** | **datetime**| Optional. The AsAt date time of the data | [optional] 

### Return type

[**GeneratedPolicyComponents**](GeneratedPolicyComponents.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_policy_template**
> PolicyTemplateResponse getPolicyTemplate = get_policy_template(code, as_at=as_at, scope=scope)

[EXPERIMENTAL] GetPolicyTemplate: Retrieving one Policy Template

Gets an identified Policy Template

### Example

```python
api_instance = api_client_factory.build(PolicyTemplatesApi)
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
scope = 'scope_example' # str (optional)
api_response = api_instance.get_policy_template(code, as_at=as_at, scope=scope)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code of the Policy Template | [required] 
 **as_at** | **datetime**| Optional. The AsAt date time of the data. If not specified defaults to current time | [optional] 
 **scope** | **str**| Optional. Will use the default scope if not provided. The scope of the Policy Template | [optional] 

### Return type

[**PolicyTemplateResponse**](PolicyTemplateResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a specific Policy Template |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_policy_templates**
> ResourceListOfPolicyTemplateResponse listPolicyTemplates = list_policy_templates(as_at=as_at, sort_by=sort_by, limit=limit, filter=filter, page=page)

[EXPERIMENTAL] ListPolicyTemplates: List Policy Templates

Gets all Policy Templates with pagination support.

### Example

```python
api_instance = api_client_factory.build(PolicyTemplatesApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
sort_by = 'sort_by_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
page = 'page_example' # str (optional)
api_response = api_instance.list_policy_templates(as_at=as_at, sort_by=sort_by, limit=limit, filter=filter, page=page)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| Optional. The AsAt date time of the data | [optional] 
 **sort_by** | **str**| Optional. Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set | [optional] 
 **page** | **str**| Optional. Paging token returned from a previous result | [optional] 

### Return type

[**ResourceListOfPolicyTemplateResponse**](ResourceListOfPolicyTemplateResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List Policy Templates |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_policy_template**
> PolicyTemplateResponse updatePolicyTemplate = update_policy_template(code, policy_template_update_request=policy_template_update_request)

[EXPERIMENTAL] UpdatePolicyTemplate: Update a Policy Template

Updates an identified Policy Template

### Example

```python
api_instance = api_client_factory.build(PolicyTemplatesApi)
code = 'code_example' # str
policy_template_update_request = PolicyTemplateUpdateRequest()
api_response = api_instance.update_policy_template(code, policy_template_update_request=policy_template_update_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Code of the policy template to update | [required] 
 **policy_template_update_request** | [**PolicyTemplateUpdateRequest**](PolicyTemplateUpdateRequest.md)| Definition of the updated policy template | [optional] 

### Return type

[**PolicyTemplateResponse**](PolicyTemplateResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated Policy Template |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

