# horizon.VendorApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_core_field_mappings_for_product_entity**](VendorApi.md#get_core_field_mappings_for_product_entity) | **GET** /horizon/api/vendor/mappings/fields | [EARLY ACCESS] GetCoreFieldMappingsForProductEntity: Get core field mappings for a given vendor product&#39;s entity.
[**get_optional_mappings_for_product_entity**](VendorApi.md#get_optional_mappings_for_product_entity) | **GET** /horizon/api/vendor/mappings/optional | [EARLY ACCESS] GetOptionalMappingsForProductEntity: Get a user defined LUSID property mappings for the specified vendor / LUSID entity.
[**get_property_mappings_for_product_entity**](VendorApi.md#get_property_mappings_for_product_entity) | **GET** /horizon/api/vendor/mappings/properties | [EARLY ACCESS] GetPropertyMappingsForProductEntity: Gets the property mappings for a given vendor product&#39;s entity
[**query_vendors**](VendorApi.md#query_vendors) | **POST** /horizon/api/vendor/$query | [EARLY ACCESS] QueryVendors: Query for vendors and their packages with entities and sub-entities.
[**set_optional_mappings_for_product_entity**](VendorApi.md#set_optional_mappings_for_product_entity) | **POST** /horizon/api/vendor/mappings/optional | [EARLY ACCESS] SetOptionalMappingsForProductEntity: Create a user defined LUSID property mappings for the specified vendor / LUSID entity.


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.horizon.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.horizon.api.vendor_api import VendorApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(VendorApi)
```

---

# **get_core_field_mappings_for_product_entity**
> List[LusidField] getCoreFieldMappingsForProductEntity = get_core_field_mappings_for_product_entity(vendor_name, product_name, lusid_entity_type, lusid_entity_sub_type=lusid_entity_sub_type)

[EARLY ACCESS] GetCoreFieldMappingsForProductEntity: Get core field mappings for a given vendor product's entity.

### Example

```python
api_instance = api_client_factory.build(VendorApi)
vendor_name = 'vendor_name_example' # str
product_name = 'product_name_example' # str
lusid_entity_type = 'lusid_entity_type_example' # str
lusid_entity_sub_type = 'lusid_entity_sub_type_example' # str (optional)
api_response = api_instance.get_core_field_mappings_for_product_entity(vendor_name, product_name, lusid_entity_type, lusid_entity_sub_type=lusid_entity_sub_type)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_name** | **str**|  | [required] 
 **product_name** | **str**|  | [required] 
 **lusid_entity_type** | **str**|  | [required] 
 **lusid_entity_sub_type** | **str**|  | [optional] 

### Return type

[**List[LusidField]**](LusidField.md)

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

# **get_optional_mappings_for_product_entity**
> Dict[str, LusidPropertyDefinitionOverrides] getOptionalMappingsForProductEntity = get_optional_mappings_for_product_entity(vendor_name, product_name, lusid_entity_type, lusid_entity_sub_type=lusid_entity_sub_type)

[EARLY ACCESS] GetOptionalMappingsForProductEntity: Get a user defined LUSID property mappings for the specified vendor / LUSID entity.

### Example

```python
api_instance = api_client_factory.build(VendorApi)
vendor_name = 'vendor_name_example' # str
product_name = 'product_name_example' # str
lusid_entity_type = 'lusid_entity_type_example' # str
lusid_entity_sub_type = 'lusid_entity_sub_type_example' # str (optional)
api_response = api_instance.get_optional_mappings_for_product_entity(vendor_name, product_name, lusid_entity_type, lusid_entity_sub_type=lusid_entity_sub_type)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_name** | **str**|  | [required] 
 **product_name** | **str**|  | [required] 
 **lusid_entity_type** | **str**|  | [required] 
 **lusid_entity_sub_type** | **str**|  | [optional] 

### Return type

[**Dict[str, LusidPropertyDefinitionOverrides]**](LusidPropertyDefinitionOverrides.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | The details of the input related failure |  -  |
**200** | OK |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_property_mappings_for_product_entity**
> List[LusidPropertyToVendorFieldMapping] getPropertyMappingsForProductEntity = get_property_mappings_for_product_entity(vendor_name, product_name, lusid_entity_type, lusid_entity_sub_type=lusid_entity_sub_type)

[EARLY ACCESS] GetPropertyMappingsForProductEntity: Gets the property mappings for a given vendor product's entity

### Example

```python
api_instance = api_client_factory.build(VendorApi)
vendor_name = 'vendor_name_example' # str
product_name = 'product_name_example' # str
lusid_entity_type = 'lusid_entity_type_example' # str
lusid_entity_sub_type = 'lusid_entity_sub_type_example' # str (optional)
api_response = api_instance.get_property_mappings_for_product_entity(vendor_name, product_name, lusid_entity_type, lusid_entity_sub_type=lusid_entity_sub_type)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_name** | **str**|  | [required] 
 **product_name** | **str**|  | [required] 
 **lusid_entity_type** | **str**|  | [required] 
 **lusid_entity_sub_type** | **str**|  | [optional] 

### Return type

[**List[LusidPropertyToVendorFieldMapping]**](LusidPropertyToVendorFieldMapping.md)

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

# **query_vendors**
> PagedResourceListOfVendorProduct queryVendors = query_vendors(query_request)

[EARLY ACCESS] QueryVendors: Query for vendors and their packages with entities and sub-entities.

### Example

```python
api_instance = api_client_factory.build(VendorApi)
query_request = QueryRequest()
api_response = api_instance.query_vendors(query_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_request** | [**QueryRequest**](QueryRequest.md)|  | [required] 

### Return type

[**PagedResourceListOfVendorProduct**](PagedResourceListOfVendorProduct.md)

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

# **set_optional_mappings_for_product_entity**
> Dict[str, LusidPropertyDefinitionOverridesResponse] setOptionalMappingsForProductEntity = set_optional_mappings_for_product_entity(vendor_name, product_name, lusid_entity_type, request_body, lusid_entity_sub_type=lusid_entity_sub_type)

[EARLY ACCESS] SetOptionalMappingsForProductEntity: Create a user defined LUSID property mappings for the specified vendor / LUSID entity.

### Example

```python
api_instance = api_client_factory.build(VendorApi)
vendor_name = 'vendor_name_example' # str
product_name = 'product_name_example' # str
lusid_entity_type = 'lusid_entity_type_example' # str
request_body = {"0":{"displayNameOverride":"descriptionOverride","descriptionOverride":"displayNameOverride"},"1":{"displayNameOverride":"descriptionOverride","descriptionOverride":"displayNameOverride"}} # Dict[str, LusidPropertyDefinitionOverrides]
lusid_entity_sub_type = 'lusid_entity_sub_type_example' # str (optional)
api_response = api_instance.set_optional_mappings_for_product_entity(vendor_name, product_name, lusid_entity_type, request_body, lusid_entity_sub_type=lusid_entity_sub_type)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_name** | **str**|  | [required] 
 **product_name** | **str**|  | [required] 
 **lusid_entity_type** | **str**|  | [required] 
 **request_body** | [**Dict[str, LusidPropertyDefinitionOverrides]**](LusidPropertyDefinitionOverrides.md)|  | [required] 
 **lusid_entity_sub_type** | **str**|  | [optional] 

### Return type

[**Dict[str, LusidPropertyDefinitionOverridesResponse]**](LusidPropertyDefinitionOverridesResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | The details of the input related failure |  -  |
**200** | OK |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

