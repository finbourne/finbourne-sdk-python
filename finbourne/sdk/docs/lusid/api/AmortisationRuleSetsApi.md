# lusid.AmortisationRuleSetsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_amortisation_rule_set**](AmortisationRuleSetsApi.md#create_amortisation_rule_set) | **POST** /api/api/amortisation/rulesets/{scope} | [EXPERIMENTAL] CreateAmortisationRuleSet: Create an amortisation rule set.
[**delete_amortisation_ruleset**](AmortisationRuleSetsApi.md#delete_amortisation_ruleset) | **DELETE** /api/api/amortisation/rulesets/{scope}/{code} | [EXPERIMENTAL] DeleteAmortisationRuleset: Delete an amortisation rule set.
[**get_amortisation_rule_set**](AmortisationRuleSetsApi.md#get_amortisation_rule_set) | **GET** /api/api/amortisation/rulesets/{scope}/{code} | [EXPERIMENTAL] GetAmortisationRuleSet: Retrieve the definition of a single amortisation rule set
[**list_amortisation_rule_sets**](AmortisationRuleSetsApi.md#list_amortisation_rule_sets) | **GET** /api/api/amortisation/rulesets | [EXPERIMENTAL] ListAmortisationRuleSets: List amortisation rule sets.
[**set_amortisation_rules**](AmortisationRuleSetsApi.md#set_amortisation_rules) | **PUT** /api/api/amortisation/rulesets/{scope}/{code}/rules | [EXPERIMENTAL] SetAmortisationRules: Set Amortisation Rules on an existing Amortisation Rule Set.
[**update_amortisation_rule_set_details**](AmortisationRuleSetsApi.md#update_amortisation_rule_set_details) | **PUT** /api/api/amortisation/rulesets/{scope}/{code}/details | [EXPERIMENTAL] UpdateAmortisationRuleSetDetails: Update an amortisation rule set.


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.amortisation_rule_sets_api import AmortisationRuleSetsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(AmortisationRuleSetsApi)
```

---

# **create_amortisation_rule_set**
> AmortisationRuleSet createAmortisationRuleSet = create_amortisation_rule_set(scope, create_amortisation_rule_set_request)

[EXPERIMENTAL] CreateAmortisationRuleSet: Create an amortisation rule set.

Creates an amortisation rule set definition at the given effective time.  The user must be entitled to read any properties specified in each rule.

### Example

```python
api_instance = api_client_factory.build(AmortisationRuleSetsApi)
scope = 'scope_example' # str
create_amortisation_rule_set_request = CreateAmortisationRuleSetRequest()
api_response = api_instance.create_amortisation_rule_set(scope, create_amortisation_rule_set_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the rule set. | [required] 
 **create_amortisation_rule_set_request** | [**CreateAmortisationRuleSetRequest**](CreateAmortisationRuleSetRequest.md)| The contents of the rule set. | [required] 

### Return type

[**AmortisationRuleSet**](AmortisationRuleSet.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create a rule set for amortisation. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_amortisation_ruleset**
> DeletedEntityResponse deleteAmortisationRuleset = delete_amortisation_ruleset(scope, code)

[EXPERIMENTAL] DeleteAmortisationRuleset: Delete an amortisation rule set.

Deletes the rule set perpetually, including its rules.    The rule set will remain viewable at previous as at times, but it will no longer be considered applicable.    This cannot be undone.

### Example

```python
api_instance = api_client_factory.build(AmortisationRuleSetsApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.delete_amortisation_ruleset(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The rule set scope. | [required] 
 **code** | **str**| The rule set code. | [required] 

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

# **get_amortisation_rule_set**
> AmortisationRuleSet getAmortisationRuleSet = get_amortisation_rule_set(scope, code, effective_at=effective_at, as_at=as_at)

[EXPERIMENTAL] GetAmortisationRuleSet: Retrieve the definition of a single amortisation rule set

Retrieves the amortisation rule set definition at the given effective and as at times.

### Example

```python
api_instance = api_client_factory.build(AmortisationRuleSetsApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_amortisation_rule_set(scope, code, effective_at=effective_at, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The rule set scope. | [required] 
 **code** | **str**| The rule set code. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the rule definition.  Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the rule definition. Defaults to returning the latest version if not  specified. | [optional] 

### Return type

[**AmortisationRuleSet**](AmortisationRuleSet.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of one rule set. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_amortisation_rule_sets**
> PagedResourceListOfAmortisationRuleSet listAmortisationRuleSets = list_amortisation_rule_sets(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

[EXPERIMENTAL] ListAmortisationRuleSets: List amortisation rule sets.

Retrieves all amortisation rule sets at the given effective and as at times

### Example

```python
api_instance = api_client_factory.build(AmortisationRuleSetsApi)
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
api_response = api_instance.list_amortisation_rule_sets(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the rule definitions.  Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the rule definitions. Defaults to returning the latest version if not  specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing AmortisationRuleSets; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For more information about filtering results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 

### Return type

[**PagedResourceListOfAmortisationRuleSet**](PagedResourceListOfAmortisationRuleSet.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of rule sets available. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **set_amortisation_rules**
> AmortisationRuleSet setAmortisationRules = set_amortisation_rules(scope, code, set_amortisation_rules_request)

[EXPERIMENTAL] SetAmortisationRules: Set Amortisation Rules on an existing Amortisation Rule Set.

Sets the rules on the Amortisation Rule Set, replacing the existing rules with the set provided.

### Example

```python
api_instance = api_client_factory.build(AmortisationRuleSetsApi)
scope = 'scope_example' # str
code = 'code_example' # str
set_amortisation_rules_request = SetAmortisationRulesRequest()
api_response = api_instance.set_amortisation_rules(scope, code, set_amortisation_rules_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The rule set scope. | [required] 
 **code** | **str**| The rule set code. | [required] 
 **set_amortisation_rules_request** | [**SetAmortisationRulesRequest**](SetAmortisationRulesRequest.md)| The contents of the rules. | [required] 

### Return type

[**AmortisationRuleSet**](AmortisationRuleSet.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update the rules for an amortisation rule set. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_amortisation_rule_set_details**
> AmortisationRuleSet updateAmortisationRuleSetDetails = update_amortisation_rule_set_details(scope, code, update_amortisation_rule_set_details_request)

[EXPERIMENTAL] UpdateAmortisationRuleSetDetails: Update an amortisation rule set.

Updates the amortisation rule set definition for all effective time.

### Example

```python
api_instance = api_client_factory.build(AmortisationRuleSetsApi)
scope = 'scope_example' # str
code = 'code_example' # str
update_amortisation_rule_set_details_request = UpdateAmortisationRuleSetDetailsRequest()
api_response = api_instance.update_amortisation_rule_set_details(scope, code, update_amortisation_rule_set_details_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The rule set scope. | [required] 
 **code** | **str**| The rule set code. | [required] 
 **update_amortisation_rule_set_details_request** | [**UpdateAmortisationRuleSetDetailsRequest**](UpdateAmortisationRuleSetDetailsRequest.md)| The contents of the rule set. | [required] 

### Return type

[**AmortisationRuleSet**](AmortisationRuleSet.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update the details of an Amortisation Rule Set. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

