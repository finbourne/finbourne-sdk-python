# lusid.InstrumentEventsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_applicable_instrument_events**](InstrumentEventsApi.md#query_applicable_instrument_events) | **POST** /api/api/instrumentevents/$queryApplicableInstrumentEvents | QueryApplicableInstrumentEvents: Returns a list of applicable instrument events based on the holdings of the portfolios and date range specified in the query.
[**query_bucketed_cash_flows**](InstrumentEventsApi.md#query_bucketed_cash_flows) | **POST** /api/api/instrumentevents/$queryBucketedCashFlows | QueryBucketedCashFlows: Returns bucketed cashflows based on the holdings of the portfolios and date range specified in the query.
[**query_cash_flows**](InstrumentEventsApi.md#query_cash_flows) | **POST** /api/api/instrumentevents/$queryCashFlows | QueryCashFlows: Returns a list of cashflows based on the holdings of the portfolios and date range specified in the query.
[**query_instrument_events**](InstrumentEventsApi.md#query_instrument_events) | **POST** /api/api/instrumentevents/$query | QueryInstrumentEvents: Returns a list of instrument events based on the holdings of the portfolios and date range specified in the query.
[**query_trade_tickets**](InstrumentEventsApi.md#query_trade_tickets) | **POST** /api/api/instrumentevents/$queryTradeTickets | QueryTradeTickets: Returns a list of trade tickets based on the holdings of the portfolios and date range specified in the query.


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.instrument_events_api import InstrumentEventsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(InstrumentEventsApi)
```

---

# **query_applicable_instrument_events**
> ResourceListOfApplicableInstrumentEvent queryApplicableInstrumentEvents = query_applicable_instrument_events(as_at=as_at, limit=limit, page=page, query_applicable_instrument_events_request=query_applicable_instrument_events_request)

QueryApplicableInstrumentEvents: Returns a list of applicable instrument events based on the holdings of the portfolios and date range specified in the query.

Returns a list of applicable instrument events based on the holdings of the portfolios and date range specified in the query.

### Example

```python
api_instance = api_client_factory.build(InstrumentEventsApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
limit = 100 # int (optional)
page = 'page_example' # str (optional)
query_applicable_instrument_events_request = QueryApplicableInstrumentEventsRequest()
api_response = api_instance.query_applicable_instrument_events(as_at=as_at, limit=limit, page=page, query_applicable_instrument_events_request=query_applicable_instrument_events_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The as at time to use. | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. If not specified, a default  of 100 is used. | [optional] [default to 100]
 **page** | **str**| Optional. The pagination token to use to continue listing items from a previous call. Page values are  return from list calls, and must be supplied exactly as returned. Additionally, when specifying this | [optional] 
 **query_applicable_instrument_events_request** | [**QueryApplicableInstrumentEventsRequest**](QueryApplicableInstrumentEventsRequest.md)| The filter parameters used to retrieve applicable instrument events. | [optional] 

### Return type

[**ResourceListOfApplicableInstrumentEvent**](ResourceListOfApplicableInstrumentEvent.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Applicable Instrument Events |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **query_bucketed_cash_flows**
> BucketedCashFlowResponse queryBucketedCashFlows = query_bucketed_cash_flows(query_bucketed_cash_flows_request=query_bucketed_cash_flows_request)

QueryBucketedCashFlows: Returns bucketed cashflows based on the holdings of the portfolios and date range specified in the query.

Returns bucketed cashflows based on the holdings of the portfolios and date range specified in the query.

### Example

```python
api_instance = api_client_factory.build(InstrumentEventsApi)
query_bucketed_cash_flows_request = QueryBucketedCashFlowsRequest()
api_response = api_instance.query_bucketed_cash_flows(query_bucketed_cash_flows_request=query_bucketed_cash_flows_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_bucketed_cash_flows_request** | [**QueryBucketedCashFlowsRequest**](QueryBucketedCashFlowsRequest.md)| The Query Information. | [optional] 

### Return type

[**BucketedCashFlowResponse**](BucketedCashFlowResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Query bucketed cashflows across portfolios. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **query_cash_flows**
> ResourceListOfInstrumentCashFlow queryCashFlows = query_cash_flows(limit=limit, page=page, query_cash_flows_request=query_cash_flows_request)

QueryCashFlows: Returns a list of cashflows based on the holdings of the portfolios and date range specified in the query.

Returns a list of cashflows based on the holdings of the portfolios and date range specified in the query.

### Example

```python
api_instance = api_client_factory.build(InstrumentEventsApi)
limit = 1000 # int (optional)
page = 'page_example' # str (optional)
query_cash_flows_request = QueryCashFlowsRequest()
api_response = api_instance.query_cash_flows(limit=limit, page=page, query_cash_flows_request=query_cash_flows_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. If not specified, a default  of 1000 is used. | [optional] [default to 1000]
 **page** | **str**| Optional. The pagination token to use to continue listing items from a previous call. Page values are  return from list calls, and must be supplied exactly as returned. Additionally, when specifying this  value, queryBody, and limit must not  be modified. | [optional] 
 **query_cash_flows_request** | [**QueryCashFlowsRequest**](QueryCashFlowsRequest.md)| The filter parameters used to retrieve instrument events. | [optional] 

### Return type

[**ResourceListOfInstrumentCashFlow**](ResourceListOfInstrumentCashFlow.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Instrument Events as Cashflows. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **query_instrument_events**
> ResourceListOfInstrumentEventHolder queryInstrumentEvents = query_instrument_events(limit=limit, page=page, query_instrument_events_request=query_instrument_events_request)

QueryInstrumentEvents: Returns a list of instrument events based on the holdings of the portfolios and date range specified in the query.

Returns a list of instrument events based on the holdings of the portfolios and date range specified in the query.

### Example

```python
api_instance = api_client_factory.build(InstrumentEventsApi)
limit = 1000 # int (optional)
page = 'page_example' # str (optional)
query_instrument_events_request = QueryInstrumentEventsRequest()
api_response = api_instance.query_instrument_events(limit=limit, page=page, query_instrument_events_request=query_instrument_events_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. If not specified, a default  of 1000 is used. | [optional] [default to 1000]
 **page** | **str**| Optional. The pagination token to use to continue listing items from a previous call. Page values are  return from list calls, and must be supplied exactly as returned. Additionally, when specifying this  value, queryBody, and limit must not  be modified. | [optional] 
 **query_instrument_events_request** | [**QueryInstrumentEventsRequest**](QueryInstrumentEventsRequest.md)| The filter parameters used to retrieve instrument events. | [optional] 

### Return type

[**ResourceListOfInstrumentEventHolder**](ResourceListOfInstrumentEventHolder.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Instrument Events |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **query_trade_tickets**
> ResourceListOfPortfolioTradeTicket queryTradeTickets = query_trade_tickets(limit=limit, page=page, query_trade_tickets_request=query_trade_tickets_request)

QueryTradeTickets: Returns a list of trade tickets based on the holdings of the portfolios and date range specified in the query.

Returns a list of trade tickets based on the holdings of the portfolios and date range specified in the query.    These trade tickets are derived from events that involve transition of instrument states, such as transitions  on exercise or default of an instrument. The trade tickets are to allow the new position to be created given the  existing portfolio configuration.

### Example

```python
api_instance = api_client_factory.build(InstrumentEventsApi)
limit = 1000 # int (optional)
page = 'page_example' # str (optional)
query_trade_tickets_request = QueryTradeTicketsRequest()
api_response = api_instance.query_trade_tickets(limit=limit, page=page, query_trade_tickets_request=query_trade_tickets_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. If not specified, a default  of 1000 is used. | [optional] [default to 1000]
 **page** | **str**| Optional. The pagination token to use to continue listing items from a previous call. Page values are  return from list calls, and must be supplied exactly as returned. Additionally, when specifying this  value, queryBody, and limit must not  be modified. | [optional] 
 **query_trade_tickets_request** | [**QueryTradeTicketsRequest**](QueryTradeTicketsRequest.md)| The filter parameters used to retrieve instrument events. | [optional] 

### Return type

[**ResourceListOfPortfolioTradeTicket**](ResourceListOfPortfolioTradeTicket.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Instrument Events as Upsertable TradeTickets. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

