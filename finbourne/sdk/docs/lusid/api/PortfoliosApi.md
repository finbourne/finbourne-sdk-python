# lusid.PortfoliosApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_upsert_portfolio_access_metadata**](PortfoliosApi.md#batch_upsert_portfolio_access_metadata) | **PUT** /api/api/portfolios/metadata | [EARLY ACCESS] BatchUpsertPortfolioAccessMetadata: Upsert multiple Portfolio Access Metadata Rules to multiple Portfolios
[**delete_instrument_event_instruction**](PortfoliosApi.md#delete_instrument_event_instruction) | **DELETE** /api/api/portfolios/{scope}/{code}/instrumenteventinstructions/{instrumentEventInstructionId} | [EARLY ACCESS] DeleteInstrumentEventInstruction: Delete Instrument Event Instruction
[**delete_key_from_portfolio_access_metadata**](PortfoliosApi.md#delete_key_from_portfolio_access_metadata) | **DELETE** /api/api/portfolios/{scope}/{code}/metadata/{metadataKey} | DeleteKeyFromPortfolioAccessMetadata: Delete a Portfolio Access Metadata Rule
[**delete_portfolio**](PortfoliosApi.md#delete_portfolio) | **DELETE** /api/api/portfolios/{scope}/{code} | DeletePortfolio: Delete portfolio
[**delete_portfolio_properties**](PortfoliosApi.md#delete_portfolio_properties) | **DELETE** /api/api/portfolios/{scope}/{code}/properties | DeletePortfolioProperties: Delete portfolio properties
[**delete_portfolio_returns**](PortfoliosApi.md#delete_portfolio_returns) | **DELETE** /api/api/portfolios/{scope}/{code}/returns/{returnScope}/{returnCode}/$delete | [EARLY ACCESS] DeletePortfolioReturns: Delete Returns
[**get_aggregated_returns_dispersion_metrics**](PortfoliosApi.md#get_aggregated_returns_dispersion_metrics) | **POST** /api/api/portfolios/{scope}/{code}/returns/dispersion/$aggregated | [EARLY ACCESS] GetAggregatedReturnsDispersionMetrics: Get the Aggregated Returns Dispersion metric
[**get_composite_breakdown**](PortfoliosApi.md#get_composite_breakdown) | **POST** /api/api/portfolios/{scope}/{code}/returns/breakdown | [EARLY ACCESS] GetCompositeBreakdown: Get the Composite Breakdown on how the composite Returns are calculated
[**get_instrument_event_instruction**](PortfoliosApi.md#get_instrument_event_instruction) | **GET** /api/api/portfolios/{scope}/{code}/instrumenteventinstructions/{instrumentEventInstructionId} | [EARLY ACCESS] GetInstrumentEventInstruction: Get Instrument Event Instruction
[**get_portfolio**](PortfoliosApi.md#get_portfolio) | **GET** /api/api/portfolios/{scope}/{code} | GetPortfolio: Get portfolio
[**get_portfolio_aggregate_returns**](PortfoliosApi.md#get_portfolio_aggregate_returns) | **GET** /api/api/portfolios/{scope}/{code}/returns/{returnScope}/{returnCode}/aggregated | [DEPRECATED] GetPortfolioAggregateReturns: Aggregate Returns (This is a deprecated endpoint).
[**get_portfolio_aggregated_returns**](PortfoliosApi.md#get_portfolio_aggregated_returns) | **POST** /api/api/portfolios/{scope}/{code}/returns/$aggregated | GetPortfolioAggregatedReturns: Aggregated Returns
[**get_portfolio_commands**](PortfoliosApi.md#get_portfolio_commands) | **GET** /api/api/portfolios/{scope}/{code}/commands | GetPortfolioCommands: Get portfolio commands
[**get_portfolio_metadata**](PortfoliosApi.md#get_portfolio_metadata) | **GET** /api/api/portfolios/{scope}/{code}/metadata | GetPortfolioMetadata: Get access metadata rules for a portfolio
[**get_portfolio_properties**](PortfoliosApi.md#get_portfolio_properties) | **GET** /api/api/portfolios/{scope}/{code}/properties | GetPortfolioProperties: Get portfolio properties
[**get_portfolio_property_time_series**](PortfoliosApi.md#get_portfolio_property_time_series) | **GET** /api/api/portfolios/{scope}/{code}/properties/time-series | GetPortfolioPropertyTimeSeries: Get portfolio property time series
[**get_portfolio_relations**](PortfoliosApi.md#get_portfolio_relations) | **GET** /api/api/portfolios/{scope}/{code}/relations | [EXPERIMENTAL] GetPortfolioRelations: Get portfolio relations
[**get_portfolio_relationships**](PortfoliosApi.md#get_portfolio_relationships) | **GET** /api/api/portfolios/{scope}/{code}/relationships | GetPortfolioRelationships: Get portfolio relationships
[**get_portfolio_returns**](PortfoliosApi.md#get_portfolio_returns) | **GET** /api/api/portfolios/{scope}/{code}/returns/{returnScope}/{returnCode} | GetPortfolioReturns: Get Returns
[**get_portfolios_access_metadata_by_key**](PortfoliosApi.md#get_portfolios_access_metadata_by_key) | **GET** /api/api/portfolios/{scope}/{code}/metadata/{metadataKey} | [EARLY ACCESS] GetPortfoliosAccessMetadataByKey: Get an entry identified by a metadataKey in the access metadata object
[**list_instrument_event_instructions**](PortfoliosApi.md#list_instrument_event_instructions) | **GET** /api/api/portfolios/{scope}/{code}/instrumenteventinstructions | [EARLY ACCESS] ListInstrumentEventInstructions: List Instrument Event Instructions
[**list_portfolio_properties**](PortfoliosApi.md#list_portfolio_properties) | **GET** /api/api/portfolios/{scope}/{code}/properties/list | [EARLY ACCESS] ListPortfolioProperties: Get portfolio properties
[**list_portfolios**](PortfoliosApi.md#list_portfolios) | **GET** /api/api/portfolios | ListPortfolios: List portfolios
[**list_portfolios_for_scope**](PortfoliosApi.md#list_portfolios_for_scope) | **GET** /api/api/portfolios/{scope} | ListPortfoliosForScope: List portfolios for scope
[**patch_portfolio**](PortfoliosApi.md#patch_portfolio) | **PATCH** /api/api/portfolios/{scope}/{code} | PatchPortfolio: Patch portfolio.
[**patch_portfolio_access_metadata**](PortfoliosApi.md#patch_portfolio_access_metadata) | **PATCH** /api/api/portfolios/{scope}/{code}/metadata | [EARLY ACCESS] PatchPortfolioAccessMetadata: Patch Access Metadata rules for a Portfolio.
[**update_portfolio**](PortfoliosApi.md#update_portfolio) | **PUT** /api/api/portfolios/{scope}/{code} | UpdatePortfolio: Update portfolio
[**upsert_instrument_event_instructions**](PortfoliosApi.md#upsert_instrument_event_instructions) | **POST** /api/api/portfolios/{scope}/{code}/instrumenteventinstructions | [EARLY ACCESS] UpsertInstrumentEventInstructions: Upsert Instrument Event Instructions
[**upsert_portfolio_access_metadata**](PortfoliosApi.md#upsert_portfolio_access_metadata) | **PUT** /api/api/portfolios/{scope}/{code}/metadata/{metadataKey} | UpsertPortfolioAccessMetadata: Upsert a Portfolio Access Metadata Rule associated with specific metadataKey. This creates or updates the data in LUSID.
[**upsert_portfolio_properties**](PortfoliosApi.md#upsert_portfolio_properties) | **POST** /api/api/portfolios/{scope}/{code}/properties | UpsertPortfolioProperties: Upsert portfolio properties
[**upsert_portfolio_returns**](PortfoliosApi.md#upsert_portfolio_returns) | **POST** /api/api/portfolios/{scope}/{code}/returns/{returnScope}/{returnCode} | UpsertPortfolioReturns: Upsert Returns


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.portfolios_api import PortfoliosApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(PortfoliosApi)
```

---

# **batch_upsert_portfolio_access_metadata**
> BatchUpsertPortfolioAccessMetadataResponse batchUpsertPortfolioAccessMetadata = batch_upsert_portfolio_access_metadata(request_body, effective_at=effective_at, effective_until=effective_until)

[EARLY ACCESS] BatchUpsertPortfolioAccessMetadata: Upsert multiple Portfolio Access Metadata Rules to multiple Portfolios

Update or insert multiple Access Metadata rules for multiple Portfolios. Items will be updated if they already exist  and inserted if they do not. No other items will be affected    The response will return the successfully updated or inserted Portfolio Access Metadata Rules or a failure message if unsuccessful                Multiple rules for a metadataKey can exist with different effective at dates, when resources are accessed the rule that is active for the current time will be fetched

### Example

```python
api_instance = api_client_factory.build(PortfoliosApi)
request_body = {"firstExampleRequest":{"portfolioId":{"scope":"TestScopeA","code":"TestCodeA"},"metadata":{"metadataKey":[{"value":"SilverLicence","provider":"TestDataProvider"}]}},"secondExampleRequest":{"portfolioId":{"scope":"TestScopeB","code":"TestCodeB"},"metadata":{"metadataKey":[{"value":"SilverLicence","provider":"TestDataProvider"}]}}} # Dict[str, BatchUpsertPortfolioAccessMetadataRequest]
effective_at = 'effective_at_example' # str (optional)
effective_until = 'effective_until_example' # str (optional)
api_response = api_instance.batch_upsert_portfolio_access_metadata(request_body, effective_at=effective_at, effective_until=effective_until)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, BatchUpsertPortfolioAccessMetadataRequest]**](BatchUpsertPortfolioAccessMetadataRequest.md)| The Access Metadata Rules to upsert and the Portfolio identifiers to upsert for | [required] 
 **effective_at** | **str**| The date these rules will be effective from | [optional] 
 **effective_until** | **str**| The effective date until which the Access Metadata is valid. If not supplied, this will be valid indefinitely, or until the next &#39;effectiveAt&#39; date of the Access Metadata | [optional] 

### Return type

[**BatchUpsertPortfolioAccessMetadataResponse**](BatchUpsertPortfolioAccessMetadataResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully updated or inserted items or any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_instrument_event_instruction**
> DeletedEntityResponse deleteInstrumentEventInstruction = delete_instrument_event_instruction(scope, code, instrument_event_instruction_id, portfolio_effective_at=portfolio_effective_at)

[EARLY ACCESS] DeleteInstrumentEventInstruction: Delete Instrument Event Instruction

Delete a particular instruction for a particular portfolio

### Example

```python
api_instance = api_client_factory.build(PortfoliosApi)
scope = 'scope_example' # str
code = 'code_example' # str
instrument_event_instruction_id = 'instrument_event_instruction_id_example' # str
portfolio_effective_at = 'portfolio_effective_at_example' # str (optional)
api_response = api_instance.delete_instrument_event_instruction(scope, code, instrument_event_instruction_id, portfolio_effective_at=portfolio_effective_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | [required] 
 **code** | **str**| The code of the portfolio. Together with the scope this uniquely identifies the portfolio. | [required] 
 **instrument_event_instruction_id** | **str**| The id of the instruction to be deleted. | [required] 
 **portfolio_effective_at** | **str**| The effective date at which the portfolio will be resolved. Defaults to current time if not specified. | [optional] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the instruction was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_key_from_portfolio_access_metadata**
> DeletedEntityResponse deleteKeyFromPortfolioAccessMetadata = delete_key_from_portfolio_access_metadata(scope, code, metadata_key, effective_at=effective_at, effective_until=effective_until)

DeleteKeyFromPortfolioAccessMetadata: Delete a Portfolio Access Metadata Rule

Delete the Portfolio Access Metadata Rule that exactly matches the provided identifier parts

### Example

```python
api_instance = api_client_factory.build(PortfoliosApi)
scope = 'scope_example' # str
code = 'code_example' # str
metadata_key = 'metadata_key_example' # str
effective_at = 'effective_at_example' # str (optional)
effective_until = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.delete_key_from_portfolio_access_metadata(scope, code, metadata_key, effective_at=effective_at, effective_until=effective_until)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Quote Access Metadata Rule to retrieve. | [required] 
 **code** | **str**| Portfolio code | [required] 
 **metadata_key** | **str**| The metadataKey identifying the access metadata entry to delete | [required] 
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
**200** | The rule that has been deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_portfolio**
> DeletedEntityResponse deletePortfolio = delete_portfolio(scope, code)

DeletePortfolio: Delete portfolio

Delete a particular portfolio.                The deletion will take effect from the portfolio's creation datetime. This means that the portfolio will no longer exist at any effective datetime, as per the asAt datetime of deletion.

### Example

```python
api_instance = api_client_factory.build(PortfoliosApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.delete_portfolio(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | [required] 
 **code** | **str**| The code of the portfolio. Together with the scope this uniquely identifies the portfolio. | [required] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the portfolio was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_portfolio_properties**
> DeletedEntityResponse deletePortfolioProperties = delete_portfolio_properties(scope, code, property_keys, effective_at=effective_at)

DeletePortfolioProperties: Delete portfolio properties

Delete one or more properties from a particular portfolio. If the properties are time-variant then an effective datetime from which  to delete properties must be specified. If the properties are perpetual then it is invalid to specify an effective datetime for deletion.

### Example

```python
api_instance = api_client_factory.build(PortfoliosApi)
scope = 'scope_example' # str
code = 'code_example' # str
property_keys = ['property_keys_example'] # List[str]
effective_at = 'effective_at_example' # str (optional)
api_response = api_instance.delete_portfolio_properties(scope, code, property_keys, effective_at=effective_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | [required] 
 **code** | **str**| The code of the portfolio. Together with the scope this uniquely identifies the portfolio. | [required] 
 **property_keys** | [**List[str]**](str.md)| The property keys of the properties to delete. These must take the format              {domain}/{scope}/{code}, for example &#39;Portfolio/Manager/Id&#39;. Each property must be from the &#39;Portfolio&#39; domain. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to delete time-variant properties from.              The property must exist at the specified &#39;effectiveAt&#39; datetime. If the &#39;effectiveAt&#39; is not provided or is              before the time-variant property exists then a failure is returned. Do not specify this parameter if any of              the properties to delete are perpetual. | [optional] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the properties were deleted from the specified portfolio |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_portfolio_returns**
> DeletedEntityResponse deletePortfolioReturns = delete_portfolio_returns(scope, code, return_scope, return_code, from_effective_at, to_effective_at, period=period)

[EARLY ACCESS] DeletePortfolioReturns: Delete Returns

Cancel one or more Returns which exist into the specified portfolio.

### Example

```python
api_instance = api_client_factory.build(PortfoliosApi)
scope = 'scope_example' # str
code = 'code_example' # str
return_scope = 'return_scope_example' # str
return_code = 'return_code_example' # str
from_effective_at = 'from_effective_at_example' # str
to_effective_at = 'to_effective_at_example' # str
period = 'period_example' # str (optional)
api_response = api_instance.delete_portfolio_returns(scope, code, return_scope, return_code, from_effective_at, to_effective_at, period=period)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Portfolio. | [required] 
 **code** | **str**| The code of the  Portfolio. | [required] 
 **return_scope** | **str**| The scope of the Returns. | [required] 
 **return_code** | **str**| The code of the Returns. | [required] 
 **from_effective_at** | **str**| The start date from which to delete the Returns. | [required] 
 **to_effective_at** | **str**| The end date from which to delete the Returns. | [required] 
 **period** | **str**| The Period (Daily or Monthly) of the Returns to be deleted. Defaults to Daily. | [optional] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully deleted Returns data along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_aggregated_returns_dispersion_metrics**
> CompositeDispersionResponse getAggregatedReturnsDispersionMetrics = get_aggregated_returns_dispersion_metrics(scope, code, aggregated_returns_dispersion_request, as_at=as_at)

[EARLY ACCESS] GetAggregatedReturnsDispersionMetrics: Get the Aggregated Returns Dispersion metric

Calculate the dispersion metric with the Aggregate Returns which are on the specified portfolio.             This works only for composites which have at least 6 constituents for a full year in.

### Example

```python
api_instance = api_client_factory.build(PortfoliosApi)
scope = 'scope_example' # str
code = 'code_example' # str
aggregated_returns_dispersion_request = AggregatedReturnsDispersionRequest()
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_aggregated_returns_dispersion_metrics(scope, code, aggregated_returns_dispersion_request, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Portfolio. | [required] 
 **code** | **str**| The code of the  Portfolio. | [required] 
 **aggregated_returns_dispersion_request** | [**AggregatedReturnsDispersionRequest**](AggregatedReturnsDispersionRequest.md)| The request used in the AggregatedReturnsDispersionMetric. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Returns. Defaults to the latest. | [optional] 

### Return type

[**CompositeDispersionResponse**](CompositeDispersionResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The aggregated returns grouped by return stream. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_composite_breakdown**
> CompositeBreakdownResponse getCompositeBreakdown = get_composite_breakdown(scope, code, composite_breakdown_request, from_effective_at=from_effective_at, to_effective_at=to_effective_at, as_at=as_at)

[EARLY ACCESS] GetCompositeBreakdown: Get the Composite Breakdown on how the composite Returns are calculated

Calculate the Composite Returns and return this with the constituents which are included in this calculation

### Example

```python
api_instance = api_client_factory.build(PortfoliosApi)
scope = 'scope_example' # str
code = 'code_example' # str
composite_breakdown_request = CompositeBreakdownRequest()
from_effective_at = 'from_effective_at_example' # str (optional)
to_effective_at = 'to_effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_composite_breakdown(scope, code, composite_breakdown_request, from_effective_at=from_effective_at, to_effective_at=to_effective_at, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Portfolio. | [required] 
 **code** | **str**| The code of the  Portfolio. | [required] 
 **composite_breakdown_request** | [**CompositeBreakdownRequest**](CompositeBreakdownRequest.md)| The request used in the GetCompositeBreakdown. | [required] 
 **from_effective_at** | **str**| The start date from which to calculate the Returns. | [optional] 
 **to_effective_at** | **str**| The end date for which to calculate the Returns. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Returns. Defaults to the latest. | [optional] 

### Return type

[**CompositeBreakdownResponse**](CompositeBreakdownResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The aggregated returns grouped by return stream. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_instrument_event_instruction**
> InstrumentEventInstruction getInstrumentEventInstruction = get_instrument_event_instruction(scope, code, instrument_event_instruction_id, portfolio_effective_at=portfolio_effective_at, as_at=as_at, timeline_scope=timeline_scope, timeline_code=timeline_code, closed_period_id=closed_period_id)

[EARLY ACCESS] GetInstrumentEventInstruction: Get Instrument Event Instruction

Get a particular instruction for a particular portfolio

### Example

```python
api_instance = api_client_factory.build(PortfoliosApi)
scope = 'scope_example' # str
code = 'code_example' # str
instrument_event_instruction_id = 'instrument_event_instruction_id_example' # str
portfolio_effective_at = 'portfolio_effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
timeline_scope = 'timeline_scope_example' # str (optional)
timeline_code = 'timeline_code_example' # str (optional)
closed_period_id = 'closed_period_id_example' # str (optional)
api_response = api_instance.get_instrument_event_instruction(scope, code, instrument_event_instruction_id, portfolio_effective_at=portfolio_effective_at, as_at=as_at, timeline_scope=timeline_scope, timeline_code=timeline_code, closed_period_id=closed_period_id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | [required] 
 **code** | **str**| The code of the portfolio. Together with the scope this uniquely identifies the portfolio. | [required] 
 **instrument_event_instruction_id** | **str**| The id of the instruction to be retrieved. | [required] 
 **portfolio_effective_at** | **str**| The effective date at which the portfolio will be resolved. Defaults to current time if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the instruction. Defaults to return the latest version of the instruction if not specified. | [optional] 
 **timeline_scope** | **str**| The scope of the Timeline, used to override the AsAt, and fetch post close activity data.              If this is provided, timelineCode must also be provided. | [optional] 
 **timeline_code** | **str**| The code of the Timeline, used to override the AsAt, and fetch post close activity data.              If this is provided, timelineScope must also be provided. | [optional] 
 **closed_period_id** | **str**| The code of the ClosedPeriod attached to the timeline, used to override the AsAt, and fetch post close activity data.              If this field is left empty and the timelineScope and timelineCode fields are filled out, the portfolioEffectiveAt will be used to resolve the relevant closed period. | [optional] 

### Return type

[**InstrumentEventInstruction**](InstrumentEventInstruction.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested instrument event instruction |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_portfolio**
> Portfolio getPortfolio = get_portfolio(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys, relationship_definition_ids=relationship_definition_ids)

GetPortfolio: Get portfolio

Retrieve the definition of a particular portfolio.

### Example

```python
api_instance = api_client_factory.build(PortfoliosApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
relationship_definition_ids = ['relationship_definition_ids_example'] # List[str] (optional)
api_response = api_instance.get_portfolio(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys, relationship_definition_ids=relationship_definition_ids)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | [required] 
 **code** | **str**| The code of the portfolio. Together with the scope this uniquely identifies the portfolio. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the portfolio definition. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the portfolio definition. Defaults to returning the latest version of the portfolio definition if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Portfolio&#39; domain to decorate onto the portfolio,              or from any domain that supports relationships to decorate onto related entities. These must take the format              {domain}/{scope}/{code}, for example &#39;Portfolio/Manager/Id&#39;. | [optional] 
 **relationship_definition_ids** | [**List[str]**](str.md)| A list of relationship definitions that are used to decorate related entities              onto the portfolio in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. | [optional] 

### Return type

[**Portfolio**](Portfolio.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested portfolio definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_portfolio_aggregate_returns**
> ResourceListOfAggregatedReturn getPortfolioAggregateReturns = get_portfolio_aggregate_returns(scope, code, return_scope, return_code, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code, from_effective_at=from_effective_at, to_effective_at=to_effective_at, composite_method=composite_method, period=period, output_frequency=output_frequency, metrics=metrics, as_at=as_at, alternative_inc_date=alternative_inc_date)

[DEPRECATED] GetPortfolioAggregateReturns: Aggregate Returns (This is a deprecated endpoint).

Aggregate Returns which are on the specified portfolio.

### Example

```python
api_instance = api_client_factory.build(PortfoliosApi)
scope = 'scope_example' # str
code = 'code_example' # str
return_scope = 'return_scope_example' # str
return_code = 'return_code_example' # str
recipe_id_scope = 'recipe_id_scope_example' # str (optional)
recipe_id_code = 'recipe_id_code_example' # str (optional)
from_effective_at = 'from_effective_at_example' # str (optional)
to_effective_at = 'to_effective_at_example' # str (optional)
composite_method = 'composite_method_example' # str (optional)
period = 'period_example' # str (optional)
output_frequency = 'output_frequency_example' # str (optional)
metrics = ['metrics_example'] # List[str] (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
alternative_inc_date = 'alternative_inc_date_example' # str (optional)
api_response = api_instance.get_portfolio_aggregate_returns(scope, code, return_scope, return_code, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code, from_effective_at=from_effective_at, to_effective_at=to_effective_at, composite_method=composite_method, period=period, output_frequency=output_frequency, metrics=metrics, as_at=as_at, alternative_inc_date=alternative_inc_date)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Portfolio. | [required] 
 **code** | **str**| The code of the  Portfolio. | [required] 
 **return_scope** | **str**| The scope of the Returns. | [required] 
 **return_code** | **str**| The code of the Returns. | [required] 
 **recipe_id_scope** | **str**| The Recipe Scope for getting the fx rates | [optional] 
 **recipe_id_code** | **str**| The Recipe Code for getting the fx rates | [optional] 
 **from_effective_at** | **str**| The start date from which to calculate the Returns. | [optional] 
 **to_effective_at** | **str**| The end date for which to calculate the Returns. | [optional] 
 **composite_method** | **str**| The method used to calculate the Portfolio performance:              Equal/Asset. | [optional] 
 **period** | **str**| The type of the returns used to calculate the aggregation result: Daily/Monthly. | [optional] 
 **output_frequency** | **str**| The type of calculated output: Daily/Weekly/Monthly/Quarterly/Half-Yearly/Yearly. | [optional] 
 **metrics** | [**List[str]**](str.md)| Determines what type of returns should be calculated, see https://support.lusid.com/knowledgebase/article/KA-01675/en-us for a list of available metrics. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Returns. Defaults to the latest. | [optional] 
 **alternative_inc_date** | **str**| The date from which to consider the Returns on the Portfolio, if this is different from the date when Returns begin. Can be a date string or Portfolio property. | [optional] 

### Return type

[**ResourceListOfAggregatedReturn**](ResourceListOfAggregatedReturn.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The aggregated returns. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_portfolio_aggregated_returns**
> AggregatedReturnsResponse getPortfolioAggregatedReturns = get_portfolio_aggregated_returns(scope, code, aggregated_returns_request, from_effective_at=from_effective_at, to_effective_at=to_effective_at, as_at=as_at)

GetPortfolioAggregatedReturns: Aggregated Returns

Aggregate Returns which are on the specified portfolio.

### Example

```python
api_instance = api_client_factory.build(PortfoliosApi)
scope = 'scope_example' # str
code = 'code_example' # str
aggregated_returns_request = AggregatedReturnsRequest()
from_effective_at = 'from_effective_at_example' # str (optional)
to_effective_at = 'to_effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_portfolio_aggregated_returns(scope, code, aggregated_returns_request, from_effective_at=from_effective_at, to_effective_at=to_effective_at, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Portfolio. | [required] 
 **code** | **str**| The code of the  Portfolio. | [required] 
 **aggregated_returns_request** | [**AggregatedReturnsRequest**](AggregatedReturnsRequest.md)| The request used in the AggregatedReturns. | [required] 
 **from_effective_at** | **str**| The start date from which to calculate the Returns. | [optional] 
 **to_effective_at** | **str**| The end date for which to calculate the Returns. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Returns. Defaults to the latest. | [optional] 

### Return type

[**AggregatedReturnsResponse**](AggregatedReturnsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The aggregated returns grouped by return stream. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_portfolio_commands**
> ResourceListOfProcessedCommand getPortfolioCommands = get_portfolio_commands(scope, code, from_as_at=from_as_at, to_as_at=to_as_at, filter=filter, page=page, limit=limit)

GetPortfolioCommands: Get portfolio commands

Get all the commands that modified a particular portfolio, including any input transactions.

### Example

```python
api_instance = api_client_factory.build(PortfoliosApi)
scope = 'scope_example' # str
code = 'code_example' # str
from_as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
to_as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
filter = 'filter_example' # str (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
api_response = api_instance.get_portfolio_commands(scope, code, from_as_at=from_as_at, to_as_at=to_as_at, filter=filter, page=page, limit=limit)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | [required] 
 **code** | **str**| The code of the portfolio. Together with the scope this uniquely identifies the portfolio. | [required] 
 **from_as_at** | **datetime**| The lower bound asAt datetime (inclusive) from which to retrieve commands. There is no lower bound if this is not specified. | [optional] 
 **to_as_at** | **datetime**| The upper bound asAt datetime (inclusive) from which to retrieve commands. There is no upper bound if this is not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the User ID, specify \&quot;userId.id eq &#39;string&#39;\&quot;.              For more information about filtering, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **page** | **str**| The pagination token to use to continue listing commands; this value is returned from the previous call. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 500 if not specified. | [optional] 

### Return type

[**ResourceListOfProcessedCommand**](ResourceListOfProcessedCommand.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The commands that modified the specified portfolio. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_portfolio_metadata**
> Dict[str, List[AccessMetadataValue]] getPortfolioMetadata = get_portfolio_metadata(scope, code, effective_at=effective_at, as_at=as_at)

GetPortfolioMetadata: Get access metadata rules for a portfolio

Pass the scope and portfolio code parameters to retrieve the AccessMetadata associated with a portfolio

### Example

```python
api_instance = api_client_factory.build(PortfoliosApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_portfolio_metadata(scope, code, effective_at=effective_at, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Portfolio Access Metadata Rule to retrieve. | [required] 
 **code** | **str**| Portfolio code | [required] 
 **effective_at** | **str**| The effectiveAt datetime at which to retrieve the access metadata rule. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the portfolio access metadata. | [optional] 

### Return type

**Dict[str, List[AccessMetadataValue]]**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The filtered list of results |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_portfolio_properties**
> PortfolioProperties getPortfolioProperties = get_portfolio_properties(scope, code, effective_at=effective_at, as_at=as_at)

GetPortfolioProperties: Get portfolio properties

List all the properties of a particular portfolio.

### Example

```python
api_instance = api_client_factory.build(PortfoliosApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_portfolio_properties(scope, code, effective_at=effective_at, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | [required] 
 **code** | **str**| The code of the portfolio. Together with the scope this uniquely identifies the portfolio. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to list the portfolio&#39;s properties. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the portfolio&#39;s properties. Defaults to returning the latest version of each property if not specified. | [optional] 

### Return type

[**PortfolioProperties**](PortfolioProperties.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The properties of the specified portfolio |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_portfolio_property_time_series**
> ResourceListOfPropertyInterval getPortfolioPropertyTimeSeries = get_portfolio_property_time_series(scope, code, property_key, portfolio_effective_at=portfolio_effective_at, as_at=as_at, filter=filter, page=page, limit=limit)

GetPortfolioPropertyTimeSeries: Get portfolio property time series

Show the complete time series (history) for a particular portfolio property.

### Example

```python
api_instance = api_client_factory.build(PortfoliosApi)
scope = 'scope_example' # str
code = 'code_example' # str
property_key = 'property_key_example' # str
portfolio_effective_at = 'portfolio_effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
filter = 'filter_example' # str (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
api_response = api_instance.get_portfolio_property_time_series(scope, code, property_key, portfolio_effective_at=portfolio_effective_at, as_at=as_at, filter=filter, page=page, limit=limit)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | [required] 
 **code** | **str**| The code of the portfolio. Together with the scope this uniquely identifies the portfolio. | [required] 
 **property_key** | **str**| The property key of the property whose history to show.              This must be from the &#39;Portfolio&#39; domain and in the format {domain}/{scope}/{code}, for example &#39;Portfolio/Manager/Id&#39;. | [required] 
 **portfolio_effective_at** | **str**| The effective datetime used to resolve the portfolio. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to show the history. Defaults to returning the current datetime if not supplied. | [optional] 
 **filter** | **str**| Expression to filter the results. For more information about filtering,              see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **page** | **str**| The pagination token to use to continue listing properties; this value is returned from              the previous call. If a pagination token is provided, the filter, portfolioEffectiveAt, and asAt fields              must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. | [optional] 

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

# **get_portfolio_relations**
> ResourceListOfRelation getPortfolioRelations = get_portfolio_relations(scope, code, effective_at=effective_at, as_at=as_at, filter=filter, identifier_types=identifier_types)

[EXPERIMENTAL] GetPortfolioRelations: Get portfolio relations

Get relations for a particular portfolio.

### Example

```python
api_instance = api_client_factory.build(PortfoliosApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
filter = 'filter_example' # str (optional)
identifier_types = ['identifier_types_example'] # List[str] (optional)
api_response = api_instance.get_portfolio_relations(scope, code, effective_at=effective_at, as_at=as_at, filter=filter, identifier_types=identifier_types)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | [required] 
 **code** | **str**| The code of the portfolio. Together with the scope this uniquely identifies the portfolio. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve relations. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve relations. Defaults to returning the latest LUSID AsAt time if not specified. | [optional] 
 **filter** | **str**| Expression to filter the relations. Provide a null or empty string for this field until further notice. | [optional] 
 **identifier_types** | [**List[str]**](str.md)| Identifier types (as property keys) used for referencing Persons or Legal Entities.              These must be from the &#39;Person&#39; or &#39;LegalEntity&#39; domains and have the format {domain}/{scope}/{code}, for example              &#39;Person/CompanyDetails/Role&#39;. Only identifier types provided will be used to look up relevant entities in relations. If not applicable, provide an empty array. | [optional] 

### Return type

[**ResourceListOfRelation**](ResourceListOfRelation.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The relations for the specified portfolio. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_portfolio_relationships**
> ResourceListOfRelationship getPortfolioRelationships = get_portfolio_relationships(scope, code, effective_at=effective_at, as_at=as_at, filter=filter, identifier_types=identifier_types)

GetPortfolioRelationships: Get portfolio relationships

Get relationships for a particular portfolio.

### Example

```python
api_instance = api_client_factory.build(PortfoliosApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
filter = 'filter_example' # str (optional)
identifier_types = ['identifier_types_example'] # List[str] (optional)
api_response = api_instance.get_portfolio_relationships(scope, code, effective_at=effective_at, as_at=as_at, filter=filter, identifier_types=identifier_types)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | [required] 
 **code** | **str**| The code of the portfolio. Together with the scope this uniquely identifies the portfolio. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve relationships. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve relationships. Defaults to returning the latest LUSID AsAt time if not specified. | [optional] 
 **filter** | **str**| Expression to filter the relationships. Provide a null or empty string for this field until further notice. | [optional] 
 **identifier_types** | [**List[str]**](str.md)| Identifier types (as property keys) used for referencing Persons or Legal Entities.              These can be specified from the &#39;Person&#39; or &#39;LegalEntity&#39; domains and have the format {domain}/{scope}/{code}, for example              &#39;Person/CompanyDetails/Role&#39;. An Empty array may be used to return all related Entities. | [optional] 

### Return type

[**ResourceListOfRelationship**](ResourceListOfRelationship.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The relationships for the specified portfolio. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_portfolio_returns**
> ResourceListOfPerformanceReturn getPortfolioReturns = get_portfolio_returns(scope, code, return_scope, return_code, from_effective_at=from_effective_at, to_effective_at=to_effective_at, period=period, as_at=as_at)

GetPortfolioReturns: Get Returns

Get Returns which are on the specified portfolio.

### Example

```python
api_instance = api_client_factory.build(PortfoliosApi)
scope = 'scope_example' # str
code = 'code_example' # str
return_scope = 'return_scope_example' # str
return_code = 'return_code_example' # str
from_effective_at = 'from_effective_at_example' # str (optional)
to_effective_at = 'to_effective_at_example' # str (optional)
period = 'period_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_portfolio_returns(scope, code, return_scope, return_code, from_effective_at=from_effective_at, to_effective_at=to_effective_at, period=period, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Portfolio. | [required] 
 **code** | **str**| The code of the  Portfolio. | [required] 
 **return_scope** | **str**| The scope of the Returns. | [required] 
 **return_code** | **str**| The code of the Returns. | [required] 
 **from_effective_at** | **str**| The start date from which to get the Returns. | [optional] 
 **to_effective_at** | **str**| The end date from which to get the Returns. | [optional] 
 **period** | **str**| Show the Returns on a Daily or Monthly period. Defaults to Daily. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Returns. Defaults to the latest. | [optional] 

### Return type

[**ResourceListOfPerformanceReturn**](ResourceListOfPerformanceReturn.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Returns on the given time period. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_portfolios_access_metadata_by_key**
> List[AccessMetadataValue] getPortfoliosAccessMetadataByKey = get_portfolios_access_metadata_by_key(scope, code, metadata_key, effective_at=effective_at, as_at=as_at)

[EARLY ACCESS] GetPortfoliosAccessMetadataByKey: Get an entry identified by a metadataKey in the access metadata object

Get a specific portfolio access metadata rule by specifying the corresponding identifier parts                No matching will be performed through this endpoint. To retrieve a rule, it is necessary to specify, exactly, the identifier of the rule

### Example

```python
api_instance = api_client_factory.build(PortfoliosApi)
scope = 'scope_example' # str
code = 'code_example' # str
metadata_key = 'metadata_key_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_portfolios_access_metadata_by_key(scope, code, metadata_key, effective_at=effective_at, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Portfolio Access Metadata Rule to retrieve. | [required] 
 **code** | **str**| The code of the portfolio | [required] 
 **metadata_key** | **str**| Key of the metadata to retrieve | [required] 
 **effective_at** | **str**| The effective date of the rule | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the portfolio access metadata. | [optional] 

### Return type

[**List[AccessMetadataValue]**](AccessMetadataValue.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved Portfolio Access Metadata Rule or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_instrument_event_instructions**
> PagedResourceListOfInstrumentEventInstruction listInstrumentEventInstructions = list_instrument_event_instructions(scope, code, portfolio_effective_at=portfolio_effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, timeline_scope=timeline_scope, timeline_code=timeline_code, closed_period_id=closed_period_id)

[EARLY ACCESS] ListInstrumentEventInstructions: List Instrument Event Instructions

Lists all instructions for a particular portfolio

### Example

```python
api_instance = api_client_factory.build(PortfoliosApi)
scope = 'scope_example' # str
code = 'code_example' # str
portfolio_effective_at = 'portfolio_effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
timeline_scope = 'timeline_scope_example' # str (optional)
timeline_code = 'timeline_code_example' # str (optional)
closed_period_id = 'closed_period_id_example' # str (optional)
api_response = api_instance.list_instrument_event_instructions(scope, code, portfolio_effective_at=portfolio_effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, timeline_scope=timeline_scope, timeline_code=timeline_code, closed_period_id=closed_period_id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | [required] 
 **code** | **str**| The code of the portfolio. Together with the scope this uniquely identifies the portfolio. | [required] 
 **portfolio_effective_at** | **str**| The effective date at which the portfolio will be resolved. Defaults to current time if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the instructions. Defaults to latest if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing instructions; this value is returned from the previous call.              If a pagination token is provided, the filter, effectiveAt and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **timeline_scope** | **str**| The scope of the Timeline, used to override the AsAt, and fetch post close activity data.              If this is provided, timelineCode must also be provided. | [optional] 
 **timeline_code** | **str**| The code of the Timeline, used to override the AsAt, and fetch post close activity data.              If this is provided, timelineScope must also be provided. | [optional] 
 **closed_period_id** | **str**| The code of the ClosedPeriod attached to the timeline, used to override the AsAt, and fetch post close activity data.              If this field is left empty and the timelineScope and timelineCode fields are filled out, the portfolioEffectiveAt will be used to resolve the relevant closed period. | [optional] 

### Return type

[**PagedResourceListOfInstrumentEventInstruction**](PagedResourceListOfInstrumentEventInstruction.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested instrument event instructions |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_portfolio_properties**
> ResourceListOfProperty listPortfolioProperties = list_portfolio_properties(scope, code, effective_at=effective_at, as_at=as_at, page=page, limit=limit)

[EARLY ACCESS] ListPortfolioProperties: Get portfolio properties

List all the properties of a particular portfolio.

### Example

```python
api_instance = api_client_factory.build(PortfoliosApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
api_response = api_instance.list_portfolio_properties(scope, code, effective_at=effective_at, as_at=as_at, page=page, limit=limit)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | [required] 
 **code** | **str**| The code of the portfolio. Together with the scope this uniquely identifies the portfolio. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to list the portfolio&#39;s properties. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the portfolio&#39;s properties. Defaults to returning the latest version of each property if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing commands; this value is returned from the previous call. | [optional] 
 **limit** | **int**| When paginating, limit the results per page to this number. | [optional] 

### Return type

[**ResourceListOfProperty**](ResourceListOfProperty.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The properties of the specified portfolio |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_portfolios**
> ResourceListOfPortfolio listPortfolios = list_portfolios(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, query=query, property_keys=property_keys, relationship_definition_ids=relationship_definition_ids)

ListPortfolios: List portfolios

List all the portfolios matching particular criteria.

### Example

```python
api_instance = api_client_factory.build(PortfoliosApi)
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
query = 'query_example' # str (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
relationship_definition_ids = ['relationship_definition_ids_example'] # List[str] (optional)
api_response = api_instance.list_portfolios(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, query=query, property_keys=property_keys, relationship_definition_ids=relationship_definition_ids)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effective datetime or cut label at which to list the portfolios. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the portfolios. Defaults to returning the latest version              of each portfolio if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing portfolios; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the transaction type, specify \&quot;type eq &#39;Transaction&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **query** | **str**| Expression specifying the criteria that the returned portfolios must meet. For example, to see which              portfolios have holdings in instruments with a LusidInstrumentId (LUID) of &#39;LUID_PPA8HI6M&#39; or a Figi of &#39;BBG000BLNNH6&#39;,              specify \&quot;instrument.identifiers in ((&#39;LusidInstrumentId&#39;, &#39;LUID_PPA8HI6M&#39;), (&#39;Figi&#39;, &#39;BBG000BLNNH6&#39;))\&quot;. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Portfolio&#39; domain to decorate onto each portfolio,              or from any domain that supports relationships to decorate onto related entities. These must take the              format {domain}/{scope}/{code}, for example &#39;Portfolio/Manager/Id&#39;. | [optional] 
 **relationship_definition_ids** | [**List[str]**](str.md)| A list of relationship definitions that are used to decorate related entities              onto the portfolios in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. | [optional] 

### Return type

[**ResourceListOfPortfolio**](ResourceListOfPortfolio.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested portfolios |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_portfolios_for_scope**
> ResourceListOfPortfolio listPortfoliosForScope = list_portfolios_for_scope(scope, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys, relationship_definition_ids=relationship_definition_ids)

ListPortfoliosForScope: List portfolios for scope

List all the portfolios in a particular scope.

### Example

```python
api_instance = api_client_factory.build(PortfoliosApi)
scope = 'scope_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
relationship_definition_ids = ['relationship_definition_ids_example'] # List[str] (optional)
api_response = api_instance.list_portfolios_for_scope(scope, effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys, relationship_definition_ids=relationship_definition_ids)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope whose portfolios to list. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to list the portfolios. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the portfolios. Defaults to returning the latest version              of each portfolio if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing portfolios. This  value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt  and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to return only transactions with a transaction type of &#39;Buy&#39;, specify \&quot;type eq &#39;Buy&#39;\&quot;.              For more information about filtering results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Portfolio&#39; domain to decorate onto each portfolio,              or from any domain that supports relationships to decorate onto related entities. These must take the              format {domain}/{scope}/{code}, for example &#39;Portfolio/Manager/Id&#39;. | [optional] 
 **relationship_definition_ids** | [**List[str]**](str.md)| A list of relationship definitions that are used to decorate related entities              onto the portfolios in the response. These must take the form {relationshipDefinitionScope}/{relationshipDefinitionCode}. | [optional] 

### Return type

[**ResourceListOfPortfolio**](ResourceListOfPortfolio.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The portfolios in the specified scope |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **patch_portfolio**
> Portfolio patchPortfolio = patch_portfolio(scope, code, operation)

PatchPortfolio: Patch portfolio.

Create or update certain fields for a particular  portfolio.  The behaviour is defined by the JSON Patch specification.    Currently supported fields are: Created, InstrumentScopes, Type.

### Example

```python
api_instance = api_client_factory.build(PortfoliosApi)
scope = 'scope_example' # str
code = 'code_example' # str
operation = [{"value":"2020-01-01","path":"/creationDate","op":"add"}] # List[Operation]
api_response = api_instance.patch_portfolio(scope, code, operation)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | [required] 
 **code** | **str**| The code of the portfolio. Together with the              scope this uniquely identifies the portfolio. | [required] 
 **operation** | [**List[Operation]**](Operation.md)| The json patch document. For more check: https://datatracker.ietf.org/doc/html/rfc6902. | [required] 

### Return type

[**Portfolio**](Portfolio.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The newly patched portfolio |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **patch_portfolio_access_metadata**
> Dict[str, List[AccessMetadataValue]] patchPortfolioAccessMetadata = patch_portfolio_access_metadata(scope, code, access_metadata_operation, effective_at=effective_at, effective_until=effective_until)

[EARLY ACCESS] PatchPortfolioAccessMetadata: Patch Access Metadata rules for a Portfolio.

Patch Portfolio Access Metadata Rules in a single scope.  The behaviour is defined by the JSON Patch specification.                Currently only 'add' is a supported operation on the patch document.    Currently only valid metadata keys are supported paths on the patch document.    The response will return any affected Portfolio Access Metadata rules or a failure message if unsuccessful.    It is important to always check to verify success (or failure).                Multiple rules for a metadataKey can exist with different effective at dates, when resources are accessed the rule that is active for the current time will be fetched.

### Example

```python
api_instance = api_client_factory.build(PortfoliosApi)
scope = 'scope_example' # str
code = 'code_example' # str
access_metadata_operation = [{"value":[{"value":"SilverLicence","provider":"TestDataProvider"}],"path":"/exampleMetadataKey","op":"add"}] # List[AccessMetadataOperation]
effective_at = 'effective_at_example' # str (optional)
effective_until = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.patch_portfolio_access_metadata(scope, code, access_metadata_operation, effective_at=effective_at, effective_until=effective_until)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Portfolio Access Metadata Rule. | [required] 
 **code** | **str**| Portfolio code | [required] 
 **access_metadata_operation** | [**List[AccessMetadataOperation]**](AccessMetadataOperation.md)| The Json Patch document | [required] 
 **effective_at** | **str**| The date this rule will effective from | [optional] 
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

# **update_portfolio**
> Portfolio updatePortfolio = update_portfolio(scope, code, update_portfolio_request, effective_at=effective_at)

UpdatePortfolio: Update portfolio

Update the definition of a particular portfolio.                Note that not all elements of a portfolio definition are  modifiable due to the potential implications for data already stored.

### Example

```python
api_instance = api_client_factory.build(PortfoliosApi)
scope = 'scope_example' # str
code = 'code_example' # str
update_portfolio_request = UpdatePortfolioRequest()
effective_at = 'effective_at_example' # str (optional)
api_response = api_instance.update_portfolio(scope, code, update_portfolio_request, effective_at=effective_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | [required] 
 **code** | **str**| The code of the portfolio. Together with the scope this uniquely identifies the portfolio. | [required] 
 **update_portfolio_request** | [**UpdatePortfolioRequest**](UpdatePortfolioRequest.md)| The updated portfolio definition. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to update the definition. Defaults to the current               LUSID system datetime if not specified. | [optional] 

### Return type

[**Portfolio**](Portfolio.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated definition of the portfolio |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_instrument_event_instructions**
> InstrumentEventInstructionsResponse upsertInstrumentEventInstructions = upsert_instrument_event_instructions(scope, code, success_mode, request_body, portfolio_effective_at=portfolio_effective_at)

[EARLY ACCESS] UpsertInstrumentEventInstructions: Upsert Instrument Event Instructions

Batch upsert for instrument event instructions, for the portfolio or individual holdings

### Example

```python
api_instance = api_client_factory.build(PortfoliosApi)
scope = 'scope_example' # str
code = 'code_example' # str
success_mode = 'Partial' # str
request_body = {"request":{"instrumentEventInstructionId":"ExampleInstructionId","instrumentEventId":"ExampleInstrumentEventId","instructionType":"ElectForHolding","electionKey":"GBP","holdingId":123456789,"entitlementDateInstructed":"2020-01-01T12:00:00.0000000+00:00","ignoreCostImpact":false}} # Dict[str, InstrumentEventInstructionRequest]
portfolio_effective_at = 'portfolio_effective_at_example' # str (optional)
api_response = api_instance.upsert_instrument_event_instructions(scope, code, success_mode, request_body, portfolio_effective_at=portfolio_effective_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | [required] 
 **code** | **str**| The code of the portfolio. Together with the scope this uniquely identifies the portfolio. | [required] 
 **success_mode** | **str**| Whether the batch request should fail atomically or in a partial fashion - allowed values: Atomic, Partial (default) | [required] [default to &#39;Partial&#39;]
 **request_body** | [**Dict[str, InstrumentEventInstructionRequest]**](InstrumentEventInstructionRequest.md)| The instructions to be upserted to the portfolio. | [required] 
 **portfolio_effective_at** | **str**| The effective date at which the portfolio will be resolved. Defaults to current time if not specified. | [optional] 

### Return type

[**InstrumentEventInstructionsResponse**](InstrumentEventInstructionsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The newly inserted or updated instrument event instructions |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_portfolio_access_metadata**
> ResourceListOfAccessMetadataValueOf upsertPortfolioAccessMetadata = upsert_portfolio_access_metadata(scope, code, metadata_key, upsert_portfolio_access_metadata_request, effective_at=effective_at, effective_until=effective_until)

UpsertPortfolioAccessMetadata: Upsert a Portfolio Access Metadata Rule associated with specific metadataKey. This creates or updates the data in LUSID.

Update or insert one Portfolio Access Metadata Rule in a single scope. An item will be updated if it already exists  and inserted if it does not.    The response will return the successfully updated or inserted Portfolio Access Metadata Rule or failure message if unsuccessful    It is important to always check to verify success (or failure).                Multiple rules for a metadataKey can exists with different effective at dates, when resources are accessed the rule that is active for the current time will be fetched

### Example

```python
api_instance = api_client_factory.build(PortfoliosApi)
scope = 'scope_example' # str
code = 'code_example' # str
metadata_key = 'metadata_key_example' # str
upsert_portfolio_access_metadata_request = UpsertPortfolioAccessMetadataRequest()
effective_at = 'effective_at_example' # str (optional)
effective_until = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.upsert_portfolio_access_metadata(scope, code, metadata_key, upsert_portfolio_access_metadata_request, effective_at=effective_at, effective_until=effective_until)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to use when updating or inserting the Portfolio Access Metadata Rule. | [required] 
 **code** | **str**| Portfolio code | [required] 
 **metadata_key** | **str**| Key of the access metadata to upsert | [required] 
 **upsert_portfolio_access_metadata_request** | [**UpsertPortfolioAccessMetadataRequest**](UpsertPortfolioAccessMetadataRequest.md)| The Portfolio Access Metadata Rule to update or insert | [required] 
 **effective_at** | **str**| The date this rule will effective from | [optional] 
 **effective_until** | **datetime**| The effective date until which the Access Metadata is valid. If not supplied this will be valid indefinitely, or until the next &#39;effectiveAt&#39; date of the Access Metadata | [optional] 

### Return type

[**ResourceListOfAccessMetadataValueOf**](ResourceListOfAccessMetadataValueOf.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully updated or inserted item or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_portfolio_properties**
> PortfolioProperties upsertPortfolioProperties = upsert_portfolio_properties(scope, code, request_body)

UpsertPortfolioProperties: Upsert portfolio properties

Create or update one or more properties for a particular portfolio. A property is updated if it  already exists and created if it does not. All properties must be from the 'Portfolio' domain.                Properties have an <i>effectiveFrom</i> datetime from which the property is valid, and an <i>effectiveUntil</i>  datetime until which it is valid. Not supplying an <i>effectiveUntil</i> datetime results in the property being  valid indefinitely, or until the next <i>effectiveFrom</i> datetime of the property.

### Example

```python
api_instance = api_client_factory.build(PortfoliosApi)
scope = 'scope_example' # str
code = 'code_example' # str
request_body = {"Portfolio/MyScope/FundManagerName":{"key":"Portfolio/MyScope/FundManagerName","value":{"labelValue":"Smith"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00"},"Portfolio/MyScope/SomeProperty":{"key":"Portfolio/MyScope/SomeProperty","value":{"labelValue":"SomeValue"},"effectiveFrom":"2016-01-01T00:00:00.0000000+00:00"},"Portfolio/MyScope/AnotherProperty":{"key":"Portfolio/MyScope/AnotherProperty","value":{"labelValue":"AnotherValue"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00","effectiveUntil":"2020-01-01T00:00:00.0000000+00:00"},"Portfolio/MyScope/ReBalanceInterval":{"key":"Portfolio/MyScope/ReBalanceInterval","value":{"metricValue":{"value":30.0,"unit":"Days"}}}} # Dict[str, ModelProperty]
api_response = api_instance.upsert_portfolio_properties(scope, code, request_body)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | [required] 
 **code** | **str**| The code of the portfolio. Together with the scope this uniquely identifies the portfolio. | [required] 
 **request_body** | [**Dict[str, ModelProperty]**](ModelProperty.md)| The properties to be created or updated. Each property in               the request must be keyed by its unique property key. This has the format {domain}/{scope}/{code}, for example               &#39;Portfolio/Manager/Id&#39;. | [required] 

### Return type

[**PortfolioProperties**](PortfolioProperties.md)

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

# **upsert_portfolio_returns**
> UpsertReturnsResponse upsertPortfolioReturns = upsert_portfolio_returns(scope, code, return_scope, return_code, performance_return)

UpsertPortfolioReturns: Upsert Returns

Update or insert returns into the specified portfolio.

### Example

```python
api_instance = api_client_factory.build(PortfoliosApi)
scope = 'scope_example' # str
code = 'code_example' # str
return_scope = 'return_scope_example' # str
return_code = 'return_code_example' # str
performance_return = [{"effectiveAt":"2019-11-28T00:00:00.0000000+00:00","rateOfReturn":0.1,"openingMarketValue":500.0,"closingMarketValue":550.0,"period":"Daily"},{"effectiveAt":"2019-11-29T00:00:00.0000000+00:00","rateOfReturn":-0.2,"openingMarketValue":550.0,"closingMarketValue":440.0,"period":"Daily"}] # List[PerformanceReturn]
api_response = api_instance.upsert_portfolio_returns(scope, code, return_scope, return_code, performance_return)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Portfolio. | [required] 
 **code** | **str**| The code of the  Portfolio. | [required] 
 **return_scope** | **str**| The scope of the Returns. | [required] 
 **return_code** | **str**| The code of the Returns. | [required] 
 **performance_return** | [**List[PerformanceReturn]**](PerformanceReturn.md)| This contains the Returns which need to be upsert. | [required] 

### Return type

[**UpsertReturnsResponse**](UpsertReturnsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The version of the portfolio that contains the newly updated or inserted Returns. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

