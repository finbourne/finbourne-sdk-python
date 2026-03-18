# lusid.AborConfigurationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_abor_configuration**](AborConfigurationApi.md#create_abor_configuration) | **POST** /api/api/aborconfiguration/{scope} | [EXPERIMENTAL] CreateAborConfiguration: Create an AborConfiguration.
[**delete_abor_configuration**](AborConfigurationApi.md#delete_abor_configuration) | **DELETE** /api/api/aborconfiguration/{scope}/{code} | [EXPERIMENTAL] DeleteAborConfiguration: Delete an AborConfiguration.
[**get_abor_configuration**](AborConfigurationApi.md#get_abor_configuration) | **GET** /api/api/aborconfiguration/{scope}/{code} | [EXPERIMENTAL] GetAborConfiguration: Get AborConfiguration.
[**get_abor_configuration_properties**](AborConfigurationApi.md#get_abor_configuration_properties) | **GET** /api/api/aborconfiguration/{scope}/{code}/properties | [EXPERIMENTAL] GetAborConfigurationProperties: Get Abor Configuration properties
[**list_abor_configurations**](AborConfigurationApi.md#list_abor_configurations) | **GET** /api/api/aborconfiguration | [EXPERIMENTAL] ListAborConfigurations: List AborConfiguration.
[**patch_abor_configuration**](AborConfigurationApi.md#patch_abor_configuration) | **PATCH** /api/api/aborconfiguration/{scope}/{code} | [EXPERIMENTAL] PatchAborConfiguration: Patch Abor Configuration.
[**upsert_abor_configuration_properties**](AborConfigurationApi.md#upsert_abor_configuration_properties) | **POST** /api/api/aborconfiguration/{scope}/{code}/properties/$upsert | [EXPERIMENTAL] UpsertAborConfigurationProperties: Upsert AborConfiguration properties


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.abor_configuration_api import AborConfigurationApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(AborConfigurationApi)
```

---

# **create_abor_configuration**
> AborConfiguration createAborConfiguration = create_abor_configuration(scope, abor_configuration_request)

[EXPERIMENTAL] CreateAborConfiguration: Create an AborConfiguration.

Create the given AborConfiguration.

### Example

```python
api_instance = api_client_factory.build(AborConfigurationApi)
scope = 'scope_example' # str
abor_configuration_request = AborConfigurationRequest()
api_response = api_instance.create_abor_configuration(scope, abor_configuration_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the AborConfiguration. | [required] 
 **abor_configuration_request** | [**AborConfigurationRequest**](AborConfigurationRequest.md)| The definition of the AborConfiguration. | [required] 

### Return type

[**AborConfiguration**](AborConfiguration.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created abor configuration. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_abor_configuration**
> DeletedEntityResponse deleteAborConfiguration = delete_abor_configuration(scope, code)

[EXPERIMENTAL] DeleteAborConfiguration: Delete an AborConfiguration.

Delete the given AborConfiguration.

### Example

```python
api_instance = api_client_factory.build(AborConfigurationApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.delete_abor_configuration(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the AborConfiguration to be deleted. | [required] 
 **code** | **str**| The code of the AborConfiguration to be deleted. Together with the scope this uniquely identifies the AborConfiguration. | [required] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the Abor was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_abor_configuration**
> AborConfiguration getAborConfiguration = get_abor_configuration(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)

[EXPERIMENTAL] GetAborConfiguration: Get AborConfiguration.

Retrieve the definition of a particular AborConfiguration.

### Example

```python
api_instance = api_client_factory.build(AborConfigurationApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.get_abor_configuration(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the AborConfiguration. | [required] 
 **code** | **str**| The code of the AborConfiguration. Together with the scope this uniquely identifies the AborConfiguration. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the AborConfiguration properties. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the AborConfiguration definition. Defaults to returning the latest version of the AborConfiguration definition if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;AborConfiguration&#39; domain to decorate onto the AborConfiguration.              These must take the format {domain}/{scope}/{code}, for example &#39;AborConfiguration/Manager/Id&#39;. If no properties are specified, then no properties will be returned. | [optional] 

### Return type

[**AborConfiguration**](AborConfiguration.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested AborConfiguration definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_abor_configuration_properties**
> AborConfigurationProperties getAborConfigurationProperties = get_abor_configuration_properties(scope, code, effective_at=effective_at, as_at=as_at)

[EXPERIMENTAL] GetAborConfigurationProperties: Get Abor Configuration properties

Get all the properties of a single abor Configuration.

### Example

```python
api_instance = api_client_factory.build(AborConfigurationApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_abor_configuration_properties(scope, code, effective_at=effective_at, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Abor Configuration to list the properties for. | [required] 
 **code** | **str**| The code of the Abor Configuration to list the properties for. Together with the scope this uniquely identifies the Abor Configuration. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to list the Abor Configuration&#39;s properties. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the Abor Configuration&#39;s properties. Defaults to return the latest version of each property if not specified. | [optional] 

### Return type

[**AborConfigurationProperties**](AborConfigurationProperties.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The properties of the specified abor Configuration |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_abor_configurations**
> PagedResourceListOfAborConfiguration listAborConfigurations = list_abor_configurations(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)

[EXPERIMENTAL] ListAborConfigurations: List AborConfiguration.

List all the AborConfiguration matching particular criteria.

### Example

```python
api_instance = api_client_factory.build(AborConfigurationApi)
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.list_abor_configurations(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effective datetime or cut label at which to list the TimeVariant properties for the AborConfiguration. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the AborConfiguration. Defaults to returning the latest version of each AAborConfigurationbor if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing AborConfiguration; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the AborConfiguration type, specify \&quot;id.Code eq &#39;AborConfiguration1&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **property_keys** | [**List[str]**](str.md)| A list of property keys from the &#39;AborConfiguration&#39; domain to decorate onto each AborConfiguration.              These must take the format {domain}/{scope}/{code}, for example &#39;AborConfiguration/Manager/Id&#39;. | [optional] 

### Return type

[**PagedResourceListOfAborConfiguration**](PagedResourceListOfAborConfiguration.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested abor configurations. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **patch_abor_configuration**
> AborConfiguration patchAborConfiguration = patch_abor_configuration(scope, code, operation)

[EXPERIMENTAL] PatchAborConfiguration: Patch Abor Configuration.

Create or update certain fields for a particular AborConfiguration.  The behaviour is defined by the JSON Patch specification.    Currently supported fields are: DisplayName, Description, PostingModuleCodes, CleardownModuleCodes.

### Example

```python
api_instance = api_client_factory.build(AborConfigurationApi)
scope = 'scope_example' # str
code = 'code_example' # str
operation = [{"value":"new name","path":"/displayName","op":"add"},{"value":"newModule","path":"postingModuleCodes/-","op":"add"},{"path":"cleardownModuleCodes/1","op":"remove"}] # List[Operation]
api_response = api_instance.patch_abor_configuration(scope, code, operation)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the AborConfiguration. | [required] 
 **code** | **str**| The code of the AborConfiguration.              Together with the scope this uniquely identifies the AborConfiguration. | [required] 
 **operation** | [**List[Operation]**](Operation.md)| The json patch document. For more information see: https://datatracker.ietf.org/doc/html/rfc6902. | [required] 

### Return type

[**AborConfiguration**](AborConfiguration.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The newly patched AborConfiguration |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_abor_configuration_properties**
> AborConfigurationProperties upsertAborConfigurationProperties = upsert_abor_configuration_properties(scope, code, request_body=request_body)

[EXPERIMENTAL] UpsertAborConfigurationProperties: Upsert AborConfiguration properties

Update or insert one or more properties onto a single AborConfiguration. A property will be updated if it  already exists and inserted if it does not. All properties must be of the domain 'AborConfiguration'.                Upserting a property that exists for an AborConfiguration, with a null value, will delete the instance of the property for that group.                Properties have an <i>effectiveFrom</i> datetime for which the property is valid, and an <i>effectiveUntil</i>  datetime until which the property is valid. Not supplying an <i>effectiveUntil</i> datetime results in the property being  valid indefinitely, or until the next <i>effectiveFrom</i> datetime of the property.

### Example

```python
api_instance = api_client_factory.build(AborConfigurationApi)
scope = 'scope_example' # str
code = 'code_example' # str
request_body = {"Abor/MyScope/FundManagerName":{"key":"Abor/MyScope/FundManagerName","value":{"labelValue":"Smith"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00"},"Abor/MyScope/SomeProperty":{"key":"Abor/MyScope/SomeProperty","value":{"labelValue":"SomeValue"},"effectiveFrom":"2016-01-01T00:00:00.0000000+00:00"},"Abor/MyScope/AnotherProperty":{"key":"Abor/MyScope/AnotherProperty","value":{"labelValue":"AnotherValue"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00","effectiveUntil":"2020-01-01T00:00:00.0000000+00:00"},"Abor/MyScope/ReBalanceInterval":{"key":"Abor/MyScope/ReBalanceInterval","value":{"metricValue":{"value":30.0,"unit":"Days"}}}} # Dict[str, ModelProperty] (optional)
api_response = api_instance.upsert_abor_configuration_properties(scope, code, request_body=request_body)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the AborConfiguration to update or insert the properties onto. | [required] 
 **code** | **str**| The code of the AborConfiguration to update or insert the properties onto. Together with the scope this uniquely identifies the AborConfiguration. | [required] 
 **request_body** | [**Dict[str, ModelProperty]**](ModelProperty.md)| The properties to be updated or inserted onto the chart of account. Each property in               the request must be keyed by its unique property key. This has the format {domain}/{scope}/{code} e.g. \&quot;AborConfiguration/Manager/Id\&quot;. | [optional] 

### Return type

[**AborConfigurationProperties**](AborConfigurationProperties.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated or inserted properties |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

