# lusid.OrderManagementApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**book_transactions**](OrderManagementApi.md#book_transactions) | **POST** /api/api/ordermanagement/booktransactions | BookTransactions: Books transactions using specific allocations as a source.
[**cancel_orders**](OrderManagementApi.md#cancel_orders) | **POST** /api/api/ordermanagement/cancelorders | [EARLY ACCESS] CancelOrders: Cancel existing orders
[**cancel_orders_and_move_remaining**](OrderManagementApi.md#cancel_orders_and_move_remaining) | **POST** /api/api/ordermanagement/cancelordersandmoveremaining | [EARLY ACCESS] CancelOrdersAndMoveRemaining: Cancel existing orders and move any unplaced quantities to new orders in new blocks
[**cancel_placements**](OrderManagementApi.md#cancel_placements) | **POST** /api/api/ordermanagement/$cancelplacements | [EARLY ACCESS] CancelPlacements: Cancel existing placements
[**create_orders**](OrderManagementApi.md#create_orders) | **POST** /api/api/ordermanagement/createorders | CreateOrders: Upsert a Block and associated orders
[**get_order_history**](OrderManagementApi.md#get_order_history) | **GET** /api/api/ordermanagement/order/{scope}/{code}/$history | GetOrderHistory: Get the history of an order and related entity changes
[**move_orders**](OrderManagementApi.md#move_orders) | **POST** /api/api/ordermanagement/moveorders | [EARLY ACCESS] MoveOrders: Move orders to new or existing block
[**place_blocks**](OrderManagementApi.md#place_blocks) | **POST** /api/api/ordermanagement/placeblocks | [EARLY ACCESS] PlaceBlocks: Places blocks for a given list of placement requests.
[**run_allocation_service**](OrderManagementApi.md#run_allocation_service) | **POST** /api/api/ordermanagement/allocate | RunAllocationService: Runs the Allocation Service
[**run_allocation_service_with_weights**](OrderManagementApi.md#run_allocation_service_with_weights) | **POST** /api/api/ordermanagement/allocate/weighted | [EXPERIMENTAL] RunAllocationServiceWithWeights: Runs the Allocation Service with portfolio weights
[**sweep_blocks**](OrderManagementApi.md#sweep_blocks) | **POST** /api/api/ordermanagement/SweepBlocks | [EXPERIMENTAL] SweepBlocks: Sweeps specified blocks, for each block that meets the requirements. The request may be partially successful.
[**update_orders**](OrderManagementApi.md#update_orders) | **POST** /api/api/ordermanagement/updateorders | [EARLY ACCESS] UpdateOrders: Update existing orders
[**update_placements**](OrderManagementApi.md#update_placements) | **POST** /api/api/ordermanagement/$updateplacements | [EARLY ACCESS] UpdatePlacements: Update existing placements


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.order_management_api import OrderManagementApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(OrderManagementApi)
```

---

# **book_transactions**
> BookTransactionsResponse bookTransactions = book_transactions(book_transactions_request, apply_fees_and_commission=apply_fees_and_commission, mark_orders_and_allocations_as_booked=mark_orders_and_allocations_as_booked)

BookTransactions: Books transactions using specific allocations as a source.

Takes a collection of allocation IDs, and maps fields from those allocations and related orders onto new transactions.

### Example

```python
api_instance = api_client_factory.build(OrderManagementApi)
book_transactions_request = BookTransactionsRequest()
apply_fees_and_commission = True # bool (optional)
mark_orders_and_allocations_as_booked = False # bool (optional)
api_response = api_instance.book_transactions(book_transactions_request, apply_fees_and_commission=apply_fees_and_commission, mark_orders_and_allocations_as_booked=mark_orders_and_allocations_as_booked)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_transactions_request** | [**BookTransactionsRequest**](BookTransactionsRequest.md)| The allocations to create transactions for | [required] 
 **apply_fees_and_commission** | **bool**| Whether to apply fees and commissions to transactions (default: true) | [optional] [default to True]
 **mark_orders_and_allocations_as_booked** | **bool**| Whether to mark allocations and fully-booked orders with state Booked | [optional] [default to False]

### Return type

[**BookTransactionsResponse**](BookTransactionsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The results from booking transactions from allocations |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **cancel_orders**
> CancelOrdersResponse cancelOrders = cancel_orders(request_body)

[EARLY ACCESS] CancelOrders: Cancel existing orders

The response returns both the collection of successfully canceled orders, as well as those  that failed. For each failure, a reason is provided. It is important to check the failed set for  unsuccessful results.

### Example

```python
api_instance = api_client_factory.build(OrderManagementApi)
request_body = {"request1":{"scope":"MyScope","code":"Order00000123"},"request2":{"scope":"MyScope","code":"Order00000124"}} # Dict[str, ResourceId]
api_response = api_instance.cancel_orders(request_body)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, ResourceId]**](ResourceId.md)| The request containing the ids of the orders to be cancelled. | [required] 

### Return type

[**CancelOrdersResponse**](CancelOrdersResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully cancelled orders along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **cancel_orders_and_move_remaining**
> CancelOrdersAndMoveRemainingResponse cancelOrdersAndMoveRemaining = cancel_orders_and_move_remaining(request_body)

[EARLY ACCESS] CancelOrdersAndMoveRemaining: Cancel existing orders and move any unplaced quantities to new orders in new blocks

Cancels existing orders, reducing their quantities to those aleady placed. Any remaining quantities are moved  to new orders in new blocks. The placed quantities are distributed to the cancelled orders on a pro-rata basis.

### Example

```python
api_instance = api_client_factory.build(OrderManagementApi)
request_body = {"request1":{"cancelOrderId":{"scope":"MyScope","code":"Order1"},"moveRemainingToOrderId":{"scope":"MyScope","code":"Order1_Rollover"},"moveRemainingToBlockId":{"scope":"MyScope","code":"Block_Rollover"}},"request2":{"cancelOrderId":{"scope":"MyScope","code":"Order2"},"moveRemainingToOrderId":{"scope":"MyScope","code":"Order2_Rollover"},"moveRemainingToBlockId":{"scope":"MyScope","code":"Block_Rollover"}}} # Dict[str, CancelOrdersAndMoveRemainingRequest]
api_response = api_instance.cancel_orders_and_move_remaining(request_body)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, CancelOrdersAndMoveRemainingRequest]**](CancelOrdersAndMoveRemainingRequest.md)| The request containing the orders to be cancelled, and the destinations of remaining quantities. | [required] 

### Return type

[**CancelOrdersAndMoveRemainingResponse**](CancelOrdersAndMoveRemainingResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully cancelled and moved orders, along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **cancel_placements**
> CancelPlacementsResponse cancelPlacements = cancel_placements(request_body)

[EARLY ACCESS] CancelPlacements: Cancel existing placements

The response returns both the collection of successfully canceled placements, as well as those  that failed. For each failure, a reason is provided. It is important to check the failed set for  unsuccessful results.

### Example

```python
api_instance = api_client_factory.build(OrderManagementApi)
request_body = {"request1":{"scope":"MyScope","code":"PLAC00000123"},"request2":{"scope":"MyScope","code":"PLAC00000124"}} # Dict[str, ResourceId]
api_response = api_instance.cancel_placements(request_body)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, ResourceId]**](ResourceId.md)| The request containing the ids of the placements to be cancelled. | [required] 

### Return type

[**CancelPlacementsResponse**](CancelPlacementsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully cancelled placements along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **create_orders**
> ResourceListOfBlockAndOrders createOrders = create_orders(block_and_orders_create_request)

CreateOrders: Upsert a Block and associated orders

Create orders, and blocks if they don't already exist.  This will fail if the block exists and already references orders with differing blocking fields.

### Example

```python
api_instance = api_client_factory.build(OrderManagementApi)
block_and_orders_create_request = BlockAndOrdersCreateRequest()
api_response = api_instance.create_orders(block_and_orders_create_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_and_orders_create_request** | [**BlockAndOrdersCreateRequest**](BlockAndOrdersCreateRequest.md)| The collection of block and orders requests. | [required] 

### Return type

[**ResourceListOfBlockAndOrders**](ResourceListOfBlockAndOrders.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A collection of block and associated orders. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_order_history**
> ResourceListOfChangeIntervalWithOrderManagementDetail getOrderHistory = get_order_history(scope, code, as_at=as_at)

GetOrderHistory: Get the history of an order and related entity changes

Get the changes that have happened to an order and related entities.

### Example

```python
api_instance = api_client_factory.build(OrderManagementApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_order_history(scope, code, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the order. | [required] 
 **code** | **str**| The code of the order. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the history of the order and related entities. Defaults              to return the latest version if not specified. | [optional] 

### Return type

[**ResourceListOfChangeIntervalWithOrderManagementDetail**](ResourceListOfChangeIntervalWithOrderManagementDetail.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The history of the specified order and related entities (changes that have been made to it). |  -  |
**400** | The details of the input related failure |  -  |
**404** | Order not found. |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **move_orders**
> ResourceListOfMovedOrderToDifferentBlockResponse moveOrders = move_orders(move_orders_to_different_blocks_request)

[EARLY ACCESS] MoveOrders: Move orders to new or existing block

Move an order to a block, creating the block if it does not already exist.   This will fail if the block exists and already references orders with differing fields to the upsert request.

### Example

```python
api_instance = api_client_factory.build(OrderManagementApi)
move_orders_to_different_blocks_request = MoveOrdersToDifferentBlocksRequest()
api_response = api_instance.move_orders(move_orders_to_different_blocks_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_orders_to_different_blocks_request** | [**MoveOrdersToDifferentBlocksRequest**](MoveOrdersToDifferentBlocksRequest.md)| The collection of order and destination block ids. | [required] 

### Return type

[**ResourceListOfMovedOrderToDifferentBlockResponse**](ResourceListOfMovedOrderToDifferentBlockResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of block and order pairs for each order moved into a block, and the Id of the order&#39;s previous block (if any). |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **place_blocks**
> ResourceListOfPlacement placeBlocks = place_blocks(place_blocks_request=place_blocks_request)

[EARLY ACCESS] PlaceBlocks: Places blocks for a given list of placement requests.

The referenced block's existence will be verified.

### Example

```python
api_instance = api_client_factory.build(OrderManagementApi)
place_blocks_request = PlaceBlocksRequest()
api_response = api_instance.place_blocks(place_blocks_request=place_blocks_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **place_blocks_request** | [**PlaceBlocksRequest**](PlaceBlocksRequest.md)| The request containing the blocks to the placed. | [optional] 

### Return type

[**ResourceListOfPlacement**](ResourceListOfPlacement.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The block placements. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **run_allocation_service**
> AllocationServiceRunResponse runAllocationService = run_allocation_service(resource_id, allocation_algorithm=allocation_algorithm)

RunAllocationService: Runs the Allocation Service

Allocates Executions for a given list of placements back to their originating orders using one of the LUSID algorithms, creating Allocations to record the results.

### Example

```python
api_instance = api_client_factory.build(OrderManagementApi)
resource_id = [{"scope":"MyScope","code":"PLAC00000123"}] # List[ResourceId]
allocation_algorithm = 'allocation_algorithm_example' # str (optional)
api_response = api_instance.run_allocation_service(resource_id, allocation_algorithm=allocation_algorithm)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | [**List[ResourceId]**](ResourceId.md)| The List of Placement IDs for which you wish to allocate Executions. | [required] 
 **allocation_algorithm** | **str**| A string representation of the allocation algorithm you would like to use to allocate shares from executions e.g. \&quot;PR-FIFO\&quot;.  This defaults to \&quot;PR-FIFO\&quot;. | [optional] 

### Return type

[**AllocationServiceRunResponse**](AllocationServiceRunResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of Allocations |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **run_allocation_service_with_weights**
> AllocationServiceRunResponse runAllocationServiceWithWeights = run_allocation_service_with_weights(weighted_allocation_service_run_request, allocation_algorithm=allocation_algorithm)

[EXPERIMENTAL] RunAllocationServiceWithWeights: Runs the Allocation Service with portfolio weights

Allocates Executions for a given list of placements to a specified set of portfolios by weight,  creating Allocations to record the results. Used for the unsolicited Block and Block Trade booking flows where no Orders exist against the Block.  Weights are relative to each other and are not required to sum to 1 or 100.

### Example

```python
api_instance = api_client_factory.build(OrderManagementApi)
weighted_allocation_service_run_request = WeightedAllocationServiceRunRequest()
allocation_algorithm = 'allocation_algorithm_example' # str (optional)
api_response = api_instance.run_allocation_service_with_weights(weighted_allocation_service_run_request, allocation_algorithm=allocation_algorithm)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **weighted_allocation_service_run_request** | [**WeightedAllocationServiceRunRequest**](WeightedAllocationServiceRunRequest.md)| The placement IDs to allocate against, and the portfolio weights to use for the allocation split. | [required] 
 **allocation_algorithm** | **str**| A string representation of the allocation algorithm you would like to use to allocate shares from executions e.g. \&quot;PR-LF\&quot;.  Allocating with weights means the base algorithm is always pro-rata, and the orphan allocation algorithm is either Largest First or Smallest First.  This defaults to \&quot;PR-LF\&quot;. Valid values are \&quot;PR-LF\&quot;, \&quot;PR-SF\&quot;, \&quot;LF\&quot;, \&quot;SF\&quot;. | [optional] 

### Return type

[**AllocationServiceRunResponse**](AllocationServiceRunResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of Allocations |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **sweep_blocks**
> SweepBlocksResponse sweepBlocks = sweep_blocks(sweep_blocks_request)

[EXPERIMENTAL] SweepBlocks: Sweeps specified blocks, for each block that meets the requirements. The request may be partially successful.

The requirements are:  <list type=\"bullet\"><term>The block exists.</term><term>All orders have state \"Closed\", \"Cancelled\", \"Canceled\" or \"Booked\".</term><term>All placements have state \"Allocated\" or \"Over-allocated\".</term><term>All allocations have state \"Closed\", \"Cancelled\", \"Canceled\" or \"Booked\".</term><term>No execution or allocation has been modified since the passed LatestAllowableModificationTime.</term></list>

### Example

```python
api_instance = api_client_factory.build(OrderManagementApi)
sweep_blocks_request = SweepBlocksRequest()
api_response = api_instance.sweep_blocks(sweep_blocks_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sweep_blocks_request** | [**SweepBlocksRequest**](SweepBlocksRequest.md)|  | [required] 

### Return type

[**SweepBlocksResponse**](SweepBlocksResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The results from sweeping blocks. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_orders**
> UpdateOrdersResponse updateOrders = update_orders(request_body)

[EARLY ACCESS] UpdateOrders: Update existing orders

The response returns both the collection of successfully updated orders, as well as those  that failed. For each failure, a reason is provided. It is important to check the failed set for  unsuccessful results.

### Example

```python
api_instance = api_client_factory.build(OrderManagementApi)
request_body = {"update1":{"id":{"scope":"MyScope","code":"Code1"},"quantity":101.0},"update2":{"id":{"scope":"MyScope","code":"Code2"},"quantity":100.0,"portfolioId":{"scope":"MyScope","code":"NewPortfolio"},"properties":{"Order/MyScope/OrderProperty":{"key":"Order/MyScope/OrderProperty","value":{"labelValue":"NewValue"}}},"date":"2020-01-01T00:00:00.0000000+00:00","side":"Buy"}} # Dict[str, OrderUpdateRequest]
api_response = api_instance.update_orders(request_body)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, OrderUpdateRequest]**](OrderUpdateRequest.md)| The request containing the orders to be updated. | [required] 

### Return type

[**UpdateOrdersResponse**](UpdateOrdersResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully updated orders along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **update_placements**
> UpdatePlacementsResponse updatePlacements = update_placements(request_body)

[EARLY ACCESS] UpdatePlacements: Update existing placements

The response returns both the collection of successfully updated placements, as well as those  that failed. For each failure, a reason is provided. It is important to check the failed set for  unsuccessful results.

### Example

```python
api_instance = api_client_factory.build(OrderManagementApi)
request_body = {"full_request":{"id":{"scope":"MyScope","code":"PLAC00000123"},"quantity":100.0,"properties":{"Placement/MyScope/SomePlacementProperty":{"key":"Placement/MyScope/SomePlacementProperty","value":{"labelValue":"XYZ000034567"}}},"type":"Limit","limitPrice":100.0,"stopPrice":100.0,"counterparty":"SomeCounterparty","entryType":"Manual"}} # Dict[str, PlacementUpdateRequest]
api_response = api_instance.update_placements(request_body)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, PlacementUpdateRequest]**](PlacementUpdateRequest.md)| The request containing the placements to be updated. | [required] 

### Return type

[**UpdatePlacementsResponse**](UpdatePlacementsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully updated placements along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

