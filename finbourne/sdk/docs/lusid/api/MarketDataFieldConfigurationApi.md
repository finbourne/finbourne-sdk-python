# lusid.MarketDataFieldConfigurationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_market_data_field_configuration**](MarketDataFieldConfigurationApi.md#get_market_data_field_configuration) | **GET** /api/api/marketdata/fieldconfiguration/{marketDataCategory} | [EARLY ACCESS] GetMarketDataFieldConfiguration: Get a Market Data Field Configuration
[**update_market_data_field_configuration**](MarketDataFieldConfigurationApi.md#update_market_data_field_configuration) | **POST** /api/api/marketdata/fieldconfiguration/{marketDataCategory}/$update | [EARLY ACCESS] UpdateMarketDataFieldConfiguration: Update a Market Data Field Configuration


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.market_data_field_configuration_api import MarketDataFieldConfigurationApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(MarketDataFieldConfigurationApi)
```

---

# **get_market_data_field_configuration**
> MarketDataFieldConfiguration getMarketDataFieldConfiguration = get_market_data_field_configuration(market_data_category, as_at=as_at)

[EARLY ACCESS] GetMarketDataFieldConfiguration: Get a Market Data Field Configuration

Retrieve the market data field configuration for a given market data category.  If the configuration does not yet exist, an empty configuration will be returned.

### Example

```python
api_instance = api_client_factory.build(MarketDataFieldConfigurationApi)
market_data_category = 'market_data_category_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_market_data_field_configuration(market_data_category, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market_data_category** | **str**| The market data category. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the configuration. Defaults to return the latest version if not specified. | [optional] 

### Return type

[**MarketDataFieldConfiguration**](MarketDataFieldConfiguration.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested market data field configuration. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_market_data_field_configuration**
> MarketDataFieldConfiguration updateMarketDataFieldConfiguration = update_market_data_field_configuration(market_data_category, update_market_data_field_configuration_request)

[EARLY ACCESS] UpdateMarketDataFieldConfiguration: Update a Market Data Field Configuration

Update the metadata field schema for a market data field configuration.  Allows adding, updating, and removing metadata field definitions.

### Example

```python
api_instance = api_client_factory.build(MarketDataFieldConfigurationApi)
market_data_category = 'market_data_category_example' # str
update_market_data_field_configuration_request = UpdateMarketDataFieldConfigurationRequest()
api_response = api_instance.update_market_data_field_configuration(market_data_category, update_market_data_field_configuration_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market_data_category** | **str**| The market data category. | [required] 
 **update_market_data_field_configuration_request** | [**UpdateMarketDataFieldConfigurationRequest**](UpdateMarketDataFieldConfigurationRequest.md)| The metadata fields to add, update, or remove. | [required] 

### Return type

[**MarketDataFieldConfiguration**](MarketDataFieldConfiguration.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated market data field configuration. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

