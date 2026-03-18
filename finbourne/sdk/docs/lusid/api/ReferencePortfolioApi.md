# lusid.ReferencePortfolioApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_reference_portfolio**](ReferencePortfolioApi.md#create_reference_portfolio) | **POST** /api/api/referenceportfolios/{scope} | CreateReferencePortfolio: Create reference portfolio
[**get_reference_portfolio_constituents**](ReferencePortfolioApi.md#get_reference_portfolio_constituents) | **GET** /api/api/referenceportfolios/{scope}/{code}/constituents | GetReferencePortfolioConstituents: Get reference portfolio constituents
[**list_constituents_adjustments**](ReferencePortfolioApi.md#list_constituents_adjustments) | **GET** /api/api/referenceportfolios/{scope}/{code}/constituentsadjustments | ListConstituentsAdjustments: List constituents adjustments
[**upsert_reference_portfolio_constituent_properties**](ReferencePortfolioApi.md#upsert_reference_portfolio_constituent_properties) | **POST** /api/api/referenceportfolios/{scope}/{code}/constituents/properties | [EARLY ACCESS] UpsertReferencePortfolioConstituentProperties: Upsert constituent properties
[**upsert_reference_portfolio_constituents**](ReferencePortfolioApi.md#upsert_reference_portfolio_constituents) | **POST** /api/api/referenceportfolios/{scope}/{code}/constituents | UpsertReferencePortfolioConstituents: Upsert reference portfolio constituents


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.reference_portfolio_api import ReferencePortfolioApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(ReferencePortfolioApi)
```

---

# **create_reference_portfolio**
> Portfolio createReferencePortfolio = create_reference_portfolio(scope, create_reference_portfolio_request)

CreateReferencePortfolio: Create reference portfolio

Create a reference portfolio in a particular scope.

### Example

```python
api_instance = api_client_factory.build(ReferencePortfolioApi)
scope = 'scope_example' # str
create_reference_portfolio_request = CreateReferencePortfolioRequest()
api_response = api_instance.create_reference_portfolio(scope, create_reference_portfolio_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope in which to create the reference portfolio. | [required] 
 **create_reference_portfolio_request** | [**CreateReferencePortfolioRequest**](CreateReferencePortfolioRequest.md)| The definition of the reference portfolio. | [required] 

### Return type

[**Portfolio**](Portfolio.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created reference portfolio, with populated id |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_reference_portfolio_constituents**
> GetReferencePortfolioConstituentsResponse getReferencePortfolioConstituents = get_reference_portfolio_constituents(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)

GetReferencePortfolioConstituents: Get reference portfolio constituents

Get constituents from a reference portfolio at a particular effective time.

### Example

```python
api_instance = api_client_factory.build(ReferencePortfolioApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.get_reference_portfolio_constituents(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the reference portfolio. | [required] 
 **code** | **str**| The code of the reference portfolio. Together with the scope this uniquely identifies              the reference portfolio. | [required] 
 **effective_at** | **str**| The effective date of the constituents to retrieve. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve constituents. Defaults to return the latest version              of each constituent if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;Instrument&#39; or &#39;ReferenceHolding&#39; domain to decorate onto              constituents. These take the format {domain}/{scope}/{code} e.g. &#39;Instrument/system/Name&#39; or              &#39;ReferenceHolding/strategy/quantsignal&#39;. Defaults to return all available instrument and reference holding properties if not specified. | [optional] 

### Return type

[**GetReferencePortfolioConstituentsResponse**](GetReferencePortfolioConstituentsResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested reference portfolio constituents |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_constituents_adjustments**
> ResourceListOfConstituentsAdjustmentHeader listConstituentsAdjustments = list_constituents_adjustments(scope, code, from_effective_at, to_effective_at, as_at_time=as_at_time)

ListConstituentsAdjustments: List constituents adjustments

List adjustments made to constituents in a reference portfolio.

### Example

```python
api_instance = api_client_factory.build(ReferencePortfolioApi)
scope = 'scope_example' # str
code = 'code_example' # str
from_effective_at = 'from_effective_at_example' # str
to_effective_at = 'to_effective_at_example' # str
as_at_time = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.list_constituents_adjustments(scope, code, from_effective_at, to_effective_at, as_at_time=as_at_time)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the reference portfolio. | [required] 
 **code** | **str**| The code of the reference portfolio. Together with the scope this uniquely identifies              the reference portfolio. | [required] 
 **from_effective_at** | **str**| Events between this time (inclusive) and the toEffectiveAt are returned. | [required] 
 **to_effective_at** | **str**| Events between this time (inclusive) and the fromEffectiveAt are returned. | [required] 
 **as_at_time** | **datetime**| The asAt time for which the result is valid. | [optional] 

### Return type

[**ResourceListOfConstituentsAdjustmentHeader**](ResourceListOfConstituentsAdjustmentHeader.md)

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

# **upsert_reference_portfolio_constituent_properties**
> UpsertReferencePortfolioConstituentPropertiesResponse upsertReferencePortfolioConstituentProperties = upsert_reference_portfolio_constituent_properties(scope, code, upsert_reference_portfolio_constituent_properties_request)

[EARLY ACCESS] UpsertReferencePortfolioConstituentProperties: Upsert constituent properties

Create or update one or more constituent properties for a single constituent in the reference portfolio.  Each property will be updated if it already exists, created if it does not and deleted if value is null.  Both constituent and portfolio must exist at the time when properties are created or updated.

### Example

```python
api_instance = api_client_factory.build(ReferencePortfolioApi)
scope = 'scope_example' # str
code = 'code_example' # str
upsert_reference_portfolio_constituent_properties_request = UpsertReferencePortfolioConstituentPropertiesRequest()
api_response = api_instance.upsert_reference_portfolio_constituent_properties(scope, code, upsert_reference_portfolio_constituent_properties_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the reference portfolio. | [required] 
 **code** | **str**| The code of the reference portfolio. Together with the scope this uniquely identifies              the reference portfolio. | [required] 
 **upsert_reference_portfolio_constituent_properties_request** | [**UpsertReferencePortfolioConstituentPropertiesRequest**](UpsertReferencePortfolioConstituentPropertiesRequest.md)| The request to modify properties for the constituent. | [required] 

### Return type

[**UpsertReferencePortfolioConstituentPropertiesResponse**](UpsertReferencePortfolioConstituentPropertiesResponse.md)

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

# **upsert_reference_portfolio_constituents**
> UpsertReferencePortfolioConstituentsResponse upsertReferencePortfolioConstituents = upsert_reference_portfolio_constituents(scope, code, upsert_reference_portfolio_constituents_request)

UpsertReferencePortfolioConstituents: Upsert reference portfolio constituents

Add constituents to a reference portfolio.

### Example

```python
api_instance = api_client_factory.build(ReferencePortfolioApi)
scope = 'scope_example' # str
code = 'code_example' # str
upsert_reference_portfolio_constituents_request = UpsertReferencePortfolioConstituentsRequest()
api_response = api_instance.upsert_reference_portfolio_constituents(scope, code, upsert_reference_portfolio_constituents_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the reference portfolio. | [required] 
 **code** | **str**| The code of the reference portfolio. Together with the scope this uniquely identifies              the reference portfolio. | [required] 
 **upsert_reference_portfolio_constituents_request** | [**UpsertReferencePortfolioConstituentsRequest**](UpsertReferencePortfolioConstituentsRequest.md)| The constituents to upload to the reference portfolio. | [required] 

### Return type

[**UpsertReferencePortfolioConstituentsResponse**](UpsertReferencePortfolioConstituentsResponse.md)

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

