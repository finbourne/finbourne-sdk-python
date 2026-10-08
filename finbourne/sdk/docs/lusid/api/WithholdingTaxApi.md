# lusid.WithholdingTaxApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_delete_withholding_tax_rates**](WithholdingTaxApi.md#batch_delete_withholding_tax_rates) | **POST** /api/api/withholdingtax/rates/{scope}/{code}/$batchDelete | [EARLY ACCESS] BatchDeleteWithholdingTaxRates: Batch delete Withholding Tax rate rows from a rate dataset.
[**batch_upsert_withholding_tax_rates**](WithholdingTaxApi.md#batch_upsert_withholding_tax_rates) | **POST** /api/api/withholdingtax/rates/{scope}/{code}/$batchUpsert | [EARLY ACCESS] BatchUpsertWithholdingTaxRates: Batch upsert Withholding Tax rate rows, applying the write-time gates before any row lands.
[**create_withholding_tax_dataset_definitions**](WithholdingTaxApi.md#create_withholding_tax_dataset_definitions) | **POST** /api/api/withholdingtax/datasetdefinitions | [EARLY ACCESS] CreateWithholdingTaxDatasetDefinitions: Create the Withholding Tax dataset definitions.
[**delete_withholding_tax_configuration**](WithholdingTaxApi.md#delete_withholding_tax_configuration) | **DELETE** /api/api/withholdingtax/configurations/{scope}/{code} | [EARLY ACCESS] DeleteWithholdingTaxConfiguration: Delete a Withholding Tax Configuration.
[**delete_withholding_tax_dataset_definition**](WithholdingTaxApi.md#delete_withholding_tax_dataset_definition) | **DELETE** /api/api/withholdingtax/datasetdefinitions/{scope}/{code} | [EARLY ACCESS] DeleteWithholdingTaxDatasetDefinition: Delete a Withholding Tax dataset definition.
[**get_withholding_tax_configuration**](WithholdingTaxApi.md#get_withholding_tax_configuration) | **GET** /api/api/withholdingtax/configurations/{scope}/{code} | [EARLY ACCESS] GetWithholdingTaxConfiguration: Get a Withholding Tax Configuration.
[**get_withholding_tax_dataset_definition**](WithholdingTaxApi.md#get_withholding_tax_dataset_definition) | **GET** /api/api/withholdingtax/datasetdefinitions/{scope}/{code} | [EARLY ACCESS] GetWithholdingTaxDatasetDefinition: Get a Withholding Tax dataset definition.
[**list_withholding_tax_configurations**](WithholdingTaxApi.md#list_withholding_tax_configurations) | **GET** /api/api/withholdingtax/configurations | [EARLY ACCESS] ListWithholdingTaxConfigurations: List Withholding Tax Configurations.
[**list_withholding_tax_dataset_definitions**](WithholdingTaxApi.md#list_withholding_tax_dataset_definitions) | **GET** /api/api/withholdingtax/datasetdefinitions | [EARLY ACCESS] ListWithholdingTaxDatasetDefinitions: List Withholding Tax dataset definitions.
[**patch_withholding_tax_dataset_definition**](WithholdingTaxApi.md#patch_withholding_tax_dataset_definition) | **PATCH** /api/api/withholdingtax/datasetdefinitions/{scope}/{code} | [EARLY ACCESS] PatchWithholdingTaxDatasetDefinition: Patch a Withholding Tax dataset definition.
[**upsert_withholding_tax_configuration**](WithholdingTaxApi.md#upsert_withholding_tax_configuration) | **POST** /api/api/withholdingtax/configurations/{scope}/{code} | [EARLY ACCESS] UpsertWithholdingTaxConfiguration: Upsert a Withholding Tax Configuration.


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.withholding_tax_api import WithholdingTaxApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(WithholdingTaxApi)
```

---

# **batch_delete_withholding_tax_rates**
> BatchDeleteRelationalDataResponse batchDeleteWithholdingTaxRates = batch_delete_withholding_tax_rates(scope, code, request_body, success_mode=success_mode)

[EARLY ACCESS] BatchDeleteWithholdingTaxRates: Batch delete Withholding Tax rate rows from a rate dataset.

Also how a rate with no replacement is expired, there being no effectiveTo field. Deletes are  bitemporal, so rows stay readable at a prior asAt.

### Example

```python
api_instance = api_client_factory.build(WithholdingTaxApi)
scope = 'scope_example' # str
code = 'code_example' # str
request_body = {"gb-treaty-us":{"seriesIdentifiers":{"taxCountry":"GB","profileType":"TreatyEligible","instrumentDomicile":"US"},"effectiveAt":"2026-01-01T00:00:00.0000000+00:00"}} # Dict[str, DeleteWithholdingTaxRateRequest]
success_mode = 'Atomic' # str (optional)
api_response = api_instance.batch_delete_withholding_tax_rates(scope, code, request_body, success_mode=success_mode)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The Scope of the rate dataset&#39;s relational dataset definition. | [required] 
 **code** | **str**| The Code of the rate dataset&#39;s relational dataset definition. | [required] 
 **request_body** | [**Dict[str, DeleteWithholdingTaxRateRequest]**](../model/DeleteWithholdingTaxRateRequest.md)| The rate rows to delete, keyed by a correlation id echoed back in the response. | [required] 
 **success_mode** | **str**| Atomic or Partial; defaults to Atomic. In Partial mode failures are returned              in the response body with a 200 status. | [optional] [default to &#39;Atomic&#39;]

### Return type

[**BatchDeleteRelationalDataResponse**](../model/BatchDeleteRelationalDataResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The deleted rate row metadata. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **batch_upsert_withholding_tax_rates**
> BatchUpsertWithholdingTaxRatesResponse batchUpsertWithholdingTaxRates = batch_upsert_withholding_tax_rates(scope, code, request_body, success_mode=success_mode)

[EARLY ACCESS] BatchUpsertWithholdingTaxRates: Batch upsert Withholding Tax rate rows, applying the write-time gates before any row lands.

Row identity is the matching dimensions plus effectiveAt; a rate is superseded by loading a row with a  later effectiveAt for the same dimensions.

### Example

```python
api_instance = api_client_factory.build(WithholdingTaxApi)
scope = 'scope_example' # str
code = 'code_example' # str
request_body = {"gb-treaty-us":{"seriesIdentifiers":{"taxCountry":"GB","profileType":"TreatyEligible","instrumentDomicile":"US"},"effectiveAt":"2026-01-01T00:00:00.0000000+00:00","valueFields":{"countryRate":0.3,"treatyRate":0.15,"treatyRAS":true}},"gb-treaty-fr":{"seriesIdentifiers":{"taxCountry":"GB","profileType":"TreatyEligible","instrumentDomicile":"FR"},"effectiveAt":"2026-01-01T00:00:00.0000000+00:00","valueFields":{"countryRate":0.25,"treatyRate":0.15,"treatyRAS":false}}} # Dict[str, UpsertWithholdingTaxRateRequest]
success_mode = 'Atomic' # str (optional)
api_response = api_instance.batch_upsert_withholding_tax_rates(scope, code, request_body, success_mode=success_mode)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The Scope of the rate dataset&#39;s relational dataset definition. | [required] 
 **code** | **str**| The Code of the rate dataset&#39;s relational dataset definition. | [required] 
 **request_body** | [**Dict[str, UpsertWithholdingTaxRateRequest]**](../model/UpsertWithholdingTaxRateRequest.md)| The rate rows to upsert, keyed by a correlation id echoed back in the response. | [required] 
 **success_mode** | **str**| Atomic or Partial; defaults to Atomic, because a partly loaded feed silently              under-withholds. In Partial mode failures are returned in the response body with a 200 status. | [optional] [default to &#39;Atomic&#39;]

### Return type

[**BatchUpsertWithholdingTaxRatesResponse**](../model/BatchUpsertWithholdingTaxRatesResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Withholding Tax rate rows that were upserted. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **create_withholding_tax_dataset_definitions**
> WithholdingTaxDatasetDefinitions createWithholdingTaxDatasetDefinitions = create_withholding_tax_dataset_definitions(create_withholding_tax_dataset_definitions_request)

[EARLY ACCESS] CreateWithholdingTaxDatasetDefinitions: Create the Withholding Tax dataset definitions.

Create the anomaly and the main relational dataset definition for a customer domain, in a single call.                The definitions are constructed rather than accepted as given, so the fields the engine reads by name cannot  be absent, misspelled or created in the wrong field category. LUSID adds the mandatory core to both: taxCountry  and profileType as series identifiers, countryRate, treatyRate, betterRate and enhancedRate as value fields,  treatyRAS, betterRAS and enhancedRAS as value fields, and rank as a value field on the anomaly definition only.                The caller supplies only their own matching dimensions, given per dataset. The two schemas need not be  identical: a dimension present on only one dataset is simply not matched on when the other is queried, an ISIN  dimension on the anomaly dataset alone being the usual case. The request is rejected if it names a dimension  that collides with a mandatory core field, or if it omits a scope or a code.

### Example

```python
api_instance = api_client_factory.build(WithholdingTaxApi)
create_withholding_tax_dataset_definitions_request = CreateWithholdingTaxDatasetDefinitionsRequest()
api_response = api_instance.create_withholding_tax_dataset_definitions(create_withholding_tax_dataset_definitions_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_withholding_tax_dataset_definitions_request** | [**CreateWithholdingTaxDatasetDefinitionsRequest**](../model/CreateWithholdingTaxDatasetDefinitionsRequest.md)| The scope, code and matching dimensions of each of the two datasets to create. | [required] 

### Return type

[**WithholdingTaxDatasetDefinitions**](../model/WithholdingTaxDatasetDefinitions.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created anomaly and main relational dataset definitions. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_withholding_tax_configuration**
> DeletedEntityResponse deleteWithholdingTaxConfiguration = delete_withholding_tax_configuration(scope, code)

[EARLY ACCESS] DeleteWithholdingTaxConfiguration: Delete a Withholding Tax Configuration.

Delete the Withholding Tax Configuration at the given scope and code. Rejected if a portfolio, fund or share  class still references the configuration, rather than orphaning those references.

### Example

```python
api_instance = api_client_factory.build(WithholdingTaxApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.delete_withholding_tax_configuration(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Withholding Tax Configuration to be deleted. | [required] 
 **code** | **str**| The code of the Withholding Tax Configuration to be deleted. Together with the scope this uniquely identifies the configuration. | [required] 

### Return type

[**DeletedEntityResponse**](../model/DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the Withholding Tax Configuration was deleted. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_withholding_tax_dataset_definition**
> DeletedEntityResponse deleteWithholdingTaxDatasetDefinition = delete_withholding_tax_dataset_definition(scope, code)

[EARLY ACCESS] DeleteWithholdingTaxDatasetDefinition: Delete a Withholding Tax dataset definition.

Delete one Withholding Tax relational dataset definition, subject to the platform's own rules on what may be  changed on a populated dataset.

### Example

```python
api_instance = api_client_factory.build(WithholdingTaxApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.delete_withholding_tax_dataset_definition(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the dataset definition to be deleted. | [required] 
 **code** | **str**| The code of the dataset definition to be deleted. Together with the scope this uniquely identifies the definition. | [required] 

### Return type

[**DeletedEntityResponse**](../model/DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the relational dataset definition was deleted. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_withholding_tax_configuration**
> WithholdingTaxConfiguration getWithholdingTaxConfiguration = get_withholding_tax_configuration(scope, code, as_at=as_at)

[EARLY ACCESS] GetWithholdingTaxConfiguration: Get a Withholding Tax Configuration.

Retrieve a single Withholding Tax Configuration by scope and code.

### Example

```python
api_instance = api_client_factory.build(WithholdingTaxApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_withholding_tax_configuration(scope, code, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Withholding Tax Configuration. | [required] 
 **code** | **str**| The code of the Withholding Tax Configuration. Together with the scope this uniquely identifies the configuration. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Withholding Tax Configuration. Defaults to returning the latest version if not specified. | [optional] 

### Return type

[**WithholdingTaxConfiguration**](../model/WithholdingTaxConfiguration.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Withholding Tax Configuration. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_withholding_tax_dataset_definition**
> WithholdingTaxDataset getWithholdingTaxDatasetDefinition = get_withholding_tax_dataset_definition(scope, code, as_at=as_at)

[EARLY ACCESS] GetWithholdingTaxDatasetDefinition: Get a Withholding Tax dataset definition.

Retrieve one Withholding Tax dataset definition by scope and code, in the same shape the create returns: the  matching dimensions the caller supplied. The mandatory core is not returned here; read the full field schema  from the relational dataset definition at the returned href.

### Example

```python
api_instance = api_client_factory.build(WithholdingTaxApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_withholding_tax_dataset_definition(scope, code, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the dataset definition. | [required] 
 **code** | **str**| The code of the dataset definition. Together with the scope this uniquely identifies the definition. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the dataset definition. Defaults to returning the latest version if not specified. | [optional] 

### Return type

[**WithholdingTaxDataset**](../model/WithholdingTaxDataset.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Withholding Tax dataset definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_withholding_tax_configurations**
> PagedResourceListOfWithholdingTaxConfiguration listWithholdingTaxConfigurations = list_withholding_tax_configurations(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

[EARLY ACCESS] ListWithholdingTaxConfigurations: List Withholding Tax Configurations.

List the Withholding Tax Configurations across every scope the caller is entitled to. To list the  configurations of a single scope, filter on the scope.

### Example

```python
api_instance = api_client_factory.build(WithholdingTaxApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
api_response = api_instance.list_withholding_tax_configurations(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the Withholding Tax Configurations. Defaults to returning the latest version of each configuration if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Withholding Tax Configurations; this value is              returned from the previous call. If a pagination token is provided, the filter and asAt fields must not have              changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. For example, to filter on the scope, specify              \&quot;id.Scope eq &#39;WithholdingTax&#39;\&quot;, and to filter on the code, specify \&quot;id.Code eq &#39;UK-LIFE-BLAGAB&#39;\&quot;. For more              information about filtering results, see              https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](../model/str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 

### Return type

[**PagedResourceListOfWithholdingTaxConfiguration**](../model/PagedResourceListOfWithholdingTaxConfiguration.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Withholding Tax Configurations. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_withholding_tax_dataset_definitions**
> PagedResourceListOfWithholdingTaxDataset listWithholdingTaxDatasetDefinitions = list_withholding_tax_dataset_definitions(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

[EARLY ACCESS] ListWithholdingTaxDatasetDefinitions: List Withholding Tax dataset definitions.

List the Withholding Tax dataset definitions across every scope the caller is entitled to, each in the same  shape the create returns. To list the definitions of a single scope, filter on the scope.

### Example

```python
api_instance = api_client_factory.build(WithholdingTaxApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
api_response = api_instance.list_withholding_tax_dataset_definitions(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the dataset definitions. Defaults to returning the latest version of each definition if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing dataset definitions; this value is returned              from the previous call. If a pagination token is provided, the filter and asAt fields must not have changed              since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. For example, to filter on the scope, specify              \&quot;scope eq &#39;WithholdingTax&#39;\&quot;, and to filter on the code, specify \&quot;code eq &#39;wht-main-rates&#39;\&quot;. For more              information about filtering results, see              https://support.lusid.com/docs/filtering-information-retrieved-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](../model/str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 

### Return type

[**PagedResourceListOfWithholdingTaxDataset**](../model/PagedResourceListOfWithholdingTaxDataset.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Withholding Tax dataset definitions. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **patch_withholding_tax_dataset_definition**
> WithholdingTaxDataset patchWithholdingTaxDatasetDefinition = patch_withholding_tax_dataset_definition(scope, code, operation)

[EARLY ACCESS] PatchWithholdingTaxDatasetDefinition: Patch a Withholding Tax dataset definition.

Amend one Withholding Tax relational dataset definition, adding a matching dimension being the common case.  Subject to the platform's own rules on what may be changed on a populated dataset.                Only the matching dimensions the document addresses are affected; a dimension it does not address is left as  it is. Append a dimension with an add on \"/dimensions/-\", insert one at a position with an add on its index,  and remove one with a remove on its index. To amend a dimension, remove it and add it again.                A dimension whose name collides with a mandatory core field is rejected, as is any attempt to add a rate tier:  the tier set is fixed at four and cannot be extended by schema evolution, because the engine could never read  a tier it does not know by name. The mandatory core is not addressable by this endpoint at all.                The amended dataset is returned in the same shape the get and the list return: the matching dimensions alone.  Read the full field schema from the relational dataset definition at the returned href.  The behaviour is defined by the JSON Patch specification.    Currently supported fields are: Dimensions.

### Example

```python
api_instance = api_client_factory.build(WithholdingTaxApi)
scope = 'scope_example' # str
code = 'code_example' # str
operation = [{"value":{"fieldName":"isin","displayName":"ISIN","description":"The ISIN of the instrument the rate row applies to.","dataTypeId":{"scope":"system","code":"string"}},"path":"/dimensions/-","op":"add"}] # List[Operation]
api_response = api_instance.patch_withholding_tax_dataset_definition(scope, code, operation)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the dataset definition to amend. | [required] 
 **code** | **str**| The code of the dataset definition to amend. Together with the scope this uniquely identifies the definition. | [required] 
 **operation** | [**List[Operation]**](../model/Operation.md)| The json patch document. For more information see: https://datatracker.ietf.org/doc/html/rfc6902. | [required] 

### Return type

[**WithholdingTaxDataset**](../model/WithholdingTaxDataset.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The amended Withholding Tax dataset. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_withholding_tax_configuration**
> WithholdingTaxConfiguration upsertWithholdingTaxConfiguration = upsert_withholding_tax_configuration(scope, code, upsert_withholding_tax_configuration_request)

[EARLY ACCESS] UpsertWithholdingTaxConfiguration: Upsert a Withholding Tax Configuration.

Create or replace the Withholding Tax Configuration at the given scope and code. The write is a full replace  on the object rather than a partial update, so the request must carry the complete configuration.                The write is rejected if either referenced dataset does not exist, if either is missing a mandatory core field  or has one in the wrong field category, if any customer-defined dimension in either dataset has no value source  declaration, or if a declaration names a dimension neither dataset has. Errors name the specific field.

### Example

```python
api_instance = api_client_factory.build(WithholdingTaxApi)
scope = 'scope_example' # str
code = 'code_example' # str
upsert_withholding_tax_configuration_request = UpsertWithholdingTaxConfigurationRequest()
api_response = api_instance.upsert_withholding_tax_configuration(scope, code, upsert_withholding_tax_configuration_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Withholding Tax Configuration. | [required] 
 **code** | **str**| The code of the Withholding Tax Configuration. Together with the scope this uniquely identifies the configuration. | [required] 
 **upsert_withholding_tax_configuration_request** | [**UpsertWithholdingTaxConfigurationRequest**](../model/UpsertWithholdingTaxConfigurationRequest.md)| The complete Withholding Tax Configuration to create or replace. | [required] 

### Return type

[**WithholdingTaxConfiguration**](../model/WithholdingTaxConfiguration.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created or replaced Withholding Tax Configuration. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

