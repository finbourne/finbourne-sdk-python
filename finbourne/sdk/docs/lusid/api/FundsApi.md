# lusid.FundsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_estimate_valuation_point**](FundsApi.md#accept_estimate_valuation_point) | **POST** /api/api/funds/{scope}/{code}/valuationpoints/$acceptestimate | [EXPERIMENTAL] AcceptEstimateValuationPoint: Accepts an Estimate Valuation Point.
[**create_fee**](FundsApi.md#create_fee) | **POST** /api/api/funds/{scope}/{code}/fees | [EXPERIMENTAL] CreateFee: Create a Fee.
[**create_fund**](FundsApi.md#create_fund) | **POST** /api/api/funds/{scope} | [EXPERIMENTAL] CreateFund: Create a Fund.
[**create_fund_v2**](FundsApi.md#create_fund_v2) | **POST** /api/api/funds/v2/{scope} | [EXPERIMENTAL] CreateFundV2: Create a Fund V2 (Preview).
[**deactivate_nav_types**](FundsApi.md#deactivate_nav_types) | **POST** /api/api/funds/{scope}/{code}/deactivateNavTypes | [EXPERIMENTAL] DeactivateNavTypes: Deactivate NAV types on a Fund.
[**delete_bookmark**](FundsApi.md#delete_bookmark) | **DELETE** /api/api/funds/{scope}/{code}/bookmarks/{bookmarkCode} | [EXPERIMENTAL] DeleteBookmark: Delete a Bookmark.
[**delete_fee**](FundsApi.md#delete_fee) | **DELETE** /api/api/funds/{scope}/{code}/fees/{feeCode} | [EXPERIMENTAL] DeleteFee: Delete a Fee.
[**delete_fund**](FundsApi.md#delete_fund) | **DELETE** /api/api/funds/{scope}/{code} | [EXPERIMENTAL] DeleteFund: Delete a Fund.
[**delete_nav_activity_adjustments**](FundsApi.md#delete_nav_activity_adjustments) | **POST** /api/api/funds/{scope}/{code}/navAdjustment/$delete | [EXPERIMENTAL] DeleteNavActivityAdjustments: Delete Nav activity adjustments.
[**delete_valuation_point**](FundsApi.md#delete_valuation_point) | **DELETE** /api/api/funds/{scope}/{code}/valuationpoints/{diaryEntryCode} | [EXPERIMENTAL] DeleteValuationPoint: Delete a Valuation Point.
[**finalise_candidate_valuation_point**](FundsApi.md#finalise_candidate_valuation_point) | **POST** /api/api/funds/{scope}/{code}/valuationpoints/$finalisecandidate | [EXPERIMENTAL] FinaliseCandidateValuationPoint: Finalise a Candidate Valuation Point.
[**get_fee**](FundsApi.md#get_fee) | **GET** /api/api/funds/{scope}/{code}/fees/{feeCode} | [EXPERIMENTAL] GetFee: Get a Fee for a specified Fund.
[**get_fee_properties**](FundsApi.md#get_fee_properties) | **GET** /api/api/funds/{scope}/{code}/fees/{feeCode}/properties | [EXPERIMENTAL] GetFeeProperties: Get Fee properties.
[**get_fund**](FundsApi.md#get_fund) | **GET** /api/api/funds/{scope}/{code} | [EXPERIMENTAL] GetFund: Get a Fund.
[**get_fund_properties**](FundsApi.md#get_fund_properties) | **GET** /api/api/funds/{scope}/{code}/properties | [EXPERIMENTAL] GetFundProperties: Get Fund properties.
[**get_holding_contributors_for_fund**](FundsApi.md#get_holding_contributors_for_fund) | **POST** /api/api/funds/{scope}/{code}/holdings/{holdingId}/contributors | [EXPERIMENTAL] GetHoldingContributorsForFund: Get holdings contributors for transaction portfolios in a Fund.
[**get_holdings_for_fund**](FundsApi.md#get_holdings_for_fund) | **POST** /api/api/funds/{scope}/{code}/$holdings | [EXPERIMENTAL] GetHoldingsForFund: Get holdings for transaction portfolios in a Fund.
[**get_valuation_for_fund**](FundsApi.md#get_valuation_for_fund) | **POST** /api/api/funds/{scope}/{code}/$valuation | [EXPERIMENTAL] GetValuationForFund: Perform valuation for a Fund.
[**get_valuation_point_data**](FundsApi.md#get_valuation_point_data) | **POST** /api/api/funds/{scope}/{code}/valuationpoints/$query | [EXPERIMENTAL] GetValuationPointData: Get Valuation Point Data for a Fund.
[**get_valuation_point_journal_entry_lines**](FundsApi.md#get_valuation_point_journal_entry_lines) | **POST** /api/api/funds/{scope}/{code}/valuationpoints/journalentrylines/$query | [EXPERIMENTAL] GetValuationPointJournalEntryLines: Get the Journal Entry Lines for the given Fund.
[**get_valuation_point_pnl_summary**](FundsApi.md#get_valuation_point_pnl_summary) | **POST** /api/api/funds/{scope}/{code}/valuationpoints/pnlsummary/$query | [EXPERIMENTAL] GetValuationPointPnlSummary: Get a PnL summary for the given Valuation Point in the Fund.
[**get_valuation_point_transactions**](FundsApi.md#get_valuation_point_transactions) | **POST** /api/api/funds/{scope}/{code}/valuationpoints/transactions/$query | [EXPERIMENTAL] GetValuationPointTransactions: Get the Transactions for the given Fund.
[**get_valuation_point_trial_balance**](FundsApi.md#get_valuation_point_trial_balance) | **POST** /api/api/funds/{scope}/{code}/valuationpoints/trialbalance/$query | [EXPERIMENTAL] GetValuationPointTrialBalance: Get Trial Balance for the given Fund.
[**list_fees**](FundsApi.md#list_fees) | **GET** /api/api/funds/{scope}/{code}/fees | [EXPERIMENTAL] ListFees: List Fees for a specified Fund.
[**list_fund_calendar**](FundsApi.md#list_fund_calendar) | **GET** /api/api/funds/{scope}/{code}/calendar | [EXPERIMENTAL] ListFundCalendar: List Fund Calendar.
[**list_fund_calendar_entries**](FundsApi.md#list_fund_calendar_entries) | **GET** /api/api/funds/{scope}/{code}/calendars | [EXPERIMENTAL] ListFundCalendarEntries: List Fund Calendar Entries.
[**list_funds**](FundsApi.md#list_funds) | **GET** /api/api/funds | [EXPERIMENTAL] ListFunds: List Funds.
[**list_nav_activity_adjustments**](FundsApi.md#list_nav_activity_adjustments) | **GET** /api/api/funds/{scope}/{code}/navAdjustment | [EXPERIMENTAL] ListNavActivityAdjustments: List NAV adjustment activities applied to a valuation point
[**list_valuation_point_overview**](FundsApi.md#list_valuation_point_overview) | **GET** /api/api/funds/{scope}/{code}/valuationPointOverview | [EXPERIMENTAL] ListValuationPointOverview: List Valuation Points Overview for a given Fund.
[**patch_fee**](FundsApi.md#patch_fee) | **PATCH** /api/api/funds/{scope}/{code}/fees/{feeCode} | [EXPERIMENTAL] PatchFee: Patch Fee.
[**patch_fund**](FundsApi.md#patch_fund) | **PATCH** /api/api/funds/{scope}/{code} | [EXPERIMENTAL] PatchFund: Patch a Fund.
[**revert_valuation_point_to_estimate**](FundsApi.md#revert_valuation_point_to_estimate) | **POST** /api/api/funds/{scope}/{code}/valuationpoints/$reverttoestimate | [EXPERIMENTAL] RevertValuationPointToEstimate: Reverts a Final Valuation Point to Estimate.
[**set_share_class_instruments**](FundsApi.md#set_share_class_instruments) | **PUT** /api/api/funds/{scope}/{code}/shareclasses | [EXPERIMENTAL] SetShareClassInstruments: Set the ShareClass Instruments on a Fund.
[**upsert_bookmark**](FundsApi.md#upsert_bookmark) | **POST** /api/api/funds/{scope}/{code}/bookmarks | [EXPERIMENTAL] UpsertBookmark: Upsert a bookmark.
[**upsert_diary_entry_type_valuation_point**](FundsApi.md#upsert_diary_entry_type_valuation_point) | **POST** /api/api/funds/{scope}/{code}/valuationpoints | [EXPERIMENTAL] UpsertDiaryEntryTypeValuationPoint: Upsert a Valuation Point.
[**upsert_fee_properties**](FundsApi.md#upsert_fee_properties) | **POST** /api/api/funds/{scope}/{code}/fees/{feeCode}/properties/$upsert | [EXPERIMENTAL] UpsertFeeProperties: Upsert Fee properties.
[**upsert_fund_properties**](FundsApi.md#upsert_fund_properties) | **POST** /api/api/funds/{scope}/{code}/properties/$upsert | [EXPERIMENTAL] UpsertFundProperties: Upsert Fund properties.
[**upsert_nav_activity_adjustments**](FundsApi.md#upsert_nav_activity_adjustments) | **POST** /api/api/funds/{scope}/{code}/navAdjustment | [EXPERIMENTAL] UpsertNavActivityAdjustments: Upsert NAV adjustment activities to a valuation point


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.funds_api import FundsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(FundsApi)
```

---

# **accept_estimate_valuation_point**
> AcceptEstimateValuationPointResponse acceptEstimateValuationPoint = accept_estimate_valuation_point(scope, code, valuation_point_data_request, nav_type_code=nav_type_code)

[EXPERIMENTAL] AcceptEstimateValuationPoint: Accepts an Estimate Valuation Point.

Accepts the specified estimate Valuation Point.  Should the Valuation Point differ since the Valuation Point was last run, both Valuation Points will be returned and status will be marked as 'Candidate',  otherwise it will be marked as 'Final'.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
valuation_point_data_request = ValuationPointDataRequest()
nav_type_code = 'nav_type_code_example' # str (optional)
api_response = api_instance.accept_estimate_valuation_point(scope, code, valuation_point_data_request, nav_type_code=nav_type_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **valuation_point_data_request** | [**ValuationPointDataRequest**](ValuationPointDataRequest.md)| The valuationPointDataRequest which contains the Diary Entry code for the Estimate Valuation Point to move to Candidate or Final state. | [required] 
 **nav_type_code** | **str**| When provided, accepts the Valuation Point of the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 

### Return type

[**AcceptEstimateValuationPointResponse**](AcceptEstimateValuationPointResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Accepted Estimate point and status after being Accepted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **create_fee**
> Fee createFee = create_fee(scope, code, fee_request, nav_type_code=nav_type_code)

[EXPERIMENTAL] CreateFee: Create a Fee.

Create the given Fee.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
fee_request = FeeRequest()
nav_type_code = 'nav_type_code_example' # str (optional)
api_response = api_instance.create_fee(scope, code, fee_request, nav_type_code=nav_type_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **fee_request** | [**FeeRequest**](FeeRequest.md)| The Fee to create. | [required] 
 **nav_type_code** | **str**| When provided, creates the Fee against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 

### Return type

[**Fee**](Fee.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created Fee. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **create_fund**
> Fund createFund = create_fund(scope, fund_request)

[EXPERIMENTAL] CreateFund: Create a Fund.

Create the given Fund.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
fund_request = FundRequest()
api_response = api_instance.create_fund(scope, fund_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **fund_request** | [**FundRequest**](FundRequest.md)| The definition of the Fund. | [required] 

### Return type

[**Fund**](Fund.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created Fund. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **create_fund_v2**
> Fund createFundV2 = create_fund_v2(scope, fund_definition_request)

[EXPERIMENTAL] CreateFundV2: Create a Fund V2 (Preview).

Create the given V2 Fund.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
fund_definition_request = FundDefinitionRequest()
api_response = api_instance.create_fund_v2(scope, fund_definition_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **fund_definition_request** | [**FundDefinitionRequest**](FundDefinitionRequest.md)| The definition of the Fund. | [required] 

### Return type

[**Fund**](Fund.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created Fund. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **deactivate_nav_types**
> Fund deactivateNavTypes = deactivate_nav_types(scope, code, request_body, delete_mode=delete_mode)

[EXPERIMENTAL] DeactivateNavTypes: Deactivate NAV types on a Fund.

Deactivate the given NAV types on the Fund.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
request_body = ["NavTypeCode1","NavTypeCode2"] # List[str]
delete_mode = 'delete_mode_example' # str (optional)
api_response = api_instance.deactivate_nav_types(scope, code, request_body, delete_mode=delete_mode)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **request_body** | [**List[str]**](str.md)| The codes of the nav types to be deactivated. | [required] 
 **delete_mode** | **str**| The delete mode to use (defaults to &#39;Soft&#39;). | [optional] 

### Return type

[**Fund**](Fund.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated Fund with the specified NAV types deactivated. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_bookmark**
> DeletedEntityResponse deleteBookmark = delete_bookmark(scope, code, bookmark_code, nav_type_code=nav_type_code)

[EXPERIMENTAL] DeleteBookmark: Delete a Bookmark.

Deletes the given Bookmark.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
bookmark_code = 'bookmark_code_example' # str
nav_type_code = 'nav_type_code_example' # str (optional)
api_response = api_instance.delete_bookmark(scope, code, bookmark_code, nav_type_code=nav_type_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **bookmark_code** | **str**| The bookmark code for the bookmark to be deleted. | [required] 
 **nav_type_code** | **str**| When provided, deletes the Bookmark against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the Bookmark was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_fee**
> DeletedEntityResponse deleteFee = delete_fee(scope, code, fee_code)

[EXPERIMENTAL] DeleteFee: Delete a Fee.

Delete the given Fee.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
fee_code = 'fee_code_example' # str
api_response = api_instance.delete_fee(scope, code, fee_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **fee_code** | **str**| The code of the Fee to be deleted. | [required] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the Fee was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_fund**
> DeletedEntityResponse deleteFund = delete_fund(scope, code)

[EXPERIMENTAL] DeleteFund: Delete a Fund.

Delete the given Fund.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.delete_fund(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund to be deleted. | [required] 
 **code** | **str**| The code of the Fund to be deleted. Together with the scope this uniquely identifies the Fund. | [required] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the Fund was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_nav_activity_adjustments**
> DeletedEntityResponse deleteNavActivityAdjustments = delete_nav_activity_adjustments(scope, code, valuation_point_code, nav_activity_adjustment, nav_type_code=nav_type_code, valuation_point_code_variant=valuation_point_code_variant)

[EXPERIMENTAL] DeleteNavActivityAdjustments: Delete Nav activity adjustments.

Delete Nav activity adjustments on a Valuation Point.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
valuation_point_code = 'valuation_point_code_example' # str
nav_activity_adjustment = [{"asAt":"2024-01-01T00:00:00.0000000+00:00","portfolioScope":"portfolioScope1","portfolioCode":"portfolioCode1","transactionId":"transactionId1","navActivityAdjustmentType":"PortfolioTransaction"}] # List[NavActivityAdjustment]
nav_type_code = 'nav_type_code_example' # str (optional)
valuation_point_code_variant = 'valuation_point_code_variant_example' # str (optional)
api_response = api_instance.delete_nav_activity_adjustments(scope, code, valuation_point_code, nav_activity_adjustment, nav_type_code=nav_type_code, valuation_point_code_variant=valuation_point_code_variant)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope is the unique identifier for the given Fund. | [required] 
 **valuation_point_code** | **str**| The valuation point Code to delete the adjustment from | [required] 
 **nav_activity_adjustment** | [**List[NavActivityAdjustment]**](NavActivityAdjustment.md)| The request describing the Nav activity adjustments to delete from a specific valuation point and nav type | [required] 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 
 **valuation_point_code_variant** | **str**| The variant of the valuation point used in the request. Together with the valuation point code marks the unique branch for the NavType. | [optional] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the Nav activity adjustments were deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_valuation_point**
> DeletedEntityResponse deleteValuationPoint = delete_valuation_point(scope, code, diary_entry_code, diary_entry_code_variant=diary_entry_code_variant, nav_type_code=nav_type_code)

[EXPERIMENTAL] DeleteValuationPoint: Delete a Valuation Point.

Deletes the given Valuation Point.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
diary_entry_code = 'diary_entry_code_example' # str
diary_entry_code_variant = 'diary_entry_code_variant_example' # str (optional)
nav_type_code = 'nav_type_code_example' # str (optional)
api_response = api_instance.delete_valuation_point(scope, code, diary_entry_code, diary_entry_code_variant=diary_entry_code_variant, nav_type_code=nav_type_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **diary_entry_code** | **str**| The diary entry code for the valuation Point to be deleted. | [required] 
 **diary_entry_code_variant** | **str**| The variant of the valuation point used in the request. Together with the valuation point code marks the unique branch for the NavType. This is working only for the Estimates. | [optional] 
 **nav_type_code** | **str**| When provided, deletes the Valuation Point against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the Valuation Point was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **finalise_candidate_valuation_point**
> ValuationPointDataResponse finaliseCandidateValuationPoint = finalise_candidate_valuation_point(scope, code, valuation_point_data_request, nav_type_code=nav_type_code)

[EXPERIMENTAL] FinaliseCandidateValuationPoint: Finalise a Candidate Valuation Point.

Moves a 'Candidate' status Valuation Point to status 'Final'.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
valuation_point_data_request = ValuationPointDataRequest()
nav_type_code = 'nav_type_code_example' # str (optional)
api_response = api_instance.finalise_candidate_valuation_point(scope, code, valuation_point_data_request, nav_type_code=nav_type_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **valuation_point_data_request** | [**ValuationPointDataRequest**](ValuationPointDataRequest.md)| The details of the Valuation Point to mark as final. | [required] 
 **nav_type_code** | **str**| When provided, finalises the Valuation Point of the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 

### Return type

[**ValuationPointDataResponse**](ValuationPointDataResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated Valuation Point response as a result of it be marked as Final. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_fee**
> Fee getFee = get_fee(scope, code, fee_code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)

[EXPERIMENTAL] GetFee: Get a Fee for a specified Fund.

Retrieve a fee for a specified Fund.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
fee_code = 'fee_code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.get_fee(scope, code, fee_code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **fee_code** | **str**| The code of the Fee. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the Fee properties. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Fee. Defaults to returning the latest version of the Fee if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Fee&#39; domain to decorate onto the Fee.              These must take the format {domain}/{scope}/{code}, for example &#39;Fee/Account/Id&#39;. If no properties are specified, then no properties will be returned. | [optional] 

### Return type

[**Fee**](Fee.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Fee definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_fee_properties**
> FeeProperties getFeeProperties = get_fee_properties(scope, code, fee_code, effective_at=effective_at, as_at=as_at)

[EXPERIMENTAL] GetFeeProperties: Get Fee properties.

Get all the properties of a single fee.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
fee_code = 'fee_code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_fee_properties(scope, code, fee_code, effective_at=effective_at, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **fee_code** | **str**| The code of the Fee to get the properties for. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to list the Fee&#39;s properties. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the Fee&#39;s properties. Defaults to return the latest version of each property if not specified. | [optional] 

### Return type

[**FeeProperties**](FeeProperties.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The properties of the specified fee |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_fund**
> Fund getFund = get_fund(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)

[EXPERIMENTAL] GetFund: Get a Fund.

Retrieve the definition of a particular Fund.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.get_fund(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the Fund properties. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Fund definition. Defaults to returning the latest version of the Fund definition if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Fund&#39; domain to decorate onto the Fund.              These must take the format {domain}/{scope}/{code}, for example &#39;Fund/Manager/Id&#39;. If no properties are specified, then no properties will be returned. | [optional] 

### Return type

[**Fund**](Fund.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Fund definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_fund_properties**
> FundProperties getFundProperties = get_fund_properties(scope, code, effective_at=effective_at, as_at=as_at)

[EXPERIMENTAL] GetFundProperties: Get Fund properties.

Get all the properties of a single fund.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_fund_properties(scope, code, effective_at=effective_at, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund to list the properties for. | [required] 
 **code** | **str**| The code of the Fund to list the properties for. Together with the scope this uniquely identifies the Fund. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to list the Fund&#39;s properties. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the Fund&#39;s properties. Defaults to return the latest version of each property if not specified. | [optional] 

### Return type

[**FundProperties**](FundProperties.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The properties of the specified fund |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_holding_contributors_for_fund**
> VersionedResourceListOfHoldingContributor getHoldingContributorsForFund = get_holding_contributors_for_fund(scope, code, holding_id, valuation_point_data_query_parameters, nav_type_code=nav_type_code, include_historic=include_historic, tax_lot_id=tax_lot_id, include_unsettled_movements=include_unsettled_movements, limit=limit, as_at=as_at, page=page)

[EXPERIMENTAL] GetHoldingContributorsForFund: Get holdings contributors for transaction portfolios in a Fund.

Get the holdings of transaction portfolios in a specified Fund.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
holding_id = 56 # int
valuation_point_data_query_parameters = ValuationPointDataQueryParameters()
nav_type_code = 'nav_type_code_example' # str (optional)
include_historic = False # bool (optional)
tax_lot_id = 'tax_lot_id_example' # str (optional)
include_unsettled_movements = False # bool (optional)
limit = 56 # int (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
api_response = api_instance.get_holding_contributors_for_fund(scope, code, holding_id, valuation_point_data_query_parameters, nav_type_code=nav_type_code, include_historic=include_historic, tax_lot_id=tax_lot_id, include_unsettled_movements=include_unsettled_movements, limit=limit, as_at=as_at, page=page)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **holding_id** | **int**| The unique holding identifier | [required] 
 **valuation_point_data_query_parameters** | [**ValuationPointDataQueryParameters**](ValuationPointDataQueryParameters.md)| The arguments to use for querying the holdings.This can be a date, valuationPoint or a bookmark. | [required] 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 
 **include_historic** | **bool**| If true, transactions from previously closed holdings are returned.              If false, only transactions from last time position is opened. | [optional] [default to False]
 **tax_lot_id** | **str**| Constrains the Holding Contributors to those which contributed to the specified tax lot. | [optional] 
 **include_unsettled_movements** | **bool**| If true, contributing transaction which have not settled yet will also be returned. False by default | [optional] [default to False]
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to build the transactions. Defaults to return the latest              version of each transaction if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing transactions from a previous call to GetHoldingContributors. | [optional] 

### Return type

[**VersionedResourceListOfHoldingContributor**](VersionedResourceListOfHoldingContributor.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested holding contributors from the specified Fund and NavType. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_holdings_for_fund**
> VersionedResourceListOfPortfolioHolding getHoldingsForFund = get_holdings_for_fund(scope, code, single_valuation_point_query_parameters, nav_type_code=nav_type_code, as_at=as_at, filter=filter, property_keys=property_keys, by_taxlots=by_taxlots, include_settlement_events_after_days=include_settlement_events_after_days)

[EXPERIMENTAL] GetHoldingsForFund: Get holdings for transaction portfolios in a Fund.

Get the holdings of transaction portfolios in a specified Fund.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
single_valuation_point_query_parameters = SingleValuationPointQueryParameters()
nav_type_code = 'nav_type_code_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
filter = 'filter_example' # str (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
by_taxlots = True # bool (optional)
include_settlement_events_after_days = 56 # int (optional)
api_response = api_instance.get_holdings_for_fund(scope, code, single_valuation_point_query_parameters, nav_type_code=nav_type_code, as_at=as_at, filter=filter, property_keys=property_keys, by_taxlots=by_taxlots, include_settlement_events_after_days=include_settlement_events_after_days)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **single_valuation_point_query_parameters** | [**SingleValuationPointQueryParameters**](SingleValuationPointQueryParameters.md)| The arguments to use for querying the holdings. | [required] 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the holdings of transaction portfolios in the Fund. Defaults              to return the latest version of the holdings if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the \&quot;Instrument\&quot;, \&quot;Holding\&quot; or \&quot;Portfolio\&quot; domain to decorate onto              the holdings. These take the format {domain}/{scope}/{code} e.g. \&quot;Instrument/system/Name\&quot; or \&quot;Holding/system/Cost\&quot;. | [optional] 
 **by_taxlots** | **bool**| Whether to expand the holdings to return the underlying tax-lots. Defaults to False. | [optional] 
 **include_settlement_events_after_days** | **int**| Number of days ahead to bring back settlements from, in relation to the specified effectiveAt. | [optional] 

### Return type

[**VersionedResourceListOfPortfolioHolding**](VersionedResourceListOfPortfolioHolding.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The holdings of transaction portfolios for a Fund |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_valuation_for_fund**
> ListAggregationResponse getValuationForFund = get_valuation_for_fund(scope, code, nav_type_code=nav_type_code, fund_valuation_request=fund_valuation_request)

[EXPERIMENTAL] GetValuationForFund: Perform valuation for a Fund.

Perform valuation on a specified Fund.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
nav_type_code = 'nav_type_code_example' # str (optional)
fund_valuation_request = FundValuationRequest()
api_response = api_instance.get_valuation_for_fund(scope, code, nav_type_code=nav_type_code, fund_valuation_request=fund_valuation_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 
 **fund_valuation_request** | [**FundValuationRequest**](FundValuationRequest.md)| The request specifying the dates (or DiaryEntry) on which to calculate a set of valuation metrics. | [optional] 

### Return type

[**ListAggregationResponse**](ListAggregationResponse.md)

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

# **get_valuation_point_data**
> ValuationPointDataResponse getValuationPointData = get_valuation_point_data(scope, code, valuation_point_data_query_parameters, as_at=as_at, nav_type_code=nav_type_code)

[EXPERIMENTAL] GetValuationPointData: Get Valuation Point Data for a Fund.

Retrieves the Valuation Point data between given dates or Valuation Point codes.  The endpoint will internally extract all 'Assets' and 'Liabilities' from the Fund's Trial balance to produce a GAV.  Start date will be assumed from the last 'official' ValuationPoint and EndDate will be as provided.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
valuation_point_data_query_parameters = ValuationPointDataQueryParameters()
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
nav_type_code = 'nav_type_code_example' # str (optional)
api_response = api_instance.get_valuation_point_data(scope, code, valuation_point_data_query_parameters, as_at=as_at, nav_type_code=nav_type_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **valuation_point_data_query_parameters** | [**ValuationPointDataQueryParameters**](ValuationPointDataQueryParameters.md)| The arguments to use for querying the Valuation Point data. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Fund definition. Defaults to returning the latest version of the Fund definition if not specified. | [optional] 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 

### Return type

[**ValuationPointDataResponse**](ValuationPointDataResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Valuation Point data for the Fund. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_valuation_point_journal_entry_lines**
> ValuationPointResourceListOfFundJournalEntryLine getValuationPointJournalEntryLines = get_valuation_point_journal_entry_lines(scope, code, valuation_point_data_query_parameters, general_ledger_profile_code=general_ledger_profile_code, as_at=as_at, filter=filter, limit=limit, page=page, property_keys=property_keys, nav_type_code=nav_type_code)

[EXPERIMENTAL] GetValuationPointJournalEntryLines: Get the Journal Entry Lines for the given Fund.

Gets the Journal Entry Lines for the given Valuation Point for a Fund.                The Journal Entry Lines have been generated from transactions, translated via posting rules and used in the valuation point.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
valuation_point_data_query_parameters = ValuationPointDataQueryParameters()
general_ledger_profile_code = 'general_ledger_profile_code_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
filter = 'filter_example' # str (optional)
limit = 56 # int (optional)
page = 'page_example' # str (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
nav_type_code = 'nav_type_code_example' # str (optional)
api_response = api_instance.get_valuation_point_journal_entry_lines(scope, code, valuation_point_data_query_parameters, general_ledger_profile_code=general_ledger_profile_code, as_at=as_at, filter=filter, limit=limit, page=page, property_keys=property_keys, nav_type_code=nav_type_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **valuation_point_data_query_parameters** | [**ValuationPointDataQueryParameters**](ValuationPointDataQueryParameters.md)| The arguments to use for querying the Journal Entry Lines. | [required] 
 **general_ledger_profile_code** | **str**| The optional code of a General Ledger Profile used to decorate Journal Entry Lines with levels. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve Journal Entry Lines. Defaults to returning the latest version if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Journal Entry Lines from a previous call to GetValuationPointJournalEntryLines. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Instrument&#39;, &#39;Transaction&#39;, &#39;Portfolio&#39;, &#39;Account&#39;, &#39;LegalEntity&#39; or &#39;CustodianAccount&#39;               domain to decorate onto the Journal Entry Lines. | [optional] 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 

### Return type

[**ValuationPointResourceListOfFundJournalEntryLine**](ValuationPointResourceListOfFundJournalEntryLine.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Journal Entry Lines for the specified Valuation Point for a Fund. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_valuation_point_pnl_summary**
> ValuationPointResourceListOfPnlJournalEntryLine getValuationPointPnlSummary = get_valuation_point_pnl_summary(scope, code, valuation_point_data_query_parameters, general_ledger_profile_code=general_ledger_profile_code, as_at=as_at, filter=filter, limit=limit, page=page, nav_type_code=nav_type_code)

[EXPERIMENTAL] GetValuationPointPnlSummary: Get a PnL summary for the given Valuation Point in the Fund.

Gets the PnL Summary lines from the Journal Entry Lines produced when calculating the Valuation Point.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
valuation_point_data_query_parameters = ValuationPointDataQueryParameters()
general_ledger_profile_code = 'general_ledger_profile_code_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
filter = 'filter_example' # str (optional)
limit = 56 # int (optional)
page = 'page_example' # str (optional)
nav_type_code = 'nav_type_code_example' # str (optional)
api_response = api_instance.get_valuation_point_pnl_summary(scope, code, valuation_point_data_query_parameters, general_ledger_profile_code=general_ledger_profile_code, as_at=as_at, filter=filter, limit=limit, page=page, nav_type_code=nav_type_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **valuation_point_data_query_parameters** | [**ValuationPointDataQueryParameters**](ValuationPointDataQueryParameters.md)| The arguments to use for generating the PnL summary. | [required] 
 **general_ledger_profile_code** | **str**| The optional code of a General Ledger Profile used to decorate Journal Entry Lines with levels. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve PnL summary. Defaults to returning the latest version              of each transaction if not specified. | [optional] 
 **filter** | **str**| \&quot;Expression to filter the result set.\&quot; | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing results from a previous call to GetValuationPointPnlSummary. | [optional] 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 

### Return type

[**ValuationPointResourceListOfPnlJournalEntryLine**](ValuationPointResourceListOfPnlJournalEntryLine.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested PnL summary for the specified Valuation Point for a Fund. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_valuation_point_transactions**
> ValuationPointResourceListOfAccountedTransaction getValuationPointTransactions = get_valuation_point_transactions(scope, code, valuation_point_data_query_parameters, as_at=as_at, filter=filter, limit=limit, page=page, property_keys=property_keys, nav_type_code=nav_type_code, data_model_scope=data_model_scope, data_model_code=data_model_code, show_cancelled_transactions=show_cancelled_transactions, membership_type=membership_type)

[EXPERIMENTAL] GetValuationPointTransactions: Get the Transactions for the given Fund.

Gets the Transactions for the given Valuation Point for a Fund.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
valuation_point_data_query_parameters = ValuationPointDataQueryParameters()
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
filter = 'filter_example' # str (optional)
limit = 56 # int (optional)
page = 'page_example' # str (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
nav_type_code = 'nav_type_code_example' # str (optional)
data_model_scope = 'data_model_scope_example' # str (optional)
data_model_code = 'data_model_code_example' # str (optional)
show_cancelled_transactions = True # bool (optional)
membership_type = 'membership_type_example' # str (optional)
api_response = api_instance.get_valuation_point_transactions(scope, code, valuation_point_data_query_parameters, as_at=as_at, filter=filter, limit=limit, page=page, property_keys=property_keys, nav_type_code=nav_type_code, data_model_scope=data_model_scope, data_model_code=data_model_code, show_cancelled_transactions=show_cancelled_transactions, membership_type=membership_type)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **valuation_point_data_query_parameters** | [**ValuationPointDataQueryParameters**](ValuationPointDataQueryParameters.md)| The arguments to use for querying the transactions. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve transactions. Defaults to returning the latest version              of each transaction if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing transactions from a previous call to GetValuationPointTransactions. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Instrument&#39;, &#39;Transaction&#39;, &#39;Portfolio&#39;, &#39;Account&#39;, &#39;LegalEntity&#39; or &#39;CustodianAccount&#39;              domain to decorate onto the transactions. | [optional] 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 
 **data_model_scope** | **str**| The optional scope of a Custom Data Model to use | [optional] 
 **data_model_code** | **str**| The optional code of a Custom Data Model to use | [optional] 
 **show_cancelled_transactions** | **bool**| Option to specify whether or not to include cancelled transactions,              including previous versions of transactions which have since been amended.              Defaults to False if not specified. | [optional] 
 **membership_type** | **str**| The membership types of the specified Custom Data Model to return. Allowable values are Member, Candidate and All. Defaults to Member. | [optional] 

### Return type

[**ValuationPointResourceListOfAccountedTransaction**](ValuationPointResourceListOfAccountedTransaction.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested transactions for the specified Valuation Point for a Fund. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_valuation_point_trial_balance**
> ValuationPointResourceListOfTrialBalance getValuationPointTrialBalance = get_valuation_point_trial_balance(scope, code, valuation_point_data_query_parameters, general_ledger_profile_code=general_ledger_profile_code, as_at=as_at, filter=filter, limit=limit, page=page, property_keys=property_keys, nav_type_code=nav_type_code, exclude_cleardown_module=exclude_cleardown_module)

[EXPERIMENTAL] GetValuationPointTrialBalance: Get Trial Balance for the given Fund.

Gets the Trial Balance for the given Valuation Point for a Fund.                The Trial Balance has been generated from transactions, translated via Posting Rules  and aggregated based on a General Ledger Profile (where specified).

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
valuation_point_data_query_parameters = ValuationPointDataQueryParameters()
general_ledger_profile_code = 'general_ledger_profile_code_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
filter = 'filter_example' # str (optional)
limit = 56 # int (optional)
page = 'page_example' # str (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
nav_type_code = 'nav_type_code_example' # str (optional)
exclude_cleardown_module = False # bool (optional)
api_response = api_instance.get_valuation_point_trial_balance(scope, code, valuation_point_data_query_parameters, general_ledger_profile_code=general_ledger_profile_code, as_at=as_at, filter=filter, limit=limit, page=page, property_keys=property_keys, nav_type_code=nav_type_code, exclude_cleardown_module=exclude_cleardown_module)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **valuation_point_data_query_parameters** | [**ValuationPointDataQueryParameters**](ValuationPointDataQueryParameters.md)| The arguments to use for generating the Trial Balance. | [required] 
 **general_ledger_profile_code** | **str**| The optional code of a General Ledger Profile used to decorate Journal Entry Lines with levels. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Trial Balance.               Defaults to returning the latest version if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results by.               For more information about filtering results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this number.               Defaults to 100 if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Trial Balances.               This token is returned from the previous call.               If a pagination token is provided, the filter, effectiveAt and asAt fields               must not have changed since the original request. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Instrument&#39;, &#39;Transaction&#39;, &#39;Portfolio&#39;, &#39;Account&#39;, &#39;LegalEntity&#39; or &#39;CustodianAccount&#39;               domain to decorate onto the TrialBalance. | [optional] 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 
 **exclude_cleardown_module** | **bool**| If this is set to true, no Cleardown Module will be applied to the Trial Balance. Defaults to false. | [optional] [default to False]

### Return type

[**ValuationPointResourceListOfTrialBalance**](ValuationPointResourceListOfTrialBalance.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Trial Balance for the specified Valuation Point for a Fund. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_fees**
> PagedResourceListOfFee listFees = list_fees(scope, code, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)

[EXPERIMENTAL] ListFees: List Fees for a specified Fund.

List all the Fees matching a particular criteria.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.list_fees(scope, code, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to list the TimeVariant properties for the Fees. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the Fees. Defaults to returning the latest version of each Fee if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing fees; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the treatment, specify \&quot;treatment eq &#39;Monthly&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Fee&#39; domain to decorate onto each Fee.              These must take the format {domain}/{scope}/{code}, for example &#39;Fee/Account/Id&#39;. | [optional] 

### Return type

[**PagedResourceListOfFee**](PagedResourceListOfFee.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Fees. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_fund_calendar**
> PagedResourceListOfFundCalendarEntry listFundCalendar = list_fund_calendar(scope, code, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)

[EXPERIMENTAL] ListFundCalendar: List Fund Calendar.

List all the Calendar Entries associated with the Fund.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.list_fund_calendar(scope, code, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to list the Calendar. Defaults to returning the latest version of each Calendar Entry if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Calendar Entries; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;ClosedPeriod&#39; domain to decorate onto each item. | [optional] 

### Return type

[**PagedResourceListOfFundCalendarEntry**](PagedResourceListOfFundCalendarEntry.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Fund Calendar Entries. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_fund_calendar_entries**
> PagedResourceListOfFundCalendarEntries listFundCalendarEntries = list_fund_calendar_entries(scope, code, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)

[EXPERIMENTAL] ListFundCalendarEntries: List Fund Calendar Entries.

List all the Calendar Entries associated with the Fund.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.list_fund_calendar_entries(scope, code, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to list the Calendar. Defaults to returning the latest version of each Calendar Entry if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Calendar Entries; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;DiaryEntry&#39; domain to decorate onto each item. | [optional] 

### Return type

[**PagedResourceListOfFundCalendarEntries**](PagedResourceListOfFundCalendarEntries.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Fund Calendar Entries. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_funds**
> PagedResourceListOfFund listFunds = list_funds(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)

[EXPERIMENTAL] ListFunds: List Funds.

List all the Funds matching particular criteria.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.list_funds(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effective datetime or cut label at which to list the TimeVariant properties for the Funds. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the Funds. Defaults to returning the latest version of each Fund if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Funds; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the Fund code, specify \&quot;id.Code eq &#39;Fund1&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Fund&#39; domain to decorate onto each Fund.              These must take the format {domain}/{scope}/{code}, for example &#39;Fund/Manager/Id&#39;. | [optional] 

### Return type

[**PagedResourceListOfFund**](PagedResourceListOfFund.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Funds. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_nav_activity_adjustments**
> ResourceListOfNavActivityAdjustment listNavActivityAdjustments = list_nav_activity_adjustments(scope, code, valuation_point_code, nav_type_code=nav_type_code, as_at=as_at, page=page, limit=limit, filter=filter, valuation_point_code_variant=valuation_point_code_variant)

[EXPERIMENTAL] ListNavActivityAdjustments: List NAV adjustment activities applied to a valuation point

Lists the NAV adjustment activities applied to the specified valuation point for a Fund.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
valuation_point_code = 'valuation_point_code_example' # str
nav_type_code = 'nav_type_code_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
valuation_point_code_variant = 'valuation_point_code_variant_example' # str (optional)
api_response = api_instance.list_nav_activity_adjustments(scope, code, valuation_point_code, nav_type_code=nav_type_code, as_at=as_at, page=page, limit=limit, filter=filter, valuation_point_code_variant=valuation_point_code_variant)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope is the unique identifier for the given Fund. | [required] 
 **valuation_point_code** | **str**| Fetch all NAV adjustment activities for this valuation point. | [required] 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the Nav activity adjustments. Defaults to returning the latest version of each adjustment if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Nav activity adjustments; this              value is returned from the previous call. If a pagination token is provided, the filter,              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **valuation_point_code_variant** | **str**| The variant of the valuation point used in the request. Together with the valuation point code marks the unique branch for the NavType. | [optional] 

### Return type

[**ResourceListOfNavActivityAdjustment**](ResourceListOfNavActivityAdjustment.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested NAV activity adjustments for the specific valuation point and Nav type for the Fund. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_valuation_point_overview**
> PagedResourceListOfValuationPointOverview listValuationPointOverview = list_valuation_point_overview(scope, code, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, property_keys=property_keys, nav_type_code=nav_type_code)

[EXPERIMENTAL] ListValuationPointOverview: List Valuation Points Overview for a given Fund.

List the overview of all the Valuation Points that match the given criteria for a given Fund.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
nav_type_code = 'nav_type_code_example' # str (optional)
api_response = api_instance.list_valuation_point_overview(scope, code, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, property_keys=property_keys, nav_type_code=nav_type_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to list the TimeVariant properties for the Valuation Points. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the Valuation Points. Defaults to returning the latest version of each Valuation Point if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Valuation Points; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results by.              For example, to filter on the NAV, specify \&quot;NAV gt 300\&quot;. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;DiaryEntry&#39; domain to decorate onto each ValuationPoint.              These must take the format {domain}/{scope}/{code}, for example &#39;DiaryEntry/ValuationPoint/Id&#39;. | [optional] 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 

### Return type

[**PagedResourceListOfValuationPointOverview**](PagedResourceListOfValuationPointOverview.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The overviews of the requested Valuation Points. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **patch_fee**
> Fee patchFee = patch_fee(scope, code, fee_code, operation)

[EXPERIMENTAL] PatchFee: Patch Fee.

Create or update certain fields for a particular Fee.  The behaviour is defined by the JSON Patch specification.    Currently supported fields are: EndDate, ShareClasses.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
fee_code = 'fee_code_example' # str
operation = [{"value":"2027-12-31T00:00:00.0000000+00:00","path":"/endDate","op":"add"}] # List[Operation]
api_response = api_instance.patch_fee(scope, code, fee_code, operation)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **fee_code** | **str**| The code of the Fee. | [required] 
 **operation** | [**List[Operation]**](Operation.md)| The json patch document. For more information see: https://datatracker.ietf.org/doc/html/rfc6902. | [required] 

### Return type

[**Fee**](Fee.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The newly patched Fee. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **patch_fund**
> Fund patchFund = patch_fund(scope, code, operation)

[EXPERIMENTAL] PatchFund: Patch a Fund.

Update fields on a Fund.  The behaviour is defined by the JSON Patch specification.    Currently supported fields are: DisplayName, Description, PortfolioIds, FundConfigurationId, ShareClassInstruments, Type, InceptionDate, DecimalPlaces, PrimaryNavType, AdditionalNavTypes, AborId, YearEndDate.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
operation = [{"value":"UpdatedFundName","path":"/displayName","op":"add"},{"path":"/description","op":"remove"},{"value":{"scope":"myFundConfigScope","code":"myFundConfigCode"},"path":"/fundConfigurationId","op":"add"},{"value":{"scope":"myAborScope","code":"myAborCode"},"path":"/aborId","op":"add"},{"value":["shareClassScope"],"path":"/shareClassInstrumentScopes","op":"add"},{"value":{"instrumentIdentifiers":{"Instrument/default/ClientInternal":"shareClass526"},"launchPrice":2.5,"launchDate":"2024-02-01T00:00:00.0000000+00:00"},"path":"/shareClassInstruments/-","op":"add"},{"value":"Standalone","path":"/type","op":"add"},{"value":"2024-01-01","path":"/inceptionDate","op":"add"},{"value":2,"path":"/decimalPlaces","op":"add"},{"value":{"day":24,"month":12},"path":"/yearEndDate","op":"add"}] # List[Operation]
api_response = api_instance.patch_fund(scope, code, operation)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **operation** | [**List[Operation]**](Operation.md)| The json patch document. For more information see: https://datatracker.ietf.org/doc/html/rfc6902. | [required] 

### Return type

[**Fund**](Fund.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated Fund. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **revert_valuation_point_to_estimate**
> ValuationPointDataResponse revertValuationPointToEstimate = revert_valuation_point_to_estimate(scope, code, revert_valuation_point_data_request, nav_type_code=nav_type_code)

[EXPERIMENTAL] RevertValuationPointToEstimate: Reverts a Final Valuation Point to Estimate.

Moves a 'Final' status Valuation Point to status 'Estimate'.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
revert_valuation_point_data_request = RevertValuationPointDataRequest()
nav_type_code = 'nav_type_code_example' # str (optional)
api_response = api_instance.revert_valuation_point_to_estimate(scope, code, revert_valuation_point_data_request, nav_type_code=nav_type_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **revert_valuation_point_data_request** | [**RevertValuationPointDataRequest**](RevertValuationPointDataRequest.md)| The revertValuationPointRequest which contains the Diary Entry code for the Final Valuation Point to move to Estimate status. | [required] 
 **nav_type_code** | **str**| When provided, sets the status of the Valuation Point of the specified NAV Type to be Estimate.              Otherwise, the Primary NAV Type will be used. | [optional] 

### Return type

[**ValuationPointDataResponse**](ValuationPointDataResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated Valuation Point response as a result of it be marked as Estimate. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **set_share_class_instruments**
> Fund setShareClassInstruments = set_share_class_instruments(scope, code, set_share_class_instruments_request)

[EXPERIMENTAL] SetShareClassInstruments: Set the ShareClass Instruments on a Fund.

Update the ShareClass Instruments on an existing Fund with the set of instruments provided.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
set_share_class_instruments_request = SetShareClassInstrumentsRequest()
api_response = api_instance.set_share_class_instruments(scope, code, set_share_class_instruments_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **set_share_class_instruments_request** | [**SetShareClassInstrumentsRequest**](SetShareClassInstrumentsRequest.md)| The scopes and instrument identifiers for the instruments to be set. | [required] 

### Return type

[**Fund**](Fund.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated Fund definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_bookmark**
> FundCalendarEntry upsertBookmark = upsert_bookmark(scope, code, upsert_fund_bookmark_request, nav_type_code=nav_type_code)

[EXPERIMENTAL] UpsertBookmark: Upsert a bookmark.

This method will update or upsert a Bookmark for the Fund.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
upsert_fund_bookmark_request = UpsertFundBookmarkRequest()
nav_type_code = 'nav_type_code_example' # str (optional)
api_response = api_instance.upsert_bookmark(scope, code, upsert_fund_bookmark_request, nav_type_code=nav_type_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **upsert_fund_bookmark_request** | [**UpsertFundBookmarkRequest**](UpsertFundBookmarkRequest.md)| The bookmark definition to upsert. | [required] 
 **nav_type_code** | **str**| When provided, upserts the Valuation Point against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 

### Return type

[**FundCalendarEntry**](FundCalendarEntry.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated or inserted Bookmark |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_diary_entry_type_valuation_point**
> DiaryEntry upsertDiaryEntryTypeValuationPoint = upsert_diary_entry_type_valuation_point(scope, code, upsert_valuation_point_request, nav_type_code=nav_type_code)

[EXPERIMENTAL] UpsertDiaryEntryTypeValuationPoint: Upsert a Valuation Point.

Insert the estimate Valuation Point.                If the Valuation Point does not exist, this method will create it in estimate state.                It is not possible to update an existing Valuation Point. As an alternative, the Valuation Point could be deleted and recreated.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
upsert_valuation_point_request = UpsertValuationPointRequest()
nav_type_code = 'nav_type_code_example' # str (optional)
api_response = api_instance.upsert_diary_entry_type_valuation_point(scope, code, upsert_valuation_point_request, nav_type_code=nav_type_code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **upsert_valuation_point_request** | [**UpsertValuationPointRequest**](UpsertValuationPointRequest.md)| The Valuation Point Estimate definition to upsert. | [required] 
 **nav_type_code** | **str**| When provided, upserts the Valuation Point against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 

### Return type

[**DiaryEntry**](DiaryEntry.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated or inserted estimated Valuation Point |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_fee_properties**
> FeeProperties upsertFeeProperties = upsert_fee_properties(scope, code, fee_code, request_body=request_body)

[EXPERIMENTAL] UpsertFeeProperties: Upsert Fee properties.

Update or insert one or more properties onto a single Fee. A property will be updated if it  already exists and inserted if it does not. All properties must be of the domain 'Fee'.                Upserting a property that exists for an Fee, with a null value, will delete the instance of the property for that group.                Properties have an <i>effectiveFrom</i> datetime for which the property is valid, and an <i>effectiveUntil</i>  datetime until which the property is valid. Not supplying an <i>effectiveUntil</i> datetime results in the property being  valid indefinitely, or until the next <i>effectiveFrom</i> datetime of the property.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
fee_code = 'fee_code_example' # str
request_body = {"Fee/MyScope/FundManagerName":{"key":"Fee/MyScope/FundManagerName","value":{"labelValue":"Smith"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00"},"Fee/MyScope/SomeProperty":{"key":"Fee/MyScope/SomeProperty","value":{"labelValue":"SomeValue"},"effectiveFrom":"2016-01-01T00:00:00.0000000+00:00"},"Fee/MyScope/AnotherProperty":{"key":"Fee/MyScope/AnotherProperty","value":{"labelValue":"AnotherValue"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00","effectiveUntil":"2020-01-01T00:00:00.0000000+00:00"},"Fee/MyScope/ReBalanceInterval":{"key":"Fee/MyScope/ReBalanceInterval","value":{"metricValue":{"value":30.0,"unit":"Days"}}}} # Dict[str, ModelProperty] (optional)
api_response = api_instance.upsert_fee_properties(scope, code, fee_code, request_body=request_body)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **fee_code** | **str**| The code of the Fee to update or insert the properties onto. | [required] 
 **request_body** | [**Dict[str, ModelProperty]**](ModelProperty.md)| The properties to be updated or inserted onto the Fee. Each property in               the request must be keyed by its unique property key. This has the format {domain}/{scope}/{code} e.g. \&quot;Fee/Manager/Id\&quot;. | [optional] 

### Return type

[**FeeProperties**](FeeProperties.md)

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

# **upsert_fund_properties**
> FundProperties upsertFundProperties = upsert_fund_properties(scope, code, request_body=request_body)

[EXPERIMENTAL] UpsertFundProperties: Upsert Fund properties.

Update or insert one or more properties onto a single Fund. A property will be updated if it  already exists and inserted if it does not. All properties must be of the domain 'Fund'.                Upserting a property that exists for an Fund, with a null value, will delete the instance of the property for that group.                Properties have an <i>effectiveFrom</i> datetime for which the property is valid, and an <i>effectiveUntil</i>  datetime until which the property is valid. Not supplying an <i>effectiveUntil</i> datetime results in the property being  valid indefinitely, or until the next <i>effectiveFrom</i> datetime of the property.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
request_body = {"Fund/MyScope/FundManagerName":{"key":"Fund/MyScope/FundManagerName","value":{"labelValue":"Smith"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00"},"Fund/MyScope/SomeProperty":{"key":"Fund/MyScope/SomeProperty","value":{"labelValue":"SomeValue"},"effectiveFrom":"2016-01-01T00:00:00.0000000+00:00"},"Fund/MyScope/AnotherProperty":{"key":"Fund/MyScope/AnotherProperty","value":{"labelValue":"AnotherValue"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00","effectiveUntil":"2020-01-01T00:00:00.0000000+00:00"},"Fund/MyScope/ReBalanceInterval":{"key":"Fund/MyScope/ReBalanceInterval","value":{"metricValue":{"value":30.0,"unit":"Days"}}}} # Dict[str, ModelProperty] (optional)
api_response = api_instance.upsert_fund_properties(scope, code, request_body=request_body)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope this uniquely identifies the Fund. | [required] 
 **request_body** | [**Dict[str, ModelProperty]**](ModelProperty.md)| The properties to be updated or inserted onto the Fund. Each property in               the request must be keyed by its unique property key. This has the format {domain}/{scope}/{code} e.g. \&quot;Fund/Manager/Id\&quot;. | [optional] 

### Return type

[**FundProperties**](FundProperties.md)

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

# **upsert_nav_activity_adjustments**
> datetime upsertNavActivityAdjustments = upsert_nav_activity_adjustments(scope, code, valuation_point_code, nav_activity_adjustment, nav_type_code=nav_type_code, valuation_point_code_variant=valuation_point_code_variant)

[EXPERIMENTAL] UpsertNavActivityAdjustments: Upsert NAV adjustment activities to a valuation point

Upserts the NAV adjustment activities to the specified valuation point for a Fund.

### Example

```python
api_instance = api_client_factory.build(FundsApi)
scope = 'scope_example' # str
code = 'code_example' # str
valuation_point_code = 'valuation_point_code_example' # str
nav_activity_adjustment = [{"asAt":"2024-01-01T00:00:00.0000000+00:00","portfolioScope":"portfolioScope1","portfolioCode":"portfolioCode1","transactionId":"transactionId1","navActivityAdjustmentType":"PortfolioTransaction"}] # List[NavActivityAdjustment]
nav_type_code = 'nav_type_code_example' # str (optional)
valuation_point_code_variant = 'valuation_point_code_variant_example' # str (optional)
api_response = api_instance.upsert_nav_activity_adjustments(scope, code, valuation_point_code, nav_activity_adjustment, nav_type_code=nav_type_code, valuation_point_code_variant=valuation_point_code_variant)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Fund. | [required] 
 **code** | **str**| The code of the Fund. Together with the scope is the unique identifier for the given Fund. | [required] 
 **valuation_point_code** | **str**| The valuation point Code to apply the adjustment to | [required] 
 **nav_activity_adjustment** | [**List[NavActivityAdjustment]**](NavActivityAdjustment.md)| The request describing the Nav activity adjustments to apply to a specific valuation point and nav type | [required] 
 **nav_type_code** | **str**| When provided, runs against the specified NAV Type, otherwise the Primary NAV Type will be used. | [optional] 
 **valuation_point_code_variant** | **str**| The variant of the valuation point used in the request. Together with the valuation point code marks the unique branch for the NavType. | [optional] 

### Return type

**datetime**

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The date and time of the successfully applied Nav Activity Adjustments. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

