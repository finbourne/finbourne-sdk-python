# lusid.SequencesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sequence**](SequencesApi.md#create_sequence) | **POST** /api/api/sequences/{scope} | [EARLY ACCESS] CreateSequence: Create a new sequence
[**delete_sequence**](SequencesApi.md#delete_sequence) | **DELETE** /api/api/sequences/{scope}/{code} | [EARLY ACCESS] DeleteSequence: Delete a sequence
[**get_sequence**](SequencesApi.md#get_sequence) | **GET** /api/api/sequences/{scope}/{code} | [EARLY ACCESS] GetSequence: Get a specified sequence
[**list_sequences**](SequencesApi.md#list_sequences) | **GET** /api/api/sequences | [EARLY ACCESS] ListSequences: List Sequences
[**next**](SequencesApi.md#next) | **GET** /api/api/sequences/{scope}/{code}/next | [EARLY ACCESS] Next: Get next values from sequence


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.sequences_api import SequencesApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(SequencesApi)
```

---

# **create_sequence**
> SequenceDefinition createSequence = create_sequence(scope, create_sequence_request)

[EARLY ACCESS] CreateSequence: Create a new sequence

Create a new sequence

### Example

```python
api_instance = api_client_factory.build(SequencesApi)
scope = 'scope_example' # str
create_sequence_request = CreateSequenceRequest()
api_response = api_instance.create_sequence(scope, create_sequence_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the sequence. | [required] 
 **create_sequence_request** | [**CreateSequenceRequest**](CreateSequenceRequest.md)| Request to create sequence | [required] 

### Return type

[**SequenceDefinition**](SequenceDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created Sequence |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_sequence**
> DeletedEntityResponse deleteSequence = delete_sequence(scope, code)

[EARLY ACCESS] DeleteSequence: Delete a sequence

Delete a specific sequence                WARNING! Deleting a sequence is an inherently unsafe operation. It would allow a new sequence using the same pattern to be created, which may result in existing values being returned.

### Example

```python
api_instance = api_client_factory.build(SequencesApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.delete_sequence(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the sequence. | [required] 
 **code** | **str**| Code of the sequence. This together with stated scope uniquely identifies the sequence. | [required] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response of the deleted sequence. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_sequence**
> SequenceDefinition getSequence = get_sequence(scope, code)

[EARLY ACCESS] GetSequence: Get a specified sequence

Return the details of a specified sequence

### Example

```python
api_instance = api_client_factory.build(SequencesApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.get_sequence(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the sequence. | [required] 
 **code** | **str**| Code of the sequence. This together with stated scope uniquely              identifies the sequence. | [required] 

### Return type

[**SequenceDefinition**](SequenceDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested sequence |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_sequences**
> PagedResourceListOfSequenceDefinition listSequences = list_sequences(page=page, limit=limit, filter=filter)

[EARLY ACCESS] ListSequences: List Sequences

List sequences which satisfies filtering criteria.

### Example

```python
api_instance = api_client_factory.build(SequencesApi)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
api_response = api_instance.list_sequences(page=page, limit=limit, filter=filter)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| The pagination token to use to continue listing sequences from a previous call to list sequences. This  value is returned from the previous call. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 500 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.               Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**PagedResourceListOfSequenceDefinition**](PagedResourceListOfSequenceDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The sequences matching filtering criteria |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **next**
> NextValueInSequenceResponse next = next(scope, code, batch=batch)

[EARLY ACCESS] Next: Get next values from sequence

Get the next set of values from a specified sequence

### Example

```python
api_instance = api_client_factory.build(SequencesApi)
scope = 'scope_example' # str
code = 'code_example' # str
batch = 56 # int (optional)
api_response = api_instance.next(scope, code, batch=batch)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the sequence. | [required] 
 **code** | **str**| Code of the sequence. This together with stated scope uniquely              identifies the sequence. | [required] 
 **batch** | **int**| Number of sequences items to return for the specified sequence. Default to 1 if not specified. | [optional] 

### Return type

[**NextValueInSequenceResponse**](NextValueInSequenceResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response containing next available values in specified sequence. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

