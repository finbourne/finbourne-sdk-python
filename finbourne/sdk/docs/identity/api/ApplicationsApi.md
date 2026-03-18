# identity.ApplicationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_application**](ApplicationsApi.md#create_application) | **POST** /identity/api/applications | [EARLY ACCESS] CreateApplication: Create Application
[**delete_application**](ApplicationsApi.md#delete_application) | **DELETE** /identity/api/applications/{id} | [EARLY ACCESS] DeleteApplication: Delete Application
[**get_application**](ApplicationsApi.md#get_application) | **GET** /identity/api/applications/{id} | GetApplication: Get Application
[**list_applications**](ApplicationsApi.md#list_applications) | **GET** /identity/api/applications | ListApplications: List Applications
[**rotate_application_secrets**](ApplicationsApi.md#rotate_application_secrets) | **POST** /identity/api/applications/{id}/lifecycle/$newsecret | [EARLY ACCESS] RotateApplicationSecrets: Rotate Application Secrets


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.identity.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.identity.api.applications_api import ApplicationsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(ApplicationsApi)
```

---

# **create_application**
> OAuthApplication createApplication = create_application(create_application_request=create_application_request)

[EARLY ACCESS] CreateApplication: Create Application

Create a new Application

### Example

```python
api_instance = api_client_factory.build(ApplicationsApi)
create_application_request = CreateApplicationRequest()
api_response = api_instance.create_application(create_application_request=create_application_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_application_request** | [**CreateApplicationRequest**](CreateApplicationRequest.md)| Details of the application to be created | [optional] 

### Return type

[**OAuthApplication**](OAuthApplication.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Create Application |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_application**
> deleteApplication = delete_application(id)

[EARLY ACCESS] DeleteApplication: Delete Application

Delete the specified application

### Example

```python
api_instance = api_client_factory.build(ApplicationsApi)
id = 'id_example' # str
api_instance.delete_application(id)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the application | [required] 

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

# **get_application**
> OAuthApplication getApplication = get_application(id, include_secret=include_secret)

GetApplication: Get Application

get the specified application, and optionally the OIDC secret

### Example

```python
api_instance = api_client_factory.build(ApplicationsApi)
id = 'id_example' # str
include_secret = True # bool (optional)
api_response = api_instance.get_application(id, include_secret=include_secret)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the application | [required] 
 **include_secret** | **bool**| Optional. If set to true, the application secrets will be returned in plain text | [optional] 

### Return type

[**OAuthApplication**](OAuthApplication.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get the specified application |  -  |
**404** | Not Found |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_applications**
> List[OAuthApplication] listApplications = list_applications()

ListApplications: List Applications

List the available applications

### Example

```python
api_instance = api_client_factory.build(ApplicationsApi)
api_response = api_instance.list_applications()
pprint(api_response)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[OAuthApplication]**](OAuthApplication.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List the available applications |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **rotate_application_secrets**
> OAuthApplication rotateApplicationSecrets = rotate_application_secrets(id)

[EARLY ACCESS] RotateApplicationSecrets: Rotate Application Secrets

Rotate the secrets for the specified application

### Example

```python
api_instance = api_client_factory.build(ApplicationsApi)
id = 'id_example' # str
api_response = api_instance.rotate_application_secrets(id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the application | [required] 

### Return type

[**OAuthApplication**](OAuthApplication.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rotate Application Secrets |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

