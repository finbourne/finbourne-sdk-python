# lusid.ComplianceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_compliance_template**](ComplianceApi.md#create_compliance_template) | **POST** /api/api/compliance/templates/{scope} | [EARLY ACCESS] CreateComplianceTemplate: Create a Compliance Rule Template
[**delete_compliance_rule**](ComplianceApi.md#delete_compliance_rule) | **DELETE** /api/api/compliance/rules/{scope}/{code} | [EARLY ACCESS] DeleteComplianceRule: Delete compliance rule.
[**delete_compliance_template**](ComplianceApi.md#delete_compliance_template) | **DELETE** /api/api/compliance/templates/{scope}/{code} | [EARLY ACCESS] DeleteComplianceTemplate: Delete a ComplianceRuleTemplate
[**get_compliance_rule**](ComplianceApi.md#get_compliance_rule) | **GET** /api/api/compliance/rules/{scope}/{code} | [EARLY ACCESS] GetComplianceRule: Get compliance rule.
[**get_compliance_rule_result**](ComplianceApi.md#get_compliance_rule_result) | **GET** /api/api/compliance/runs/summary/{runScope}/{runCode}/{ruleScope}/{ruleCode} | [EARLY ACCESS] GetComplianceRuleResult: Get detailed results for a specific rule within a compliance run.
[**get_compliance_template**](ComplianceApi.md#get_compliance_template) | **GET** /api/api/compliance/templates/{scope}/{code} | [EARLY ACCESS] GetComplianceTemplate: Get the requested compliance template.
[**get_decorated_compliance_run_summary**](ComplianceApi.md#get_decorated_compliance_run_summary) | **GET** /api/api/compliance/runs/summary/{scope}/{code}/$decorate | [EARLY ACCESS] GetDecoratedComplianceRunSummary: Get decorated summary results for a specific compliance run.
[**list_compliance_rules**](ComplianceApi.md#list_compliance_rules) | **GET** /api/api/compliance/rules | [EARLY ACCESS] ListComplianceRules: List compliance rules.
[**list_compliance_runs**](ComplianceApi.md#list_compliance_runs) | **GET** /api/api/compliance/runs | [EARLY ACCESS] ListComplianceRuns: List historical compliance run identifiers.
[**list_compliance_templates**](ComplianceApi.md#list_compliance_templates) | **GET** /api/api/compliance/templates | [EARLY ACCESS] ListComplianceTemplates: List compliance templates.
[**list_order_breach_history**](ComplianceApi.md#list_order_breach_history) | **GET** /api/api/compliance/runs/breaches | [EXPERIMENTAL] ListOrderBreachHistory: List Historical Order Breaches.
[**run_compliance**](ComplianceApi.md#run_compliance) | **POST** /api/api/compliance/runs | [EARLY ACCESS] RunCompliance: Run a compliance check.
[**run_compliance_preview**](ComplianceApi.md#run_compliance_preview) | **POST** /api/api/compliance/preview/runs | [EARLY ACCESS] RunCompliancePreview: Run a compliance check.
[**update_compliance_template**](ComplianceApi.md#update_compliance_template) | **PUT** /api/api/compliance/templates/{scope}/{code} | [EARLY ACCESS] UpdateComplianceTemplate: Update a ComplianceRuleTemplate
[**upsert_compliance_rule**](ComplianceApi.md#upsert_compliance_rule) | **POST** /api/api/compliance/rules | [EARLY ACCESS] UpsertComplianceRule: Upsert a compliance rule.
[**upsert_compliance_run_summary**](ComplianceApi.md#upsert_compliance_run_summary) | **POST** /api/api/compliance/runs/summary | [EARLY ACCESS] UpsertComplianceRunSummary: Upsert a compliance run summary.


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.compliance_api import ComplianceApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(ComplianceApi)
```

---

# **create_compliance_template**
> ComplianceRuleTemplate createComplianceTemplate = create_compliance_template(scope, create_compliance_template_request)

[EARLY ACCESS] CreateComplianceTemplate: Create a Compliance Rule Template

Use this endpoint to create a compliance template.

### Example

```python
api_instance = api_client_factory.build(ComplianceApi)
scope = 'scope_example' # str
create_compliance_template_request = CreateComplianceTemplateRequest()
api_response = api_instance.create_compliance_template(scope, create_compliance_template_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Compliance Rule Template. | [required] 
 **create_compliance_template_request** | [**CreateComplianceTemplateRequest**](CreateComplianceTemplateRequest.md)| Request to create a compliance rule template. | [required] 

### Return type

[**ComplianceRuleTemplate**](ComplianceRuleTemplate.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created compliance rule template |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_compliance_rule**
> DeletedEntityResponse deleteComplianceRule = delete_compliance_rule(scope, code)

[EARLY ACCESS] DeleteComplianceRule: Delete compliance rule.

Use this endpoint to delete a compliance rule. The rule will be recoverable for asat times earlier than the  delete time, but will otherwise appear to have never existed.

### Example

```python
api_instance = api_client_factory.build(ComplianceApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.delete_compliance_rule(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The compliance rule&#39;s scope. | [required] 
 **code** | **str**| The compliance rule&#39;s code. | [required] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_compliance_template**
> DeletedEntityResponse deleteComplianceTemplate = delete_compliance_template(scope, code)

[EARLY ACCESS] DeleteComplianceTemplate: Delete a ComplianceRuleTemplate

Delete the compliance rule template uniquely defined by the scope and code.

### Example

```python
api_instance = api_client_factory.build(ComplianceApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.delete_compliance_template(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the template to be deleted. | [required] 
 **code** | **str**| The code of the template to be deleted. | [required] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response from deleting a compliance rule template. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_compliance_rule**
> ComplianceRuleResponse getComplianceRule = get_compliance_rule(scope, code, as_at=as_at, property_keys=property_keys)

[EARLY ACCESS] GetComplianceRule: Get compliance rule.

Use this endpoint to retrieve a single compliance rule.

### Example

```python
api_instance = api_client_factory.build(ComplianceApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.get_compliance_rule(scope, code, as_at=as_at, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The compliance rule&#39;s scope. | [required] 
 **code** | **str**| The compliance rule&#39;s code. | [required] 
 **as_at** | **datetime**| Optional. Asat time for query. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Compliance&#39; domain to decorate onto the rule.              These must take the format {domain}/{scope}/{code}, for example &#39;Compliance/live/UCITS&#39;. | [optional] 

### Return type

[**ComplianceRuleResponse**](ComplianceRuleResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested compliance rule. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_compliance_rule_result**
> ComplianceRuleResultV2 getComplianceRuleResult = get_compliance_rule_result(run_scope, run_code, rule_scope, rule_code)

[EARLY ACCESS] GetComplianceRuleResult: Get detailed results for a specific rule within a compliance run.

Specify a run scope and code from a previously run compliance check, and the scope and code of a rule within that run, to get detailed results for that rule.

### Example

```python
api_instance = api_client_factory.build(ComplianceApi)
run_scope = 'run_scope_example' # str
run_code = 'run_code_example' # str
rule_scope = 'rule_scope_example' # str
rule_code = 'rule_code_example' # str
api_response = api_instance.get_compliance_rule_result(run_scope, run_code, rule_scope, rule_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_scope** | **str**| Required: Run Scope. | [required] 
 **run_code** | **str**| Required: Run Code. | [required] 
 **rule_scope** | **str**| Required: Rule Scope. | [required] 
 **rule_code** | **str**| Required: Rule Code. | [required] 

### Return type

[**ComplianceRuleResultV2**](ComplianceRuleResultV2.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested compliance run summary details for a specific rule. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_compliance_template**
> ComplianceTemplate getComplianceTemplate = get_compliance_template(scope, code, as_at=as_at)

[EARLY ACCESS] GetComplianceTemplate: Get the requested compliance template.

Use this endpoint to fetch a specific compliance template.

### Example

```python
api_instance = api_client_factory.build(ComplianceApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_compliance_template(scope, code, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of TemplateID | [required] 
 **code** | **str**| Code of TemplateID | [required] 
 **as_at** | **datetime**| Optional. The time at which to get results from. Default : latest | [optional] 

### Return type

[**ComplianceTemplate**](ComplianceTemplate.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested compliance template. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_decorated_compliance_run_summary**
> DecoratedComplianceRunSummary getDecoratedComplianceRunSummary = get_decorated_compliance_run_summary(scope, code)

[EARLY ACCESS] GetDecoratedComplianceRunSummary: Get decorated summary results for a specific compliance run.

Specify a run scope and code from a previously run compliance check to get an overview of result details.

### Example

```python
api_instance = api_client_factory.build(ComplianceApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.get_decorated_compliance_run_summary(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Required: Run Scope. | [required] 
 **code** | **str**| Required: Run Code. | [required] 

### Return type

[**DecoratedComplianceRunSummary**](DecoratedComplianceRunSummary.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested compliance run details. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_compliance_rules**
> PagedResourceListOfComplianceRuleResponse listComplianceRules = list_compliance_rules(as_at=as_at, page=page, limit=limit, filter=filter, property_keys=property_keys)

[EARLY ACCESS] ListComplianceRules: List compliance rules.

Use this endpoint to retrieve all compliance rules, or a subset defined by an optional filter.

### Example

```python
api_instance = api_client_factory.build(ComplianceApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.list_compliance_rules(as_at=as_at, page=page, limit=limit, filter=filter, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| Optional. Asat time. | [optional] 
 **page** | **str**| Optional. Pagination token. | [optional] 
 **limit** | **int**| Optional. Entries per page. | [optional] 
 **filter** | **str**| Optional. Filter. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Compliance&#39; domain to decorate onto each rule.              These must take the format {domain}/{scope}/{code}, for example &#39;Compliance/live/UCITS&#39;. If not provided will return all the entitled properties for each rule. | [optional] 

### Return type

[**PagedResourceListOfComplianceRuleResponse**](PagedResourceListOfComplianceRuleResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of compliance rules. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_compliance_runs**
> PagedResourceListOfComplianceRunInfoV2 listComplianceRuns = list_compliance_runs(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

[EARLY ACCESS] ListComplianceRuns: List historical compliance run identifiers.

Lists RunIds of prior compliance runs, or a subset with a filter.

### Example

```python
api_instance = api_client_factory.build(ComplianceApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
api_response = api_instance.list_compliance_runs(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| Optional. The time at which to get results from. Default : latest | [optional] 
 **page** | **str**| Optional. The pagination token to use to continue listing compliance runs from a previous call to list compliance runs.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, and asAt fields              must not have changed since the original request. | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| Optional. A list of field names to sort by, each suffixed by \&quot;ASC\&quot; or \&quot;DESC\&quot; | [optional] 

### Return type

[**PagedResourceListOfComplianceRunInfoV2**](PagedResourceListOfComplianceRunInfoV2.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of previous compliance RunIds |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_compliance_templates**
> PagedResourceListOfComplianceTemplate listComplianceTemplates = list_compliance_templates(as_at=as_at, page=page, limit=limit, filter=filter)

[EARLY ACCESS] ListComplianceTemplates: List compliance templates.

Use this endpoint to fetch a list of all available compliance template ids, or a subset using a filter.

### Example

```python
api_instance = api_client_factory.build(ComplianceApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
api_response = api_instance.list_compliance_templates(as_at=as_at, page=page, limit=limit, filter=filter)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| Optional. The time at which to get results from. Default : latest | [optional] 
 **page** | **str**| Optional. The pagination token to use to continue listing compliance runs from a previous call to list compliance runs.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, and asAt fields              must not have changed since the original request. | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**PagedResourceListOfComplianceTemplate**](PagedResourceListOfComplianceTemplate.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of compliance templates available. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_order_breach_history**
> PagedResourceListOfOrderBreachHistory listOrderBreachHistory = list_order_breach_history(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

[EXPERIMENTAL] ListOrderBreachHistory: List Historical Order Breaches.

Lists Order Ids and Run Ids of prior compliance runs, with the breached Rules Ids specified, or a subset with a filter.

### Example

```python
api_instance = api_client_factory.build(ComplianceApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
api_response = api_instance.list_order_breach_history(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| Optional. The time at which to get results from. Default : latest | [optional] 
 **page** | **str**| Optional. The pagination token to use to continue listing historical order breaches from a previous call to list historical order breaches.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, and asAt fields              must not have changed since the original request. | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| Optional. A list of field names to sort by, each suffixed by \&quot;ASC\&quot; or \&quot;DESC\&quot; | [optional] 

### Return type

[**PagedResourceListOfOrderBreachHistory**](PagedResourceListOfOrderBreachHistory.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of previous order breaches |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **run_compliance**
> ComplianceRunInfoV2 runCompliance = run_compliance(run_scope, rule_scope, is_pre_trade, recipe_id_scope, recipe_id_code)

[EARLY ACCESS] RunCompliance: Run a compliance check.

Use this endpoint to run a compliance check using rules from a specific scope.

### Example

```python
api_instance = api_client_factory.build(ComplianceApi)
run_scope = 'run_scope_example' # str
rule_scope = 'rule_scope_example' # str
is_pre_trade = True # bool
recipe_id_scope = 'recipe_id_scope_example' # str
recipe_id_code = 'recipe_id_code_example' # str
api_response = api_instance.run_compliance(run_scope, rule_scope, is_pre_trade, recipe_id_scope, recipe_id_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_scope** | **str**| Required: Scope to save the run results in. | [required] 
 **rule_scope** | **str**| Required: Scope from which to select rules to be run. | [required] 
 **is_pre_trade** | **bool**| Required: Boolean flag indicating if a run should be PreTrade (Including orders). For post-trade only, set to false | [required] 
 **recipe_id_scope** | **str**| Required: the scope of the recipe to be used | [required] 
 **recipe_id_code** | **str**| Required: The code of the recipe to be used. If left blank, the default recipe will be used. | [required] 

### Return type

[**ComplianceRunInfoV2**](ComplianceRunInfoV2.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The identifying information of a compliance run |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **run_compliance_preview**
> ComplianceRunInfoV2 runCompliancePreview = run_compliance_preview(run_scope, rule_scope, recipe_id_scope, recipe_id_code, compliance_run_configuration=compliance_run_configuration)

[EARLY ACCESS] RunCompliancePreview: Run a compliance check.

Use this endpoint to run a compliance check using rules from a specific scope.

### Example

```python
api_instance = api_client_factory.build(ComplianceApi)
run_scope = 'run_scope_example' # str
rule_scope = 'rule_scope_example' # str
recipe_id_scope = 'recipe_id_scope_example' # str
recipe_id_code = 'recipe_id_code_example' # str
compliance_run_configuration = ComplianceRunConfiguration()
api_response = api_instance.run_compliance_preview(run_scope, rule_scope, recipe_id_scope, recipe_id_code, compliance_run_configuration=compliance_run_configuration)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_scope** | **str**| Required: Scope to save the run results in. | [required] 
 **rule_scope** | **str**| Required: Scope from which to select rules to be run. | [required] 
 **recipe_id_scope** | **str**| Required: the scope of the recipe to be used | [required] 
 **recipe_id_code** | **str**| Required: The code of the recipe to be used. If left blank, the default recipe will be used. | [required] 
 **compliance_run_configuration** | [**ComplianceRunConfiguration**](ComplianceRunConfiguration.md)| Configuration options for the compliance run. | [optional] 

### Return type

[**ComplianceRunInfoV2**](ComplianceRunInfoV2.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The identifying information of a compliance run |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_compliance_template**
> ComplianceRuleTemplate updateComplianceTemplate = update_compliance_template(scope, code, update_compliance_template_request)

[EARLY ACCESS] UpdateComplianceTemplate: Update a ComplianceRuleTemplate

Use this endpoint to update a specified compliance template.

### Example

```python
api_instance = api_client_factory.build(ComplianceApi)
scope = 'scope_example' # str
code = 'code_example' # str
update_compliance_template_request = UpdateComplianceTemplateRequest()
api_response = api_instance.update_compliance_template(scope, code, update_compliance_template_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Compliance Rule Template. | [required] 
 **code** | **str**| The code of the Compliance Rule Template. | [required] 
 **update_compliance_template_request** | [**UpdateComplianceTemplateRequest**](UpdateComplianceTemplateRequest.md)| Request to update a compliance rule template. | [required] 

### Return type

[**ComplianceRuleTemplate**](ComplianceRuleTemplate.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated compliance rule template |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_compliance_rule**
> ComplianceRuleResponse upsertComplianceRule = upsert_compliance_rule(upsert_compliance_rule_request=upsert_compliance_rule_request)

[EARLY ACCESS] UpsertComplianceRule: Upsert a compliance rule.

Use this endpoint to upsert a single compliance rule. The template and variation specified must already  exist, as must the portfolio group. The parameters passed must match those required by the template variation.

### Example

```python
api_instance = api_client_factory.build(ComplianceApi)
upsert_compliance_rule_request = UpsertComplianceRuleRequest()
api_response = api_instance.upsert_compliance_rule(upsert_compliance_rule_request=upsert_compliance_rule_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_compliance_rule_request** | [**UpsertComplianceRuleRequest**](UpsertComplianceRuleRequest.md)|  | [optional] 

### Return type

[**ComplianceRuleResponse**](ComplianceRuleResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The upserted compliance rule. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_compliance_run_summary**
> UpsertComplianceRunSummaryResult upsertComplianceRunSummary = upsert_compliance_run_summary(upsert_compliance_run_summary_request=upsert_compliance_run_summary_request)

[EARLY ACCESS] UpsertComplianceRunSummary: Upsert a compliance run summary.

Use this endpoint to upsert a compliance run result summary.

### Example

```python
api_instance = api_client_factory.build(ComplianceApi)
upsert_compliance_run_summary_request = UpsertComplianceRunSummaryRequest()
api_response = api_instance.upsert_compliance_run_summary(upsert_compliance_run_summary_request=upsert_compliance_run_summary_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_compliance_run_summary_request** | [**UpsertComplianceRunSummaryRequest**](UpsertComplianceRunSummaryRequest.md)|  | [optional] 

### Return type

[**UpsertComplianceRunSummaryResult**](UpsertComplianceRunSummaryResult.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The upserted compliance run summary. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

