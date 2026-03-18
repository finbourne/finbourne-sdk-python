# lusid.CheckDefinitionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_check_definition**](CheckDefinitionsApi.md#create_check_definition) | **POST** /api/api/dataquality/checkdefinitions | [EXPERIMENTAL] CreateCheckDefinition: Create a Check Definition
[**delete_check_definition**](CheckDefinitionsApi.md#delete_check_definition) | **DELETE** /api/api/dataquality/checkdefinitions/{scope}/{code} | [EXPERIMENTAL] DeleteCheckDefinition: Deletes a particular Check Definition
[**delete_rules**](CheckDefinitionsApi.md#delete_rules) | **POST** /api/api/dataquality/checkdefinitions/{scope}/{code}/$deleteRules | [EXPERIMENTAL] DeleteRules: Delete rules on a particular Check Definition
[**get_check_definition**](CheckDefinitionsApi.md#get_check_definition) | **GET** /api/api/dataquality/checkdefinitions/{scope}/{code} | [EXPERIMENTAL] GetCheckDefinition: Get a single Check Definition by scope and code.
[**list_check_definitions**](CheckDefinitionsApi.md#list_check_definitions) | **GET** /api/api/dataquality/checkdefinitions | [EXPERIMENTAL] ListCheckDefinitions: List Check Definitions
[**run_check_definition**](CheckDefinitionsApi.md#run_check_definition) | **POST** /api/api/dataquality/checkdefinitions/{scope}/{code}/$run | [EXPERIMENTAL] RunCheckDefinition: Runs a Check Definition against given dataset.
[**update_check_definition**](CheckDefinitionsApi.md#update_check_definition) | **PUT** /api/api/dataquality/checkdefinitions/{scope}/{code} | [EXPERIMENTAL] UpdateCheckDefinition: Update Check Definition defined by scope and code
[**upsert_rules**](CheckDefinitionsApi.md#upsert_rules) | **POST** /api/api/dataquality/checkdefinitions/{scope}/{code}/$upsertRules | [EXPERIMENTAL] UpsertRules: Upsert rules to a particular Check Definition


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.check_definitions_api import CheckDefinitionsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(CheckDefinitionsApi)
```

---

# **create_check_definition**
> CheckDefinition createCheckDefinition = create_check_definition(create_check_definition_request=create_check_definition_request)

[EXPERIMENTAL] CreateCheckDefinition: Create a Check Definition

Creates a Check Definition. Returns the created Check Definition at the current effectiveAt.  Note that Check Definitions are mono-temporal, however they can have Time-Variant Properties.  Upserted Properties will be returned at the latest AsAt and EffectiveAt

### Example

```python
api_instance = api_client_factory.build(CheckDefinitionsApi)
create_check_definition_request = CreateCheckDefinitionRequest()
api_response = api_instance.create_check_definition(create_check_definition_request=create_check_definition_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_check_definition_request** | [**CreateCheckDefinitionRequest**](CreateCheckDefinitionRequest.md)| The request containing the details of the Check Definition | [optional] 

### Return type

[**CheckDefinition**](CheckDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created Check Definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_check_definition**
> DeletedEntityResponse deleteCheckDefinition = delete_check_definition(scope, code)

[EXPERIMENTAL] DeleteCheckDefinition: Deletes a particular Check Definition

The deletion will take effect from the Check Definition deletion datetime.  i.e. will no longer exist at any asAt datetime after the asAt datetime of deletion.

### Example

```python
api_instance = api_client_factory.build(CheckDefinitionsApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.delete_check_definition(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the specified Check Definition. | [required] 
 **code** | **str**| The code of the specified Check Definition. Together with the domain and scope this uniquely              identifies the Check Definition. | [required] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The deleted entity metadata |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_rules**
> CheckDefinition deleteRules = delete_rules(scope, code, delete_data_quality_rule=delete_data_quality_rule)

[EXPERIMENTAL] DeleteRules: Delete rules on a particular Check Definition

Delete rules for a given check definition. This will not affect any other rules that are not included in the request.

### Example

```python
api_instance = api_client_factory.build(CheckDefinitionsApi)
scope = 'scope_example' # str
code = 'code_example' # str
delete_data_quality_rule = [{"ruleSetKey":"ruleSetKey1","ruleKey":"ruleKey1"},{"ruleSetKey":"ruleSetKey2","ruleKey":"ruleKey2"}] # List[DeleteDataQualityRule] (optional)
api_response = api_instance.delete_rules(scope, code, delete_data_quality_rule=delete_data_quality_rule)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the specified Check Definition. | [required] 
 **code** | **str**| The code of the specified Check Definition. Together with the domain and scope this uniquely              identifies the Check Definition. | [required] 
 **delete_data_quality_rule** | [**List[DeleteDataQualityRule]**](DeleteDataQualityRule.md)| The request containing the rules to be deleted | [optional] 

### Return type

[**CheckDefinition**](CheckDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated check definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_check_definition**
> CheckDefinition getCheckDefinition = get_check_definition(scope, code, as_at=as_at, effective_at=effective_at, property_keys=property_keys)

[EXPERIMENTAL] GetCheckDefinition: Get a single Check Definition by scope and code.

Retrieves one Check Definition by scope and code.  Check Definitions are mono-temporal. The EffectiveAt is only applied to Time-Variant Properties.

### Example

```python
api_instance = api_client_factory.build(CheckDefinitionsApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
effective_at = 'effective_at_example' # str (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.get_check_definition(scope, code, as_at=as_at, effective_at=effective_at, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the specified Check Definition. | [required] 
 **code** | **str**| The code of the specified Check Definition. Together with the scope this uniquely              identifies the Check Definition. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Check Definition definition. Defaults to return              the latest version of the definition if not specified. | [optional] 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the check definition properties.              Defaults to the current LUSID system datetime if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;CheckDefinition&#39; domain to decorate onto              the Check Definition.              These must have the format {domain}/{scope}/{code}, for example &#39;CheckDefinition/system/Name&#39;. | [optional] 

### Return type

[**CheckDefinition**](CheckDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Check Definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_check_definitions**
> PagedResourceListOfCheckDefinition listCheckDefinitions = list_check_definitions(as_at=as_at, effective_at=effective_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)

[EXPERIMENTAL] ListCheckDefinitions: List Check Definitions

List all the Check Definitions matching a particular criteria.

### Example

```python
api_instance = api_client_factory.build(CheckDefinitionsApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
effective_at = 'effective_at_example' # str (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.list_check_definitions(as_at=as_at, effective_at=effective_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the Check Definitions. Defaults to returning the latest version of each Check Definition if not specified. | [optional] 
 **effective_at** | **str**| The effective datetime or cut label at which to list the Check Definitions.              Note that Check Definitions are monotemporal, the effectiveAt is for Timevariant Properties on the Check Definition only.              Defaults to the current LUSID system datetime if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Check Definitions; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the displayName, specify \&quot;displayName eq &#39;MyCheckDefinition&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;CheckDefinition&#39; domain to decorate onto each Check Definition.              These must take the format {domain}/{scope}/{code}, for example &#39;CheckDefinition/Account/id&#39;. | [optional] 

### Return type

[**PagedResourceListOfCheckDefinition**](PagedResourceListOfCheckDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Check Definitions. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **run_check_definition**
> RunCheckResponse runCheckDefinition = run_check_definition(scope, code, run_check_request=run_check_request)

[EXPERIMENTAL] RunCheckDefinition: Runs a Check Definition against given dataset.

Runs a Check Definition against given dataset.

### Example

```python
api_instance = api_client_factory.build(CheckDefinitionsApi)
scope = 'scope_example' # str
code = 'code_example' # str
run_check_request = RunCheckRequest()
api_response = api_instance.run_check_definition(scope, code, run_check_request=run_check_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the CheckDefinition to run. | [required] 
 **code** | **str**| Code of the CheckDefinition to run. | [required] 
 **run_check_request** | [**RunCheckRequest**](RunCheckRequest.md)| Run request defining what dataset to run against. | [optional] 

### Return type

[**RunCheckResponse**](RunCheckResponse.md)

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

# **update_check_definition**
> CheckDefinition updateCheckDefinition = update_check_definition(scope, code, update_check_definition_request=update_check_definition_request)

[EXPERIMENTAL] UpdateCheckDefinition: Update Check Definition defined by scope and code

Overwrites an existing Check Definition  Update request has the same required fields as Create apart from the id.  Returns the updated Check Definition at the current effectiveAt.  Note that Check Definitions are mono-temporal, however they can have Time-Variant Properties.  Updated Properties will be returned at the latest AsAt and EffectiveAt

### Example

```python
api_instance = api_client_factory.build(CheckDefinitionsApi)
scope = 'scope_example' # str
code = 'code_example' # str
update_check_definition_request = UpdateCheckDefinitionRequest()
api_response = api_instance.update_check_definition(scope, code, update_check_definition_request=update_check_definition_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the specified Check Definition. | [required] 
 **code** | **str**| The code of the specified Check Definition. Together with the domain and scope this uniquely identifies the Check Definition. | [required] 
 **update_check_definition_request** | [**UpdateCheckDefinitionRequest**](UpdateCheckDefinitionRequest.md)| The request containing the updated details of the Check Definition | [optional] 

### Return type

[**CheckDefinition**](CheckDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated version of the requested Check Definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_rules**
> CheckDefinition upsertRules = upsert_rules(scope, code, upsert_data_quality_rule=upsert_data_quality_rule)

[EXPERIMENTAL] UpsertRules: Upsert rules to a particular Check Definition

Upsert rules for a given check definition. This will not affect any other rules that are not included in the request.

### Example

```python
api_instance = api_client_factory.build(CheckDefinitionsApi)
scope = 'scope_example' # str
code = 'code_example' # str
upsert_data_quality_rule = [{"ruleSetKey":"ruleSetKey1","rule":{"ruleKey":"ruleKey1","displayName":"ruleName","description":"description1","ruleFormula":"expression1","severity":1}},{"ruleSetKey":"ruleSetKey2","rule":{"ruleKey":"ruleKey2","displayName":"ruleName","description":"description2","ruleFormula":"expression2","severity":5}}] # List[UpsertDataQualityRule] (optional)
api_response = api_instance.upsert_rules(scope, code, upsert_data_quality_rule=upsert_data_quality_rule)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the specified Check Definition. | [required] 
 **code** | **str**| The code of the specified Check Definition. Together with the domain and scope this uniquely              identifies the Check Definition. | [required] 
 **upsert_data_quality_rule** | [**List[UpsertDataQualityRule]**](UpsertDataQualityRule.md)| The request containing the rules to be upserted | [optional] 

### Return type

[**CheckDefinition**](CheckDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated check definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

