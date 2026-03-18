# lusid.RelationalDatasetsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_delete_relational_data**](RelationalDatasetsApi.md#batch_delete_relational_data) | **POST** /api/api/relationaldatasets/{relationalDatasetDefinitionScope}/{relationalDatasetDefinitionCode}/$batchDelete | BatchDeleteRelationalData: Batch Delete Relational Data Points for a given Relational Dataset Definition.
[**batch_upsert_relational_data**](RelationalDatasetsApi.md#batch_upsert_relational_data) | **POST** /api/api/relationaldatasets/{relationalDatasetDefinitionScope}/{relationalDatasetDefinitionCode}/$batchUpsert | BatchUpsertRelationalData: Batch Upsert Relational Data Points for a given Relational Dataset Definition.
[**query_relational_data**](RelationalDatasetsApi.md#query_relational_data) | **POST** /api/api/relationaldatasets/{relationalDatasetDefinitionScope}/{relationalDatasetDefinitionCode}/$query | QueryRelationalData: Query Relational Data Points for a given Relational Dataset Definition.


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.relational_datasets_api import RelationalDatasetsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(RelationalDatasetsApi)
```

---

# **batch_delete_relational_data**
> BatchDeleteRelationalDataResponse batchDeleteRelationalData = batch_delete_relational_data(relational_dataset_definition_scope, relational_dataset_definition_code, request_body, success_mode=success_mode)

BatchDeleteRelationalData: Batch Delete Relational Data Points for a given Relational Dataset Definition.

Batch Delete Relational Data Points for a given Relational Dataset Definition.

### Example

```python
api_instance = api_client_factory.build(RelationalDatasetsApi)
relational_dataset_definition_scope = 'relational_dataset_definition_scope_example' # str
relational_dataset_definition_code = 'relational_dataset_definition_code_example' # str
request_body = {"point1":{"dataSeries":{"seriesScope":"SeriesScope","applicableEntity":{"entityType":"Instrument","entityScope":"InstrumentScope","identifierScope":"default","identifierType":"default","identifierValue":"IdentifierValue"},"seriesIdentifiers":{"instrumentId":"SomeValue"}},"effectiveAt":"2019-01-01T12:00:00.0000000+00:00"},"point2":{"dataSeries":{"seriesScope":"SeriesScope","applicableEntity":{"entityType":"Instrument"},"seriesIdentifiers":{}},"effectiveAt":"2019-01-02T12:00:00.0000000+00:00"}} # Dict[str, DeleteRelationalDataPointRequest]
success_mode = 'Partial' # str (optional)
api_response = api_instance.batch_delete_relational_data(relational_dataset_definition_scope, relational_dataset_definition_code, request_body, success_mode=success_mode)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relational_dataset_definition_scope** | **str**| The Scope of the relational dataset definition. | [required] 
 **relational_dataset_definition_code** | **str**| The Code of the relational dataset definition. | [required] 
 **request_body** | [**Dict[str, DeleteRelationalDataPointRequest]**](DeleteRelationalDataPointRequest.md)| The Delete Request. | [required] 
 **success_mode** | **str**| Whether the batch request should fail Atomically or in a Partial fashion - Allowed Values: Atomic, Partial.              Note: If using partial failure modes, then it is important to check the response body for failures as any failures will still return a 200 status code. | [optional] [default to &#39;Partial&#39;]

### Return type

[**BatchDeleteRelationalDataResponse**](BatchDeleteRelationalDataResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The deleted DataPoint metadata. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **batch_upsert_relational_data**
> BatchUpsertRelationalDatasetsResponse batchUpsertRelationalData = batch_upsert_relational_data(relational_dataset_definition_scope, relational_dataset_definition_code, request_body, success_mode=success_mode)

BatchUpsertRelationalData: Batch Upsert Relational Data Points for a given Relational Dataset Definition.

Batch Upsert Relational Data Points for a given Relational Dataset Definition.

### Example

```python
api_instance = api_client_factory.build(RelationalDatasetsApi)
relational_dataset_definition_scope = 'relational_dataset_definition_scope_example' # str
relational_dataset_definition_code = 'relational_dataset_definition_code_example' # str
request_body = {"point1":{"dataSeries":{"seriesScope":"SeriesScope","applicableEntity":{"entityType":"Instrument","entityScope":"InstrumentScope","identifierScope":"default","identifierType":"default","identifierValue":"IdentifierValue"},"seriesIdentifiers":{"instrumentId":"SomeValue"}},"effectiveAt":"2019-01-01T12:00:00.0000000+00:00","valueFields":{"price":100},"metaDataFields":{"currency":"USD"}},"point2":{"dataSeries":{"seriesScope":"SeriesScope","applicableEntity":{"entityType":"Instrument"},"seriesIdentifiers":{"instrumentId":"SomeValue"}},"effectiveAt":"2019-01-02T12:00:00.0000000+00:00","valueFields":{"price":200},"metaDataFields":{"currency":"GBP"}},"point3":{"dataSeries":{"seriesScope":"SeriesScope","applicableEntity":{"entityType":"LegalEntity","entityScope":"LegalEntityScope","identifierScope":"default","identifierType":"default","identifierValue":"IdentifierValue"},"seriesIdentifiers":{"instrumentId":"OtherValue"}},"effectiveAt":"2019-01-01T12:00:00.0000000+00:00","valueFields":{"price":250},"metaDataFields":{"currency":"EUR"}}} # Dict[str, UpsertRelationalDataPointRequest]
success_mode = 'Partial' # str (optional)
api_response = api_instance.batch_upsert_relational_data(relational_dataset_definition_scope, relational_dataset_definition_code, request_body, success_mode=success_mode)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relational_dataset_definition_scope** | **str**| The Scope of the relational dataset definition. | [required] 
 **relational_dataset_definition_code** | **str**| The Code of the relational dataset definition. | [required] 
 **request_body** | [**Dict[str, UpsertRelationalDataPointRequest]**](UpsertRelationalDataPointRequest.md)| The DataPoints to upsert. | [required] 
 **success_mode** | **str**| Whether the batch request should fail Atomically or in a Partial fashion - Allowed Values: Atomic, Partial.              Note: If using partial failure modes, then it is important to check the response body for failures as any failures will still return a 200 status code. | [optional] [default to &#39;Partial&#39;]

### Return type

[**BatchUpsertRelationalDatasetsResponse**](BatchUpsertRelationalDatasetsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The relational data points that were upserted. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **query_relational_data**
> PagedResourceListOfRelationalDataPointResponse queryRelationalData = query_relational_data(relational_dataset_definition_scope, relational_dataset_definition_code, as_at=as_at, effective_at=effective_at, page=page, limit=limit, query_relational_dataset_request=query_relational_dataset_request)

QueryRelationalData: Query Relational Data Points for a given Relational Dataset Definition.

Query Relational Data Points for a given Relational Dataset Definition.

### Example

```python
api_instance = api_client_factory.build(RelationalDatasetsApi)
relational_dataset_definition_scope = 'relational_dataset_definition_scope_example' # str
relational_dataset_definition_code = 'relational_dataset_definition_code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
effective_at = 'effective_at_example' # str (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
query_relational_dataset_request = QueryRelationalDatasetRequest()
api_response = api_instance.query_relational_data(relational_dataset_definition_scope, relational_dataset_definition_code, as_at=as_at, effective_at=effective_at, page=page, limit=limit, query_relational_dataset_request=query_relational_dataset_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relational_dataset_definition_scope** | **str**| The Scope of the relational dataset definition. | [required] 
 **relational_dataset_definition_code** | **str**| The Code of the relational dataset definition. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the dataset(s). Defaults to returning the latest version of each dataset if not specified. | [optional] 
 **effective_at** | **str**| The effective datetime or cut label at which to query the datasets.              Defaults to the current LUSID system datetime if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue query datasets. This value is returned from the previous call.              If a pagination token is provided, the filter, customSortBy, effectiveAt and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **query_relational_dataset_request** | [**QueryRelationalDatasetRequest**](QueryRelationalDatasetRequest.md)| The query request. | [optional] 

### Return type

[**PagedResourceListOfRelationalDataPointResponse**](PagedResourceListOfRelationalDataPointResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The relational data points that were queried. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

