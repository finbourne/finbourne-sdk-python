# lusid.SearchApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**instruments_search**](SearchApi.md#instruments_search) | **POST** /api/api/search/instruments | [EARLY ACCESS] InstrumentsSearch: Instruments search
[**search_portfolio_groups**](SearchApi.md#search_portfolio_groups) | **GET** /api/api/search/portfoliogroups | SearchPortfolioGroups: Search Portfolio Groups
[**search_portfolios**](SearchApi.md#search_portfolios) | **GET** /api/api/search/portfolios | SearchPortfolios: Search Portfolios
[**search_properties**](SearchApi.md#search_properties) | **GET** /api/api/search/propertydefinitions | SearchProperties: Search Property Definitions


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.search_api import SearchApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(SearchApi)
```

---

# **instruments_search**
> List[InstrumentMatch] instrumentsSearch = instruments_search(instrument_search_property, mastered_effective_at=mastered_effective_at, mastered_only=mastered_only, scope=scope)

[EARLY ACCESS] InstrumentsSearch: Instruments search

Search across all instruments that have been mastered in LUSID. Optionally augment the results with instruments from an external symbology service,  currently OpenFIGI.

### Example

```python
api_instance = api_client_factory.build(SearchApi)
instrument_search_property = [{"key":"Instrument/default/Isin","value":"US0378331005"}] # List[InstrumentSearchProperty]
mastered_effective_at = 'mastered_effective_at_example' # str (optional)
mastered_only = False # bool (optional)
scope = 'scope_example' # str (optional)
api_response = api_instance.instruments_search(instrument_search_property, mastered_effective_at=mastered_effective_at, mastered_only=mastered_only, scope=scope)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_search_property** | [**List[InstrumentSearchProperty]**](InstrumentSearchProperty.md)| A collection of instrument properties to search for. LUSID will return instruments for any matched              properties. | [required] 
 **mastered_effective_at** | **str**| The effective datetime or cut label to use when searching mastered instruments. This parameter has no effect on instruments that  have not been mastered within LUSID. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **mastered_only** | **bool**| If set to true, only search over instruments that have been mastered within LUSID. Defaults to false. | [optional] [default to False]
 **scope** | **str**| The scope in which the instrument lies. | [optional] 

### Return type

[**List[InstrumentMatch]**](InstrumentMatch.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The instruments found by the search |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **search_portfolio_groups**
> PagedResourceListOfPortfolioGroupSearchResult searchPortfolioGroups = search_portfolio_groups(search=search, filter=filter, sort_by=sort_by, limit=limit, page=page)

SearchPortfolioGroups: Search Portfolio Groups

Search through all portfolio groups

### Example

```python
api_instance = api_client_factory.build(SearchApi)
search = 'search_example' # str (optional)
filter = 'filter_example' # str (optional)
sort_by = 'sort_by_example' # str (optional)
limit = 56 # int (optional)
page = 'page_example' # str (optional)
api_response = api_instance.search_portfolio_groups(search=search, filter=filter, sort_by=sort_by, limit=limit, page=page)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A parameter used for searching any portfolio group field. Wildcards(*) are supported at the end of words (e.g. &#39;Port*&#39;). Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **filter** | **str**| Expression to filter the result set.   For example, to filter on the Scope, use \&quot;id.scope eq &#39;string&#39;\&quot;  Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | **str**| Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName | [optional] 
 **limit** | **int**| When paginating, only return this number of records | [optional] 
 **page** | **str**| Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter, sortBy and search fields should not be supplied. | [optional] 

### Return type

[**PagedResourceListOfPortfolioGroupSearchResult**](PagedResourceListOfPortfolioGroupSearchResult.md)

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

# **search_portfolios**
> PagedResourceListOfPortfolioSearchResult searchPortfolios = search_portfolios(search=search, filter=filter, sort_by=sort_by, limit=limit, page=page)

SearchPortfolios: Search Portfolios

Search through all portfolios

### Example

```python
api_instance = api_client_factory.build(SearchApi)
search = 'search_example' # str (optional)
filter = 'filter_example' # str (optional)
sort_by = 'sort_by_example' # str (optional)
limit = 56 # int (optional)
page = 'page_example' # str (optional)
api_response = api_instance.search_portfolios(search=search, filter=filter, sort_by=sort_by, limit=limit, page=page)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A parameter used for searching any portfolio field. Wildcards(*) are supported at the end of words (e.g. &#39;Port*&#39;). Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **filter** | **str**| Expression to filter the result set.   For example, to filter on the portfolio Type, use \&quot;type eq &#39;Transaction&#39;\&quot;  Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | **str**| Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName | [optional] 
 **limit** | **int**| When paginating, only return this number of records | [optional] 
 **page** | **str**| Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter, sortBy and search fields should not be supplied. | [optional] 

### Return type

[**PagedResourceListOfPortfolioSearchResult**](PagedResourceListOfPortfolioSearchResult.md)

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

# **search_properties**
> PagedResourceListOfPropertyDefinitionSearchResult searchProperties = search_properties(search=search, filter=filter, sort_by=sort_by, limit=limit, page=page)

SearchProperties: Search Property Definitions

Search through all Property Definitions

### Example

```python
api_instance = api_client_factory.build(SearchApi)
search = 'search_example' # str (optional)
filter = 'filter_example' # str (optional)
sort_by = 'sort_by_example' # str (optional)
limit = 56 # int (optional)
page = 'page_example' # str (optional)
api_response = api_instance.search_properties(search=search, filter=filter, sort_by=sort_by, limit=limit, page=page)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A parameter used for searching any field. Wildcards(*) are supported at the end of words (e.g. &#39;Port*&#39;). Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **filter** | **str**| Expression to filter the result set.   For example, to filter on the Value Type, use \&quot;valueType eq &#39;string&#39;\&quot;  Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | **str**| Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName | [optional] 
 **limit** | **int**| When paginating, only return this number of records | [optional] 
 **page** | **str**| Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter, sortBy and search fields should not be supplied. | [optional] 

### Return type

[**PagedResourceListOfPropertyDefinitionSearchResult**](PagedResourceListOfPropertyDefinitionSearchResult.md)

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

