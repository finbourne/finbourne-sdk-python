# horizon.InstrumentApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_instrument**](InstrumentApi.md#create_instrument) | **POST** /horizon/api/instrument/onboarding/create | [EARLY ACCESS] CreateInstrument: Creates and masters instruments with third party vendors.
[**enrich_instrument**](InstrumentApi.md#enrich_instrument) | **POST** /horizon/api/instrument/onboarding/enrich | [EARLY ACCESS] EnrichInstrument: Enriches an existing LUSID instrument using vendor data. Enrichment included identifiers, properties and market data.
[**get_open_figi_parameter_option**](InstrumentApi.md#get_open_figi_parameter_option) | **GET** /horizon/api/instrument/onboarding/search/openfigi/parameterOptions | [EARLY ACCESS] GetOpenFigiParameterOption: Get all supported market sector values for OpenFigi search
[**retrieve_perm_id_result**](InstrumentApi.md#retrieve_perm_id_result) | **GET** /horizon/api/instrument/onboarding/search/permid/{id} | [EARLY ACCESS] RetrievePermIdResult: Retrieve PermId results from a previous query.
[**search_open_figi**](InstrumentApi.md#search_open_figi) | **GET** /horizon/api/instrument/onboarding/search/openfigi | [EARLY ACCESS] SearchOpenFigi: Search OpenFigi for instruments that match the specified terms.
[**vendors**](InstrumentApi.md#vendors) | **GET** /horizon/api/instrument/onboarding/vendors | [EARLY ACCESS] Vendors: Gets the VendorProducts of any supported and licenced integrations for a given market sector and security type.


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.horizon.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.horizon.api.instrument_api import InstrumentApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(InstrumentApi)
```

---

# **create_instrument**
> OnboardInstrumentResponse createInstrument = create_instrument(onboard_instrument_request)

[EARLY ACCESS] CreateInstrument: Creates and masters instruments with third party vendors.

### Example

```python
api_instance = api_client_factory.build(InstrumentApi)
onboard_instrument_request = OnboardInstrumentRequest()
api_response = api_instance.create_instrument(onboard_instrument_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **onboard_instrument_request** | [**OnboardInstrumentRequest**](OnboardInstrumentRequest.md)|  | [required] 

### Return type

[**OnboardInstrumentResponse**](OnboardInstrumentResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **enrich_instrument**
> EnrichmentResponse enrichInstrument = enrich_instrument(vendor_product_key, identifiers)

[EARLY ACCESS] EnrichInstrument: Enriches an existing LUSID instrument using vendor data. Enrichment included identifiers, properties and market data.

### Example

```python
api_instance = api_client_factory.build(InstrumentApi)
vendor_product_key = 'vendor_product_key_example' # str
identifiers = Identifiers()
api_response = api_instance.enrich_instrument(vendor_product_key, identifiers)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_product_key** | **str**|  | [required] 
 **identifiers** | [**Identifiers**](Identifiers.md)|  | [required] 

### Return type

[**EnrichmentResponse**](EnrichmentResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_open_figi_parameter_option**
> List[AllowedParameterValue] getOpenFigiParameterOption = get_open_figi_parameter_option(parameter_name)

[EARLY ACCESS] GetOpenFigiParameterOption: Get all supported market sector values for OpenFigi search

### Example

```python
api_instance = api_client_factory.build(InstrumentApi)
parameter_name = horizon.OpenFigiParameterOptionName() # OpenFigiParameterOptionName
api_response = api_instance.get_open_figi_parameter_option(parameter_name)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parameter_name** | [**OpenFigiParameterOptionName**](.md)| OpenFigi API Parameters that have a restricted / permitted range of values. | [required] 

### Return type

[**List[AllowedParameterValue]**](AllowedParameterValue.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **retrieve_perm_id_result**
> List[PermIdData] retrievePermIdResult = retrieve_perm_id_result(id)

[EARLY ACCESS] RetrievePermIdResult: Retrieve PermId results from a previous query.

### Example

```python
api_instance = api_client_factory.build(InstrumentApi)
id = 'id_example' # str
api_response = api_instance.retrieve_perm_id_result(id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The execution ID returned by a previous query | [required] 

### Return type

[**List[PermIdData]**](PermIdData.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **search_open_figi**
> OpenFigiSearchResult searchOpenFigi = search_open_figi(query, use_perm_id, limit=limit, market_sector=market_sector)

[EARLY ACCESS] SearchOpenFigi: Search OpenFigi for instruments that match the specified terms.

### Example

```python
api_instance = api_client_factory.build(InstrumentApi)
query = 'query_example' # str
use_perm_id = False # bool
limit = 25 # int (optional)
market_sector = 'All' # str (optional)
api_response = api_instance.search_open_figi(query, use_perm_id, limit=limit, market_sector=market_sector)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | [required] 
 **use_perm_id** | **bool**| Should also search PermId for additional information, defaults to &#x60;false&#x60;. | [required] [default to False]
 **limit** | **int**| Only affects results rom OpenFigi general text search | [optional] [default to 25]
 **market_sector** | **str**| The market sector to search, defaults to &#x60;All&#x60;. | [optional] [default to &#39;All&#39;]

### Return type

[**OpenFigiSearchResult**](OpenFigiSearchResult.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **vendors**
> List[VendorProduct] vendors = vendors(market_sector, security_type, general_security_type)

[EARLY ACCESS] Vendors: Gets the VendorProducts of any supported and licenced integrations for a given market sector and security type.

### Example

```python
api_instance = api_client_factory.build(InstrumentApi)
market_sector = 'market_sector_example' # str
security_type = 'security_type_example' # str
general_security_type = 'general_security_type_example' # str
api_response = api_instance.vendors(market_sector, security_type, general_security_type)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market_sector** | **str**|  | [required] 
 **security_type** | **str**|  | [required] 
 **general_security_type** | **str**|  | [required] 

### Return type

[**List[VendorProduct]**](VendorProduct.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

