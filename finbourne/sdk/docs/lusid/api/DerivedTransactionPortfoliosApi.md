# lusid.DerivedTransactionPortfoliosApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_derived_portfolio**](DerivedTransactionPortfoliosApi.md#create_derived_portfolio) | **POST** /api/api/derivedtransactionportfolios/{scope} | CreateDerivedPortfolio: Create derived portfolio
[**delete_derived_portfolio_details**](DerivedTransactionPortfoliosApi.md#delete_derived_portfolio_details) | **DELETE** /api/api/derivedtransactionportfolios/{scope}/{code}/details | [EARLY ACCESS] DeleteDerivedPortfolioDetails: Delete derived portfolio details


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.derived_transaction_portfolios_api import DerivedTransactionPortfoliosApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(DerivedTransactionPortfoliosApi)
```

---

# **create_derived_portfolio**
> Portfolio createDerivedPortfolio = create_derived_portfolio(scope, create_derived_transaction_portfolio_request=create_derived_transaction_portfolio_request)

CreateDerivedPortfolio: Create derived portfolio

Create a derived transaction portfolio from a parent transaction portfolio (which may itself be derived).

### Example

```python
api_instance = api_client_factory.build(DerivedTransactionPortfoliosApi)
scope = 'scope_example' # str
create_derived_transaction_portfolio_request = CreateDerivedTransactionPortfolioRequest()
api_response = api_instance.create_derived_portfolio(scope, create_derived_transaction_portfolio_request=create_derived_transaction_portfolio_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope in which to create the derived transaction portfolio. | [required] 
 **create_derived_transaction_portfolio_request** | [**CreateDerivedTransactionPortfolioRequest**](CreateDerivedTransactionPortfolioRequest.md)| The definition of the derived transaction portfolio. | [optional] 

### Return type

[**Portfolio**](Portfolio.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created derived portfolio, with populated id |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_derived_portfolio_details**
> DeletedEntityResponse deleteDerivedPortfolioDetails = delete_derived_portfolio_details(scope, code, effective_at=effective_at)

[EARLY ACCESS] DeleteDerivedPortfolioDetails: Delete derived portfolio details

Delete all the portfolio details for a derived transaction portfolio.

### Example

```python
api_instance = api_client_factory.build(DerivedTransactionPortfoliosApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
api_response = api_instance.delete_derived_portfolio_details(scope, code, effective_at=effective_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the derived transaction portfolio. | [required] 
 **code** | **str**| The code of the derived transaction portfolio. Together with the scope this uniquely identifies              the derived transaction portfolio. | [required] 
 **effective_at** | **str**| The effective date of the change. | [optional] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

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

