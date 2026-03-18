# lusid.PortfolioGroupsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_portfolio_to_group**](PortfolioGroupsApi.md#add_portfolio_to_group) | **POST** /api/api/portfoliogroups/{scope}/{code}/portfolios | [EARLY ACCESS] AddPortfolioToGroup: Add portfolio to group
[**add_sub_group_to_group**](PortfolioGroupsApi.md#add_sub_group_to_group) | **POST** /api/api/portfoliogroups/{scope}/{code}/subgroups | [EARLY ACCESS] AddSubGroupToGroup: Add sub group to group
[**build_transactions_for_portfolio_group**](PortfolioGroupsApi.md#build_transactions_for_portfolio_group) | **POST** /api/api/portfoliogroups/{scope}/{code}/transactions/$build | BuildTransactionsForPortfolioGroup: Build transactions for transaction portfolios in a portfolio group
[**create_portfolio_group**](PortfolioGroupsApi.md#create_portfolio_group) | **POST** /api/api/portfoliogroups/{scope} | CreatePortfolioGroup: Create portfolio group
[**delete_group_properties**](PortfolioGroupsApi.md#delete_group_properties) | **POST** /api/api/portfoliogroups/{scope}/{code}/properties/$delete | [EARLY ACCESS] DeleteGroupProperties: Delete group properties
[**delete_key_from_portfolio_group_access_metadata**](PortfolioGroupsApi.md#delete_key_from_portfolio_group_access_metadata) | **DELETE** /api/api/portfoliogroups/{scope}/{code}/metadata/{metadataKey} | [EARLY ACCESS] DeleteKeyFromPortfolioGroupAccessMetadata: Delete a Portfolio Group Access Metadata entry
[**delete_portfolio_from_group**](PortfolioGroupsApi.md#delete_portfolio_from_group) | **DELETE** /api/api/portfoliogroups/{scope}/{code}/portfolios/{portfolioScope}/{portfolioCode} | [EARLY ACCESS] DeletePortfolioFromGroup: Delete portfolio from group
[**delete_portfolio_group**](PortfolioGroupsApi.md#delete_portfolio_group) | **DELETE** /api/api/portfoliogroups/{scope}/{code} | [EARLY ACCESS] DeletePortfolioGroup: Delete portfolio group
[**delete_sub_group_from_group**](PortfolioGroupsApi.md#delete_sub_group_from_group) | **DELETE** /api/api/portfoliogroups/{scope}/{code}/subgroups/{subgroupScope}/{subgroupCode} | [EARLY ACCESS] DeleteSubGroupFromGroup: Delete sub group from group
[**get_a2_b_data_for_portfolio_group**](PortfolioGroupsApi.md#get_a2_b_data_for_portfolio_group) | **GET** /api/api/portfoliogroups/{scope}/{code}/a2b | [EARLY ACCESS] GetA2BDataForPortfolioGroup: Get A2B data for a Portfolio Group
[**get_group_properties**](PortfolioGroupsApi.md#get_group_properties) | **GET** /api/api/portfoliogroups/{scope}/{code}/properties | [EARLY ACCESS] GetGroupProperties: Get group properties
[**get_holdings_for_portfolio_group**](PortfolioGroupsApi.md#get_holdings_for_portfolio_group) | **GET** /api/api/portfoliogroups/{scope}/{code}/holdings | GetHoldingsForPortfolioGroup: Get holdings for transaction portfolios in portfolio group
[**get_portfolio_group**](PortfolioGroupsApi.md#get_portfolio_group) | **GET** /api/api/portfoliogroups/{scope}/{code} | GetPortfolioGroup: Get portfolio group
[**get_portfolio_group_access_metadata_by_key**](PortfolioGroupsApi.md#get_portfolio_group_access_metadata_by_key) | **GET** /api/api/portfoliogroups/{scope}/{code}/metadata/{metadataKey} | [EARLY ACCESS] GetPortfolioGroupAccessMetadataByKey: Get an entry identified by a metadataKey in the Access Metadata of a Portfolio Group
[**get_portfolio_group_commands**](PortfolioGroupsApi.md#get_portfolio_group_commands) | **GET** /api/api/portfoliogroups/{scope}/{code}/commands | GetPortfolioGroupCommands: Get portfolio group commands
[**get_portfolio_group_expansion**](PortfolioGroupsApi.md#get_portfolio_group_expansion) | **GET** /api/api/portfoliogroups/{scope}/{code}/expansion | [EARLY ACCESS] GetPortfolioGroupExpansion: Get portfolio group expansion
[**get_portfolio_group_metadata**](PortfolioGroupsApi.md#get_portfolio_group_metadata) | **GET** /api/api/portfoliogroups/{scope}/{code}/metadata | [EARLY ACCESS] GetPortfolioGroupMetadata: Get Access Metadata rules for Portfolio Group
[**get_portfolio_group_property_time_series**](PortfolioGroupsApi.md#get_portfolio_group_property_time_series) | **GET** /api/api/portfoliogroups/{scope}/{code}/properties/time-series | [EARLY ACCESS] GetPortfolioGroupPropertyTimeSeries: Get the time series of a portfolio group property
[**get_portfolio_group_relations**](PortfolioGroupsApi.md#get_portfolio_group_relations) | **GET** /api/api/portfoliogroups/{scope}/{code}/relations | [EXPERIMENTAL] GetPortfolioGroupRelations: Get Relations for Portfolio Group
[**get_portfolio_group_relationships**](PortfolioGroupsApi.md#get_portfolio_group_relationships) | **GET** /api/api/portfoliogroups/{scope}/{code}/relationships | [EARLY ACCESS] GetPortfolioGroupRelationships: Get Relationships for Portfolio Group
[**get_transactions_for_portfolio_group**](PortfolioGroupsApi.md#get_transactions_for_portfolio_group) | **GET** /api/api/portfoliogroups/{scope}/{code}/transactions | GetTransactionsForPortfolioGroup: Get transactions for transaction portfolios in a portfolio group
[**list_portfolio_groups**](PortfolioGroupsApi.md#list_portfolio_groups) | **GET** /api/api/portfoliogroups/{scope} | ListPortfolioGroups: List portfolio groups
[**patch_portfolio_group_access_metadata**](PortfolioGroupsApi.md#patch_portfolio_group_access_metadata) | **PATCH** /api/api/portfoliogroups/{scope}/{code}/metadata | [EARLY ACCESS] PatchPortfolioGroupAccessMetadata: Patch Access Metadata rules for a Portfolio Group.
[**update_portfolio_group**](PortfolioGroupsApi.md#update_portfolio_group) | **PUT** /api/api/portfoliogroups/{scope}/{code} | [EARLY ACCESS] UpdatePortfolioGroup: Update portfolio group
[**upsert_group_properties**](PortfolioGroupsApi.md#upsert_group_properties) | **POST** /api/api/portfoliogroups/{scope}/{code}/properties/$upsert | [EARLY ACCESS] UpsertGroupProperties: Upsert group properties
[**upsert_portfolio_group_access_metadata**](PortfolioGroupsApi.md#upsert_portfolio_group_access_metadata) | **PUT** /api/api/portfoliogroups/{scope}/{code}/metadata/{metadataKey} | UpsertPortfolioGroupAccessMetadata: Upsert a Portfolio Group Access Metadata entry associated with a specific metadataKey. This creates or updates the data in LUSID.


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.portfolio_groups_api import PortfolioGroupsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(PortfolioGroupsApi)
```

---

# **add_portfolio_to_group**
> PortfolioGroup addPortfolioToGroup = add_portfolio_to_group(scope, code, effective_at=effective_at, resource_id=resource_id)

[EARLY ACCESS] AddPortfolioToGroup: Add portfolio to group

Add a single portfolio to a portfolio group.

### Example

```python
api_instance = api_client_factory.build(PortfolioGroupsApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
resource_id = ResourceId()
api_response = api_instance.add_portfolio_to_group(scope, code, effective_at=effective_at, resource_id=resource_id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group to add a portfolio to. | [required] 
 **code** | **str**| The code of the portfolio group to add a portfolio to. Together with the scope this uniquely identifies the portfolio group. | [required] 
 **effective_at** | **str**| The effective datetime or cut label from which the portfolio will be added to the group. | [optional] 
 **resource_id** | [**ResourceId**](ResourceId.md)| The resource identifier of the portfolio to add to the portfolio group. | [optional] 

### Return type

[**PortfolioGroup**](PortfolioGroup.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The portfolio group containing the newly added portfolio |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **add_sub_group_to_group**
> PortfolioGroup addSubGroupToGroup = add_sub_group_to_group(scope, code, effective_at=effective_at, resource_id=resource_id)

[EARLY ACCESS] AddSubGroupToGroup: Add sub group to group

Add a portfolio group to a portfolio group as a sub group.

### Example

```python
api_instance = api_client_factory.build(PortfolioGroupsApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
resource_id = ResourceId()
api_response = api_instance.add_sub_group_to_group(scope, code, effective_at=effective_at, resource_id=resource_id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group to add a portfolio group to. | [required] 
 **code** | **str**| The code of the portfolio group to add a portfolio group to. Together with the scope this uniquely identifies the portfolio group. | [required] 
 **effective_at** | **str**| The effective datetime or cut label from which the sub group will be added to the group. | [optional] 
 **resource_id** | [**ResourceId**](ResourceId.md)| The resource identifier of the portfolio group to add to the portfolio group as a sub group. | [optional] 

### Return type

[**PortfolioGroup**](PortfolioGroup.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The portfolio group containing the newly added portfolio group as a sub group |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **build_transactions_for_portfolio_group**
> VersionedResourceListOfOutputTransaction buildTransactionsForPortfolioGroup = build_transactions_for_portfolio_group(scope, code, transaction_query_parameters, as_at=as_at, filter=filter, property_keys=property_keys, limit=limit, page=page, data_model_scope=data_model_scope, data_model_code=data_model_code, membership_type=membership_type)

BuildTransactionsForPortfolioGroup: Build transactions for transaction portfolios in a portfolio group

Build transactions for transaction portfolios in a portfolio group over a given interval of effective time.                When the specified portfolio in a portfolio group is a derived transaction portfolio, the returned set of transactions is the  union set of all transactions of the parent (and any grandparents etc.) and the specified derived transaction portfolio itself.

### Example

```python
api_instance = api_client_factory.build(PortfolioGroupsApi)
scope = 'scope_example' # str
code = 'code_example' # str
transaction_query_parameters = TransactionQueryParameters()
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
filter = 'filter_example' # str (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
limit = 56 # int (optional)
page = 'page_example' # str (optional)
data_model_scope = 'data_model_scope_example' # str (optional)
data_model_code = 'data_model_code_example' # str (optional)
membership_type = 'membership_type_example' # str (optional)
api_response = api_instance.build_transactions_for_portfolio_group(scope, code, transaction_query_parameters, as_at=as_at, filter=filter, property_keys=property_keys, limit=limit, page=page, data_model_scope=data_model_scope, data_model_code=data_model_code, membership_type=membership_type)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group. | [required] 
 **code** | **str**| The code of the portfolio group. Together with the scope this uniquely identifies               the portfolio group. | [required] 
 **transaction_query_parameters** | [**TransactionQueryParameters**](TransactionQueryParameters.md)| The query queryParameters which control how the output transactions are built. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to build the transactions. Defaults to return the latest               version of each transaction if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.               For example, to filter on the Transaction Type, use \&quot;type eq &#39;Buy&#39;\&quot;               Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Instrument\&quot; or \&quot;Transaction\&quot; domain to decorate onto               the transactions. These take the format {domain}/{scope}/{code} e.g. \&quot;Instrument/system/Name\&quot; or               \&quot;Transaction/strategy/quantsignal\&quot;. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing transactions from a previous call to BuildTransactions. | [optional] 
 **data_model_scope** | **str**| The optional scope of a Custom Data Model to use | [optional] 
 **data_model_code** | **str**| The optional code of a Custom Data Model to use | [optional] 
 **membership_type** | **str**| The membership types of the specified Custom Data Model to return. Allowable values are Member, Candidate and All. Defaults to Member. | [optional] 

### Return type

[**VersionedResourceListOfOutputTransaction**](VersionedResourceListOfOutputTransaction.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested transactions from transaction portfolios in the specified portfolio group |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **create_portfolio_group**
> PortfolioGroup createPortfolioGroup = create_portfolio_group(scope, create_portfolio_group_request=create_portfolio_group_request)

CreatePortfolioGroup: Create portfolio group

Create a portfolio group in a specific scope.

### Example

```python
api_instance = api_client_factory.build(PortfolioGroupsApi)
scope = 'scope_example' # str
create_portfolio_group_request = CreatePortfolioGroupRequest()
api_response = api_instance.create_portfolio_group(scope, create_portfolio_group_request=create_portfolio_group_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that the portfolio group will be created in. | [required] 
 **create_portfolio_group_request** | [**CreatePortfolioGroupRequest**](CreatePortfolioGroupRequest.md)| The definition and details of the portfolio group. | [optional] 

### Return type

[**PortfolioGroup**](PortfolioGroup.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created portfolio group |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_group_properties**
> DeletedEntityResponse deleteGroupProperties = delete_group_properties(scope, code, request_body, effective_at=effective_at)

[EARLY ACCESS] DeleteGroupProperties: Delete group properties

Delete one or more properties from a single portfolio group. If the properties are time variant then an effective date time from which the properties  will be deleted must be specified. If the properties are perpetual then it is invalid to specify an effective date time for deletion.

### Example

```python
api_instance = api_client_factory.build(PortfolioGroupsApi)
scope = 'scope_example' # str
code = 'code_example' # str
request_body = ["PortfolioGroup/MyScope/MyPropertyName","PortfolioGroup/MyScope/MyPropertyName2"] # List[str]
effective_at = 'effective_at_example' # str (optional)
api_response = api_instance.delete_group_properties(scope, code, request_body, effective_at=effective_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the group to delete properties from. | [required] 
 **code** | **str**| The code of the group to delete properties from. Together with the scope this uniquely identifies the group. | [required] 
 **request_body** | [**List[str]**](str.md)| The property keys of the properties to delete. These take the format              {domain}/{scope}/{code} e.g. \&quot;PortfolioGroup/Manager/Id\&quot;. Each property must be from the \&quot;PortfolioGroup\&quot; domain. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to delete time-variant properties from.              The property must exist at the specified &#39;effectiveAt&#39; datetime. If the &#39;effectiveAt&#39; is not provided or is              before the time-variant property exists then a failure is returned. Do not specify this parameter if any of              the properties to delete are perpetual. | [optional] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the properties were deleted from the specified group |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_key_from_portfolio_group_access_metadata**
> DeletedEntityResponse deleteKeyFromPortfolioGroupAccessMetadata = delete_key_from_portfolio_group_access_metadata(scope, code, metadata_key, effective_at=effective_at, effective_until=effective_until)

[EARLY ACCESS] DeleteKeyFromPortfolioGroupAccessMetadata: Delete a Portfolio Group Access Metadata entry

Deletes the Portfolio Group Access Metadata entry that exactly matches the provided identifier parts.    It is important to always check to verify success (or failure).

### Example

```python
api_instance = api_client_factory.build(PortfolioGroupsApi)
scope = 'scope_example' # str
code = 'code_example' # str
metadata_key = 'metadata_key_example' # str
effective_at = 'effective_at_example' # str (optional)
effective_until = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.delete_key_from_portfolio_group_access_metadata(scope, code, metadata_key, effective_at=effective_at, effective_until=effective_until)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Portfolio Group | [required] 
 **code** | **str**| The Portfolio Group code | [required] 
 **metadata_key** | **str**| Key of the Access Metadata entry to delete | [required] 
 **effective_at** | **str**| The effective date to delete at, if this is not supplied, it will delete all data found | [optional] 
 **effective_until** | **datetime**| The effective date until which the delete is valid. If not supplied this will be valid indefinitely, or until the next &#39;effectiveAt&#39; date of the Access Metadata | [optional] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The has been deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_portfolio_from_group**
> PortfolioGroup deletePortfolioFromGroup = delete_portfolio_from_group(scope, code, portfolio_scope, portfolio_code, effective_at=effective_at)

[EARLY ACCESS] DeletePortfolioFromGroup: Delete portfolio from group

Remove a single portfolio from a portfolio group.

### Example

```python
api_instance = api_client_factory.build(PortfolioGroupsApi)
scope = 'scope_example' # str
code = 'code_example' # str
portfolio_scope = 'portfolio_scope_example' # str
portfolio_code = 'portfolio_code_example' # str
effective_at = 'effective_at_example' # str (optional)
api_response = api_instance.delete_portfolio_from_group(scope, code, portfolio_scope, portfolio_code, effective_at=effective_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group to remove the portfolio from. | [required] 
 **code** | **str**| The code of the portfolio group to remove the portfolio from. Together with the scope this uniquely identifies the portfolio group. | [required] 
 **portfolio_scope** | **str**| The scope of the portfolio being removed from the portfolio group. | [required] 
 **portfolio_code** | **str**| The code of the portfolio being removed from the portfolio group. Together with the scope this uniquely identifies the portfolio to remove. | [required] 
 **effective_at** | **str**| The effective datetime or cut label from which the portfolio will be removed from the portfolio group. | [optional] 

### Return type

[**PortfolioGroup**](PortfolioGroup.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The portfolio group with the portfolio removed from the group |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_portfolio_group**
> DeletedEntityResponse deletePortfolioGroup = delete_portfolio_group(scope, code)

[EARLY ACCESS] DeletePortfolioGroup: Delete portfolio group

Delete a single portfolio group. A portfolio group can be deleted while it still contains portfolios or sub groups.  In this case any portfolios or sub groups contained in this group will not be deleted, however they will no longer be grouped together by this portfolio group.  The deletion will be valid from the portfolio group's creation datetime, ie. the portfolio group will no longer exist at any effective datetime from the asAt datetime of deletion.

### Example

```python
api_instance = api_client_factory.build(PortfolioGroupsApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.delete_portfolio_group(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group to delete. | [required] 
 **code** | **str**| The code of the portfolio group to delete. Together with the scope this uniquely identifies the portfolio group to delete. | [required] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the portfolio group was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_sub_group_from_group**
> PortfolioGroup deleteSubGroupFromGroup = delete_sub_group_from_group(scope, code, subgroup_scope, subgroup_code, effective_at=effective_at)

[EARLY ACCESS] DeleteSubGroupFromGroup: Delete sub group from group

Remove a single portfolio group (sub group) from a portfolio group.

### Example

```python
api_instance = api_client_factory.build(PortfolioGroupsApi)
scope = 'scope_example' # str
code = 'code_example' # str
subgroup_scope = 'subgroup_scope_example' # str
subgroup_code = 'subgroup_code_example' # str
effective_at = 'effective_at_example' # str (optional)
api_response = api_instance.delete_sub_group_from_group(scope, code, subgroup_scope, subgroup_code, effective_at=effective_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group to remove the sub group from. | [required] 
 **code** | **str**| The code of the portfolio group to remove the sub group from. Together with the scope this uniquely identifies the portfolio group. | [required] 
 **subgroup_scope** | **str**| The scope of the sub group to remove from the portfolio group. | [required] 
 **subgroup_code** | **str**| The code of the sub group to remove from the portfolio group. Together with the scope this uniquely identifies the sub group. | [required] 
 **effective_at** | **str**| The effective datetime or cut label from which the sub group will be removed from the portfolio group. | [optional] 

### Return type

[**PortfolioGroup**](PortfolioGroup.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The portfolio group with the sub group removed from the group |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_a2_b_data_for_portfolio_group**
> VersionedResourceListOfA2BDataRecord getA2BDataForPortfolioGroup = get_a2_b_data_for_portfolio_group(scope, code, from_effective_at, to_effective_at, as_at=as_at, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code, property_keys=property_keys, filter=filter)

[EARLY ACCESS] GetA2BDataForPortfolioGroup: Get A2B data for a Portfolio Group

Get an A2B report for all Transaction Portfolios within the given portfolio group.

### Example

```python
api_instance = api_client_factory.build(PortfolioGroupsApi)
scope = 'scope_example' # str
code = 'code_example' # str
from_effective_at = 'from_effective_at_example' # str
to_effective_at = 'to_effective_at_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
recipe_id_scope = 'recipe_id_scope_example' # str (optional)
recipe_id_code = 'recipe_id_code_example' # str (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
filter = 'filter_example' # str (optional)
api_response = api_instance.get_a2_b_data_for_portfolio_group(scope, code, from_effective_at, to_effective_at, as_at=as_at, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code, property_keys=property_keys, filter=filter)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the group to retrieve the A2B report for. | [required] 
 **code** | **str**| The code of the group to retrieve the A2B report for. Together with the scope this              uniquely identifies the portfolio group. | [required] 
 **from_effective_at** | **str**| The lower bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no lower bound if this is not specified. | [required] 
 **to_effective_at** | **str**| The upper bound effective datetime or cut label (inclusive) from which to retrieve the data.              There is no upper bound if this is not specified. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the portfolio. Defaults to return the latest version              of each transaction if not specified. | [optional] 
 **recipe_id_scope** | **str**| The scope of the given recipeId | [optional] 
 **recipe_id_code** | **str**| The code of the given recipeId | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Instrument\&quot; domain to decorate onto              the results. These take the format {domain}/{scope}/{code} e.g. \&quot;Instrument/system/Name\&quot;. | [optional] 
 **filter** | **str**| Expression to filter the result set.              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**VersionedResourceListOfA2BDataRecord**](VersionedResourceListOfA2BDataRecord.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested group A2B data |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_group_properties**
> PortfolioGroupProperties getGroupProperties = get_group_properties(scope, code, effective_at=effective_at, as_at=as_at)

[EARLY ACCESS] GetGroupProperties: Get group properties

List all the properties of a single portfolio group.

### Example

```python
api_instance = api_client_factory.build(PortfolioGroupsApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_group_properties(scope, code, effective_at=effective_at, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the group to list the properties for. | [required] 
 **code** | **str**| The code of the group to list the properties for. Together with the scope this uniquely identifies the group. | [required] 
 **effective_at** | **str**| The effective date time or cut label at which to list the group&#39;s properties. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt date time at which to list the group&#39;s properties. Defaults to return the latest version of each property if not specified. | [optional] 

### Return type

[**PortfolioGroupProperties**](PortfolioGroupProperties.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The properties of the specified group |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_holdings_for_portfolio_group**
> VersionedResourceListOfPortfolioHolding getHoldingsForPortfolioGroup = get_holdings_for_portfolio_group(scope, code, effective_at=effective_at, as_at=as_at, filter=filter, property_keys=property_keys, by_taxlots=by_taxlots, include_settlement_events_after_days=include_settlement_events_after_days)

GetHoldingsForPortfolioGroup: Get holdings for transaction portfolios in portfolio group

Get the holdings of transaction portfolios in specified portfolio group.

### Example

```python
api_instance = api_client_factory.build(PortfolioGroupsApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
filter = 'filter_example' # str (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
by_taxlots = True # bool (optional)
include_settlement_events_after_days = 56 # int (optional)
api_response = api_instance.get_holdings_for_portfolio_group(scope, code, effective_at=effective_at, as_at=as_at, filter=filter, property_keys=property_keys, by_taxlots=by_taxlots, include_settlement_events_after_days=include_settlement_events_after_days)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group. | [required] 
 **code** | **str**| The code of the portfolio group. Together with the scope this uniquely identifies              the portfolio group. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the holdings of transaction              portfolios in the portfolio group. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the holdings of transaction portfolios in the portfolio group. Defaults              to return the latest version of the holdings if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Instrument\&quot;, \&quot;Holding\&quot; or \&quot;Portfolio\&quot; domain to decorate onto              the holdings. These take the format {domain}/{scope}/{code} e.g. \&quot;Instrument/system/Name\&quot; or \&quot;Holding/system/Cost\&quot;. | [optional] 
 **by_taxlots** | **bool**| Whether or not to expand the holdings to return the underlying tax-lots. Defaults to              False. | [optional] 
 **include_settlement_events_after_days** | **int**| Number of days ahead to bring back settlements from, in relation to the specified effectiveAt | [optional] 

### Return type

[**VersionedResourceListOfPortfolioHolding**](VersionedResourceListOfPortfolioHolding.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The holdings of transaction portfolios in a specific version of portfolio group |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_portfolio_group**
> PortfolioGroup getPortfolioGroup = get_portfolio_group(scope, code, effective_at=effective_at, as_at=as_at, related_entity_property_keys=related_entity_property_keys, relationship_definition_ids=relationship_definition_ids)

GetPortfolioGroup: Get portfolio group

Retrieve the definition of a single portfolio group.

### Example

```python
api_instance = api_client_factory.build(PortfolioGroupsApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
related_entity_property_keys = ['related_entity_property_keys_example'] # List[str] (optional)
relationship_definition_ids = ['relationship_definition_ids_example'] # List[str] (optional)
api_response = api_instance.get_portfolio_group(scope, code, effective_at=effective_at, as_at=as_at, related_entity_property_keys=related_entity_property_keys, relationship_definition_ids=relationship_definition_ids)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group to retrieve the definition for. | [required] 
 **code** | **str**| The code of the portfolio group to retrieve the definition for. Together with the scope              this uniquely identifies the portfolio group. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the portfolio group definition. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the portfolio group definition. Defaults to return              the latest version of the portfolio group definition if not specified. | [optional] 
 **related_entity_property_keys** | [**List[str]**](str.md)| A list of property keys from any domain that supports relationships              to decorate onto related entities. These must take the format {domain}/{scope}/{code}, for example &#39;Portfolio/Manager/Id&#39;. | [optional] 
 **relationship_definition_ids** | [**List[str]**](str.md)| A list of relationship definitions that are used to decorate related entities              onto the portfolio group in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. | [optional] 

### Return type

[**PortfolioGroup**](PortfolioGroup.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested portfolio group definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_portfolio_group_access_metadata_by_key**
> List[AccessMetadataValue] getPortfolioGroupAccessMetadataByKey = get_portfolio_group_access_metadata_by_key(scope, code, metadata_key, effective_at=effective_at, as_at=as_at)

[EARLY ACCESS] GetPortfolioGroupAccessMetadataByKey: Get an entry identified by a metadataKey in the Access Metadata of a Portfolio Group

Get a specific Portfolio Group access metadata by specifying the corresponding identifier parts                No matching will be performed through this endpoint. To retrieve a rule, it is necessary to specify, exactly, the identifier of the rule

### Example

```python
api_instance = api_client_factory.build(PortfolioGroupsApi)
scope = 'scope_example' # str
code = 'code_example' # str
metadata_key = 'metadata_key_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_portfolio_group_access_metadata_by_key(scope, code, metadata_key, effective_at=effective_at, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Portfolio Group | [required] 
 **code** | **str**| The Portfolio Group code | [required] 
 **metadata_key** | **str**| Key of the metadata entry to retrieve | [required] 
 **effective_at** | **str**| The effectiveAt datetime at which to retrieve the access metadata | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the access metadata | [optional] 

### Return type

[**List[AccessMetadataValue]**](AccessMetadataValue.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved Portfolio group access metadata filtered by metadataKey or any failure. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_portfolio_group_commands**
> ResourceListOfProcessedCommand getPortfolioGroupCommands = get_portfolio_group_commands(scope, code, from_as_at=from_as_at, to_as_at=to_as_at, filter=filter)

GetPortfolioGroupCommands: Get portfolio group commands

Gets all the commands that modified a single portfolio group.

### Example

```python
api_instance = api_client_factory.build(PortfolioGroupsApi)
scope = 'scope_example' # str
code = 'code_example' # str
from_as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
to_as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
filter = 'filter_example' # str (optional)
api_response = api_instance.get_portfolio_group_commands(scope, code, from_as_at=from_as_at, to_as_at=to_as_at, filter=filter)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group to retrieve the commands for. | [required] 
 **code** | **str**| The code of the portfolio group to retrieve the commands for. Together with the scope this uniquely identifies the portfolio group. | [required] 
 **from_as_at** | **datetime**| The lower bound asAt datetime (inclusive) from which to retrieve commands. There is no lower bound if this is not specified. | [optional] 
 **to_as_at** | **datetime**| The upper bound asAt datetime (inclusive) from which to retrieve commands. There is no upper bound if this is not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.               For example, to filter on the User ID, use \&quot;userId.id eq &#39;string&#39;\&quot;              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**ResourceListOfProcessedCommand**](ResourceListOfProcessedCommand.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The commands that modified the specified portfolio group |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_portfolio_group_expansion**
> ExpandedGroup getPortfolioGroupExpansion = get_portfolio_group_expansion(scope, code, effective_at=effective_at, as_at=as_at, property_filter=property_filter)

[EARLY ACCESS] GetPortfolioGroupExpansion: Get portfolio group expansion

List all the portfolios in a group, including all portfolios within sub groups in the group. Each portfolio will be decorated with all of its properties unless a property filter is specified.

### Example

```python
api_instance = api_client_factory.build(PortfolioGroupsApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
property_filter = ['property_filter_example'] # List[str] (optional)
api_response = api_instance.get_portfolio_group_expansion(scope, code, effective_at=effective_at, as_at=as_at, property_filter=property_filter)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group to expand. | [required] 
 **code** | **str**| The code of the portfolio group to expand. Together with the scope this uniquely identifies the portfolio              group to expand. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to expand the portfolio group. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to expand the portfolio group. Defaults to return the latest version of each portfolio in the group if not specified. | [optional] 
 **property_filter** | [**List[str]**](str.md)| The restricted list of property keys from the \&quot;Portfolio\&quot; domain which will be decorated onto each portfolio. These take the format {domain}/{scope}/{code} e.g. \&quot;Portfolio/Manager/Id\&quot;. | [optional] 

### Return type

[**ExpandedGroup**](ExpandedGroup.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The expanded portfolio group |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_portfolio_group_metadata**
> Dict[str, List[AccessMetadataValue]] getPortfolioGroupMetadata = get_portfolio_group_metadata(scope, code, effective_at=effective_at, as_at=as_at)

[EARLY ACCESS] GetPortfolioGroupMetadata: Get Access Metadata rules for Portfolio Group

Pass the scope and Portfolio Group code parameters to retrieve the associated Access Metadata

### Example

```python
api_instance = api_client_factory.build(PortfolioGroupsApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_portfolio_group_metadata(scope, code, effective_at=effective_at, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Portfolio Group | [required] 
 **code** | **str**| The Portfolio Group code | [required] 
 **effective_at** | **str**| The effectiveAt datetime at which to retrieve the Access Metadata | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Access Metadata | [optional] 

### Return type

**Dict[str, List[AccessMetadataValue]]**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The access metadata for the portfolio group or any failure. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_portfolio_group_property_time_series**
> ResourceListOfPropertyInterval getPortfolioGroupPropertyTimeSeries = get_portfolio_group_property_time_series(scope, code, property_key, portfolio_group_effective_at=portfolio_group_effective_at, as_at=as_at, filter=filter, page=page, limit=limit)

[EARLY ACCESS] GetPortfolioGroupPropertyTimeSeries: Get the time series of a portfolio group property

List the complete time series of a portfolio group property.

### Example

```python
api_instance = api_client_factory.build(PortfolioGroupsApi)
scope = 'scope_example' # str
code = 'code_example' # str
property_key = 'property_key_example' # str
portfolio_group_effective_at = 'portfolio_group_effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
filter = 'filter_example' # str (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
api_response = api_instance.get_portfolio_group_property_time_series(scope, code, property_key, portfolio_group_effective_at=portfolio_group_effective_at, as_at=as_at, filter=filter, page=page, limit=limit)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the group. | [required] 
 **code** | **str**| The code of the group. Together with the scope this uniquely identifies              the portfolio group. | [required] 
 **property_key** | **str**| The property key of the property that will have its history shown. These must be in the format {domain}/{scope}/{code} e.g. \&quot;PortfolioGroup/Manager/Id\&quot;.              Each property must be from the \&quot;PortfolioGroup\&quot; domain. | [required] 
 **portfolio_group_effective_at** | **str**| The effective datetime used to resolve the portfolio group. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the portfolio group&#39;s property history. Defaults to return the current datetime if not supplied. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **page** | **str**| The pagination token to use to continue listing properties from a previous call to get property time series.              This value is returned from the previous call. If a pagination token is provided the filter, effectiveAt, and asAt fields              must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 

### Return type

[**ResourceListOfPropertyInterval**](ResourceListOfPropertyInterval.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The time series of the property |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_portfolio_group_relations**
> ResourceListOfRelation getPortfolioGroupRelations = get_portfolio_group_relations(scope, code, effective_at=effective_at, as_at=as_at, filter=filter, identifier_types=identifier_types)

[EXPERIMENTAL] GetPortfolioGroupRelations: Get Relations for Portfolio Group

Get relations for the specified Portfolio Group

### Example

```python
api_instance = api_client_factory.build(PortfolioGroupsApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
filter = 'filter_example' # str (optional)
identifier_types = ['identifier_types_example'] # List[str] (optional)
api_response = api_instance.get_portfolio_group_relations(scope, code, effective_at=effective_at, as_at=as_at, filter=filter, identifier_types=identifier_types)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group. | [required] 
 **code** | **str**| The code of the portfolio group. Together with the scope this uniquely identifies              the portfolio group. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve relations. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve relations. Defaults to return the latest LUSID AsAt time if not specified. | [optional] 
 **filter** | **str**| Expression to filter the relations. Users should provide null or empty string for this field until further notice. | [optional] 
 **identifier_types** | [**List[str]**](str.md)| Identifiers types (as property keys) used for referencing Persons or Legal Entities. These take the format              {domain}/{scope}/{code} e.g. \&quot;Person/CompanyDetails/Role\&quot;. They must be from the \&quot;Person\&quot; or \&quot;LegalEntity\&quot; domain.              Only identifier types stated will be used to look up relevant entities in relations. If not applicable, provide an empty array. | [optional] 

### Return type

[**ResourceListOfRelation**](ResourceListOfRelation.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The relations for the specific portfolio group. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_portfolio_group_relationships**
> ResourceListOfRelationship getPortfolioGroupRelationships = get_portfolio_group_relationships(scope, code, effective_at=effective_at, as_at=as_at, filter=filter, identifier_types=identifier_types)

[EARLY ACCESS] GetPortfolioGroupRelationships: Get Relationships for Portfolio Group

Get relationships for the specified Portfolio Group

### Example

```python
api_instance = api_client_factory.build(PortfolioGroupsApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
filter = 'filter_example' # str (optional)
identifier_types = ['identifier_types_example'] # List[str] (optional)
api_response = api_instance.get_portfolio_group_relationships(scope, code, effective_at=effective_at, as_at=as_at, filter=filter, identifier_types=identifier_types)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group. | [required] 
 **code** | **str**| The code of the portfolio group. Together with the scope this uniquely identifies              the portfolio group. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve relationship. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve relationships. Defaults to return the latest LUSID AsAt time if not specified. | [optional] 
 **filter** | **str**| Expression to filter relationships. Users should provide null or empty string for this field until further notice. | [optional] 
 **identifier_types** | [**List[str]**](str.md)| Identifier types (as property keys) used for referencing Persons or Legal Entities.              These can be specified from the &#39;Person&#39; or &#39;LegalEntity&#39; domains and have the format {domain}/{scope}/{code}, for example              &#39;Person/CompanyDetails/Role&#39;. An Empty array may be used to return all related Entities. | [optional] 

### Return type

[**ResourceListOfRelationship**](ResourceListOfRelationship.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The relationships for the specific portfolio group. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_transactions_for_portfolio_group**
> VersionedResourceListOfTransaction getTransactionsForPortfolioGroup = get_transactions_for_portfolio_group(scope, code, from_transaction_date=from_transaction_date, to_transaction_date=to_transaction_date, as_at=as_at, filter=filter, property_keys=property_keys, limit=limit, page=page, show_cancelled_transactions=show_cancelled_transactions, sort_by=sort_by, data_model_scope=data_model_scope, data_model_code=data_model_code, membership_type=membership_type)

GetTransactionsForPortfolioGroup: Get transactions for transaction portfolios in a portfolio group

Get transactions for transaction portfolios in a portfolio group over a given interval of effective time.                When the specified portfolio in a portfolio group is a derived transaction portfolio, the returned set of transactions is the  union set of all transactions of the parent (and any grandparents etc.) and the specified derived transaction portfolio itself.

### Example

```python
api_instance = api_client_factory.build(PortfolioGroupsApi)
scope = 'scope_example' # str
code = 'code_example' # str
from_transaction_date = 'from_transaction_date_example' # str (optional)
to_transaction_date = 'to_transaction_date_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
filter = 'filter_example' # str (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
limit = 56 # int (optional)
page = 'page_example' # str (optional)
show_cancelled_transactions = True # bool (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
data_model_scope = 'data_model_scope_example' # str (optional)
data_model_code = 'data_model_code_example' # str (optional)
membership_type = 'membership_type_example' # str (optional)
api_response = api_instance.get_transactions_for_portfolio_group(scope, code, from_transaction_date=from_transaction_date, to_transaction_date=to_transaction_date, as_at=as_at, filter=filter, property_keys=property_keys, limit=limit, page=page, show_cancelled_transactions=show_cancelled_transactions, sort_by=sort_by, data_model_scope=data_model_scope, data_model_code=data_model_code, membership_type=membership_type)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group. | [required] 
 **code** | **str**| The code of the portfolio group. Together with the scope this uniquely identifies               the portfolio group. | [required] 
 **from_transaction_date** | **str**| The lower bound effective datetime or cut label (inclusive) from which to retrieve the transactions.               There is no lower bound if this is not specified. | [optional] 
 **to_transaction_date** | **str**| The upper bound effective datetime or cut label (inclusive) from which to retrieve transactions.               There is no upper bound if this is not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the transactions. Defaults to return the latest version               of each transaction if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.               For example, to filter on the Transaction Type, use \&quot;type eq &#39;Buy&#39;\&quot;               Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Instrument\&quot;, \&quot;Transaction\&quot;, \&quot;LegalEntity\&quot; or \&quot;CustodianAccount\&quot; domain to decorate onto               the transactions. These take the format {domain}/{scope}/{code} e.g. \&quot;Instrument/system/Name\&quot; or               \&quot;Transaction/strategy/quantsignal\&quot;. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing transactions from a previous call to GetTransactions. | [optional] 
 **show_cancelled_transactions** | **bool**| Option to specify whether or not to include cancelled transactions,               including previous versions of transactions which have since been amended.               Defaults to False if not specified. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **data_model_scope** | **str**| The optional scope of a Custom Data Model to use | [optional] 
 **data_model_code** | **str**| The optional code of a Custom Data Model to use | [optional] 
 **membership_type** | **str**| The membership types of the specified Custom Data Model to return. Allowable values are Member, Candidate and All. Defaults to Member. | [optional] 

### Return type

[**VersionedResourceListOfTransaction**](VersionedResourceListOfTransaction.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested transactions from transaction portfolios in the specified portfolio group |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_portfolio_groups**
> PagedResourceListOfPortfolioGroup listPortfolioGroups = list_portfolio_groups(scope, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, related_entity_property_keys=related_entity_property_keys, relationship_definition_ids=relationship_definition_ids)

ListPortfolioGroups: List portfolio groups

List all the portfolio groups in a single scope.

### Example

```python
api_instance = api_client_factory.build(PortfolioGroupsApi)
scope = 'scope_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
related_entity_property_keys = ['related_entity_property_keys_example'] # List[str] (optional)
relationship_definition_ids = ['relationship_definition_ids_example'] # List[str] (optional)
api_response = api_instance.list_portfolio_groups(scope, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, related_entity_property_keys=related_entity_property_keys, relationship_definition_ids=relationship_definition_ids)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to list the portfolio groups in. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to list the portfolio groups. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the portfolio groups. Defaults to return the latest version of each portfolio group if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing portfolio groups from a previous call to list portfolio groups. This  value is returned from the previous call. If a pagination token is provided the filter, effectiveAt, sortBy  and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to no limit if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.              For example, to filter on the Display Name, use \&quot;displayName eq &#39;string&#39;\&quot;              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 
 **related_entity_property_keys** | [**List[str]**](str.md)| A list of property keys from any domain that supports relationships              to decorate onto related entities. These must take the format {domain}/{scope}/{code}, for example &#39;Portfolio/Manager/Id&#39;. | [optional] 
 **relationship_definition_ids** | [**List[str]**](str.md)| A list of relationship definitions that are used to decorate related entities              onto the portfolio groups in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. | [optional] 

### Return type

[**PagedResourceListOfPortfolioGroup**](PagedResourceListOfPortfolioGroup.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The portfolio groups in the specified scope |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **patch_portfolio_group_access_metadata**
> Dict[str, List[AccessMetadataValue]] patchPortfolioGroupAccessMetadata = patch_portfolio_group_access_metadata(scope, code, access_metadata_operation, effective_at=effective_at, effective_until=effective_until)

[EARLY ACCESS] PatchPortfolioGroupAccessMetadata: Patch Access Metadata rules for a Portfolio Group.

Patch Portfolio Group Access Metadata Rules in a single scope.  The behaviour is defined by the JSON Patch specification.                Currently only 'add' is a supported operation on the patch document.    Currently only valid metadata keys are supported paths on the patch document.                The response will return any affected Portfolio Group Access Metadata rules or a failure message if unsuccessful.                It is important to always check to verify success (or failure).                Multiple rules for a metadataKey can exist with different effective at dates, when resources are accessed the rule that is active for the current time will be fetched.

### Example

```python
api_instance = api_client_factory.build(PortfolioGroupsApi)
scope = 'scope_example' # str
code = 'code_example' # str
access_metadata_operation = [{"value":[{"value":"SilverLicence","provider":"TestDataProvider"}],"path":"/exampleMetadataKey","op":"add"}] # List[AccessMetadataOperation]
effective_at = 'effective_at_example' # str (optional)
effective_until = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.patch_portfolio_group_access_metadata(scope, code, access_metadata_operation, effective_at=effective_at, effective_until=effective_until)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Portfolio Group | [required] 
 **code** | **str**| The Portfolio Group code | [required] 
 **access_metadata_operation** | [**List[AccessMetadataOperation]**](AccessMetadataOperation.md)| The Json patch document | [required] 
 **effective_at** | **str**| The date this rule will be effective from | [optional] 
 **effective_until** | **datetime**| The effective date until which the Access Metadata is valid. If not supplied this will be valid indefinitely, or until the next &#39;effectiveAt&#39; date of the Access Metadata | [optional] 

### Return type

**Dict[str, List[AccessMetadataValue]]**

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully patched items. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_portfolio_group**
> PortfolioGroup updatePortfolioGroup = update_portfolio_group(scope, code, effective_at=effective_at, update_portfolio_group_request=update_portfolio_group_request)

[EARLY ACCESS] UpdatePortfolioGroup: Update portfolio group

Update the definition of a single portfolio group. Not all elements within a portfolio group definition are modifiable  due to the potential implications for data already stored against the portfolio group.

### Example

```python
api_instance = api_client_factory.build(PortfolioGroupsApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
update_portfolio_group_request = UpdatePortfolioGroupRequest()
api_response = api_instance.update_portfolio_group(scope, code, effective_at=effective_at, update_portfolio_group_request=update_portfolio_group_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group to update the definition for. | [required] 
 **code** | **str**| The code of the portfolio group to update the definition for. Together with the scope this uniquely identifies the portfolio group. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to update the definition. | [optional] 
 **update_portfolio_group_request** | [**UpdatePortfolioGroupRequest**](UpdatePortfolioGroupRequest.md)| The updated portfolio group definition. | [optional] 

### Return type

[**PortfolioGroup**](PortfolioGroup.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated definition of the portfolio group |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_group_properties**
> PortfolioGroupProperties upsertGroupProperties = upsert_group_properties(scope, code, request_body=request_body)

[EARLY ACCESS] UpsertGroupProperties: Upsert group properties

Update or insert one or more properties onto a single group. A property will be updated if it  already exists and inserted if it does not. All properties must be of the domain 'PortfolioGroup'.                Upserting a property that exists for a group, with a null value, will delete the instance of the property for that group.                Properties have an <i>effectiveFrom</i> datetime for which the property is valid, and an <i>effectiveUntil</i>  datetime until which the property is valid. Not supplying an <i>effectiveUntil</i> datetime results in the property being  valid indefinitely, or until the next <i>effectiveFrom</i> datetime of the property.

### Example

```python
api_instance = api_client_factory.build(PortfolioGroupsApi)
scope = 'scope_example' # str
code = 'code_example' # str
request_body = {"PortfolioGroup/MyScope/FundManagerName":{"key":"PortfolioGroup/MyScope/FundManagerName","value":{"labelValue":"Smith"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00"},"PortfolioGroup/MyScope/SomeProperty":{"key":"PortfolioGroup/MyScope/SomeProperty","value":{"labelValue":"SomeValue"},"effectiveFrom":"2016-01-01T00:00:00.0000000+00:00"},"PortfolioGroup/MyScope/AnotherProperty":{"key":"PortfolioGroup/MyScope/AnotherProperty","value":{"labelValue":"AnotherValue"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00","effectiveUntil":"2020-01-01T00:00:00.0000000+00:00"},"PortfolioGroup/MyScope/ReBalanceInterval":{"key":"PortfolioGroup/MyScope/ReBalanceInterval","value":{"metricValue":{"value":30.0,"unit":"Days"}}}} # Dict[str, ModelProperty] (optional)
api_response = api_instance.upsert_group_properties(scope, code, request_body=request_body)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the group to update or insert the properties onto. | [required] 
 **code** | **str**| The code of the group to update or insert the properties onto. Together with the scope this uniquely identifies the group. | [required] 
 **request_body** | [**Dict[str, ModelProperty]**](ModelProperty.md)| The properties to be updated or inserted onto the group. Each property in               the request must be keyed by its unique property key. This has the format {domain}/{scope}/{code} e.g. \&quot;PortfolioGroup/Manager/Id\&quot;. | [optional] 

### Return type

[**PortfolioGroupProperties**](PortfolioGroupProperties.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated or inserted properties |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_portfolio_group_access_metadata**
> ResourceListOfAccessMetadataValueOf upsertPortfolioGroupAccessMetadata = upsert_portfolio_group_access_metadata(scope, code, metadata_key, upsert_portfolio_group_access_metadata_request, effective_at=effective_at, effective_until=effective_until)

UpsertPortfolioGroupAccessMetadata: Upsert a Portfolio Group Access Metadata entry associated with a specific metadataKey. This creates or updates the data in LUSID.

Update or insert one Portfolio Group Access Metadata Entry in a single scope. An item will be updated if it already exists  and inserted if it does not.                The response will return the successfully updated or inserted Portfolio Group Access Metadata rule or failure message if unsuccessful.                It is important to always check to verify success (or failure).                Multiple rules for a metadataKey can exist with different effective at dates, when resources are accessed the rule that is active for the current time will be fetched.

### Example

```python
api_instance = api_client_factory.build(PortfolioGroupsApi)
scope = 'scope_example' # str
code = 'code_example' # str
metadata_key = 'metadata_key_example' # str
upsert_portfolio_group_access_metadata_request = UpsertPortfolioGroupAccessMetadataRequest()
effective_at = 'effective_at_example' # str (optional)
effective_until = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.upsert_portfolio_group_access_metadata(scope, code, metadata_key, upsert_portfolio_group_access_metadata_request, effective_at=effective_at, effective_until=effective_until)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Portfolio Group | [required] 
 **code** | **str**| The Portfolio Group code | [required] 
 **metadata_key** | **str**| Key of the access metadata entry to upsert | [required] 
 **upsert_portfolio_group_access_metadata_request** | [**UpsertPortfolioGroupAccessMetadataRequest**](UpsertPortfolioGroupAccessMetadataRequest.md)| The Portfolio Group Access Metadata rule to upsert | [required] 
 **effective_at** | **str**| The date this rule will be effective from | [optional] 
 **effective_until** | **datetime**| The effective date until which the Access Metadata is valid. If not supplied this will be valid indefinitely, or until the next &#39;effectiveAt&#39; date of the Access Metadata | [optional] 

### Return type

[**ResourceListOfAccessMetadataValueOf**](ResourceListOfAccessMetadataValueOf.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully updated or inserted item or any failure. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

