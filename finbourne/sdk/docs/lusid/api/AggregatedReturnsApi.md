# lusid.AggregatedReturnsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_returns**](AggregatedReturnsApi.md#delete_returns) | **DELETE** /api/api/returns/{scope}/{code}/{entityType}/{entityScope}/{entityCode}/$delete | [EXPERIMENTAL] DeleteReturns: Delete Returns
[**delete_returns_entity**](AggregatedReturnsApi.md#delete_returns_entity) | **DELETE** /api/api/returns/{scope}/{code} | [EXPERIMENTAL] DeleteReturnsEntity: Delete returns entity.
[**get_aggregated_returns**](AggregatedReturnsApi.md#get_aggregated_returns) | **POST** /api/api/returns/$aggregated | [EXPERIMENTAL] GetAggregatedReturns: Calculate aggregated returns for an entity.
[**get_returns**](AggregatedReturnsApi.md#get_returns) | **GET** /api/api/returns/{scope}/{code}/{entityType}/{entityScope}/{entityCode} | [EXPERIMENTAL] GetReturns: Get Returns
[**get_returns_entity**](AggregatedReturnsApi.md#get_returns_entity) | **GET** /api/api/returns/{scope}/{code} | [EXPERIMENTAL] GetReturnsEntity: Get returns entity.
[**list_returns_entities**](AggregatedReturnsApi.md#list_returns_entities) | **GET** /api/api/returns | [EXPERIMENTAL] ListReturnsEntities: List returns entities.
[**upsert_returns**](AggregatedReturnsApi.md#upsert_returns) | **POST** /api/api/returns/{scope}/{code}/{entityType}/{entityScope}/{entityCode} | [EXPERIMENTAL] UpsertReturns: Upsert Returns
[**upsert_returns_entity**](AggregatedReturnsApi.md#upsert_returns_entity) | **POST** /api/api/returns | [EXPERIMENTAL] UpsertReturnsEntity: Upsert returns entity.


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.aggregated_returns_api import AggregatedReturnsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(AggregatedReturnsApi)
```

---

# **delete_returns**
> DeletedEntityResponse deleteReturns = delete_returns(scope, code, entity_type, entity_scope, entity_code, from_effective_at, to_effective_at, period=period)

[EXPERIMENTAL] DeleteReturns: Delete Returns

Cancel the Returns stored under the returns series against the specified entity inside the window.

### Example

```python
api_instance = api_client_factory.build(AggregatedReturnsApi)
scope = 'scope_example' # str
code = 'code_example' # str
entity_type = 'entity_type_example' # str
entity_scope = 'entity_scope_example' # str
entity_code = 'entity_code_example' # str
from_effective_at = 'from_effective_at_example' # str
to_effective_at = 'to_effective_at_example' # str
period = 'period_example' # str (optional)
api_response = api_instance.delete_returns(scope, code, entity_type, entity_scope, entity_code, from_effective_at, to_effective_at, period=period)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Returns. | [required] 
 **code** | **str**| The code of the Returns. | [required] 
 **entity_type** | **str**| The type of the entity the Returns are stored against: &#39;Portfolio&#39; or &#39;PortfolioGroup&#39;. Available values: Portfolio, PortfolioGroup. | [required] 
 **entity_scope** | **str**| The scope of the entity. | [required] 
 **entity_code** | **str**| The code of the entity. | [required] 
 **from_effective_at** | **str**| The start date from which to delete the Returns. | [required] 
 **to_effective_at** | **str**| The end date from which to delete the Returns. | [required] 
 **period** | **str**| The period of the Returns to be deleted. Default value: Daily. Available values: Daily, Monthly. | [optional] 

### Return type

[**DeletedEntityResponse**](../model/DeletedEntityResponse.md)

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

# **delete_returns_entity**
> DeletedEntityResponse deleteReturnsEntity = delete_returns_entity(scope, code)

[EXPERIMENTAL] DeleteReturnsEntity: Delete returns entity.

Delete returns entity.

### Example

```python
api_instance = api_client_factory.build(AggregatedReturnsApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.delete_returns_entity(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Returns entity scope. | [required] 
 **code** | **str**| Returns entity code. | [required] 

### Return type

[**DeletedEntityResponse**](../model/DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The time that the returns entity was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_aggregated_returns**
> AggregatedReturnsResponse getAggregatedReturns = get_aggregated_returns(aggregated_returns_entity_request)

[EXPERIMENTAL] GetAggregatedReturns: Calculate aggregated returns for an entity.

Report daily returns for the entity specified in the request body over the effective window.              Supports a Portfolio, or a PortfolioGroup whose members' returns are rolled up in their common base              currency, on a daily return grid. Returns upserted to the Returns store under the supplied returns id              take precedence: if any exist in the window for a portfolio they are reported as-is and nothing is              calculated for it. A group member's upserted returns are weighted by their stored (net) opening market              value and contribute only on the days they cover; a day with no upserted return for that member is              reported from the other members alone. Otherwise time-weighted returns are calculated using the              recipe, fee handling and flow-discrepancy handling of the persisted Returns entity identified by the              returns id, and the request fails if no such entity exists. A calculated day's return is the day's              profit and loss over the portfolio's net opening value, cash included and signed, so a portfolio              financed by overdraft reports a return on its negative capital; a portfolio whose net opening value is              zero and that takes in no capital during the day reports a zero return, with the day's gain or loss              visible in its market values. When a reporting currency is requested the Returns entity is also              required, as its recipe supplies the FX rates.

### Example

```python
api_instance = api_client_factory.build(AggregatedReturnsApi)
aggregated_returns_entity_request = AggregatedReturnsEntityRequest()
api_response = api_instance.get_aggregated_returns(aggregated_returns_entity_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aggregated_returns_entity_request** | [**AggregatedReturnsEntityRequest**](../model/AggregatedReturnsEntityRequest.md)| The entity to report returns for, the returns id under which upserted returns              are stored and the Returns entity that configures a calculation, the effective window and the metrics              to report. | [required] 

### Return type

[**AggregatedReturnsResponse**](../model/AggregatedReturnsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The aggregated returns grouped by entity. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_returns**
> ResourceListOfPerformanceReturn getReturns = get_returns(scope, code, entity_type, entity_scope, entity_code, from_effective_at=from_effective_at, to_effective_at=to_effective_at, period=period, as_at=as_at)

[EXPERIMENTAL] GetReturns: Get Returns

Get the Returns stored under the returns series against the specified entity.

### Example

```python
api_instance = api_client_factory.build(AggregatedReturnsApi)
scope = 'scope_example' # str
code = 'code_example' # str
entity_type = 'entity_type_example' # str
entity_scope = 'entity_scope_example' # str
entity_code = 'entity_code_example' # str
from_effective_at = 'from_effective_at_example' # str (optional)
to_effective_at = 'to_effective_at_example' # str (optional)
period = 'period_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_returns(scope, code, entity_type, entity_scope, entity_code, from_effective_at=from_effective_at, to_effective_at=to_effective_at, period=period, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Returns. | [required] 
 **code** | **str**| The code of the Returns. | [required] 
 **entity_type** | **str**| The type of the entity the Returns are stored against: &#39;Portfolio&#39; or &#39;PortfolioGroup&#39;. Available values: Portfolio, PortfolioGroup. | [required] 
 **entity_scope** | **str**| The scope of the entity. | [required] 
 **entity_code** | **str**| The code of the entity. | [required] 
 **from_effective_at** | **str**| The start date from which to get the Returns. | [optional] 
 **to_effective_at** | **str**| The end date from which to get the Returns. | [optional] 
 **period** | **str**| The period for which to show the Returns. Default value: Daily. Available values: Daily, Monthly. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Returns. Defaults to the latest. | [optional] 

### Return type

[**ResourceListOfPerformanceReturn**](../model/ResourceListOfPerformanceReturn.md)

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

# **get_returns_entity**
> ReturnsEntity getReturnsEntity = get_returns_entity(scope, code, as_at=as_at)

[EXPERIMENTAL] GetReturnsEntity: Get returns entity.

Get returns entity.

### Example

```python
api_instance = api_client_factory.build(AggregatedReturnsApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_returns_entity(scope, code, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Returns entity scope. | [required] 
 **code** | **str**| Returns entity code. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the returns entity. Defaults to return              the latest version of the definition if not specified. | [optional] 

### Return type

[**ReturnsEntity**](../model/ReturnsEntity.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested returns entity |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_returns_entities**
> ResourceListOfReturnsEntity listReturnsEntities = list_returns_entities(as_at=as_at)

[EXPERIMENTAL] ListReturnsEntities: List returns entities.

List returns entities.

### Example

```python
api_instance = api_client_factory.build(AggregatedReturnsApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.list_returns_entities(as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to retrieve the relation definitions. Defaults to return              the latest version of each definition if not specified. | [optional] 

### Return type

[**ResourceListOfReturnsEntity**](../model/ResourceListOfReturnsEntity.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested returns entities |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_returns**
> UpsertReturnsResponse upsertReturns = upsert_returns(scope, code, entity_type, entity_scope, entity_code, performance_return)

[EXPERIMENTAL] UpsertReturns: Upsert Returns

Update or insert returns stored under the returns series against the specified entity. Stored              returns take precedence over a calculation in the aggregated returns of that entity.

### Example

```python
api_instance = api_client_factory.build(AggregatedReturnsApi)
scope = 'scope_example' # str
code = 'code_example' # str
entity_type = 'entity_type_example' # str
entity_scope = 'entity_scope_example' # str
entity_code = 'entity_code_example' # str
performance_return = [{"effectiveAt":"2019-11-28T00:00:00.0000000+00:00","rateOfReturn":0.1,"openingMarketValue":500.0,"closingMarketValue":550.0,"period":"Daily"},{"effectiveAt":"2019-11-29T00:00:00.0000000+00:00","rateOfReturn":-0.2,"openingMarketValue":550.0,"closingMarketValue":440.0,"period":"Daily"}] # List[PerformanceReturn]
api_response = api_instance.upsert_returns(scope, code, entity_type, entity_scope, entity_code, performance_return)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Returns. | [required] 
 **code** | **str**| The code of the Returns. | [required] 
 **entity_type** | **str**| The type of the entity the Returns are stored against: &#39;Portfolio&#39; or &#39;PortfolioGroup&#39;. Available values: Portfolio, PortfolioGroup. | [required] 
 **entity_scope** | **str**| The scope of the entity. | [required] 
 **entity_code** | **str**| The code of the entity. | [required] 
 **performance_return** | [**List[PerformanceReturn]**](../model/PerformanceReturn.md)| This contains the Returns which need to be upsert. | [required] 

### Return type

[**UpsertReturnsResponse**](../model/UpsertReturnsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The version of the entity that contains the newly updated or inserted Returns. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_returns_entity**
> ReturnsEntity upsertReturnsEntity = upsert_returns_entity(returns_entity)

[EXPERIMENTAL] UpsertReturnsEntity: Upsert returns entity.

Upsert returns entity.

### Example

```python
api_instance = api_client_factory.build(AggregatedReturnsApi)
returns_entity = ReturnsEntity()
api_response = api_instance.upsert_returns_entity(returns_entity)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **returns_entity** | [**ReturnsEntity**](../model/ReturnsEntity.md)| Definition of the returns entity. | [required] 

### Return type

[**ReturnsEntity**](../model/ReturnsEntity.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The upserted returns entity |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

