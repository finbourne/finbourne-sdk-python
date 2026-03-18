# identity.ExternalTokenIssuersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_external_token_issuer**](ExternalTokenIssuersApi.md#create_external_token_issuer) | **POST** /identity/api/externaltokenissuers | [EARLY ACCESS] CreateExternalTokenIssuer: Create an External Token Issuer
[**delete_external_token_issuer**](ExternalTokenIssuersApi.md#delete_external_token_issuer) | **DELETE** /identity/api/externaltokenissuers/{code} | [EARLY ACCESS] DeleteExternalTokenIssuer: Deletes an External Token Issuer by code
[**get_external_token_issuer**](ExternalTokenIssuersApi.md#get_external_token_issuer) | **GET** /identity/api/externaltokenissuers/{code} | [EARLY ACCESS] GetExternalTokenIssuer: Gets an External Token Issuer with code
[**list_external_token_issuers**](ExternalTokenIssuersApi.md#list_external_token_issuers) | **GET** /identity/api/externaltokenissuers | [EARLY ACCESS] ListExternalTokenIssuers: Lists all External Token Issuers for a domain
[**update_external_token_issuer**](ExternalTokenIssuersApi.md#update_external_token_issuer) | **PUT** /identity/api/externaltokenissuers/{code} | [EARLY ACCESS] UpdateExternalTokenIssuer: Updates an existing External Token Issuer


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.identity.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.identity.api.external_token_issuers_api import ExternalTokenIssuersApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(ExternalTokenIssuersApi)
```

---

# **create_external_token_issuer**
> ExternalTokenIssuerResponse createExternalTokenIssuer = create_external_token_issuer(create_external_token_issuer_request)

[EARLY ACCESS] CreateExternalTokenIssuer: Create an External Token Issuer

Creates an External Token Issuer

### Example

```python
api_instance = api_client_factory.build(ExternalTokenIssuersApi)
create_external_token_issuer_request = CreateExternalTokenIssuerRequest()
api_response = api_instance.create_external_token_issuer(create_external_token_issuer_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_external_token_issuer_request** | [**CreateExternalTokenIssuerRequest**](CreateExternalTokenIssuerRequest.md)|  | [required] 

### Return type

[**ExternalTokenIssuerResponse**](ExternalTokenIssuerResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create External Token Issuer |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_external_token_issuer**
> deleteExternalTokenIssuer = delete_external_token_issuer(code)

[EARLY ACCESS] DeleteExternalTokenIssuer: Deletes an External Token Issuer by code

Deletes an External Token Issuer

### Example

```python
api_instance = api_client_factory.build(ExternalTokenIssuersApi)
code = 'code_example' # str
api_instance.delete_external_token_issuer(code)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Identifier of the External Token Issuer to delete | [required] 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_external_token_issuer**
> ExternalTokenIssuerResponse getExternalTokenIssuer = get_external_token_issuer(code)

[EARLY ACCESS] GetExternalTokenIssuer: Gets an External Token Issuer with code

Gets an External Token Issuer

### Example

```python
api_instance = api_client_factory.build(ExternalTokenIssuersApi)
code = 'code_example' # str
api_response = api_instance.get_external_token_issuer(code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Identifier of the External Token Issuer | [required] 

### Return type

[**ExternalTokenIssuerResponse**](ExternalTokenIssuerResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get External Token Issuer |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_external_token_issuers**
> List[ExternalTokenIssuerResponse] listExternalTokenIssuers = list_external_token_issuers()

[EARLY ACCESS] ListExternalTokenIssuers: Lists all External Token Issuers for a domain

Lists all External Token Issuers

### Example

```python
api_instance = api_client_factory.build(ExternalTokenIssuersApi)
api_response = api_instance.list_external_token_issuers()
pprint(api_response)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[ExternalTokenIssuerResponse]**](ExternalTokenIssuerResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List External Token Issuers |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_external_token_issuer**
> ExternalTokenIssuerResponse updateExternalTokenIssuer = update_external_token_issuer(code, update_external_token_issuer_request)

[EARLY ACCESS] UpdateExternalTokenIssuer: Updates an existing External Token Issuer

Updates an External Token Issuer

### Example

```python
api_instance = api_client_factory.build(ExternalTokenIssuersApi)
code = 'code_example' # str
update_external_token_issuer_request = UpdateExternalTokenIssuerRequest()
api_response = api_instance.update_external_token_issuer(code, update_external_token_issuer_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Identifier of the External Token Issuer to update | [required] 
 **update_external_token_issuer_request** | [**UpdateExternalTokenIssuerRequest**](UpdateExternalTokenIssuerRequest.md)|  | [required] 

### Return type

[**ExternalTokenIssuerResponse**](ExternalTokenIssuerResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update External Token Issuer |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

