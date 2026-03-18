# lusid.ConventionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_cds_flow_conventions**](ConventionsApi.md#delete_cds_flow_conventions) | **DELETE** /api/api/conventions/credit/conventions/{scope}/{code} | [BETA] DeleteCdsFlowConventions: Delete the CDS Flow Conventions of given scope and code, assuming that it is present.
[**delete_flow_conventions**](ConventionsApi.md#delete_flow_conventions) | **DELETE** /api/api/conventions/rates/flowconventions/{scope}/{code} | [BETA] DeleteFlowConventions: Delete the Flow Conventions of given scope and code, assuming that it is present.
[**delete_index_convention**](ConventionsApi.md#delete_index_convention) | **DELETE** /api/api/conventions/rates/indexconventions/{scope}/{code} | [BETA] DeleteIndexConvention: Delete the Index Convention of given scope and code, assuming that it is present.
[**get_cds_flow_conventions**](ConventionsApi.md#get_cds_flow_conventions) | **GET** /api/api/conventions/credit/conventions/{scope}/{code} | [BETA] GetCdsFlowConventions: Get CDS Flow Conventions
[**get_flow_conventions**](ConventionsApi.md#get_flow_conventions) | **GET** /api/api/conventions/rates/flowconventions/{scope}/{code} | [BETA] GetFlowConventions: Get Flow Conventions
[**get_index_convention**](ConventionsApi.md#get_index_convention) | **GET** /api/api/conventions/rates/indexconventions/{scope}/{code} | [BETA] GetIndexConvention: Get Index Convention
[**list_cds_flow_conventions**](ConventionsApi.md#list_cds_flow_conventions) | **GET** /api/api/conventions/credit/conventions | [BETA] ListCdsFlowConventions: List the set of CDS Flow Conventions
[**list_flow_conventions**](ConventionsApi.md#list_flow_conventions) | **GET** /api/api/conventions/rates/flowconventions | [BETA] ListFlowConventions: List the set of Flow Conventions
[**list_index_convention**](ConventionsApi.md#list_index_convention) | **GET** /api/api/conventions/rates/indexconventions | [BETA] ListIndexConvention: List the set of Index Conventions
[**upsert_cds_flow_conventions**](ConventionsApi.md#upsert_cds_flow_conventions) | **POST** /api/api/conventions/credit/conventions | [BETA] UpsertCdsFlowConventions: Upsert a set of CDS Flow Conventions. This creates or updates the data in Lusid.
[**upsert_flow_conventions**](ConventionsApi.md#upsert_flow_conventions) | **POST** /api/api/conventions/rates/flowconventions | [BETA] UpsertFlowConventions: Upsert Flow Conventions. This creates or updates the data in Lusid.
[**upsert_index_convention**](ConventionsApi.md#upsert_index_convention) | **POST** /api/api/conventions/rates/indexconventions | [BETA] UpsertIndexConvention: Upsert a set of Index Convention. This creates or updates the data in Lusid.


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.conventions_api import ConventionsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(ConventionsApi)
```

---

# **delete_cds_flow_conventions**
> AnnulSingleStructuredDataResponse deleteCdsFlowConventions = delete_cds_flow_conventions(scope, code)

[BETA] DeleteCdsFlowConventions: Delete the CDS Flow Conventions of given scope and code, assuming that it is present.

Delete the specified CDS Flow Conventions from a single scope.  The response will return either detail of the deleted item, or an explanation (failure) as to why this did not succeed.  It is important to always check for any unsuccessful response.

### Example

```python
api_instance = api_client_factory.build(ConventionsApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.delete_cds_flow_conventions(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the CDS Flow Conventions to delete. | [required] 
 **code** | **str**| The CDS Flow Conventions to delete. | [required] 

### Return type

[**AnnulSingleStructuredDataResponse**](AnnulSingleStructuredDataResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The AsAt of deletion or failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_flow_conventions**
> AnnulSingleStructuredDataResponse deleteFlowConventions = delete_flow_conventions(scope, code)

[BETA] DeleteFlowConventions: Delete the Flow Conventions of given scope and code, assuming that it is present.

Delete the specified conventions from a single scope.  The response will return either detail of the deleted item, or an explanation (failure) as to why this did not succeed.  It is important to always check for any unsuccessful response.

### Example

```python
api_instance = api_client_factory.build(ConventionsApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.delete_flow_conventions(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Flow Conventions to delete. | [required] 
 **code** | **str**| The Flow Conventions to delete. | [required] 

### Return type

[**AnnulSingleStructuredDataResponse**](AnnulSingleStructuredDataResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The AsAt of deletion or failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_index_convention**
> AnnulSingleStructuredDataResponse deleteIndexConvention = delete_index_convention(scope, code)

[BETA] DeleteIndexConvention: Delete the Index Convention of given scope and code, assuming that it is present.

Delete the specified Index Convention from a single scope.  The response will return either detail of the deleted item, or an explanation (failure) as to why this did not succeed.  It is important to always check for any unsuccessful response.

### Example

```python
api_instance = api_client_factory.build(ConventionsApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.delete_index_convention(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Index Convention to delete. | [required] 
 **code** | **str**| The Index Convention to delete. | [required] 

### Return type

[**AnnulSingleStructuredDataResponse**](AnnulSingleStructuredDataResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The AsAt of deletion or failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_cds_flow_conventions**
> GetCdsFlowConventionsResponse getCdsFlowConventions = get_cds_flow_conventions(scope, code, as_at=as_at)

[BETA] GetCdsFlowConventions: Get CDS Flow Conventions

Get a CDS Flow Conventions from a single scope.  The response will return either the conventions that has been stored, or a failure explaining why the request was unsuccessful.  It is important to always check for any unsuccessful requests (failures).

### Example

```python
api_instance = api_client_factory.build(ConventionsApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_cds_flow_conventions(scope, code, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the CDS Flow Conventions to retrieve. | [required] 
 **code** | **str**| The name of the CDS Flow Conventions to retrieve the data for. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the CDS Flow Conventions. Defaults to return the latest version if not specified. | [optional] 

### Return type

[**GetCdsFlowConventionsResponse**](GetCdsFlowConventionsResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved CDS Flow Conventions or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_flow_conventions**
> GetFlowConventionsResponse getFlowConventions = get_flow_conventions(scope, code, as_at=as_at)

[BETA] GetFlowConventions: Get Flow Conventions

Get a Flow Conventions from a single scope.  The response will return either the conventions that has been stored, or a failure explaining why the request was unsuccessful.  It is important to always check for any unsuccessful requests (failures).

### Example

```python
api_instance = api_client_factory.build(ConventionsApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_flow_conventions(scope, code, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Flow Conventions to retrieve. | [required] 
 **code** | **str**| The name of the Flow Conventions to retrieve the data for. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Flow Conventions. Defaults to return the latest version if not specified. | [optional] 

### Return type

[**GetFlowConventionsResponse**](GetFlowConventionsResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved Flow Conventions or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_index_convention**
> GetIndexConventionResponse getIndexConvention = get_index_convention(scope, code, as_at=as_at)

[BETA] GetIndexConvention: Get Index Convention

Get a Index Convention from a single scope.  The response will return either the conventions that has been stored, or a failure explaining why the request was unsuccessful.  It is important to always check for any unsuccessful requests (failures).

### Example

```python
api_instance = api_client_factory.build(ConventionsApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_index_convention(scope, code, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Index Convention to retrieve. | [required] 
 **code** | **str**| The name of the Index Convention to retrieve the data for. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Index Convention. Defaults to return the latest version if not specified. | [optional] 

### Return type

[**GetIndexConventionResponse**](GetIndexConventionResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved Index Convention or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_cds_flow_conventions**
> ResourceListOfGetCdsFlowConventionsResponse listCdsFlowConventions = list_cds_flow_conventions(as_at=as_at)

[BETA] ListCdsFlowConventions: List the set of CDS Flow Conventions

List the set of CDS Flow Conventions at the specified date/time

### Example

```python
api_instance = api_client_factory.build(ConventionsApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.list_cds_flow_conventions(as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the conventions. Defaults to latest if not specified. | [optional] 

### Return type

[**ResourceListOfGetCdsFlowConventionsResponse**](ResourceListOfGetCdsFlowConventionsResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested CDS Flow conventions |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_flow_conventions**
> ResourceListOfGetFlowConventionsResponse listFlowConventions = list_flow_conventions(as_at=as_at)

[BETA] ListFlowConventions: List the set of Flow Conventions

List the set of Flow Conventions at the specified date/time

### Example

```python
api_instance = api_client_factory.build(ConventionsApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.list_flow_conventions(as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the conventions. Defaults to latest if not specified. | [optional] 

### Return type

[**ResourceListOfGetFlowConventionsResponse**](ResourceListOfGetFlowConventionsResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Flow conventions |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_index_convention**
> ResourceListOfGetIndexConventionResponse listIndexConvention = list_index_convention(as_at=as_at)

[BETA] ListIndexConvention: List the set of Index Conventions

List the set of Index Conventions at the specified date/time

### Example

```python
api_instance = api_client_factory.build(ConventionsApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.list_index_convention(as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the conventions. Defaults to latest if not specified. | [optional] 

### Return type

[**ResourceListOfGetIndexConventionResponse**](ResourceListOfGetIndexConventionResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Index conventions |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_cds_flow_conventions**
> UpsertSingleStructuredDataResponse upsertCdsFlowConventions = upsert_cds_flow_conventions(upsert_cds_flow_conventions_request)

[BETA] UpsertCdsFlowConventions: Upsert a set of CDS Flow Conventions. This creates or updates the data in Lusid.

Update or insert CDS Flow Conventions in a single scope. An item will be updated if it already exists  and inserted if it does not.                The response will return the successfully updated or inserted CDS Flow Conventions or failure message if unsuccessful                It is important to always check to verify success (or failure).

### Example

```python
api_instance = api_client_factory.build(ConventionsApi)
upsert_cds_flow_conventions_request = UpsertCdsFlowConventionsRequest()
api_response = api_instance.upsert_cds_flow_conventions(upsert_cds_flow_conventions_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_cds_flow_conventions_request** | [**UpsertCdsFlowConventionsRequest**](UpsertCdsFlowConventionsRequest.md)| The CDS Flow Conventions to update or insert | [required] 

### Return type

[**UpsertSingleStructuredDataResponse**](UpsertSingleStructuredDataResponse.md)

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

# **upsert_flow_conventions**
> UpsertSingleStructuredDataResponse upsertFlowConventions = upsert_flow_conventions(upsert_flow_conventions_request)

[BETA] UpsertFlowConventions: Upsert Flow Conventions. This creates or updates the data in Lusid.

Update or insert Flow Conventions in a single scope. An item will be updated if it already exists  and inserted if it does not.                The response will return the successfully updated or inserted Flow Conventions or failure message if unsuccessful                It is important to always check to verify success (or failure).

### Example

```python
api_instance = api_client_factory.build(ConventionsApi)
upsert_flow_conventions_request = UpsertFlowConventionsRequest()
api_response = api_instance.upsert_flow_conventions(upsert_flow_conventions_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_flow_conventions_request** | [**UpsertFlowConventionsRequest**](UpsertFlowConventionsRequest.md)| The Flow Conventions to update or insert | [required] 

### Return type

[**UpsertSingleStructuredDataResponse**](UpsertSingleStructuredDataResponse.md)

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

# **upsert_index_convention**
> UpsertSingleStructuredDataResponse upsertIndexConvention = upsert_index_convention(upsert_index_convention_request)

[BETA] UpsertIndexConvention: Upsert a set of Index Convention. This creates or updates the data in Lusid.

Update or insert Index Convention in a single scope. An item will be updated if it already exists  and inserted if it does not.                The response will return the successfully updated or inserted Index Convention or failure message if unsuccessful                It is important to always check to verify success (or failure).

### Example

```python
api_instance = api_client_factory.build(ConventionsApi)
upsert_index_convention_request = UpsertIndexConventionRequest()
api_response = api_instance.upsert_index_convention(upsert_index_convention_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_index_convention_request** | [**UpsertIndexConventionRequest**](UpsertIndexConventionRequest.md)| The Index Conventions to update or insert | [required] 

### Return type

[**UpsertSingleStructuredDataResponse**](UpsertSingleStructuredDataResponse.md)

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

