# horizon.TradePublicationFrameworkApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_run_file_content**](TradePublicationFrameworkApi.md#get_run_file_content) | **GET** /horizon/api/trade-publication-framework/instances/{instanceId}/runs/{runId}/files/{fileUuid}/content | [EXPERIMENTAL] GetRunFileContent: Download a file a run delivered, rebuilt from the run&#39;s retained build rows in the instance&#39;s output format
[**get_tpf_file_deliveries**](TradePublicationFrameworkApi.md#get_tpf_file_deliveries) | **GET** /horizon/api/trade-publication-framework/instances/{instanceId}/deliveries | [EXPERIMENTAL] GetTpfFileDeliveries: Search TPF file deliveries for a specific instance
[**get_tpf_transaction_history_search**](TradePublicationFrameworkApi.md#get_tpf_transaction_history_search) | **POST** /horizon/api/trade-publication-framework/transactions/search | [EXPERIMENTAL] GetTpfTransactionHistorySearch: Search TPF transactions by transaction ID(s) and/or instrument identifier(s), with optional filtering by instance, date range, publication status, and a Finbourne Filtering expression. Accepts multiple values in TransactionIds and InstrumentIdentifiers (OR&#39;d within each filter, AND&#39;d between filters). Instrument identifiers are matched exactly against the stored instrument id; Isin, Figi, Ticker, Cusip, Sedol or ClientInternal values are also resolved against LUSID instruments in the default scope. Filterable properties (via the filter body field): transactionId, instanceName, runStartTime, instrumentName, instrumentType, instrumentId, tradeDate, settlementDate, publicationStatus, skipReason, failureReason, fileName, portfolioScope, portfolioCode. Sortable by the same properties. RunStartTime DESC is the default tiebreaker.
[**get_transaction_payload**](TradePublicationFrameworkApi.md#get_transaction_payload) | **GET** /horizon/api/trade-publication-framework/instances/{instanceId}/runs/{runId}/transactions/payload | [EXPERIMENTAL] GetTransactionPayload: Transaction payloads for a run, with pagination support. When transactionId is supplied the single matching payload is returned; otherwise all payloads for the instance/run are returned.
[**list_failed_deliveries**](TradePublicationFrameworkApi.md#list_failed_deliveries) | **GET** /horizon/api/trade-publication-framework/instances/{instanceId}/failed | [EXPERIMENTAL] ListFailedDeliveries: List failed deliveries for a given TPF instance, filtered by resolved state, with pagination support.
[**list_instance_run_history**](TradePublicationFrameworkApi.md#list_instance_run_history) | **GET** /horizon/api/trade-publication-framework/instances/{instanceId}/runs | [EXPERIMENTAL] ListInstanceRunHistory: List run history for a given TPF instance, with pagination support.
[**list_instances_with_status**](TradePublicationFrameworkApi.md#list_instances_with_status) | **GET** /horizon/api/trade-publication-framework/instances | [EXPERIMENTAL] ListInstancesWithStatus: Lists all instances of the Trade Publication Framework (TPF).
[**list_run_files**](TradePublicationFrameworkApi.md#list_run_files) | **GET** /horizon/api/trade-publication-framework/instances/{instanceId}/runs/{runId}/files | [EXPERIMENTAL] ListRunFiles: List the file deliveries of a run, one row per file and destination. Each row&#39;s destinations list holds exactly one element; key rows on fileUuid.
[**list_run_transactions**](TradePublicationFrameworkApi.md#list_run_transactions) | **GET** /horizon/api/trade-publication-framework/instances/{instanceId}/runs/{runId}/transactions | [EXPERIMENTAL] ListRunTransactions: List Transactions in a run.
[**replay_transactions**](TradePublicationFrameworkApi.md#replay_transactions) | **POST** /horizon/api/trade-publication-framework/instances/{instanceId}/replay | [EXPERIMENTAL] ReplayTransactions: Replay one or more transactions through a TPF instance
[**resolve_failed_delivery**](TradePublicationFrameworkApi.md#resolve_failed_delivery) | **PUT** /horizon/api/trade-publication-framework/instances/{instanceId}/failed/{batchReferenceId}/resolve | [EXPERIMENTAL] ResolveFailedDelivery: Resolve a failed delivery without retry
[**retry_tpf_sftp_delivery**](TradePublicationFrameworkApi.md#retry_tpf_sftp_delivery) | **POST** /horizon/api/trade-publication-framework/instances/{instanceId}/files/{fileUuid}/retry-sftp | [EXPERIMENTAL] RetryTpfSftpDelivery: Resend a TPF file to the destination it was delivered to or failed to reach (SFTP or Drive)


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

# **get_run_file_content**
> bytes getRunFileContent = get_run_file_content(instance_id, run_id, file_uuid)

[EXPERIMENTAL] GetRunFileContent: Download a file a run delivered, rebuilt from the run's retained build rows in the instance's output format

Returns the file exactly as the instance built it, so it can be pushed by hand when Horizon cannot. The content is rebuilt the way a resend rebuilds it, so it is only available while the build rows are retained and the response is 410 once retention has purged them. An encrypted instance's file is returned as plaintext.

### Example

```python
api_instance = api_client_factory.build(TradePublicationFrameworkApi)
instance_id = 'instance_id_example' # str
run_id = 'run_id_example' # str
file_uuid = 'file_uuid_example' # str
api_response = api_instance.get_run_file_content(instance_id, run_id, file_uuid)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Integration instance ID. | [required] 
 **run_id** | **str**| Run ID within the instance, or any retry attempt of it. | [required] 
 **file_uuid** | **str**| File delivery UUID, as returned by the run-files listing. | [required] 

### Return type

**bytes**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv, application/xml, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The file as the instance built it, text/csv or application/xml |  -  |
**400** | The details of the input related failure |  -  |
**404** | The requested TPF instance, run or file does not exist. |  -  |
**410** | The build rows the file is rebuilt from have been purged by retention. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_tpf_file_deliveries**
> PagedResourceListOfTpfFileDeliveryResponse getTpfFileDeliveries = get_tpf_file_deliveries(instance_id, status=status, date_from=date_from, date_to=date_to, limit=limit, page=page)

[EXPERIMENTAL] GetTpfFileDeliveries: Search TPF file deliveries for a specific instance

Retrieve file delivery records for a Trade Publication Framework instance. Returns an aggregated view of file delivery outcomes across all runs. Filterable by delivery status and date range. Supports pagination for large result sets.

### Example

```python
api_instance = api_client_factory.build(TradePublicationFrameworkApi)
instance_id = 'instance_id_example' # str
status = horizon.TpfFileDeliveryDisplayStatus() # TpfFileDeliveryDisplayStatus (optional)
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
 **status** | [**TpfFileDeliveryDisplayStatus**](../model/.md)| Filter by delivery outcome (Delivered, Failed, Pending) | [optional] 
 **date_from** | **datetime**| Filter deliveries from this time (inclusive) | [optional] 
 **date_to** | **datetime**| Filter deliveries to this time (inclusive) | [optional] 
 **limit** | **int**| Page size for pagination (default 50, max 500) | [optional] [default to 50]
 **page** | **str**| Pagination token from previous response | [optional] [default to &#39;&#39;]

### Return type

[**PagedResourceListOfTpfFileDeliveryResponse**](../model/PagedResourceListOfTpfFileDeliveryResponse.md)

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
> PagedResourceListOfTpfTransactionSearchResponse getTpfTransactionHistorySearch = get_tpf_transaction_history_search(tpf_transaction_search_request=tpf_transaction_search_request)

[EXPERIMENTAL] GetTpfTransactionHistorySearch: Search TPF transactions by transaction ID(s) and/or instrument identifier(s), with optional filtering by instance, date range, publication status, and a Finbourne Filtering expression. Accepts multiple values in TransactionIds and InstrumentIdentifiers (OR'd within each filter, AND'd between filters). Instrument identifiers are matched exactly against the stored instrument id; Isin, Figi, Ticker, Cusip, Sedol or ClientInternal values are also resolved against LUSID instruments in the default scope. Filterable properties (via the filter body field): transactionId, instanceName, runStartTime, instrumentName, instrumentType, instrumentId, tradeDate, settlementDate, publicationStatus, skipReason, failureReason, fileName, portfolioScope, portfolioCode. Sortable by the same properties. RunStartTime DESC is the default tiebreaker.

### Example

```python
api_instance = api_client_factory.build(TradePublicationFrameworkApi)
tpf_transaction_search_request = TpfTransactionSearchRequest()
api_response = api_instance.get_tpf_transaction_history_search(tpf_transaction_search_request=tpf_transaction_search_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpf_transaction_search_request** | [**TpfTransactionSearchRequest**](../model/TpfTransactionSearchRequest.md)| Search filters, sort order, and pagination options. | [optional] 

### Return type

[**PagedResourceListOfTpfTransactionSearchResponse**](../model/PagedResourceListOfTpfTransactionSearchResponse.md)

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

# **get_transaction_payload**
> PagedResourceListOfTransactionPayload getTransactionPayload = get_transaction_payload(instance_id, run_id, transaction_id=transaction_id, page=page, page_size=page_size, filter=filter, sort_by=sort_by)

[EXPERIMENTAL] GetTransactionPayload: Transaction payloads for a run, with pagination support. When transactionId is supplied the single matching payload is returned; otherwise all payloads for the instance/run are returned.

### Example

```python
api_instance = api_client_factory.build(TradePublicationFrameworkApi)
instance_id = 'instance_id_example' # str
run_id = 'run_id_example' # str
transaction_id = 'transaction_id_example' # str (optional)
page = '' # str (optional)
page_size = 100 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
api_response = api_instance.get_transaction_payload(instance_id, run_id, transaction_id=transaction_id, page=page, page_size=page_size, filter=filter, sort_by=sort_by)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Integration instance ID. | [required] 
 **run_id** | **str**| Run ID within the instance. | [required] 
 **transaction_id** | **str**| Return only this transaction&#39;s payload. Applied together with &lt;i&gt;filter&lt;/i&gt;. | [optional] 
 **page** | **str**| The pagination token from the previous response; &lt;i&gt;filter&lt;/i&gt; and &lt;i&gt;sortBy&lt;/i&gt; must be unchanged. | [optional] [default to &#39;&#39;]
 **page_size** | **int**| Number of results per page. | [optional] [default to 100]
 **filter** | **str**| A Finbourne filter on: transactionId, publicationStatus (Sent, Failed) and the instance&#39;s own output columns, e.g. SIDE eq &#39;B&#39;. Values are compared as text, range operators included, so QTY gt &#39;50&#39; is a text comparison, and null is not accepted. Only output columns named with letters, digits and underscores can be filtered on; the rest can still be sorted. An unknown field is rejected with the fields the run accepts. | [optional] 
 **sort_by** | [**List[str]**](../model/str.md)| Up to two filterable fields, each suffixed \&quot; ASC\&quot; or \&quot; DESC\&quot;. Output columns order nulls, then numbers by value, then the rest as text. Defaults to transactionId ASC. | [optional] 

### Return type

[**PagedResourceListOfTransactionPayload**](../model/PagedResourceListOfTransactionPayload.md)

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

[**PagedResourceListOfFailedDeliveryResponse**](../model/PagedResourceListOfFailedDeliveryResponse.md)

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
> PagedResourceListOfInstanceRunResponse listInstanceRunHistory = list_instance_run_history(instance_id, page=page, page_size=page_size, filter=filter, sort_by=sort_by)

[EXPERIMENTAL] ListInstanceRunHistory: List run history for a given TPF instance, with pagination support.

### Example

```python
api_instance = api_client_factory.build(TradePublicationFrameworkApi)
instance_id = 'instance_id_example' # str
page = '' # str (optional)
page_size = 100 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
api_response = api_instance.list_instance_run_history(instance_id, page=page, page_size=page_size, filter=filter, sort_by=sort_by)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**|  | [required] 
 **page** | **str**| The pagination token from the previous response; &lt;i&gt;filter&lt;/i&gt; and &lt;i&gt;sortBy&lt;/i&gt; must be unchanged. | [optional] [default to &#39;&#39;]
 **page_size** | **int**|  | [optional] [default to 100]
 **filter** | **str**| A Finbourne filter on any response field except duration, e.g. startTime gte &#39;2026-04-01T00:00:00Z&#39; and status eq &#39;Auto-retry&#39;. status is the displayed status. | [optional] 
 **sort_by** | [**List[str]**](../model/str.md)| Up to two filterable fields, each suffixed \&quot; ASC\&quot; or \&quot; DESC\&quot;. Defaults to newest first. | [optional] 

### Return type

[**PagedResourceListOfInstanceRunResponse**](../model/PagedResourceListOfInstanceRunResponse.md)

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

[**InstancesResponse**](../model/InstancesResponse.md)

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
> PagedResourceListOfRunFileResponse listRunFiles = list_run_files(instance_id, run_id, page=page, page_size=page_size, filter=filter, sort_by=sort_by)

[EXPERIMENTAL] ListRunFiles: List the file deliveries of a run, one row per file and destination. Each row's destinations list holds exactly one element; key rows on fileUuid.

### Example

```python
api_instance = api_client_factory.build(TradePublicationFrameworkApi)
instance_id = 'instance_id_example' # str
run_id = 'run_id_example' # str
page = '' # str (optional)
page_size = 100 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
api_response = api_instance.list_run_files(instance_id, run_id, page=page, page_size=page_size, filter=filter, sort_by=sort_by)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Integration instance ID. | [required] 
 **run_id** | **str**| Run ID within the instance. | [required] 
 **page** | **str**| The pagination token from the previous response; &lt;i&gt;filter&lt;/i&gt; and &lt;i&gt;sortBy&lt;/i&gt; must be unchanged. | [optional] [default to &#39;&#39;]
 **page_size** | **int**| Number of results per page. | [optional] [default to 100]
 **filter** | **str**| A Finbourne filter on: fileName, generatedAt, rowCount, fileHash, encrypted, destinationType, destinationPath, destinationName, status, fileUuid, deliveredAt. | [optional] 
 **sort_by** | [**List[str]**](../model/str.md)| Up to two filterable fields, each suffixed \&quot; ASC\&quot; or \&quot; DESC\&quot;. Defaults to newest first (GeneratedAt DESC, Id DESC). | [optional] 

### Return type

[**PagedResourceListOfRunFileResponse**](../model/PagedResourceListOfRunFileResponse.md)

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
> PagedResourceListOfTransactionResponse listRunTransactions = list_run_transactions(instance_id, run_id, status=status, page=page, page_size=page_size, filter=filter, sort_by=sort_by)

[EXPERIMENTAL] ListRunTransactions: List Transactions in a run.

### Example

```python
api_instance = api_client_factory.build(TradePublicationFrameworkApi)
instance_id = 'instance_id_example' # str
run_id = 'run_id_example' # str
status = 'status_example' # str (optional)
page = '' # str (optional)
page_size = 100 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
api_response = api_instance.list_run_transactions(instance_id, run_id, status=status, page=page, page_size=page_size, filter=filter, sort_by=sort_by)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Integration instance ID. | [required] 
 **run_id** | **str**| Run ID within the instance. | [required] 
 **status** | **str**| Filter by publication status (Sent, Skipped, Failed). This is the publication outcome, not the batched-transaction status. | [optional] 
 **page** | **str**| The pagination token from the previous response; &lt;i&gt;filter&lt;/i&gt; and &lt;i&gt;sortBy&lt;/i&gt; must be unchanged. | [optional] [default to &#39;&#39;]
 **page_size** | **int**| Number of results per page. | [optional] [default to 100]
 **filter** | **str**| A Finbourne filter on: transactionId, portfolioScope, portfolioCode, instrumentId, instrumentType, instrumentName, tradeDate, settlementDate, status, skipReason, failureReason, outputFileName, sentAt. The status field here is the batched-transaction status (Complete, Skipped, Failed), not the publication status — use the ?status&#x3D; query parameter for that. | [optional] 
 **sort_by** | [**List[str]**](../model/str.md)| Up to two filterable fields, each suffixed \&quot; ASC\&quot; or \&quot; DESC\&quot;. Defaults to Id ASC. | [optional] 

### Return type

[**PagedResourceListOfTransactionResponse**](../model/PagedResourceListOfTransactionResponse.md)

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
 **replay_transactions_request** | [**ReplayTransactionsRequest**](../model/ReplayTransactionsRequest.md)|  | [required] 

### Return type

[**ReplayTransactionsResponse**](../model/ReplayTransactionsResponse.md)

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
 **resolve_failed_delivery_request** | [**ResolveFailedDeliveryRequest**](../model/ResolveFailedDeliveryRequest.md)|  | [required] 

### Return type

[**ResolveFailedDeliveryResponse**](../model/ResolveFailedDeliveryResponse.md)

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

# **retry_tpf_sftp_delivery**
> TpfRetrySftpResponse retryTpfSftpDelivery = retry_tpf_sftp_delivery(instance_id, file_uuid, confirm_duplicate=confirm_duplicate)

[EXPERIMENTAL] RetryTpfSftpDelivery: Resend a TPF file to the destination it was delivered to or failed to reach (SFTP or Drive)

### Example

```python
api_instance = api_client_factory.build(TradePublicationFrameworkApi)
instance_id = 'instance_id_example' # str
file_uuid = 'file_uuid_example' # str
confirm_duplicate = False # bool (optional)
api_response = api_instance.retry_tpf_sftp_delivery(instance_id, file_uuid, confirm_duplicate=confirm_duplicate)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Integration instance ID | [required] 
 **file_uuid** | **str**| File delivery UUID to retry, as returned by the run-files and file-deliveries listings | [required] 
 **confirm_duplicate** | **bool**| Resend even though the file already reached this destination | [optional] [default to False]

### Return type

[**TpfRetrySftpResponse**](../model/TpfRetrySftpResponse.md)

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

