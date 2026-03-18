# lusid.InstrumentEventTypesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_transaction_template**](InstrumentEventTypesApi.md#create_transaction_template) | **POST** /api/api/instrumenteventtypes/{instrumentEventType}/transactiontemplates/{instrumentType}/{scope} | CreateTransactionTemplate: Create Transaction Template
[**delete_transaction_template**](InstrumentEventTypesApi.md#delete_transaction_template) | **DELETE** /api/api/instrumenteventtypes/{instrumentEventType}/transactiontemplates/{instrumentType}/{scope} | DeleteTransactionTemplate: Delete Transaction Template
[**get_transaction_template**](InstrumentEventTypesApi.md#get_transaction_template) | **GET** /api/api/instrumenteventtypes/{instrumentEventType}/transactiontemplates/{instrumentType}/{scope} | GetTransactionTemplate: Get Transaction Template
[**get_transaction_template_specification**](InstrumentEventTypesApi.md#get_transaction_template_specification) | **GET** /api/api/instrumenteventtypes/{instrumentEventType}/transactiontemplatespecification | GetTransactionTemplateSpecification: Get Transaction Template Specification.
[**list_transaction_template_specifications**](InstrumentEventTypesApi.md#list_transaction_template_specifications) | **GET** /api/api/instrumenteventtypes/transactiontemplatespecifications | ListTransactionTemplateSpecifications: List Transaction Template Specifications.
[**list_transaction_templates**](InstrumentEventTypesApi.md#list_transaction_templates) | **GET** /api/api/instrumenteventtypes/transactiontemplates | ListTransactionTemplates: List Transaction Templates
[**update_transaction_template**](InstrumentEventTypesApi.md#update_transaction_template) | **PUT** /api/api/instrumenteventtypes/{instrumentEventType}/transactiontemplates/{instrumentType}/{scope} | UpdateTransactionTemplate: Update Transaction Template


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.instrument_event_types_api import InstrumentEventTypesApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(InstrumentEventTypesApi)
```

---

# **create_transaction_template**
> TransactionTemplate createTransactionTemplate = create_transaction_template(instrument_event_type, instrument_type, scope, transaction_template_request)

CreateTransactionTemplate: Create Transaction Template

Create a transaction template for a particular instrument event type in a scope.

### Example

```python
api_instance = api_client_factory.build(InstrumentEventTypesApi)
instrument_event_type = 'instrument_event_type_example' # str
instrument_type = 'instrument_type_example' # str
scope = 'scope_example' # str
transaction_template_request = TransactionTemplateRequest()
api_response = api_instance.create_transaction_template(instrument_event_type, instrument_type, scope, transaction_template_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_event_type** | **str**| The type of instrument events that the template is applied to. | [required] 
 **instrument_type** | **str**| The instrument type of the transaction template. The combination of the instrument              event type, instrument type and scope uniquely identifies a transaction template | [required] 
 **scope** | **str**| The scope in which the template lies. | [required] 
 **transaction_template_request** | [**TransactionTemplateRequest**](TransactionTemplateRequest.md)| A request defining a new transaction template to be created. | [required] 

### Return type

[**TransactionTemplate**](TransactionTemplate.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The response of the transaction template that was created. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_transaction_template**
> datetime deleteTransactionTemplate = delete_transaction_template(instrument_event_type, instrument_type, scope)

DeleteTransactionTemplate: Delete Transaction Template

Delete a transaction template for a particular instrument event type in a scope.

### Example

```python
api_instance = api_client_factory.build(InstrumentEventTypesApi)
instrument_event_type = 'instrument_event_type_example' # str
instrument_type = 'instrument_type_example' # str
scope = 'scope_example' # str
api_response = api_instance.delete_transaction_template(instrument_event_type, instrument_type, scope)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_event_type** | **str**| The type of instrument events that the template is applied to. | [required] 
 **instrument_type** | **str**| The instrument type of the transaction template. The combination of the instrument              event type, instrument type and scope uniquely identifies a transaction template | [required] 
 **scope** | **str**| The scope of the template. | [required] 

### Return type

**datetime**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The AsAt Time the Template was deleted. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_transaction_template**
> TransactionTemplate getTransactionTemplate = get_transaction_template(instrument_event_type, instrument_type, scope, as_at=as_at)

GetTransactionTemplate: Get Transaction Template

Gets the Transaction Template that for the instrument event type within the scope specified.

### Example

```python
api_instance = api_client_factory.build(InstrumentEventTypesApi)
instrument_event_type = 'instrument_event_type_example' # str
instrument_type = 'instrument_type_example' # str
scope = 'scope_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_transaction_template(instrument_event_type, instrument_type, scope, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_event_type** | **str**| The instrument event type of the transaction template | [required] 
 **instrument_type** | **str**| The instrument type of the transaction template. The combination of the instrument              event type, instrument type and scope uniquely identifies a transaction template | [required] 
 **scope** | **str**| The scope in which the template lies. When not supplied the scope is &#39;default&#39;. | [required] 
 **as_at** | **datetime**| The AsAt time of the requested Transaction Template | [optional] 

### Return type

[**TransactionTemplate**](TransactionTemplate.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The transaction template. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_transaction_template_specification**
> TransactionTemplateSpecification getTransactionTemplateSpecification = get_transaction_template_specification(instrument_event_type)

GetTransactionTemplateSpecification: Get Transaction Template Specification.

Retrieve the transaction template specification for a particular event type.

### Example

```python
api_instance = api_client_factory.build(InstrumentEventTypesApi)
instrument_event_type = 'instrument_event_type_example' # str
api_response = api_instance.get_transaction_template_specification(instrument_event_type)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_event_type** | **str**| The requested instrument event type. | [required] 

### Return type

[**TransactionTemplateSpecification**](TransactionTemplateSpecification.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Transaction Template Specification. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_transaction_template_specifications**
> PagedResourceListOfTransactionTemplateSpecification listTransactionTemplateSpecifications = list_transaction_template_specifications(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

ListTransactionTemplateSpecifications: List Transaction Template Specifications.

Retrieves all transaction template specifications.

### Example

```python
api_instance = api_client_factory.build(InstrumentEventTypesApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
api_response = api_instance.list_transaction_template_specifications(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| AsAt of the request | [optional] 
 **page** | **str**| The pagination token to use to continue listing Transaction Template Specifications from              a previous call to list Transaction Template Specifications.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, and asAt              fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 

### Return type

[**PagedResourceListOfTransactionTemplateSpecification**](PagedResourceListOfTransactionTemplateSpecification.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Transaction Template Specifications. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_transaction_templates**
> PagedResourceListOfTransactionTemplate listTransactionTemplates = list_transaction_templates(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

ListTransactionTemplates: List Transaction Templates

Lists all Transaction Templates.

### Example

```python
api_instance = api_client_factory.build(InstrumentEventTypesApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
api_response = api_instance.list_transaction_templates(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The AsAt time at which to retrieve the Transaction Templates | [optional] 
 **page** | **str**| The pagination token to use to continue listing Transaction Templates from a previous call to list Transaction Templates.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, limit, and asAt fields              must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 

### Return type

[**PagedResourceListOfTransactionTemplate**](PagedResourceListOfTransactionTemplate.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The transaction templates. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_transaction_template**
> TransactionTemplate updateTransactionTemplate = update_transaction_template(instrument_event_type, instrument_type, scope, transaction_template_request)

UpdateTransactionTemplate: Update Transaction Template

Update a transaction template for a particular instrument event type in a scope.

### Example

```python
api_instance = api_client_factory.build(InstrumentEventTypesApi)
instrument_event_type = 'instrument_event_type_example' # str
instrument_type = 'instrument_type_example' # str
scope = 'scope_example' # str
transaction_template_request = TransactionTemplateRequest()
api_response = api_instance.update_transaction_template(instrument_event_type, instrument_type, scope, transaction_template_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_event_type** | **str**| The type of instrument events that the template is applied to. | [required] 
 **instrument_type** | **str**| The instrument type of the transaction template. The combination of the instrument              event type, instrument type and scope uniquely identifies a transaction template | [required] 
 **scope** | **str**| The scope in which the template lies. | [required] 
 **transaction_template_request** | [**TransactionTemplateRequest**](TransactionTemplateRequest.md)| A request defining the updated values for the transaction template. | [required] 

### Return type

[**TransactionTemplate**](TransactionTemplate.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response of the transaction template that was updated. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

