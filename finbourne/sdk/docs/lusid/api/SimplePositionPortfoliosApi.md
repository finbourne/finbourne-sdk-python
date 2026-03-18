# lusid.SimplePositionPortfoliosApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_simple_position_portfolio**](SimplePositionPortfoliosApi.md#create_simple_position_portfolio) | **POST** /api/api/simpleposition/{scope} | [EARLY ACCESS] CreateSimplePositionPortfolio: Create simple position portfolio


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.simple_position_portfolios_api import SimplePositionPortfoliosApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(SimplePositionPortfoliosApi)
```

---

# **create_simple_position_portfolio**
> Portfolio createSimplePositionPortfolio = create_simple_position_portfolio(scope, create_simple_position_portfolio_request)

[EARLY ACCESS] CreateSimplePositionPortfolio: Create simple position portfolio

Create a simple position portfolio in a particular scope.

### Example

```python
api_instance = api_client_factory.build(SimplePositionPortfoliosApi)
scope = 'scope_example' # str
create_simple_position_portfolio_request = CreateSimplePositionPortfolioRequest()
api_response = api_instance.create_simple_position_portfolio(scope, create_simple_position_portfolio_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope in which to create the simple position portfolio. | [required] 
 **create_simple_position_portfolio_request** | [**CreateSimplePositionPortfolioRequest**](CreateSimplePositionPortfolioRequest.md)| The definition of the simple position portfolio. | [required] 

### Return type

[**Portfolio**](Portfolio.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created simple position portfolio, with populated id |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

