# lusid.CollateralApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_margin_call**](CollateralApi.md#accept_margin_call) | **POST** /api/api/collateral/margincalls/{runId}/{agreementScope}/{agreementCode}/{item}/{marginType}/{direction}/$accept | [EXPERIMENTAL] AcceptMarginCall: Accept a margin call.
[**batch_accept_margin_calls**](CollateralApi.md#batch_accept_margin_calls) | **POST** /api/api/collateral/margincalls/$batchAccept | [EXPERIMENTAL] BatchAcceptMarginCalls: Accept several margin calls.
[**dispute_margin_call**](CollateralApi.md#dispute_margin_call) | **POST** /api/api/collateral/margincalls/{runId}/{agreementScope}/{agreementCode}/{item}/{marginType}/{direction}/$dispute | [EXPERIMENTAL] DisputeMarginCall: Dispute a margin call.
[**get_margin_call**](CollateralApi.md#get_margin_call) | **GET** /api/api/collateral/margincalls/{runId}/{agreementScope}/{agreementCode}/{item}/{marginType}/{direction} | [EXPERIMENTAL] GetMarginCall: Get a margin call.
[**get_margin_call_allocation**](CollateralApi.md#get_margin_call_allocation) | **GET** /api/api/collateral/margincalls/{runId}/{agreementScope}/{agreementCode}/{item}/{marginType}/{direction}/$allocation | [EXPERIMENTAL] GetMarginCallAllocation: [EXPERIMENTAL] GetMarginCallAllocation: Get the collateral proposed for a margin call.
[**get_margin_call_explanation**](CollateralApi.md#get_margin_call_explanation) | **GET** /api/api/collateral/margincalls/{runId}/{agreementScope}/{agreementCode}/{item}/{marginType}/{direction}/$explain | [EXPERIMENTAL] GetMarginCallExplanation: Explain a margin call.
[**get_margin_line_explanation**](CollateralApi.md#get_margin_line_explanation) | **GET** /api/api/collateral/runs/{runId}/lines/{lineKey}/$explain | [EXPERIMENTAL] GetMarginLineExplanation: Explain a margin line.
[**get_margin_run**](CollateralApi.md#get_margin_run) | **GET** /api/api/collateral/runs/{runId} | [EXPERIMENTAL] GetMarginRun: Get a margin run.
[**list_margin_call_lines**](CollateralApi.md#list_margin_call_lines) | **GET** /api/api/collateral/margincalls/{runId}/{agreementScope}/{agreementCode}/{item}/{marginType}/{direction}/lines | [EXPERIMENTAL] ListMarginCallLines: List the margin lines of a call.
[**list_margin_calls**](CollateralApi.md#list_margin_calls) | **GET** /api/api/collateral/margincalls | [EXPERIMENTAL] ListMarginCalls: List margin calls.
[**list_margin_lines**](CollateralApi.md#list_margin_lines) | **GET** /api/api/collateral/runs/{runId}/lines | [EXPERIMENTAL] ListMarginLines: List the margin lines of a run.
[**list_margin_run_recommendations**](CollateralApi.md#list_margin_run_recommendations) | **GET** /api/api/collateral/runs/{runId}/recommendations | [EXPERIMENTAL] ListMarginRunRecommendations: List a margin run&#39;s netting recommendations.
[**list_margin_runs**](CollateralApi.md#list_margin_runs) | **GET** /api/api/collateral/runs | [EXPERIMENTAL] ListMarginRuns: List margin runs.
[**list_netting_recommendations**](CollateralApi.md#list_netting_recommendations) | **GET** /api/api/collateral/recommendations | [EXPERIMENTAL] ListNettingRecommendations: List the current netting recommendations.
[**rank_margin_call**](CollateralApi.md#rank_margin_call) | **POST** /api/api/collateral/margincalls/{runId}/{agreementScope}/{agreementCode}/{item}/{marginType}/{direction}/$rank | [EXPERIMENTAL] RankMarginCall: [EXPERIMENTAL] RankMarginCall: Rank the collateral for a margin call again, with the caller&#39;s choices.
[**record_counterparty_demand**](CollateralApi.md#record_counterparty_demand) | **POST** /api/api/collateral/margincalls/{runId}/{agreementScope}/{agreementCode}/{item}/{marginType}/{direction}/$recordCounterpartyDemand | [EXPERIMENTAL] RecordCounterpartyDemand: Record the counterparty&#39;s demand against a margin call.
[**retry_margin_run**](CollateralApi.md#retry_margin_run) | **POST** /api/api/collateral/runs/{runId}/$retry | [EXPERIMENTAL] RetryMarginRun: Retry a margin run.
[**run_margin_calculation**](CollateralApi.md#run_margin_calculation) | **POST** /api/api/collateral/$run | [EXPERIMENTAL] RunMarginCalculation: Run the margin calculation.


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.collateral_api import CollateralApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(CollateralApi)
```

---

# **accept_margin_call**
> MarginCall acceptMarginCall = accept_margin_call(run_id, agreement_scope, agreement_code, item, margin_type, direction, accept_margin_call_request=accept_margin_call_request)

[EXPERIMENTAL] AcceptMarginCall: Accept a margin call.

Accept a margin call at the agreed amount: our figure when matched, the counterparty's when within tolerance, or  the amount given, which is required when the demand breaks tolerance or has not been recorded. Allowed from the  calculated and disputed states.

### Example

```python
api_instance = api_client_factory.build(CollateralApi)
run_id = 'run_id_example' # str
agreement_scope = 'agreement_scope_example' # str
agreement_code = 'agreement_code_example' # str
item = 'item_example' # str
margin_type = 'margin_type_example' # str
direction = 'direction_example' # str
accept_margin_call_request = AcceptMarginCallRequest()
api_response = api_instance.accept_margin_call(run_id, agreement_scope, agreement_code, item, margin_type, direction, accept_margin_call_request=accept_margin_call_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| The identifier of the margin run. | [required] 
 **agreement_scope** | **str**| The scope of the call&#39;s collateral agreement. | [required] 
 **agreement_code** | **str**| The code of the call&#39;s collateral agreement. | [required] 
 **item** | **str**| The margin item of the call. | [required] 
 **margin_type** | **str**| The margin type of the call. Currently VariationMargin. | [required] 
 **direction** | **str**| Who posts under the call. One of WePost, TheyPost or None. | [required] 
 **accept_margin_call_request** | [**AcceptMarginCallRequest**](../model/AcceptMarginCallRequest.md)| The amount to accept, when the default does not apply. | [optional] 

### Return type

[**MarginCall**](../model/MarginCall.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The accepted margin call. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **batch_accept_margin_calls**
> BatchAcceptMarginCallsResponse batchAcceptMarginCalls = batch_accept_margin_calls(batch_accept_margin_calls_request)

[EXPERIMENTAL] BatchAcceptMarginCalls: Accept several margin calls.

Accept each of the given margin calls at its default agreed amount. A call that cannot be accepted is reported  in the response and does not stop the others.

### Example

```python
api_instance = api_client_factory.build(CollateralApi)
batch_accept_margin_calls_request = BatchAcceptMarginCallsRequest()
api_response = api_instance.batch_accept_margin_calls(batch_accept_margin_calls_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_accept_margin_calls_request** | [**BatchAcceptMarginCallsRequest**](../model/BatchAcceptMarginCallsRequest.md)| The margin calls to accept. | [required] 

### Return type

[**BatchAcceptMarginCallsResponse**](../model/BatchAcceptMarginCallsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The calls accepted, and those that could not be. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **dispute_margin_call**
> MarginCall disputeMarginCall = dispute_margin_call(run_id, agreement_scope, agreement_code, item, margin_type, direction, dispute_margin_call_request)

[EXPERIMENTAL] DisputeMarginCall: Dispute a margin call.

Dispute a margin call: move the agreed amount now and leave the rest of the counterparty's demand in dispute,  with a reason and an owner. Allowed from the calculated and accepted states.

### Example

```python
api_instance = api_client_factory.build(CollateralApi)
run_id = 'run_id_example' # str
agreement_scope = 'agreement_scope_example' # str
agreement_code = 'agreement_code_example' # str
item = 'item_example' # str
margin_type = 'margin_type_example' # str
direction = 'direction_example' # str
dispute_margin_call_request = DisputeMarginCallRequest()
api_response = api_instance.dispute_margin_call(run_id, agreement_scope, agreement_code, item, margin_type, direction, dispute_margin_call_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| The identifier of the margin run. | [required] 
 **agreement_scope** | **str**| The scope of the call&#39;s collateral agreement. | [required] 
 **agreement_code** | **str**| The code of the call&#39;s collateral agreement. | [required] 
 **item** | **str**| The margin item of the call. | [required] 
 **margin_type** | **str**| The margin type of the call. Currently VariationMargin. | [required] 
 **direction** | **str**| Who posts under the call. One of WePost, TheyPost or None. | [required] 
 **dispute_margin_call_request** | [**DisputeMarginCallRequest**](../model/DisputeMarginCallRequest.md)| The amount to move now, the reason and the owner. | [required] 

### Return type

[**MarginCall**](../model/MarginCall.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The disputed margin call. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_margin_call**
> MarginCall getMarginCall = get_margin_call(run_id, agreement_scope, agreement_code, item, margin_type, direction)

[EXPERIMENTAL] GetMarginCall: Get a margin call.

Retrieve one margin call of a run by its business key.

### Example

```python
api_instance = api_client_factory.build(CollateralApi)
run_id = 'run_id_example' # str
agreement_scope = 'agreement_scope_example' # str
agreement_code = 'agreement_code_example' # str
item = 'item_example' # str
margin_type = 'margin_type_example' # str
direction = 'direction_example' # str
api_response = api_instance.get_margin_call(run_id, agreement_scope, agreement_code, item, margin_type, direction)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| The identifier of the margin run. | [required] 
 **agreement_scope** | **str**| The scope of the call&#39;s collateral agreement. | [required] 
 **agreement_code** | **str**| The code of the call&#39;s collateral agreement. | [required] 
 **item** | **str**| The margin item of the call. | [required] 
 **margin_type** | **str**| The margin type of the call. Currently VariationMargin. | [required] 
 **direction** | **str**| Who posts under the call. One of WePost, TheyPost or None. | [required] 

### Return type

[**MarginCall**](../model/MarginCall.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested margin call. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_margin_call_allocation**
> CollateralAllocation getMarginCallAllocation = get_margin_call_allocation(run_id, agreement_scope, agreement_code, item, margin_type, direction)

[EXPERIMENTAL] GetMarginCallAllocation: [EXPERIMENTAL] GetMarginCallAllocation: Get the collateral proposed for a margin call.

Retrieve the assets the run's allocation pass proposes to deliver for the call, or to take back for a return, with  every holding it considered and either its rank or the constraint that excluded it. Each line carries what a  transaction moving it needs: the instrument, the portfolio and custodian account, the units, the price and the  consideration. Not found until the run's allocation pass has completed, or when the call moves no collateral of ours.

### Example

```python
api_instance = api_client_factory.build(CollateralApi)
run_id = 'run_id_example' # str
agreement_scope = 'agreement_scope_example' # str
agreement_code = 'agreement_code_example' # str
item = 'item_example' # str
margin_type = 'margin_type_example' # str
direction = 'direction_example' # str
api_response = api_instance.get_margin_call_allocation(run_id, agreement_scope, agreement_code, item, margin_type, direction)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| The identifier of the margin run. | [required] 
 **agreement_scope** | **str**| The scope of the call&#39;s collateral agreement. | [required] 
 **agreement_code** | **str**| The code of the call&#39;s collateral agreement. | [required] 
 **item** | **str**| The margin item of the call. | [required] 
 **margin_type** | **str**| The margin type of the call. One of VariationMargin or InitialMargin. | [required] 
 **direction** | **str**| Who posts under the call. One of WePost, TheyPost or None. | [required] 

### Return type

[**CollateralAllocation**](../model/CollateralAllocation.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The collateral proposed for the margin call. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_margin_call_explanation**
> MarginExplanation getMarginCallExplanation = get_margin_call_explanation(run_id, agreement_scope, agreement_code, item, margin_type, direction)

[EXPERIMENTAL] GetMarginCallExplanation: Explain a margin call.

Show how the required amount of one initial-margin call of a run was arrived at, as a tree of components. Only an  initial-margin call whose run stored its working can be explained, as the call's ExplainAvailable says. The working  of portfolios the caller may not read is replaced by a single redacted component that keeps its parent adding up.

### Example

```python
api_instance = api_client_factory.build(CollateralApi)
run_id = 'run_id_example' # str
agreement_scope = 'agreement_scope_example' # str
agreement_code = 'agreement_code_example' # str
item = 'item_example' # str
margin_type = 'margin_type_example' # str
direction = 'direction_example' # str
api_response = api_instance.get_margin_call_explanation(run_id, agreement_scope, agreement_code, item, margin_type, direction)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| The identifier of the margin run. | [required] 
 **agreement_scope** | **str**| The scope of the call&#39;s collateral agreement. | [required] 
 **agreement_code** | **str**| The code of the call&#39;s collateral agreement. | [required] 
 **item** | **str**| The margin item of the call. | [required] 
 **margin_type** | **str**| The margin type of the call. Only InitialMargin calls can be explained. | [required] 
 **direction** | **str**| Who posts under the call. One of WePost, TheyPost or None. | [required] 

### Return type

[**MarginExplanation**](../model/MarginExplanation.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | How the call&#39;s required amount was arrived at. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_margin_line_explanation**
> MarginExplanation getMarginLineExplanation = get_margin_line_explanation(run_id, line_key, figure=figure)

[EXPERIMENTAL] GetMarginLineExplanation: Explain a margin line.

Show how the figures of one margin line of a run were arrived at, as a tree of components for each figure. The run  must have stored its working, as its lines' ExplainAvailable says. The working of portfolios the caller may not  read is replaced by a single redacted component that keeps its parent adding up. A line the caller may not read is  reported as not found.

### Example

```python
api_instance = api_client_factory.build(CollateralApi)
run_id = 'run_id_example' # str
line_key = 'line_key_example' # str
figure = 'figure_example' # str (optional)
api_response = api_instance.get_margin_line_explanation(run_id, line_key, figure=figure)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| The identifier of the margin run. | [required] 
 **line_key** | **str**| The key of the margin line, as listed in the line&#39;s LineKey. | [required] 
 **figure** | **str**| The figure of the line to explain: VariationMargin or InitialMargin. Explains every figure of the line that the run explained if not specified. Available values: VariationMargin, InitialMargin. | [optional] 

### Return type

[**MarginExplanation**](../model/MarginExplanation.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | How the line&#39;s figures were arrived at. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_margin_run**
> MarginRun getMarginRun = get_margin_run(run_id)

[EXPERIMENTAL] GetMarginRun: Get a margin run.

Retrieve a margin run with its progress: the status of each shard, the calls and lines published so far, and  anything it could not value.

### Example

```python
api_instance = api_client_factory.build(CollateralApi)
run_id = 'run_id_example' # str
api_response = api_instance.get_margin_run(run_id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| The identifier of the margin run. | [required] 

### Return type

[**MarginRun**](../model/MarginRun.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested margin run. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_margin_call_lines**
> PagedResourceListOfMarginLine listMarginCallLines = list_margin_call_lines(run_id, agreement_scope, agreement_code, item, margin_type, direction, page=page, limit=limit, filter=filter)

[EXPERIMENTAL] ListMarginCallLines: List the margin lines of a call.

List the holding lines behind one margin call: our side of the figure the counterparty's statement is matched against.

### Example

```python
api_instance = api_client_factory.build(CollateralApi)
run_id = 'run_id_example' # str
agreement_scope = 'agreement_scope_example' # str
agreement_code = 'agreement_code_example' # str
item = 'item_example' # str
margin_type = 'margin_type_example' # str
direction = 'direction_example' # str
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
api_response = api_instance.list_margin_call_lines(run_id, agreement_scope, agreement_code, item, margin_type, direction, page=page, limit=limit, filter=filter)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| The identifier of the margin run. | [required] 
 **agreement_scope** | **str**| The scope of the call&#39;s collateral agreement. | [required] 
 **agreement_code** | **str**| The code of the call&#39;s collateral agreement. | [required] 
 **item** | **str**| The margin item of the call. | [required] 
 **margin_type** | **str**| The margin type of the call. Currently VariationMargin. | [required] 
 **direction** | **str**| Who posts under the call. One of WePost, TheyPost or None. | [required] 
 **page** | **str**| The pagination token to use to continue listing margin lines; this value is returned from the previous call. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. The filterable fields are PortfolioId.Scope, PortfolioId.Code, HoldingId, CustodianAccountScope, CustodianAccountCode, CustodianAccountName, Units, Pv, VariationMargin and CollateralValue. For more information about filtering results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. | [optional] 

### Return type

[**PagedResourceListOfMarginLine**](../model/PagedResourceListOfMarginLine.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested margin lines. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_margin_calls**
> PagedResourceListOfMarginCall listMarginCalls = list_margin_calls(effective_at=effective_at, run_id=run_id, page=page, limit=limit, filter=filter, scenarios=scenarios, effective_from=effective_from)

[EXPERIMENTAL] ListMarginCalls: List margin calls.

List the margin calls of one run when a run id is given. Otherwise list the current calls for a business date:  those of the latest run for the date, with an agreement that run could not value served from the most recent run  that did. With an effectiveFrom the current calls of each date from it to effectiveAt are listed, in date order.  Restricted to the agreements the caller may read.

### Example

```python
api_instance = api_client_factory.build(CollateralApi)
effective_at = 'effective_at_example' # str (optional)
run_id = 'run_id_example' # str (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
scenarios = ['scenarios_example'] # List[str] (optional)
effective_from = 'effective_from_example' # str (optional)
api_response = api_instance.list_margin_calls(effective_at=effective_at, run_id=run_id, page=page, limit=limit, filter=filter, scenarios=scenarios, effective_from=effective_from)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The business date, datetime or cut label to list the current margin calls for, or the last date of the range when effectiveFrom is given. Defaults to today if not specified. Ignored when a run id is given. | [optional] 
 **run_id** | **str**| The identifier of the margin run to list the calls of. Lists the current calls for the business date if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing margin calls; this value is returned from the previous call. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. The filterable fields are RunId, AgreementId.Scope, AgreementId.Code, Counterparty.Code, Counterparty.IdTypeScope, Counterparty.IdTypeCode, Item, MarginType, Method, Settlement, Direction, Currency, Required, Held, Call, CounterpartyDemand, Difference, MatchStatus, AgreedAmount, DisputedAmount, DisputeOwner, State and Deadline. For example, to find the breaks, specify \&quot;MatchStatus eq &#39;Break&#39;\&quot;. For more information about filtering results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. | [optional] 
 **scenarios** | [**List[str]**](../model/str.md)| The scenarios, each as scope/code, whose calls are listed beside the base case calls, which are always listed. Lists the base case calls only if not specified. | [optional] 
 **effective_from** | **str**| The first business date, datetime or cut label of a range ending at effectiveAt, for a time series of calls. Lists the one business date if not specified. Ignored when a run id is given. | [optional] 

### Return type

[**PagedResourceListOfMarginCall**](../model/PagedResourceListOfMarginCall.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested margin calls. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_margin_lines**
> PagedResourceListOfMarginLine listMarginLines = list_margin_lines(run_id, page=page, limit=limit, filter=filter, scenarios=scenarios)

[EXPERIMENTAL] ListMarginLines: List the margin lines of a run.

List the holding lines behind every margin call of a run, restricted to the agreements the caller may read.

### Example

```python
api_instance = api_client_factory.build(CollateralApi)
run_id = 'run_id_example' # str
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
scenarios = ['scenarios_example'] # List[str] (optional)
api_response = api_instance.list_margin_lines(run_id, page=page, limit=limit, filter=filter, scenarios=scenarios)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| The identifier of the margin run. | [required] 
 **page** | **str**| The pagination token to use to continue listing margin lines; this value is returned from the previous call. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. The filterable fields are AgreementId.Scope, AgreementId.Code, Item, PortfolioId.Scope, PortfolioId.Code, HoldingId, CustodianAccountScope, CustodianAccountCode, CustodianAccountName, Units, Pv, VariationMargin and CollateralValue. For more information about filtering results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. | [optional] 
 **scenarios** | [**List[str]**](../model/str.md)| The scenarios, each as scope/code, whose lines are listed beside the base case lines, which are always listed. Lists the base case lines only if not specified. | [optional] 

### Return type

[**PagedResourceListOfMarginLine**](../model/PagedResourceListOfMarginLine.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested margin lines. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_margin_run_recommendations**
> PagedResourceListOfNettingRecommendation listMarginRunRecommendations = list_margin_run_recommendations(run_id, page=page, limit=limit, filter=filter)

[EXPERIMENTAL] ListMarginRunRecommendations: List a margin run's netting recommendations.

List the trades a run's optimisation pass found would attract less initial margin in another netting set of the  run, with both sets' initial margin before and after the move. Empty until the run's optimisation pass has  completed. Restricted to recommendations whose source and target agreements the caller may read.

### Example

```python
api_instance = api_client_factory.build(CollateralApi)
run_id = 'run_id_example' # str
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
api_response = api_instance.list_margin_run_recommendations(run_id, page=page, limit=limit, filter=filter)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| The identifier of the margin run. | [required] 
 **page** | **str**| The pagination token to use to continue listing recommendations; this value is returned from the previous call. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. The filterable fields are RunId, SourceAgreementId.Scope, SourceAgreementId.Code, SourceItem, TargetAgreementId.Scope, TargetAgreementId.Code, TargetItem, Transfer, InstrumentType, Currency, MaturityBucket, SavingPerDay, OneOffCost, PaybackDays and InitialMarginChange. For more information about filtering results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. | [optional] 

### Return type

[**PagedResourceListOfNettingRecommendation**](../model/PagedResourceListOfNettingRecommendation.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested recommendations. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_margin_runs**
> PagedResourceListOfMarginRun listMarginRuns = list_margin_runs(page=page, limit=limit, filter=filter)

[EXPERIMENTAL] ListMarginRuns: List margin runs.

List the margin runs on record, most recent first.

### Example

```python
api_instance = api_client_factory.build(CollateralApi)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
api_response = api_instance.list_margin_runs(page=page, limit=limit, filter=filter)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| The pagination token to use to continue listing margin runs; this value is returned from the previous call. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. The filterable fields are Id, EffectiveAt, AsAt, Status, CallCount and LineCount. For example, to find the runs for a business date, specify \&quot;EffectiveAt eq 2026-09-04\&quot;. For more information about filtering results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. | [optional] 

### Return type

[**PagedResourceListOfMarginRun**](../model/PagedResourceListOfMarginRun.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested margin runs. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_netting_recommendations**
> PagedResourceListOfNettingRecommendation listNettingRecommendations = list_netting_recommendations(effective_at=effective_at, page=page, limit=limit, filter=filter)

[EXPERIMENTAL] ListNettingRecommendations: List the current netting recommendations.

List the netting recommendations in force for a business date: those of the latest run for the date whose  optimisation pass completed, with an agreement that run could not value served from the most recent run that  did. Restricted to recommendations whose source and target agreements the caller may read.

### Example

```python
api_instance = api_client_factory.build(CollateralApi)
effective_at = 'effective_at_example' # str (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
api_response = api_instance.list_netting_recommendations(effective_at=effective_at, page=page, limit=limit, filter=filter)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The business date, datetime or cut label to list the current recommendations for. Defaults to today if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing recommendations; this value is returned from the previous call. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. The filterable fields are RunId, SourceAgreementId.Scope, SourceAgreementId.Code, SourceItem, TargetAgreementId.Scope, TargetAgreementId.Code, TargetItem, Transfer, InstrumentType, Currency, MaturityBucket, SavingPerDay, OneOffCost, PaybackDays and InitialMarginChange. For more information about filtering results, see https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. | [optional] 

### Return type

[**PagedResourceListOfNettingRecommendation**](../model/PagedResourceListOfNettingRecommendation.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested recommendations. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **rank_margin_call**
> CollateralAllocation rankMarginCall = rank_margin_call(run_id, agreement_scope, agreement_code, item, margin_type, direction, rank_margin_call_request=rank_margin_call_request)

[EXPERIMENTAL] RankMarginCall: [EXPERIMENTAL] RankMarginCall: Rank the collateral for a margin call again, with the caller's choices.

Value the call's agreement as of now for the run's business date and rank its free, eligible holdings for the  call again, keeping the assets and units the caller chose. Each choice is validated against the agreement's  constraints and kept with its reason when it fails one; the rest of the call is filled from the ranking, cheapest  first, unless fillRemainder is false. Nothing is stored: the result is what to book, for the caller to decide on.

### Example

```python
api_instance = api_client_factory.build(CollateralApi)
run_id = 'run_id_example' # str
agreement_scope = 'agreement_scope_example' # str
agreement_code = 'agreement_code_example' # str
item = 'item_example' # str
margin_type = 'margin_type_example' # str
direction = 'direction_example' # str
rank_margin_call_request = RankMarginCallRequest()
api_response = api_instance.rank_margin_call(run_id, agreement_scope, agreement_code, item, margin_type, direction, rank_margin_call_request=rank_margin_call_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| The identifier of the margin run. | [required] 
 **agreement_scope** | **str**| The scope of the call&#39;s collateral agreement. | [required] 
 **agreement_code** | **str**| The code of the call&#39;s collateral agreement. | [required] 
 **item** | **str**| The margin item of the call. | [required] 
 **margin_type** | **str**| The margin type of the call. One of VariationMargin or InitialMargin. | [required] 
 **direction** | **str**| Who posts under the call. One of WePost, TheyPost or None. | [required] 
 **rank_margin_call_request** | [**RankMarginCallRequest**](../model/RankMarginCallRequest.md)| The assets the caller chose, and whether to fill the rest. | [optional] 

### Return type

[**CollateralAllocation**](../model/CollateralAllocation.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The collateral ranked for the margin call. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **record_counterparty_demand**
> MarginCall recordCounterpartyDemand = record_counterparty_demand(run_id, agreement_scope, agreement_code, item, margin_type, direction, record_counterparty_demand_request)

[EXPERIMENTAL] RecordCounterpartyDemand: Record the counterparty's demand against a margin call.

Record the counterparty's figure for a margin call and match it to ours: equal is matched, a difference within the  agreement's tolerance is within tolerance, and a larger difference is a break. The call's state is not changed,  except that a call already accepted or disputed returns to calculated when its demand changes.

### Example

```python
api_instance = api_client_factory.build(CollateralApi)
run_id = 'run_id_example' # str
agreement_scope = 'agreement_scope_example' # str
agreement_code = 'agreement_code_example' # str
item = 'item_example' # str
margin_type = 'margin_type_example' # str
direction = 'direction_example' # str
record_counterparty_demand_request = RecordCounterpartyDemandRequest()
api_response = api_instance.record_counterparty_demand(run_id, agreement_scope, agreement_code, item, margin_type, direction, record_counterparty_demand_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| The identifier of the margin run. | [required] 
 **agreement_scope** | **str**| The scope of the call&#39;s collateral agreement. | [required] 
 **agreement_code** | **str**| The code of the call&#39;s collateral agreement. | [required] 
 **item** | **str**| The margin item of the call. | [required] 
 **margin_type** | **str**| The margin type of the call. Currently VariationMargin. | [required] 
 **direction** | **str**| Who posts under the call. One of WePost, TheyPost or None. | [required] 
 **record_counterparty_demand_request** | [**RecordCounterpartyDemandRequest**](../model/RecordCounterpartyDemandRequest.md)| The counterparty&#39;s demand. | [required] 

### Return type

[**MarginCall**](../model/MarginCall.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The margin call with the demand matched against it. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **retry_margin_run**
> MarginRun retryMarginRun = retry_margin_run(run_id)

[EXPERIMENTAL] RetryMarginRun: Retry a margin run.

Value the failed shards of a completed margin run again, at the run's asAt. Refused while the run is in progress  or when no shard failed.

### Example

```python
api_instance = api_client_factory.build(CollateralApi)
run_id = 'run_id_example' # str
api_response = api_instance.retry_margin_run(run_id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| The identifier of the margin run. | [required] 

### Return type

[**MarginRun**](../model/MarginRun.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The margin run with its failed shards pending again. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **run_margin_calculation**
> PagedResourceListOfMarginRun runMarginCalculation = run_margin_calculation(margin_run_request)

[EXPERIMENTAL] RunMarginCalculation: Run the margin calculation.

Value the collateral agreements for a business date, or for each weekday of a span, in the background and publish  their margin calls as a run for each date. The base case is always valued, with each scenario named in the request  valued beside it as a case of the same run. A date after the asAt is a projection on the market as at the asAt.  The runs are returned as planned, in date order; poll GetMarginRun for the progress of each, and list the calls as they are published.

### Example

```python
api_instance = api_client_factory.build(CollateralApi)
margin_run_request = MarginRunRequest()
api_response = api_instance.run_margin_calculation(margin_run_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **margin_run_request** | [**MarginRunRequest**](../model/MarginRunRequest.md)| The business date to value, or the span of dates ending at it, and optionally the asAt, the agreements to include and the scenarios to value beside the base case. | [required] 

### Return type

[**PagedResourceListOfMarginRun**](../model/PagedResourceListOfMarginRun.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The margin runs as planned, one for each date valued. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

