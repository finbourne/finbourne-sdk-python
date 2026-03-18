# lusid.QuotesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_quote_access_metadata_rule**](QuotesApi.md#delete_quote_access_metadata_rule) | **DELETE** /api/api/metadata/quotes/rules/{scope} | [EXPERIMENTAL] DeleteQuoteAccessMetadataRule: Delete a Quote Access Metadata Rule
[**delete_quotes**](QuotesApi.md#delete_quotes) | **POST** /api/api/quotes/{scope}/$delete | DeleteQuotes: Delete quotes
[**get_quotes**](QuotesApi.md#get_quotes) | **POST** /api/api/quotes/{scope}/$get | GetQuotes: Get quotes
[**get_quotes_access_metadata_rule**](QuotesApi.md#get_quotes_access_metadata_rule) | **GET** /api/api/metadata/quotes/rules | [EXPERIMENTAL] GetQuotesAccessMetadataRule: Get a quote access metadata rule
[**list_quotes**](QuotesApi.md#list_quotes) | **GET** /api/api/quotes/{scope}/$deprecated | [DEPRECATED] ListQuotes: List quotes
[**list_quotes_access_metadata_rules**](QuotesApi.md#list_quotes_access_metadata_rules) | **GET** /api/api/metadata/quotes/rules/{scope} | [EXPERIMENTAL] ListQuotesAccessMetadataRules: List all quote access metadata rules in a scope
[**list_quotes_for_scope**](QuotesApi.md#list_quotes_for_scope) | **GET** /api/api/quotes/{scope} | ListQuotesForScope: List quotes for scope
[**upsert_quote_access_metadata_rule**](QuotesApi.md#upsert_quote_access_metadata_rule) | **POST** /api/api/metadata/quotes/rules/{scope} | [EXPERIMENTAL] UpsertQuoteAccessMetadataRule: Upsert a Quote Access Metadata Rule. This creates or updates the data in LUSID.
[**upsert_quotes**](QuotesApi.md#upsert_quotes) | **POST** /api/api/quotes/{scope} | UpsertQuotes: Upsert quotes


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.quotes_api import QuotesApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(QuotesApi)
```

---

# **delete_quote_access_metadata_rule**
> QuoteAccessMetadataRule deleteQuoteAccessMetadataRule = delete_quote_access_metadata_rule(scope, provider=provider, price_source=price_source, instrument_id_type=instrument_id_type, instrument_id=instrument_id, quote_type=quote_type, var_field=var_field, effective_at=effective_at)

[EXPERIMENTAL] DeleteQuoteAccessMetadataRule: Delete a Quote Access Metadata Rule

Delete the Quote Access Metadata Rule that exactly matches the provided identifier parts

### Example

```python
api_instance = api_client_factory.build(QuotesApi)
scope = 'scope_example' # str
provider = 'provider_example' # str (optional)
price_source = 'price_source_example' # str (optional)
instrument_id_type = 'instrument_id_type_example' # str (optional)
instrument_id = 'instrument_id_example' # str (optional)
quote_type = 'quote_type_example' # str (optional)
var_field = 'var_field_example' # str (optional)
effective_at = 'effective_at_example' # str (optional)
api_response = api_instance.delete_quote_access_metadata_rule(scope, provider=provider, price_source=price_source, instrument_id_type=instrument_id_type, instrument_id=instrument_id, quote_type=quote_type, var_field=var_field, effective_at=effective_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Quote Access Metadata Rule to retrieve. | [required] 
 **provider** | **str**| The Provider of the rule | [optional] 
 **price_source** | **str**| The PriceSource of the rule | [optional] 
 **instrument_id_type** | **str**| The InstrumentIdType of the rule | [optional] 
 **instrument_id** | **str**| The InstrumentId of the rule | [optional] 
 **quote_type** | **str**| The QuoteType of the rule | [optional] 
 **var_field** | **str**| The Field of the rule | [optional] 
 **effective_at** | **str**| The effective date to delete at, if this is not supplied, it will delete all data found | [optional] 

### Return type

[**QuoteAccessMetadataRule**](QuoteAccessMetadataRule.md)

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

# **delete_quotes**
> AnnulQuotesResponse deleteQuotes = delete_quotes(scope, request_body=request_body)

DeleteQuotes: Delete quotes

Delete one or more specified quotes from a single scope. A quote is identified by its unique id which includes information about  the type of quote as well as the exact effective datetime (to the microsecond) from which it became valid.                In the request each quote must be keyed by a unique correlation id. This id is ephemeral and is not stored by LUSID.  It serves only as a way to easily identify each quote in the response.                The response will return both the collection of successfully deleted quotes, as well as those that failed.  For the failures a reason will be provided explaining why the quote could not be deleted.                It is important to always check the failed set for any unsuccessful results.

### Example

```python
api_instance = api_client_factory.build(QuotesApi)
scope = 'scope_example' # str
request_body = {"DS-VOD-PRICE-MID":{"quoteSeriesId":{"provider":"DataScope","priceSource":"","instrumentId":"GB00BH4HKS39","instrumentIdType":"Isin","quoteType":"Price","field":"mid"},"effectiveAt":"2018-03-05T00:00:00.0000000+00:00"}} # Dict[str, QuoteId] (optional)
api_response = api_instance.delete_quotes(scope, request_body=request_body)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the quotes to delete. | [required] 
 **request_body** | [**Dict[str, QuoteId]**](QuoteId.md)| The quotes to delete keyed by a unique correlation id. | [optional] 

### Return type

[**AnnulQuotesResponse**](AnnulQuotesResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully deleted quotes along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_quotes**
> GetQuotesResponse getQuotes = get_quotes(scope, effective_at=effective_at, as_at=as_at, max_age=max_age, request_body=request_body)

GetQuotes: Get quotes

Get one or more quotes from a single scope.                Each quote can be identified by its time invariant quote series id.                For each quote series id LUSID will return the most recent quote with respect to the provided (or default) effective datetime.                 An optional maximum age range window can be specified which defines how far back to look back for a quote from the specified effective datetime.  LUSID will return the most recent quote within this window.                In the request each quote series id must be keyed by a unique correlation id. This id is ephemeral and is not stored by LUSID.  It serves only as a way to easily identify each quote in the response.                The response will return three collections. One, the successfully retrieved quotes. Two, those that had a  valid quote series id but could not be found. Three, those that failed because LUSID could not construct a valid quote series id from the request.    For the quotes that failed or could not be found a reason will be provided explaining why the quote could not be retrieved.                It is important to always check the failed and not found sets for any unsuccessful results.  The maximum number of quotes that this method can get per request is 2,000.

### Example

```python
api_instance = api_client_factory.build(QuotesApi)
scope = 'scope_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
max_age = 'max_age_example' # str (optional)
request_body = {"DS-VOD-PRICE-MID":{"provider":"DataScope","priceSource":"","instrumentId":"GB00BH4HKS39","instrumentIdType":"Isin","quoteType":"Price","field":"mid"}} # Dict[str, QuoteSeriesId] (optional)
api_response = api_instance.get_quotes(scope, effective_at=effective_at, as_at=as_at, max_age=max_age, request_body=request_body)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the quotes to retrieve. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the quotes. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the quotes. Defaults to return the latest version of each quote if not specified. | [optional] 
 **max_age** | **str**| The duration of the look back window in an ISO8601 time interval format e.g. P1Y2M3DT4H30M (1 year, 2 months, 3 days, 4 hours and 30 minutes).               This is subtracted from the provided effectiveAt datetime or cut label to generate a effective datetime window inside which a quote must exist to be retrieved. | [optional] 
 **request_body** | [**Dict[str, QuoteSeriesId]**](QuoteSeriesId.md)| The time invariant quote series ids of the quotes to retrieve. These need to be               keyed by a unique correlation id allowing the retrieved quote to be identified in the response. | [optional] 

### Return type

[**GetQuotesResponse**](GetQuotesResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved quotes along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_quotes_access_metadata_rule**
> QuoteAccessMetadataRule getQuotesAccessMetadataRule = get_quotes_access_metadata_rule(scope, provider=provider, price_source=price_source, instrument_id_type=instrument_id_type, instrument_id=instrument_id, quote_type=quote_type, var_field=var_field, effective_at=effective_at, as_at=as_at)

[EXPERIMENTAL] GetQuotesAccessMetadataRule: Get a quote access metadata rule

Get a specific quote access metadata rule by specifying the corresponding identifier parts                No matching will be performed through this endpoint. To retrieve a rule, it is necessary to specify, exactly, the identifier of the rule

### Example

```python
api_instance = api_client_factory.build(QuotesApi)
scope = 'scope_example' # str
provider = 'provider_example' # str (optional)
price_source = 'price_source_example' # str (optional)
instrument_id_type = 'instrument_id_type_example' # str (optional)
instrument_id = 'instrument_id_example' # str (optional)
quote_type = 'quote_type_example' # str (optional)
var_field = 'var_field_example' # str (optional)
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_quotes_access_metadata_rule(scope, provider=provider, price_source=price_source, instrument_id_type=instrument_id_type, instrument_id=instrument_id, quote_type=quote_type, var_field=var_field, effective_at=effective_at, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Quote Access Metadata Rule to retrieve. | [required] 
 **provider** | **str**| The Provider of the rule | [optional] 
 **price_source** | **str**| The PriceSource of the rule | [optional] 
 **instrument_id_type** | **str**| The InstrumentIdType of the rule | [optional] 
 **instrument_id** | **str**| The InstrumentId of the rule | [optional] 
 **quote_type** | **str**| The QuoteType of the rule | [optional] 
 **var_field** | **str**| The Field of the rule | [optional] 
 **effective_at** | **str**| The effective date of the rule | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the access metadata rule. Defaults to return the latest version if not specified. | [optional] 

### Return type

[**QuoteAccessMetadataRule**](QuoteAccessMetadataRule.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved Quote Access Metadata Rule or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_quotes**
> ResourceListOfQuote listQuotes = list_quotes(scope, as_at=as_at, page=page, limit=limit, filter=filter)

[DEPRECATED] ListQuotes: List quotes

List all the quotes from a single scope at the specified date/time  Please use ListQuotesForScope - the signature and behaviour of this endpoint will be changing to omit scope

### Example

```python
api_instance = api_client_factory.build(QuotesApi)
scope = 'scope_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
api_response = api_instance.list_quotes(scope, as_at=as_at, page=page, limit=limit, filter=filter)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the quotes to list. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to list the quotes. Defaults to latest if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing quotes from a previous call to list quotes.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set.              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**ResourceListOfQuote**](ResourceListOfQuote.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested quotes |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_quotes_access_metadata_rules**
> ResourceListOfQuoteAccessMetadataRule listQuotesAccessMetadataRules = list_quotes_access_metadata_rules(scope, as_at=as_at)

[EXPERIMENTAL] ListQuotesAccessMetadataRules: List all quote access metadata rules in a scope

Get all the quote access metadata rules in the specified scope

### Example

```python
api_instance = api_client_factory.build(QuotesApi)
scope = 'scope_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.list_quotes_access_metadata_rules(scope, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Quote Access Metadata Rule to retrieve. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the access metadata rule. Defaults to return the latest version if not specified. | [optional] 

### Return type

[**ResourceListOfQuoteAccessMetadataRule**](ResourceListOfQuoteAccessMetadataRule.md)

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

# **list_quotes_for_scope**
> ResourceListOfQuote listQuotesForScope = list_quotes_for_scope(scope, as_at=as_at, page=page, limit=limit, filter=filter)

ListQuotesForScope: List quotes for scope

List all the quotes from a single scope at the specified date/time

### Example

```python
api_instance = api_client_factory.build(QuotesApi)
scope = 'scope_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
api_response = api_instance.list_quotes_for_scope(scope, as_at=as_at, page=page, limit=limit, filter=filter)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the quotes to list. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to list the quotes. Defaults to latest if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing quotes from a previous call to list quotes.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set.              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**ResourceListOfQuote**](ResourceListOfQuote.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested quotes |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_quote_access_metadata_rule**
> QuoteAccessMetadataRule upsertQuoteAccessMetadataRule = upsert_quote_access_metadata_rule(scope, upsert_quote_access_metadata_rule_request, effective_at=effective_at, effective_until=effective_until)

[EXPERIMENTAL] UpsertQuoteAccessMetadataRule: Upsert a Quote Access Metadata Rule. This creates or updates the data in LUSID.

Update or insert one Quote Access Metadata Rule in a single scope. An item will be updated if it already exists  and inserted if it does not.    The response will return the successfully updated or inserted Quote Access Metadata Rule or failure message if unsuccessful    It is important to always check to verify success (or failure).                Multiple rules for a key can exists with different effective at dates, when resources are accessed the rule that is active for the current time will be fetched

### Example

```python
api_instance = api_client_factory.build(QuotesApi)
scope = 'scope_example' # str
upsert_quote_access_metadata_rule_request = UpsertQuoteAccessMetadataRuleRequest()
effective_at = 'effective_at_example' # str (optional)
effective_until = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.upsert_quote_access_metadata_rule(scope, upsert_quote_access_metadata_rule_request, effective_at=effective_at, effective_until=effective_until)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to use when updating or inserting the Quote Access Metadata Rule. | [required] 
 **upsert_quote_access_metadata_rule_request** | [**UpsertQuoteAccessMetadataRuleRequest**](UpsertQuoteAccessMetadataRuleRequest.md)| The Quote Access Metadata Rule to update or insert | [required] 
 **effective_at** | **str**| The date this rule will effective from | [optional] 
 **effective_until** | **datetime**| The effective date until which the Access Metadata is valid. If not supplied this will be valid indefinitely, or until the next &#39;effectiveAt&#39; date of the Access Metadata | [optional] 

### Return type

[**QuoteAccessMetadataRule**](QuoteAccessMetadataRule.md)

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

# **upsert_quotes**
> UpsertQuotesResponse upsertQuotes = upsert_quotes(scope, request_body=request_body)

UpsertQuotes: Upsert quotes

Update or insert one or more quotes in a single scope. A quote will be updated if it already exists  and inserted if it does not.                In the request each quote must be keyed by a unique correlation id. This id is ephemeral and is not stored by LUSID.  It serves only as a way to easily identify each quote in the response.                The response will return both the collection of successfully updated or inserted quotes, as well as those that failed.  For the failures a reason will be provided explaining why the quote could not be updated or inserted.                It is important to always check the failed set for any unsuccessful results.  The maximum number of quotes that this method can upsert per request is 2,000.

### Example

```python
api_instance = api_client_factory.build(QuotesApi)
scope = 'scope_example' # str
request_body = {"DS-VOD-PRICE-MID":{"quoteId":{"quoteSeriesId":{"provider":"DataScope","priceSource":"","instrumentId":"GB00BH4HKS39","instrumentIdType":"Isin","quoteType":"Price","field":"mid"},"effectiveAt":"2018-03-05T00:00:00.0000000+00:00"},"metricValue":{"value":1460.0,"unit":"CNY"}},"O-C-EURUSD-PRICE-BID":{"quoteId":{"quoteSeriesId":{"provider":"Oanda","priceSource":"Citi","instrumentId":"EUR/USD","instrumentIdType":"CurrencyPair","quoteType":"Price","field":"bid"},"effectiveAt":"2018-03-05T00:00:00.0000000+00:00"},"metricValue":{"value":1.367,"unit":"EUR/USD"},"lineage":"Oanda/FxRates_2018-10-22T00:00:00.0000000+00:00.csv"}} # Dict[str, UpsertQuoteRequest] (optional)
api_response = api_instance.upsert_quotes(scope, request_body=request_body)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to use when updating or inserting the quotes. | [required] 
 **request_body** | [**Dict[str, UpsertQuoteRequest]**](UpsertQuoteRequest.md)| The quotes to update or insert keyed by a unique correlation id. | [optional] 

### Return type

[**UpsertQuotesResponse**](UpsertQuotesResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully updated or inserted quotes along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

