# lusid.ChartOfAccountsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_chart_of_accounts**](ChartOfAccountsApi.md#create_chart_of_accounts) | **POST** /api/api/chartofaccounts/{scope} | [EXPERIMENTAL] CreateChartOfAccounts: Create a Chart of Accounts
[**create_cleardown_module**](ChartOfAccountsApi.md#create_cleardown_module) | **POST** /api/api/chartofaccounts/{scope}/{code}/cleardownmodules | [EXPERIMENTAL] CreateCleardownModule: Create a Cleardown Module
[**create_general_ledger_profile**](ChartOfAccountsApi.md#create_general_ledger_profile) | **POST** /api/api/chartofaccounts/{scope}/{code}/generalledgerprofile | [EXPERIMENTAL] CreateGeneralLedgerProfile: Create a General Ledger Profile.
[**create_posting_module**](ChartOfAccountsApi.md#create_posting_module) | **POST** /api/api/chartofaccounts/{scope}/{code}/postingmodules | [EXPERIMENTAL] CreatePostingModule: Create a Posting Module
[**delete_accounts**](ChartOfAccountsApi.md#delete_accounts) | **POST** /api/api/chartofaccounts/{scope}/{code}/accounts/$delete | [EXPERIMENTAL] DeleteAccounts: Soft or hard delete multiple accounts
[**delete_chart_of_accounts**](ChartOfAccountsApi.md#delete_chart_of_accounts) | **DELETE** /api/api/chartofaccounts/{scope}/{code} | [EXPERIMENTAL] DeleteChartOfAccounts: Delete a Chart of Accounts
[**delete_cleardown_module**](ChartOfAccountsApi.md#delete_cleardown_module) | **DELETE** /api/api/chartofaccounts/{scope}/{code}/cleardownmodules/{cleardownModuleCode} | [EXPERIMENTAL] DeleteCleardownModule: Delete a Cleardown Module.
[**delete_general_ledger_profile**](ChartOfAccountsApi.md#delete_general_ledger_profile) | **DELETE** /api/api/chartofaccounts/{scope}/{code}/generalledgerprofile/{generalLedgerProfileCode} | [EXPERIMENTAL] DeleteGeneralLedgerProfile: Delete a General Ledger Profile.
[**delete_posting_module**](ChartOfAccountsApi.md#delete_posting_module) | **DELETE** /api/api/chartofaccounts/{scope}/{code}/postingmodules/{postingModuleCode} | [EXPERIMENTAL] DeletePostingModule: Delete a Posting Module.
[**get_account**](ChartOfAccountsApi.md#get_account) | **GET** /api/api/chartofaccounts/{scope}/{code}/accounts/{accountCode} | [EXPERIMENTAL] GetAccount: Get Account
[**get_account_properties**](ChartOfAccountsApi.md#get_account_properties) | **GET** /api/api/chartofaccounts/{scope}/{code}/accounts/{accountCode}/properties | [EXPERIMENTAL] GetAccountProperties: Get Account properties
[**get_chart_of_accounts**](ChartOfAccountsApi.md#get_chart_of_accounts) | **GET** /api/api/chartofaccounts/{scope}/{code} | [EXPERIMENTAL] GetChartOfAccounts: Get ChartOfAccounts
[**get_chart_of_accounts_properties**](ChartOfAccountsApi.md#get_chart_of_accounts_properties) | **GET** /api/api/chartofaccounts/{scope}/{code}/properties | [EXPERIMENTAL] GetChartOfAccountsProperties: Get chart of accounts properties
[**get_cleardown_module**](ChartOfAccountsApi.md#get_cleardown_module) | **GET** /api/api/chartofaccounts/{scope}/{code}/cleardownmodules/{cleardownModuleCode} | [EXPERIMENTAL] GetCleardownModule: Get a Cleardown Module
[**get_general_ledger_profile**](ChartOfAccountsApi.md#get_general_ledger_profile) | **GET** /api/api/chartofaccounts/{scope}/{code}/generalledgerprofile/{generalLedgerProfileCode} | [EXPERIMENTAL] GetGeneralLedgerProfile: Get a General Ledger Profile.
[**get_posting_module**](ChartOfAccountsApi.md#get_posting_module) | **GET** /api/api/chartofaccounts/{scope}/{code}/postingmodules/{postingModuleCode} | [EXPERIMENTAL] GetPostingModule: Get a Posting Module
[**list_accounts**](ChartOfAccountsApi.md#list_accounts) | **GET** /api/api/chartofaccounts/{scope}/{code}/accounts | [EXPERIMENTAL] ListAccounts: List Accounts
[**list_charts_of_accounts**](ChartOfAccountsApi.md#list_charts_of_accounts) | **GET** /api/api/chartofaccounts | [EXPERIMENTAL] ListChartsOfAccounts: List Charts of Accounts
[**list_cleardown_module_rules**](ChartOfAccountsApi.md#list_cleardown_module_rules) | **GET** /api/api/chartofaccounts/{scope}/{code}/cleardownmodules/{cleardownModuleCode}/cleardownrules | [EXPERIMENTAL] ListCleardownModuleRules: List Cleardown Module Rules
[**list_cleardown_modules**](ChartOfAccountsApi.md#list_cleardown_modules) | **GET** /api/api/chartofaccounts/{scope}/{code}/cleardownmodules | [EXPERIMENTAL] ListCleardownModules: List Cleardown Modules
[**list_general_ledger_profiles**](ChartOfAccountsApi.md#list_general_ledger_profiles) | **GET** /api/api/chartofaccounts/{scope}/{code}/generalledgerprofile | [EXPERIMENTAL] ListGeneralLedgerProfiles: List General Ledger Profiles.
[**list_posting_module_rules**](ChartOfAccountsApi.md#list_posting_module_rules) | **GET** /api/api/chartofaccounts/{scope}/{code}/postingmodules/{postingModuleCode}/postingrules | [EXPERIMENTAL] ListPostingModuleRules: List Posting Module Rules
[**list_posting_modules**](ChartOfAccountsApi.md#list_posting_modules) | **GET** /api/api/chartofaccounts/{scope}/{code}/postingmodules | [EXPERIMENTAL] ListPostingModules: List Posting Modules
[**patch_chart_of_accounts**](ChartOfAccountsApi.md#patch_chart_of_accounts) | **PATCH** /api/api/chartofaccounts/{scope}/{code} | [EXPERIMENTAL] PatchChartOfAccounts: Patch a Chart of Accounts.
[**patch_cleardown_module**](ChartOfAccountsApi.md#patch_cleardown_module) | **PATCH** /api/api/chartofaccounts/{scope}/{code}/cleardownmodules/{cleardownModuleCode} | [EXPERIMENTAL] PatchCleardownModule: Patch a Cleardown Module
[**patch_posting_module**](ChartOfAccountsApi.md#patch_posting_module) | **PATCH** /api/api/chartofaccounts/{scope}/{code}/postingmodules/{postingModuleCode} | [EXPERIMENTAL] PatchPostingModule: Patch a Posting Module
[**set_cleardown_module_details**](ChartOfAccountsApi.md#set_cleardown_module_details) | **PUT** /api/api/chartofaccounts/{scope}/{code}/cleardownmodules/{cleardownModuleCode} | [EXPERIMENTAL] SetCleardownModuleDetails: Set the details of a Cleardown Module
[**set_cleardown_module_rules**](ChartOfAccountsApi.md#set_cleardown_module_rules) | **PUT** /api/api/chartofaccounts/{scope}/{code}/cleardownmodules/{cleardownModuleCode}/cleardownrules | [EXPERIMENTAL] SetCleardownModuleRules: Set the rules of a Cleardown Module
[**set_general_ledger_profile_mappings**](ChartOfAccountsApi.md#set_general_ledger_profile_mappings) | **PUT** /api/api/chartofaccounts/{scope}/{code}/generalledgerprofile/{generalLedgerProfileCode}/mappings | [EXPERIMENTAL] SetGeneralLedgerProfileMappings: Sets the General Ledger Profile Mappings.
[**set_posting_module_details**](ChartOfAccountsApi.md#set_posting_module_details) | **PUT** /api/api/chartofaccounts/{scope}/{code}/postingmodules/{postingModuleCode} | [EXPERIMENTAL] SetPostingModuleDetails: Set the details of a Posting Module
[**set_posting_module_rules**](ChartOfAccountsApi.md#set_posting_module_rules) | **PUT** /api/api/chartofaccounts/{scope}/{code}/postingmodules/{postingModuleCode}/postingrules | [EXPERIMENTAL] SetPostingModuleRules: Set the rules of a Posting Module
[**upsert_account_properties**](ChartOfAccountsApi.md#upsert_account_properties) | **POST** /api/api/chartofaccounts/{scope}/{code}/accounts/{accountCode}/properties/$upsert | [EXPERIMENTAL] UpsertAccountProperties: Upsert account properties
[**upsert_accounts**](ChartOfAccountsApi.md#upsert_accounts) | **POST** /api/api/chartofaccounts/{scope}/{code}/accounts | [EXPERIMENTAL] UpsertAccounts: Upsert Accounts
[**upsert_chart_of_accounts_properties**](ChartOfAccountsApi.md#upsert_chart_of_accounts_properties) | **POST** /api/api/chartofaccounts/{scope}/{code}/properties/$upsert | [EXPERIMENTAL] UpsertChartOfAccountsProperties: Upsert Chart of Accounts properties


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.chart_of_accounts_api import ChartOfAccountsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(ChartOfAccountsApi)
```

---

# **create_chart_of_accounts**
> ChartOfAccounts createChartOfAccounts = create_chart_of_accounts(scope, chart_of_accounts_request)

[EXPERIMENTAL] CreateChartOfAccounts: Create a Chart of Accounts

Create the given Chart of Accounts.

### Example

```python
api_instance = api_client_factory.build(ChartOfAccountsApi)
scope = 'scope_example' # str
chart_of_accounts_request = ChartOfAccountsRequest()
api_response = api_instance.create_chart_of_accounts(scope, chart_of_accounts_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts. | [required] 
 **chart_of_accounts_request** | [**ChartOfAccountsRequest**](ChartOfAccountsRequest.md)| The definition of the Chart of Accounts. | [required] 

### Return type

[**ChartOfAccounts**](ChartOfAccounts.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created Chart of Accounts. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **create_cleardown_module**
> CleardownModuleResponse createCleardownModule = create_cleardown_module(scope, code, cleardown_module_request)

[EXPERIMENTAL] CreateCleardownModule: Create a Cleardown Module

Create the given Cleardown Module.

### Example

```python
api_instance = api_client_factory.build(ChartOfAccountsApi)
scope = 'scope_example' # str
code = 'code_example' # str
cleardown_module_request = CleardownModuleRequest()
api_response = api_instance.create_cleardown_module(scope, code, cleardown_module_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts. | [required] 
 **code** | **str**| The code of the Chart of Accounts. Together with the scope this uniquely identifies the Chart of Accounts. | [required] 
 **cleardown_module_request** | [**CleardownModuleRequest**](CleardownModuleRequest.md)| The definition of the Cleardown Module. | [required] 

### Return type

[**CleardownModuleResponse**](CleardownModuleResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created Cleardown Module. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **create_general_ledger_profile**
> GeneralLedgerProfileResponse createGeneralLedgerProfile = create_general_ledger_profile(scope, code, general_ledger_profile_request)

[EXPERIMENTAL] CreateGeneralLedgerProfile: Create a General Ledger Profile.

Create the given General Ledger profile.

### Example

```python
api_instance = api_client_factory.build(ChartOfAccountsApi)
scope = 'scope_example' # str
code = 'code_example' # str
general_ledger_profile_request = GeneralLedgerProfileRequest()
api_response = api_instance.create_general_ledger_profile(scope, code, general_ledger_profile_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts. | [required] 
 **code** | **str**| The code of the Chart of Accounts. | [required] 
 **general_ledger_profile_request** | [**GeneralLedgerProfileRequest**](GeneralLedgerProfileRequest.md)| The definition of the General Ledger Profile. | [required] 

### Return type

[**GeneralLedgerProfileResponse**](GeneralLedgerProfileResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created General Ledger Profile. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **create_posting_module**
> PostingModuleResponse createPostingModule = create_posting_module(scope, code, posting_module_request)

[EXPERIMENTAL] CreatePostingModule: Create a Posting Module

Create the given Posting Module.

### Example

```python
api_instance = api_client_factory.build(ChartOfAccountsApi)
scope = 'scope_example' # str
code = 'code_example' # str
posting_module_request = PostingModuleRequest()
api_response = api_instance.create_posting_module(scope, code, posting_module_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts. | [required] 
 **code** | **str**| The code of the Chart of Accounts. Together with the scope this uniquely identifies the Chart of Accounts. | [required] 
 **posting_module_request** | [**PostingModuleRequest**](PostingModuleRequest.md)| The definition of the Posting Module. | [required] 

### Return type

[**PostingModuleResponse**](PostingModuleResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created Posting Module. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_accounts**
> DeleteAccountsResponse deleteAccounts = delete_accounts(scope, code, request_body, delete_mode=delete_mode)

[EXPERIMENTAL] DeleteAccounts: Soft or hard delete multiple accounts

Delete one or more account from the Chart of Accounts. Soft deletion marks the account as inactive  While the Hard deletion is deleting the account.  The maximum number of accounts that this method can delete per request is 2,000.

### Example

```python
api_instance = api_client_factory.build(ChartOfAccountsApi)
scope = 'scope_example' # str
code = 'code_example' # str
request_body = ["AccountCode1","AccountCode2"] # List[str]
delete_mode = 'delete_mode_example' # str (optional)
api_response = api_instance.delete_accounts(scope, code, request_body, delete_mode=delete_mode)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts. | [required] 
 **code** | **str**| The code of the Chart of Accounts. Together with the scope this uniquely identifies              the Chart of Accounts. | [required] 
 **request_body** | [**List[str]**](str.md)| The codes of the accounts to delete. | [required] 
 **delete_mode** | **str**| The delete mode to use (defaults to &#39;Soft&#39;). | [optional] 

### Return type

[**DeleteAccountsResponse**](DeleteAccountsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the Accounts were deleted. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_chart_of_accounts**
> DeletedEntityResponse deleteChartOfAccounts = delete_chart_of_accounts(scope, code)

[EXPERIMENTAL] DeleteChartOfAccounts: Delete a Chart of Accounts

Delete the given Chart of Accounts.

### Example

```python
api_instance = api_client_factory.build(ChartOfAccountsApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.delete_chart_of_accounts(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts to be deleted. | [required] 
 **code** | **str**| The code of the Chart of Accounts to be deleted. Together with the scope this uniquely identifies the Chart of Accounts. | [required] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the Chart of Accounts was deleted. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_cleardown_module**
> DeletedEntityResponse deleteCleardownModule = delete_cleardown_module(scope, code, cleardown_module_code)

[EXPERIMENTAL] DeleteCleardownModule: Delete a Cleardown Module.

Delete the given Cleardown Module.

### Example

```python
api_instance = api_client_factory.build(ChartOfAccountsApi)
scope = 'scope_example' # str
code = 'code_example' # str
cleardown_module_code = 'cleardown_module_code_example' # str
api_response = api_instance.delete_cleardown_module(scope, code, cleardown_module_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts. | [required] 
 **code** | **str**| The code of the Chart of Accounts. Together with the scope this uniquely identifies the Chart of Accounts. | [required] 
 **cleardown_module_code** | **str**| The code of the Cleardown Module to be deleted. | [required] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the Cleardown Module was deleted. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_general_ledger_profile**
> DeletedEntityResponse deleteGeneralLedgerProfile = delete_general_ledger_profile(scope, code, general_ledger_profile_code)

[EXPERIMENTAL] DeleteGeneralLedgerProfile: Delete a General Ledger Profile.

Delete the given General Ledger Profile.

### Example

```python
api_instance = api_client_factory.build(ChartOfAccountsApi)
scope = 'scope_example' # str
code = 'code_example' # str
general_ledger_profile_code = 'general_ledger_profile_code_example' # str
api_response = api_instance.delete_general_ledger_profile(scope, code, general_ledger_profile_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts for the General Ledger Profile. | [required] 
 **code** | **str**| The code of the Chart of Accounts for the General Ledger Profile. | [required] 
 **general_ledger_profile_code** | **str**| The Code of the General Ledger Profile. | [required] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the General Ledger Profile was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_posting_module**
> DeletedEntityResponse deletePostingModule = delete_posting_module(scope, code, posting_module_code)

[EXPERIMENTAL] DeletePostingModule: Delete a Posting Module.

Delete the given Posting Module.

### Example

```python
api_instance = api_client_factory.build(ChartOfAccountsApi)
scope = 'scope_example' # str
code = 'code_example' # str
posting_module_code = 'posting_module_code_example' # str
api_response = api_instance.delete_posting_module(scope, code, posting_module_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts. | [required] 
 **code** | **str**| The code of the Chart of Accounts. Together with the scope this uniquely identifies the Chart of Accounts. | [required] 
 **posting_module_code** | **str**| The code of the Posting Module to be deleted. | [required] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the Posting Module was deleted. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_account**
> Account getAccount = get_account(scope, code, account_code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)

[EXPERIMENTAL] GetAccount: Get Account

Retrieve the definition of a particular Account which is part of a Chart of Accounts.

### Example

```python
api_instance = api_client_factory.build(ChartOfAccountsApi)
scope = 'scope_example' # str
code = 'code_example' # str
account_code = 'account_code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.get_account(scope, code, account_code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts. | [required] 
 **code** | **str**| The code of the Chart of Accounts. Together with the scope this uniquely identifies the Chart of Accounts. | [required] 
 **account_code** | **str**| The code of the Account. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the Account properties. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Account definition. Defaults to returning the latest version of the Account definition if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Account&#39; domain to decorate onto the Account.              These must take the format {domain}/{scope}/{code}, for example &#39;Account/Manager/Id&#39;. If no properties are specified, then no properties will be returned. | [optional] 

### Return type

[**Account**](Account.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Account definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_account_properties**
> AccountProperties getAccountProperties = get_account_properties(scope, code, account_code, effective_at=effective_at, as_at=as_at)

[EXPERIMENTAL] GetAccountProperties: Get Account properties

Get all the properties of a single account.

### Example

```python
api_instance = api_client_factory.build(ChartOfAccountsApi)
scope = 'scope_example' # str
code = 'code_example' # str
account_code = 'account_code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_account_properties(scope, code, account_code, effective_at=effective_at, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts to update or insert the properties onto. | [required] 
 **code** | **str**| The code of the Chart of Accounts to update or insert the properties onto. Together with the scope this uniquely identifies the Chart of Accounts. | [required] 
 **account_code** | **str**| The unique ID of the account to get properties for. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to list the Account&#39;s properties. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the Account&#39;s properties. Defaults to return the latest version of each property if not specified. | [optional] 

### Return type

[**AccountProperties**](AccountProperties.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The properties of the specified account |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_chart_of_accounts**
> ChartOfAccounts getChartOfAccounts = get_chart_of_accounts(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)

[EXPERIMENTAL] GetChartOfAccounts: Get ChartOfAccounts

Retrieve the definition of a particular Chart of Accounts.

### Example

```python
api_instance = api_client_factory.build(ChartOfAccountsApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.get_chart_of_accounts(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts. | [required] 
 **code** | **str**| The code of the Chart of Accounts. Together with the scope this uniquely identifies the Chart of Accounts. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the Chart of Accounts properties. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Chart of Accounts definition. Defaults to returning the latest version of the Chart of Accounts definition if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;ChartOfAccounts&#39; domain to decorate onto the Chart of Accounts.              These must take the format {domain}/{scope}/{code}, for example &#39;ChartOfAccounts/Manager/Id&#39;. If no properties are specified, then no properties will be returned. | [optional] 

### Return type

[**ChartOfAccounts**](ChartOfAccounts.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Chart Of Accounts definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_chart_of_accounts_properties**
> ChartOfAccountsProperties getChartOfAccountsProperties = get_chart_of_accounts_properties(scope, code, effective_at=effective_at, as_at=as_at)

[EXPERIMENTAL] GetChartOfAccountsProperties: Get chart of accounts properties

Get all the properties of a single chart of accounts.

### Example

```python
api_instance = api_client_factory.build(ChartOfAccountsApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_chart_of_accounts_properties(scope, code, effective_at=effective_at, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the chart of accounts to list the properties for. | [required] 
 **code** | **str**| The code of the chart of accounts to list the properties for. Together with the scope this uniquely identifies the chart of accounts. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to list the chart of accounts&#39; properties. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the chart of accounts&#39; properties. Defaults to return the latest version of each property if not specified. | [optional] 

### Return type

[**ChartOfAccountsProperties**](ChartOfAccountsProperties.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The properties of the specified chartOfAccounts |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_cleardown_module**
> CleardownModuleResponse getCleardownModule = get_cleardown_module(scope, code, cleardown_module_code, as_at=as_at)

[EXPERIMENTAL] GetCleardownModule: Get a Cleardown Module

Retrieve the definition of a Cleardown Module complete with its rules.

### Example

```python
api_instance = api_client_factory.build(ChartOfAccountsApi)
scope = 'scope_example' # str
code = 'code_example' # str
cleardown_module_code = 'cleardown_module_code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_cleardown_module(scope, code, cleardown_module_code, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts. | [required] 
 **code** | **str**| The code of the Chart of Accounts. Together with the scope this uniquely identifies the Chart of Accounts. | [required] 
 **cleardown_module_code** | **str**| The code of the Cleardown Module. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Cleardown Module. Defaults to return the latest version of the Cleardown Module if not specified. | [optional] 

### Return type

[**CleardownModuleResponse**](CleardownModuleResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The full definition of the Cleardown Module. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_general_ledger_profile**
> GeneralLedgerProfileResponse getGeneralLedgerProfile = get_general_ledger_profile(scope, code, general_ledger_profile_code, as_at=as_at)

[EXPERIMENTAL] GetGeneralLedgerProfile: Get a General Ledger Profile.

Get the given General Ledger Profile.

### Example

```python
api_instance = api_client_factory.build(ChartOfAccountsApi)
scope = 'scope_example' # str
code = 'code_example' # str
general_ledger_profile_code = 'general_ledger_profile_code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_general_ledger_profile(scope, code, general_ledger_profile_code, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts for the General Ledger Profile. | [required] 
 **code** | **str**| The code of the Chart of Accounts for the General Ledger Profile. | [required] 
 **general_ledger_profile_code** | **str**| The General Ledger Profile Code of the General Ledger Profile. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the General Ledger Profile. Defaults to return the latest version of the General Ledger Profile if not specified. | [optional] 

### Return type

[**GeneralLedgerProfileResponse**](GeneralLedgerProfileResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested General Ledger Profile entry. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_posting_module**
> PostingModuleResponse getPostingModule = get_posting_module(scope, code, posting_module_code, as_at=as_at)

[EXPERIMENTAL] GetPostingModule: Get a Posting Module

Retrieve the definition of a Posting Module complete with its rules.

### Example

```python
api_instance = api_client_factory.build(ChartOfAccountsApi)
scope = 'scope_example' # str
code = 'code_example' # str
posting_module_code = 'posting_module_code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_posting_module(scope, code, posting_module_code, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts. | [required] 
 **code** | **str**| The code of the Chart of Accounts. Together with the scope this uniquely identifies the Chart of Accounts. | [required] 
 **posting_module_code** | **str**| The code of the Posting Module. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Posting Module. Defaults to return the latest version of the Posting Module if not specified. | [optional] 

### Return type

[**PostingModuleResponse**](PostingModuleResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The full definition of the Posting Module. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_accounts**
> PagedResourceListOfAccount listAccounts = list_accounts(scope, code, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, property_keys=property_keys)

[EXPERIMENTAL] ListAccounts: List Accounts

List the accounts in a Chart of Accounts

### Example

```python
api_instance = api_client_factory.build(ChartOfAccountsApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.list_accounts(scope, code, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts. | [required] 
 **code** | **str**| The code of the Chart of Accounts. Together with the scope this uniquely identifies              the Chart of Accounts. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to list the TimeVariant properties decorated on Accounts. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Accounts. Defaults to              returning the latest version if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing charts of accounts; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the Account type, specify \&quot;code eq &#39;001&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Account&#39; domain to decorate onto the Account.              These must have the format {domain}/{scope}/{code}, for example &#39;Account/system/Name&#39;. | [optional] 

### Return type

[**PagedResourceListOfAccount**](PagedResourceListOfAccount.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Accounts in the given Chart of Accounts. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_charts_of_accounts**
> PagedResourceListOfChartOfAccounts listChartsOfAccounts = list_charts_of_accounts(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)

[EXPERIMENTAL] ListChartsOfAccounts: List Charts of Accounts

List all the Charts of Accounts matching particular criteria.

### Example

```python
api_instance = api_client_factory.build(ChartOfAccountsApi)
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.list_charts_of_accounts(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effective datetime or cut label at which to list the TimeVariant properties for the Chart Of Accounts. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the charts of accounts. Defaults to returning the latest version              of each Chart of Accounts if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing charts of accounts; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the Chart of Accounts type, specify \&quot;id.Code eq &#39;001&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;ChartOfAccounts&#39; domain to decorate onto each Chart of Accounts.              These must take the format {domain}/{scope}/{code}, for example &#39;ChartOfAccounts/Manager/Id&#39;. | [optional] 

### Return type

[**PagedResourceListOfChartOfAccounts**](PagedResourceListOfChartOfAccounts.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Charts of Accounts. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_cleardown_module_rules**
> PagedResourceListOfCleardownModuleRule listCleardownModuleRules = list_cleardown_module_rules(scope, code, cleardown_module_code, as_at=as_at, page=page, limit=limit, filter=filter)

[EXPERIMENTAL] ListCleardownModuleRules: List Cleardown Module Rules

List the Rules in a Cleardown Module

### Example

```python
api_instance = api_client_factory.build(ChartOfAccountsApi)
scope = 'scope_example' # str
code = 'code_example' # str
cleardown_module_code = 'cleardown_module_code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
api_response = api_instance.list_cleardown_module_rules(scope, code, cleardown_module_code, as_at=as_at, page=page, limit=limit, filter=filter)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts. | [required] 
 **code** | **str**| The code of the Chart of Accounts. Together with the scope this uniquely identifies the Chart of Accounts. | [required] 
 **cleardown_module_code** | **str**| The code of the cleardown module. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the instrument. Defaults to              returning the latest version if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing cleardown module rules; this              value is returned from the previous call. If a pagination token is provided, the filter              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the rule id, specify \&quot;ruleId eq &#39;rule 1&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 

### Return type

[**PagedResourceListOfCleardownModuleRule**](PagedResourceListOfCleardownModuleRule.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The rules in the given Cleardown Module. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_cleardown_modules**
> PagedResourceListOfCleardownModuleResponse listCleardownModules = list_cleardown_modules(scope, code, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

[EXPERIMENTAL] ListCleardownModules: List Cleardown Modules

List all the Cleardown Modules matching particular criteria.

### Example

```python
api_instance = api_client_factory.build(ChartOfAccountsApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
api_response = api_instance.list_cleardown_modules(scope, code, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts. | [required] 
 **code** | **str**| The code of the Chart of Accounts. Together with the scope this uniquely identifies the Chart of Accounts. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to list the Cleardown Module. Defaults to returning the latest version              of each Cleardown Module if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Cleardown Modules; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the Cleardown Module status, specify \&quot;status eq &#39;Active&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 

### Return type

[**PagedResourceListOfCleardownModuleResponse**](PagedResourceListOfCleardownModuleResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Cleardown Modules. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_general_ledger_profiles**
> PagedResourceListOfGeneralLedgerProfileResponse listGeneralLedgerProfiles = list_general_ledger_profiles(scope, code, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

[EXPERIMENTAL] ListGeneralLedgerProfiles: List General Ledger Profiles.

List all the General Ledger profiles matching particular criteria.

### Example

```python
api_instance = api_client_factory.build(ChartOfAccountsApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
api_response = api_instance.list_general_ledger_profiles(scope, code, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts | [required] 
 **code** | **str**| The code of the Chart of Accounts | [required] 
 **as_at** | **datetime**| The asAt datetime at which to list the General Ledger Profiles. Defaults to returning the latest version of each General Ledger Profile if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing General Ledger Profiles; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the General Ledger profiles type, specify \&quot;type eq &#39;PeriodBoundary&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 

### Return type

[**PagedResourceListOfGeneralLedgerProfileResponse**](PagedResourceListOfGeneralLedgerProfileResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested General Ledger Profile entries. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_posting_module_rules**
> PagedResourceListOfPostingModuleRule listPostingModuleRules = list_posting_module_rules(scope, code, posting_module_code, as_at=as_at, page=page, limit=limit, filter=filter)

[EXPERIMENTAL] ListPostingModuleRules: List Posting Module Rules

List the Rules in a Posting Module

### Example

```python
api_instance = api_client_factory.build(ChartOfAccountsApi)
scope = 'scope_example' # str
code = 'code_example' # str
posting_module_code = 'posting_module_code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
api_response = api_instance.list_posting_module_rules(scope, code, posting_module_code, as_at=as_at, page=page, limit=limit, filter=filter)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts. | [required] 
 **code** | **str**| The code of the Chart of Accounts. Together with the scope this uniquely identifies the Chart of Accounts. | [required] 
 **posting_module_code** | **str**| The code of the posting module. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the instrument. Defaults to              returning the latest version if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing posting module rules; this              value is returned from the previous call. If a pagination token is provided, the filter              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the rule id, specify \&quot;ruleId eq &#39;rule 1&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 

### Return type

[**PagedResourceListOfPostingModuleRule**](PagedResourceListOfPostingModuleRule.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The rules in the given Posting Module. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_posting_modules**
> PagedResourceListOfPostingModuleResponse listPostingModules = list_posting_modules(scope, code, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

[EXPERIMENTAL] ListPostingModules: List Posting Modules

List all the Posting Modules matching particular criteria.

### Example

```python
api_instance = api_client_factory.build(ChartOfAccountsApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
api_response = api_instance.list_posting_modules(scope, code, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts. | [required] 
 **code** | **str**| The code of the Chart of Accounts. Together with the scope this uniquely identifies the Chart of Accounts. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to list the Posting Module. Defaults to returning the latest version              of each Posting Module if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Posting Modules; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the Posting Module status, specify \&quot;status eq &#39;Active&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 

### Return type

[**PagedResourceListOfPostingModuleResponse**](PagedResourceListOfPostingModuleResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Posting Modules. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **patch_chart_of_accounts**
> ChartOfAccounts patchChartOfAccounts = patch_chart_of_accounts(scope, code, operation)

[EXPERIMENTAL] PatchChartOfAccounts: Patch a Chart of Accounts.

Update fields on a Chart of Accounts.  The behaviour is defined by the JSON Patch specification.    Currently supported fields are: DisplayName, Description.

### Example

```python
api_instance = api_client_factory.build(ChartOfAccountsApi)
scope = 'scope_example' # str
code = 'code_example' # str
operation = [{"value":"UpdatedChartOfAccountDisplayName","path":"/displayName","op":"add"},{"path":"/description","op":"remove"}] # List[Operation]
api_response = api_instance.patch_chart_of_accounts(scope, code, operation)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts. | [required] 
 **code** | **str**| The code of the Chart of Accounts. Together with the scope this uniquely identifies the Chart of Accounts. | [required] 
 **operation** | [**List[Operation]**](Operation.md)| The json patch document. For more information see: https://datatracker.ietf.org/doc/html/rfc6902. | [required] 

### Return type

[**ChartOfAccounts**](ChartOfAccounts.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated Chart of Accounts. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **patch_cleardown_module**
> CleardownModuleResponse patchCleardownModule = patch_cleardown_module(scope, code, cleardown_module_code, operation)

[EXPERIMENTAL] PatchCleardownModule: Patch a Cleardown Module

Update fields on a Cleardown Module.  The behaviour is defined by the JSON Patch specification.    Currently supported fields are: DisplayName, Description, Rules.

### Example

```python
api_instance = api_client_factory.build(ChartOfAccountsApi)
scope = 'scope_example' # str
code = 'code_example' # str
cleardown_module_code = 'cleardown_module_code_example' # str
operation = [{"value":{"ruleId":"rule3","generalLedgerAccountCode":"100002354","ruleFilter":"Account.Code startswith '200'"},"path":"/rules/-","op":"add"},{"value":"CleardownModuleDescriptionUpdated","path":"/description","op":"add"}] # List[Operation]
api_response = api_instance.patch_cleardown_module(scope, code, cleardown_module_code, operation)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts. | [required] 
 **code** | **str**| The code of the Chart of Accounts. Together with the scope this uniquely identifies the Chart of Accounts. | [required] 
 **cleardown_module_code** | **str**| The code of the Cleardown Module to be updated. | [required] 
 **operation** | [**List[Operation]**](Operation.md)| The json patch document. For more information see: https://datatracker.ietf.org/doc/html/rfc6902. | [required] 

### Return type

[**CleardownModuleResponse**](CleardownModuleResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated Cleardown Module. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **patch_posting_module**
> PostingModuleResponse patchPostingModule = patch_posting_module(scope, code, posting_module_code, operation)

[EXPERIMENTAL] PatchPostingModule: Patch a Posting Module

Update fields on a Posting Module.  The behaviour is defined by the JSON Patch specification.    Currently supported fields are: DisplayName, Description, Rules.

### Example

```python
api_instance = api_client_factory.build(ChartOfAccountsApi)
scope = 'scope_example' # str
code = 'code_example' # str
posting_module_code = 'posting_module_code_example' # str
operation = [{"value":{"ruleId":"rule3","generalLedgerAccountCode":"100002354","ruleFilter":"EconomicBucket eq 'PL_Other'"},"path":"/rules/-","op":"add"},{"value":"PostingModuleDescriptionUpdated","path":"/description","op":"add"}] # List[Operation]
api_response = api_instance.patch_posting_module(scope, code, posting_module_code, operation)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts. | [required] 
 **code** | **str**| The code of the Chart of Accounts. Together with the scope this uniquely identifies the Chart of Accounts. | [required] 
 **posting_module_code** | **str**| The code of the Posting Module to be updated. | [required] 
 **operation** | [**List[Operation]**](Operation.md)| The json patch document. For more information see: https://datatracker.ietf.org/doc/html/rfc6902. | [required] 

### Return type

[**PostingModuleResponse**](PostingModuleResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated Posting Module. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **set_cleardown_module_details**
> CleardownModuleResponse setCleardownModuleDetails = set_cleardown_module_details(scope, code, cleardown_module_code, cleardown_module_details)

[EXPERIMENTAL] SetCleardownModuleDetails: Set the details of a Cleardown Module

Update the given Cleardown Module details.

### Example

```python
api_instance = api_client_factory.build(ChartOfAccountsApi)
scope = 'scope_example' # str
code = 'code_example' # str
cleardown_module_code = 'cleardown_module_code_example' # str
cleardown_module_details = CleardownModuleDetails()
api_response = api_instance.set_cleardown_module_details(scope, code, cleardown_module_code, cleardown_module_details)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts. | [required] 
 **code** | **str**| The code of the Chart of Accounts. Together with the scope this uniquely identifies the Chart of Accounts. | [required] 
 **cleardown_module_code** | **str**| The code of the Cleardown Module to be updated. | [required] 
 **cleardown_module_details** | [**CleardownModuleDetails**](CleardownModuleDetails.md)| The new details for the Cleardown Module. | [required] 

### Return type

[**CleardownModuleResponse**](CleardownModuleResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated Cleardown Module. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **set_cleardown_module_rules**
> CleardownModuleRulesUpdatedResponse setCleardownModuleRules = set_cleardown_module_rules(scope, code, cleardown_module_code, cleardown_module_rule)

[EXPERIMENTAL] SetCleardownModuleRules: Set the rules of a Cleardown Module

Set the given Cleardown Modules rules, this will replace the existing set of rules for the cleardown module.

### Example

```python
api_instance = api_client_factory.build(ChartOfAccountsApi)
scope = 'scope_example' # str
code = 'code_example' # str
cleardown_module_code = 'cleardown_module_code_example' # str
cleardown_module_rule = [{"ruleId":"rule1","generalLedgerAccountCode":"100002354","ruleFilter":"Account.Type in 'Income','Expense','Revenue'"},{"ruleId":"rule2","generalLedgerAccountCode":"123456789","ruleFilter":"true eq true"}] # List[CleardownModuleRule]
api_response = api_instance.set_cleardown_module_rules(scope, code, cleardown_module_code, cleardown_module_rule)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts. | [required] 
 **code** | **str**| The code of the Chart of Accounts. Together with the scope this uniquely identifies the Chart of Accounts. | [required] 
 **cleardown_module_code** | **str**| The code of the Cleardown Module to be updated. | [required] 
 **cleardown_module_rule** | [**List[CleardownModuleRule]**](CleardownModuleRule.md)| The new rule set for the Cleardown Module. | [required] 

### Return type

[**CleardownModuleRulesUpdatedResponse**](CleardownModuleRulesUpdatedResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Cleardown Module with updated rules. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **set_general_ledger_profile_mappings**
> GeneralLedgerProfileResponse setGeneralLedgerProfileMappings = set_general_ledger_profile_mappings(scope, code, general_ledger_profile_code, general_ledger_profile_mapping)

[EXPERIMENTAL] SetGeneralLedgerProfileMappings: Sets the General Ledger Profile Mappings.

Update the given General Ledger profile Mappings.

### Example

```python
api_instance = api_client_factory.build(ChartOfAccountsApi)
scope = 'scope_example' # str
code = 'code_example' # str
general_ledger_profile_code = 'general_ledger_profile_code_example' # str
general_ledger_profile_mapping = [{"mappingFilter":"Account eq 'INVESTMENTS'","levels":["local.currency"]},{"mappingFilter":"Properties['Account/default/Profile'] eq 'CCY'","levels":["local.currency"]}] # List[GeneralLedgerProfileMapping]
api_response = api_instance.set_general_ledger_profile_mappings(scope, code, general_ledger_profile_code, general_ledger_profile_mapping)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts. | [required] 
 **code** | **str**| The code of the Chart of Accounts. | [required] 
 **general_ledger_profile_code** | **str**| The code of the General Ledger Profile | [required] 
 **general_ledger_profile_mapping** | [**List[GeneralLedgerProfileMapping]**](GeneralLedgerProfileMapping.md)| The updated General Ledger Profile Mappings, the previous mappings will be wholly replaced with this data. Mappings will be evaluated in the order they are provided. | [required] 

### Return type

[**GeneralLedgerProfileResponse**](GeneralLedgerProfileResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The General Ledger Profile that holds the updated mappings. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **set_posting_module_details**
> PostingModuleResponse setPostingModuleDetails = set_posting_module_details(scope, code, posting_module_code, posting_module_details)

[EXPERIMENTAL] SetPostingModuleDetails: Set the details of a Posting Module

Update the given Posting Module details.

### Example

```python
api_instance = api_client_factory.build(ChartOfAccountsApi)
scope = 'scope_example' # str
code = 'code_example' # str
posting_module_code = 'posting_module_code_example' # str
posting_module_details = PostingModuleDetails()
api_response = api_instance.set_posting_module_details(scope, code, posting_module_code, posting_module_details)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts. | [required] 
 **code** | **str**| The code of the Chart of Accounts. Together with the scope this uniquely identifies the Chart of Accounts. | [required] 
 **posting_module_code** | **str**| The code of the Posting Module to be updated. | [required] 
 **posting_module_details** | [**PostingModuleDetails**](PostingModuleDetails.md)| The new details for the Posting Module. | [required] 

### Return type

[**PostingModuleResponse**](PostingModuleResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated Posting Module. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **set_posting_module_rules**
> PostingModuleRulesUpdatedResponse setPostingModuleRules = set_posting_module_rules(scope, code, posting_module_code, posting_module_rule)

[EXPERIMENTAL] SetPostingModuleRules: Set the rules of a Posting Module

Set the given Posting Modules rules, this will replace the existing set of rules for the posting module.

### Example

```python
api_instance = api_client_factory.build(ChartOfAccountsApi)
scope = 'scope_example' # str
code = 'code_example' # str
posting_module_code = 'posting_module_code_example' # str
posting_module_rule = [{"ruleId":"rule 1","generalLedgerAccountCode":"100002354","ruleFilter":"1 eq 1"},{"ruleId":"rule 2","generalLedgerAccountCode":"123456789","ruleFilter":"true eq true"}] # List[PostingModuleRule]
api_response = api_instance.set_posting_module_rules(scope, code, posting_module_code, posting_module_rule)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts. | [required] 
 **code** | **str**| The code of the Chart of Accounts. Together with the scope this uniquely identifies the Chart of Accounts. | [required] 
 **posting_module_code** | **str**| The code of the Posting Module to be updated. | [required] 
 **posting_module_rule** | [**List[PostingModuleRule]**](PostingModuleRule.md)| The new rule set for the Posting Module. | [required] 

### Return type

[**PostingModuleRulesUpdatedResponse**](PostingModuleRulesUpdatedResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Posting Module with updated rules. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_account_properties**
> AccountProperties upsertAccountProperties = upsert_account_properties(scope, code, account_code, request_body=request_body)

[EXPERIMENTAL] UpsertAccountProperties: Upsert account properties

Update or insert one or more properties onto a single account. A property will be updated if it  already exists and inserted if it does not. All properties must be of the domain 'Account'.                Upserting a property that exists for an account, with a null value, will delete the instance of the property for that group.                Properties have an <i>effectiveFrom</i> datetime for which the property is valid, and an <i>effectiveUntil</i>  datetime until which the property is valid. Not supplying an <i>effectiveUntil</i> datetime results in the property being  valid indefinitely, or until the next <i>effectiveFrom</i> datetime of the property.

### Example

```python
api_instance = api_client_factory.build(ChartOfAccountsApi)
scope = 'scope_example' # str
code = 'code_example' # str
account_code = 'account_code_example' # str
request_body = {"Account/MyScope/FundManagerName":{"key":"Account/MyScope/FundManagerName","value":{"labelValue":"Smith"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00"},"Account/MyScope/SomeProperty":{"key":"Account/MyScope/SomeProperty","value":{"labelValue":"SomeValue"},"effectiveFrom":"2016-01-01T00:00:00.0000000+00:00"},"Account/MyScope/AnotherProperty":{"key":"Account/MyScope/AnotherProperty","value":{"labelValue":"AnotherValue"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00","effectiveUntil":"2020-01-01T00:00:00.0000000+00:00"},"Account/MyScope/ReBalanceInterval":{"key":"Account/MyScope/ReBalanceInterval","value":{"metricValue":{"value":30.0,"unit":"Days"}}}} # Dict[str, ModelProperty] (optional)
api_response = api_instance.upsert_account_properties(scope, code, account_code, request_body=request_body)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts to update or insert the properties onto. | [required] 
 **code** | **str**| The code of the Chart of Accounts to update or insert the properties onto. Together with the scope this uniquely identifies the Chart of Accounts. | [required] 
 **account_code** | **str**| The unique ID of the account to create or update properties for. | [required] 
 **request_body** | [**Dict[str, ModelProperty]**](ModelProperty.md)| The properties to be updated or inserted onto the chart of account. Each property in               the request must be keyed by its unique property key. This has the format {domain}/{scope}/{code} e.g. \&quot;Account/Manager/Id\&quot;. | [optional] 

### Return type

[**AccountProperties**](AccountProperties.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated or inserted properties. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_accounts**
> AccountsUpsertResponse upsertAccounts = upsert_accounts(scope, code, account)

[EXPERIMENTAL] UpsertAccounts: Upsert Accounts

Create or update accounts in the Chart of Accounts. An account will be updated  if it already exists and created if it does not.  The maximum number of accounts that this method can upsert per request is 2,000.

### Example

```python
api_instance = api_client_factory.build(ChartOfAccountsApi)
scope = 'scope_example' # str
code = 'code_example' # str
account = [{"code":"001456","description":"Cash","type":"Asset","status":"Active","control":"Manual","properties":{}},{"code":"123653","description":"Dividends","type":"Revenue","status":"Inactive","control":"System","properties":{}}] # List[Account]
api_response = api_instance.upsert_accounts(scope, code, account)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts. | [required] 
 **code** | **str**| The code of the Chart of Accounts. Together with the scope this uniquely identifies              the Chart of Accounts. | [required] 
 **account** | [**List[Account]**](Account.md)| A list of accounts to be created or updated. | [required] 

### Return type

[**AccountsUpsertResponse**](AccountsUpsertResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The newly upserted Accounts. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_chart_of_accounts_properties**
> ChartOfAccountsProperties upsertChartOfAccountsProperties = upsert_chart_of_accounts_properties(scope, code, request_body=request_body)

[EXPERIMENTAL] UpsertChartOfAccountsProperties: Upsert Chart of Accounts properties

Update or insert one or more properties onto a single Chart of Accounts. A property will be updated if it  already exists and inserted if it does not. All properties must be of the domain 'ChartOfAccounts'.                Upserting a property that exists for a Chart of Accounts, with a null value, will delete the instance of the property for that group.                Properties have an <i>effectiveFrom</i> datetime for which the property is valid, and an <i>effectiveUntil</i>  datetime until which the property is valid. Not supplying an <i>effectiveUntil</i> datetime results in the property being  valid indefinitely, or until the next <i>effectiveFrom</i> datetime of the property.

### Example

```python
api_instance = api_client_factory.build(ChartOfAccountsApi)
scope = 'scope_example' # str
code = 'code_example' # str
request_body = {"ChartOfAccounts/MyScope/FundManagerName":{"key":"ChartOfAccounts/MyScope/FundManagerName","value":{"labelValue":"Smith"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00"},"ChartOfAccounts/MyScope/SomeProperty":{"key":"ChartOfAccounts/MyScope/SomeProperty","value":{"labelValue":"SomeValue"},"effectiveFrom":"2016-01-01T00:00:00.0000000+00:00"},"ChartOfAccounts/MyScope/AnotherProperty":{"key":"ChartOfAccounts/MyScope/AnotherProperty","value":{"labelValue":"AnotherValue"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00","effectiveUntil":"2020-01-01T00:00:00.0000000+00:00"},"ChartOfAccounts/MyScope/ReBalanceInterval":{"key":"ChartOfAccounts/MyScope/ReBalanceInterval","value":{"metricValue":{"value":30.0,"unit":"Days"}}}} # Dict[str, ModelProperty] (optional)
api_response = api_instance.upsert_chart_of_accounts_properties(scope, code, request_body=request_body)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts to update or insert the properties onto. | [required] 
 **code** | **str**| The code of the Chart of Accounts to update or insert the properties onto. Together with the scope this uniquely identifies the Chart of Accounts. | [required] 
 **request_body** | [**Dict[str, ModelProperty]**](ModelProperty.md)| The properties to be updated or inserted onto the chart of account. Each property in               the request must be keyed by its unique property key. This has the format {domain}/{scope}/{code} e.g. \&quot;ChartOfAccounts/Manager/Id\&quot;. | [optional] 

### Return type

[**ChartOfAccountsProperties**](ChartOfAccountsProperties.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated or inserted properties. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

