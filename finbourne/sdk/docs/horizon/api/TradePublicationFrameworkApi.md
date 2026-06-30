# horizon.TradePublicationFrameworkApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tpf_file_deliveries**](TradePublicationFrameworkApi.md#get_tpf_file_deliveries) | **GET** /horizon/api/trade-publication-framework/instances/{instanceId}/deliveries | [EXPERIMENTAL] GetTpfFileDeliveries: Search TPF file deliveries for a specific instance
[**get_tpf_transaction_history_search**](TradePublicationFrameworkApi.md#get_tpf_transaction_history_search) | **GET** /horizon/api/trade-publication-framework/transactions/search | [EXPERIMENTAL] GetTpfTransactionHistorySearch: Endpoint to search TPF transaction by transaction ID and/or instrument identifier, with filtering by instance and date range
[**get_transaction_payload**](TradePublicationFrameworkApi.md#get_transaction_payload) | **GET** /horizon/api/trade-publication-framework/instances/{instanceId}/runs/{runId}/transactions/{transactionId}/payload | [EXPERIMENTAL] GetTransactionPayload: Transaction payload detail
[**list_failed_deliveries**](TradePublicationFrameworkApi.md#list_failed_deliveries) | **GET** /horizon/api/trade-publication-framework/instances/{instanceId}/failed | [EXPERIMENTAL] ListFailedDeliveries: List failed deliveries for a given TPF instance, filtered by resolved state, with pagination support.
[**list_instance_run_history**](TradePublicationFrameworkApi.md#list_instance_run_history) | **GET** /horizon/api/trade-publication-framework/instances/{instanceId}/runs | [EXPERIMENTAL] ListInstanceRunHistory: List run history for a given TPF instance, with pagination support.
[**list_instances_with_status**](TradePublicationFrameworkApi.md#list_instances_with_status) | **GET** /horizon/api/trade-publication-framework/instances | [EXPERIMENTAL] ListInstancesWithStatus: Lists all instances of the Trade Publication Framework (TPF).
[**list_run_files**](TradePublicationFrameworkApi.md#list_run_files) | **GET** /horizon/api/trade-publication-framework/instances/{instanceId}/runs/{runId}/files | [EXPERIMENTAL] ListRunFiles: List Files in a run
[**list_run_transactions**](TradePublicationFrameworkApi.md#list_run_transactions) | **GET** /horizon/api/trade-publication-framework/instances/{instanceId}/runs/{runId}/transactions | [EXPERIMENTAL] ListRunTransactions: List Transactions in a run.
[**replay_transactions**](TradePublicationFrameworkApi.md#replay_transactions) | **POST** /horizon/api/trade-publication-framework/instances/{instanceId}/replay | [EXPERIMENTAL] ReplayTransactions: Replay one or more transactions through a TPF instance
[**resolve_failed_delivery**](TradePublicationFrameworkApi.md#resolve_failed_delivery) | **PUT** /horizon/api/trade-publication-framework/instances/{instanceId}/failed/{batchReferenceId}/resolve | [EXPERIMENTAL] ResolveFailedDelivery: Resolve a failed delivery without retry
[**retry_failed_delivery**](TradePublicationFrameworkApi.md#retry_failed_delivery) | **POST** /horizon/api/trade-publication-framework/instances/{instanceId}/failed/retry | [EXPERIMENTAL] RetryFailedDelivery: Retry failed deliveries for Trade Publication Framework
[**retry_tpf_sftp_delivery**](TradePublicationFrameworkApi.md#retry_tpf_sftp_delivery) | **POST** /horizon/api/trade-publication-framework/instances/{instanceId}/files/{fileId}/retry-sftp | [EXPERIMENTAL] RetryTpfSftpDelivery: Retry SFTP delivery for a previously sent TPF file


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.horizon.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.horizon.api.trade_publication_framework_api import TradePublicationFrameworkApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(TradePublicationFrameworkApi)
```

---

# **get_tpf_file_deliveries**
> PagedResourceListOfTpfFileDeliveryResponse getTpfFileDeliveries = get_tpf_file_deliveries(instance_id, status=status, date_from=date_from, date_to=date_to, limit=limit, page=page)

[EXPERIMENTAL] GetTpfFileDeliveries: Search TPF file deliveries for a specific instance

Retrieve file delivery records for a Trade Publication Framework instance. Returns an aggregated view of file delivery outcomes across all runs. Filterable by delivery status and date range. Supports pagination for large result sets.

### Example

```python
api_instance = api_client_factory.build(TradePublicationFrameworkApi)
instance_id = 'instance_id_example' # str
status = horizon.FileDeliveryStatus() # FileDeliveryStatus (optional)
date_from = '2013-10-20T19:20:30+01:00' # datetime (optional)
date_to = '2013-10-20T19:20:30+01:00' # datetime (optional)
limit = 50 # int (optional)
page = '' # str (optional)
api_response = api_instance.get_tpf_file_deliveries(instance_id, status=status, date_from=date_from, date_to=date_to, limit=limit, page=page)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Integration instance ID | [required] 
 **status** | [**FileDeliveryStatus**](.md)| Filter by delivery status (Completed, Error, Pending) | [optional] 
 **date_from** | **datetime**| Filter deliveries from this time (inclusive) | [optional] 
 **date_to** | **datetime**| Filter deliveries to this time (inclusive) | [optional] 
 **limit** | **int**| Page size for pagination (default 50, max 500) | [optional] [default to 50]
 **page** | **str**| Pagination token from previous response | [optional] [default to &#39;&#39;]

### Return type

[**PagedResourceListOfTpfFileDeliveryResponse**](PagedResourceListOfTpfFileDeliveryResponse.md)

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

# **get_tpf_transaction_history_search**
> PagedResourceListOfTpfTransactionSearchResponse getTpfTransactionHistorySearch = get_tpf_transaction_history_search(transaction_id=transaction_id, instrument_id=instrument_id, date_from=date_from, date_to=date_to, status=status, instance_id=instance_id, page_size=page_size, page_token=page_token)

[EXPERIMENTAL] GetTpfTransactionHistorySearch: Endpoint to search TPF transaction by transaction ID and/or instrument identifier, with filtering by instance and date range

### Example

```python
api_instance = api_client_factory.build(TradePublicationFrameworkApi)
transaction_id = 'transaction_id_example' # str (optional)
instrument_id = 'instrument_id_example' # str (optional)
date_from = 'date_from_example' # str (optional)
date_to = 'date_to_example' # str (optional)
status = 'status_example' # str (optional)
instance_id = 'instance_id_example' # str (optional)
page_size = 400 # int (optional)
page_token = '' # str (optional)
api_response = api_instance.get_tpf_transaction_history_search(transaction_id=transaction_id, instrument_id=instrument_id, date_from=date_from, date_to=date_to, status=status, instance_id=instance_id, page_size=page_size, page_token=page_token)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**|  | [optional] 
 **instrument_id** | **str**|  | [optional] 
 **date_from** | **str**|  | [optional] 
 **date_to** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **instance_id** | **str**|  | [optional] 
 **page_size** | **int**|  | [optional] [default to 400]
 **page_token** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**PagedResourceListOfTpfTransactionSearchResponse**](PagedResourceListOfTpfTransactionSearchResponse.md)

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

# **get_transaction_payload**
> TransactionPayloadResponse getTransactionPayload = get_transaction_payload(instance_id, run_id, transaction_id)

[EXPERIMENTAL] GetTransactionPayload: Transaction payload detail

### Example

```python
api_instance = api_client_factory.build(TradePublicationFrameworkApi)
instance_id = 'instance_id_example' # str
run_id = 'run_id_example' # str
transaction_id = 'transaction_id_example' # str
api_response = api_instance.get_transaction_payload(instance_id, run_id, transaction_id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**|  | [required] 
 **run_id** | **str**|  | [required] 
 **transaction_id** | **str**|  | [required] 

### Return type

[**TransactionPayloadResponse**](TransactionPayloadResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | The requested TPF instance, run, or transaction payload does not exist. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_failed_deliveries**
> PagedResourceListOfFailedDeliveryResponse listFailedDeliveries = list_failed_deliveries(instance_id, resolved=resolved, page=page, page_size=page_size)

[EXPERIMENTAL] ListFailedDeliveries: List failed deliveries for a given TPF instance, filtered by resolved state, with pagination support.

### Example

```python
api_instance = api_client_factory.build(TradePublicationFrameworkApi)
instance_id = 'instance_id_example' # str
resolved = False # bool (optional)
page = '' # str (optional)
page_size = 100 # int (optional)
api_response = api_instance.list_failed_deliveries(instance_id, resolved=resolved, page=page, page_size=page_size)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**|  | [required] 
 **resolved** | **bool**|  | [optional] [default to False]
 **page** | **str**|  | [optional] [default to &#39;&#39;]
 **page_size** | **int**|  | [optional] [default to 100]

### Return type

[**PagedResourceListOfFailedDeliveryResponse**](PagedResourceListOfFailedDeliveryResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | The requested TPF instance does not exist. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_instance_run_history**
> PagedResourceListOfInstanceRunResponse listInstanceRunHistory = list_instance_run_history(instance_id, page=page, page_size=page_size)

[EXPERIMENTAL] ListInstanceRunHistory: List run history for a given TPF instance, with pagination support.

### Example

```python
api_instance = api_client_factory.build(TradePublicationFrameworkApi)
instance_id = 'instance_id_example' # str
page = '' # str (optional)
page_size = 100 # int (optional)
api_response = api_instance.list_instance_run_history(instance_id, page=page, page_size=page_size)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**|  | [required] 
 **page** | **str**|  | [optional] [default to &#39;&#39;]
 **page_size** | **int**|  | [optional] [default to 100]

### Return type

[**PagedResourceListOfInstanceRunResponse**](PagedResourceListOfInstanceRunResponse.md)

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

# **list_instances_with_status**
> InstancesResponse listInstancesWithStatus = list_instances_with_status()

[EXPERIMENTAL] ListInstancesWithStatus: Lists all instances of the Trade Publication Framework (TPF).

### Example

```python
api_instance = api_client_factory.build(TradePublicationFrameworkApi)
api_response = api_instance.list_instances_with_status()
pprint(api_response)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InstancesResponse**](InstancesResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_run_files**
> PagedResourceListOfRunFileResponse listRunFiles = list_run_files(instance_id, run_id, page=page, page_size=page_size)

[EXPERIMENTAL] ListRunFiles: List Files in a run

### Example

```python
api_instance = api_client_factory.build(TradePublicationFrameworkApi)
instance_id = 'instance_id_example' # str
run_id = 'run_id_example' # str
page = '' # str (optional)
page_size = 100 # int (optional)
api_response = api_instance.list_run_files(instance_id, run_id, page=page, page_size=page_size)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**|  | [required] 
 **run_id** | **str**|  | [required] 
 **page** | **str**|  | [optional] [default to &#39;&#39;]
 **page_size** | **int**|  | [optional] [default to 100]

### Return type

[**PagedResourceListOfRunFileResponse**](PagedResourceListOfRunFileResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | The requested TPF instance or run does not exist. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_run_transactions**
> PagedResourceListOfTransactionResponse listRunTransactions = list_run_transactions(instance_id, run_id, status=status, page=page, page_size=page_size)

[EXPERIMENTAL] ListRunTransactions: List Transactions in a run.

### Example

```python
api_instance = api_client_factory.build(TradePublicationFrameworkApi)
instance_id = 'instance_id_example' # str
run_id = 'run_id_example' # str
status = 'status_example' # str (optional)
page = '' # str (optional)
page_size = 100 # int (optional)
api_response = api_instance.list_run_transactions(instance_id, run_id, status=status, page=page, page_size=page_size)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**|  | [required] 
 **run_id** | **str**|  | [required] 
 **status** | **str**|  | [optional] 
 **page** | **str**|  | [optional] [default to &#39;&#39;]
 **page_size** | **int**|  | [optional] [default to 100]

### Return type

[**PagedResourceListOfTransactionResponse**](PagedResourceListOfTransactionResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | The requested TPF instance or run does not exist. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **replay_transactions**
> ReplayTransactionsResponse replayTransactions = replay_transactions(instance_id, replay_transactions_request)

[EXPERIMENTAL] ReplayTransactions: Replay one or more transactions through a TPF instance

### Example

```python
api_instance = api_client_factory.build(TradePublicationFrameworkApi)
instance_id = 'instance_id_example' # str
replay_transactions_request = ReplayTransactionsRequest()
api_response = api_instance.replay_transactions(instance_id, replay_transactions_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**|  | [required] 
 **replay_transactions_request** | [**ReplayTransactionsRequest**](ReplayTransactionsRequest.md)|  | [required] 

### Return type

[**ReplayTransactionsResponse**](ReplayTransactionsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | The requested TPF instance does not exist. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **resolve_failed_delivery**
> ResolveFailedDeliveryResponse resolveFailedDelivery = resolve_failed_delivery(instance_id, batch_reference_id, resolve_failed_delivery_request)

[EXPERIMENTAL] ResolveFailedDelivery: Resolve a failed delivery without retry

### Example

```python
api_instance = api_client_factory.build(TradePublicationFrameworkApi)
instance_id = 'instance_id_example' # str
batch_reference_id = 'batch_reference_id_example' # str
resolve_failed_delivery_request = ResolveFailedDeliveryRequest()
api_response = api_instance.resolve_failed_delivery(instance_id, batch_reference_id, resolve_failed_delivery_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**|  | [required] 
 **batch_reference_id** | **str**|  | [required] 
 **resolve_failed_delivery_request** | [**ResolveFailedDeliveryRequest**](ResolveFailedDeliveryRequest.md)|  | [required] 

### Return type

[**ResolveFailedDeliveryResponse**](ResolveFailedDeliveryResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | No failed delivery was found for the batch. |  -  |
**409** | The failed deliveries for the batch have already been resolved. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **retry_failed_delivery**
> TpfFailedDeliveryResponse retryFailedDelivery = retry_failed_delivery(instance_id, tpf_retry_failed_delivery_request)

[EXPERIMENTAL] RetryFailedDelivery: Retry failed deliveries for Trade Publication Framework

Re-runs the delivery task only (payload already built - skips build task). Always committed - no preview mode. Increments attempt count on failure, sets resolved to true on success. Uses existing ReplayBatchElement on ITradeTrackingRepository. Requires entitlement to execute integrations.

### Example

```python
api_instance = api_client_factory.build(TradePublicationFrameworkApi)
instance_id = 'instance_id_example' # str
tpf_retry_failed_delivery_request = TpfRetryFailedDeliveryRequest()
api_response = api_instance.retry_failed_delivery(instance_id, tpf_retry_failed_delivery_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Integration instance identifier | [required] 
 **tpf_retry_failed_delivery_request** | [**TpfRetryFailedDeliveryRequest**](TpfRetryFailedDeliveryRequest.md)| Request containing batch element reference identifiers to retry | [required] 

### Return type

[**TpfFailedDeliveryResponse**](TpfFailedDeliveryResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | The requested instance does not exist. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **retry_tpf_sftp_delivery**
> TpfRetrySftpResponse retryTpfSftpDelivery = retry_tpf_sftp_delivery(instance_id, file_id)

[EXPERIMENTAL] RetryTpfSftpDelivery: Retry SFTP delivery for a previously sent TPF file

### Example

```python
api_instance = api_client_factory.build(TradePublicationFrameworkApi)
instance_id = 'instance_id_example' # str
file_id = 56 # int
api_response = api_instance.retry_tpf_sftp_delivery(instance_id, file_id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Integration instance ID | [required] 
 **file_id** | **int**| File delivery ID to retry | [required] 

### Return type

[**TpfRetrySftpResponse**](TpfRetrySftpResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retry succeeded - file re-sent to SFTP |  -  |
**400** | The details of the input related failure |  -  |
**404** | File delivery record not found |  -  |
**409** | Duplicate file detected - same hash already delivered to destination |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

