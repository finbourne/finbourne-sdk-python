# lusid.FeeTypesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_fee_type**](FeeTypesApi.md#create_fee_type) | **POST** /api/api/feetypes/{scope} | [EXPERIMENTAL] CreateFeeType: Create a FeeType.
[**delete_fee_type**](FeeTypesApi.md#delete_fee_type) | **DELETE** /api/api/feetypes/{scope}/{code} | [EXPERIMENTAL] DeleteFeeType: Delete a FeeType.
[**get_fee_template_specifications**](FeeTypesApi.md#get_fee_template_specifications) | **GET** /api/api/feetypes/feetransactiontemplatespecification | [EXPERIMENTAL] GetFeeTemplateSpecifications: Get FeeTemplateSpecifications used in the FeeType.
[**get_fee_type**](FeeTypesApi.md#get_fee_type) | **GET** /api/api/feetypes/{scope}/{code} | [EXPERIMENTAL] GetFeeType: Get a FeeType
[**list_fee_types**](FeeTypesApi.md#list_fee_types) | **GET** /api/api/feetypes | [EXPERIMENTAL] ListFeeTypes: List FeeTypes
[**update_fee_type**](FeeTypesApi.md#update_fee_type) | **PUT** /api/api/feetypes/{scope}/{code} | [EXPERIMENTAL] UpdateFeeType: Update a FeeType.


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.fee_types_api import FeeTypesApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(FeeTypesApi)
```

---

# **create_fee_type**
> FeeType createFeeType = create_fee_type(scope, fee_type_request)

[EXPERIMENTAL] CreateFeeType: Create a FeeType.

Create a FeeType that contains templates used to create fee transactions.

### Example

```python
api_instance = api_client_factory.build(FeeTypesApi)
scope = 'scope_example' # str
fee_type_request = FeeTypeRequest()
api_response = api_instance.create_fee_type(scope, fee_type_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the FeeType. | [required] 
 **fee_type_request** | [**FeeTypeRequest**](FeeTypeRequest.md)| The contents of the FeeType. | [required] 

### Return type

[**FeeType**](FeeType.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create a FeeType. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_fee_type**
> DeletedEntityResponse deleteFeeType = delete_fee_type(scope, code)

[EXPERIMENTAL] DeleteFeeType: Delete a FeeType.

Delete a FeeType that contains templates used to create fee transactions.

### Example

```python
api_instance = api_client_factory.build(FeeTypesApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.delete_fee_type(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the FeeType. | [required] 
 **code** | **str**| The code of the fee type | [required] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete a FeeType. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_fee_template_specifications**
> FeeTransactionTemplateSpecification getFeeTemplateSpecifications = get_fee_template_specifications()

[EXPERIMENTAL] GetFeeTemplateSpecifications: Get FeeTemplateSpecifications used in the FeeType.

Get FeeTemplateSpecifications used in the FeeType.

### Example

```python
api_instance = api_client_factory.build(FeeTypesApi)
api_response = api_instance.get_fee_template_specifications()
pprint(api_response)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FeeTransactionTemplateSpecification**](FeeTransactionTemplateSpecification.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fee template specifications used with a FeeType. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_fee_type**
> FeeType getFeeType = get_fee_type(scope, code, as_at=as_at)

[EXPERIMENTAL] GetFeeType: Get a FeeType

Get a FeeType that contains templates used to create fee transactions.

### Example

```python
api_instance = api_client_factory.build(FeeTypesApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_fee_type(scope, code, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the FeeType | [required] 
 **code** | **str**| The code of the FeeType | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the FeeType. Defaults to returning the latest version of the FeeType, if not specified. | [optional] 

### Return type

[**FeeType**](FeeType.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested FeeType. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_fee_types**
> PagedResourceListOfFeeType listFeeTypes = list_fee_types(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

[EXPERIMENTAL] ListFeeTypes: List FeeTypes

List FeeTypes that contain templates used to create fee transactions.

### Example

```python
api_instance = api_client_factory.build(FeeTypesApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
api_response = api_instance.list_fee_types(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the FeeTypes. Defaults to returning the latest version of each FeeType if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing FeeTypes; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the Code of the FeeType type, specify \&quot;id.Code eq &#39;FeeType1&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 

### Return type

[**PagedResourceListOfFeeType**](PagedResourceListOfFeeType.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Fee Types |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_fee_type**
> FeeType updateFeeType = update_fee_type(scope, code, update_fee_type_request)

[EXPERIMENTAL] UpdateFeeType: Update a FeeType.

Update a FeeType that contains templates used to create fee transactions.

### Example

```python
api_instance = api_client_factory.build(FeeTypesApi)
scope = 'scope_example' # str
code = 'code_example' # str
update_fee_type_request = UpdateFeeTypeRequest()
api_response = api_instance.update_fee_type(scope, code, update_fee_type_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the FeeType. | [required] 
 **code** | **str**| The code of the fee type | [required] 
 **update_fee_type_request** | [**UpdateFeeTypeRequest**](UpdateFeeTypeRequest.md)| The contents of the FeeType. | [required] 

### Return type

[**FeeType**](FeeType.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update a FeeType. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

