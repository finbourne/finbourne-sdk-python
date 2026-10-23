# lusid.AllocationEventsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**book_allocation_event**](AllocationEventsApi.md#book_allocation_event) | **POST** /api/api/allocationevents/{scope}/{code}/book | [EXPERIMENTAL] BookAllocationEvent: Book an Allocation Event.
[**create_allocation_event**](AllocationEventsApi.md#create_allocation_event) | **POST** /api/api/allocationevents/{scope} | [EXPERIMENTAL] CreateAllocationEvent: Create an Allocation Event.
[**delete_allocation_event**](AllocationEventsApi.md#delete_allocation_event) | **DELETE** /api/api/allocationevents/{scope}/{code} | [EXPERIMENTAL] DeleteAllocationEvent: Delete an Allocation Event.
[**get_allocation_event**](AllocationEventsApi.md#get_allocation_event) | **GET** /api/api/allocationevents/{scope}/{code} | [EXPERIMENTAL] GetAllocationEvent: Get an Allocation Event.
[**get_allocation_event_notices**](AllocationEventsApi.md#get_allocation_event_notices) | **GET** /api/api/allocationevents/{scope}/{code}/notices | [EARLY ACCESS] GetAllocationEventNotices: [EARLY ACCESS] GetAllocationEventNotices: Get the notices an allocation event issues to its partners.
[**get_allocation_event_receivables**](AllocationEventsApi.md#get_allocation_event_receivables) | **GET** /api/api/allocationevents/{scope}/{code}/receivables | [EXPERIMENTAL] GetAllocationEventReceivables: Get the receivables of an Allocation Event.
[**list_allocation_events**](AllocationEventsApi.md#list_allocation_events) | **GET** /api/api/allocationevents | [EXPERIMENTAL] ListAllocationEvents: List Allocation Events.
[**list_allocation_payment_holds**](AllocationEventsApi.md#list_allocation_payment_holds) | **GET** /api/api/allocationevents/{scope}/{code}/allocations/{investorRecordId}/holds | [EARLY ACCESS] ListAllocationPaymentHolds: [EARLY ACCESS] ListAllocationPaymentHolds: List the holds placed on a partner&#39;s payment.
[**plan_allocation_event_booking**](AllocationEventsApi.md#plan_allocation_event_booking) | **POST** /api/api/allocationevents/{scope}/{code}/plan | [EXPERIMENTAL] PlanAllocationEventBooking: Plan the booking of an Allocation Event.
[**put_allocation_payment_hold**](AllocationEventsApi.md#put_allocation_payment_hold) | **PUT** /api/api/allocationevents/{scope}/{code}/allocations/{investorRecordId}/hold | [EARLY ACCESS] PutAllocationPaymentHold: [EARLY ACCESS] PutAllocationPaymentHold: Place, move or release a hold on a partner&#39;s payment.
[**reallocate_allocation_event**](AllocationEventsApi.md#reallocate_allocation_event) | **POST** /api/api/allocationevents/{scope}/{code}/reallocate | [EXPERIMENTAL] ReallocateAllocationEvent: Reallocate an Allocation Event.
[**receive_allocation_event**](AllocationEventsApi.md#receive_allocation_event) | **POST** /api/api/allocationevents/{scope}/{code}/receipts | [EXPERIMENTAL] ReceiveAllocationEvent: Record a receipt against an Allocation Event.
[**reverse_allocation_event**](AllocationEventsApi.md#reverse_allocation_event) | **POST** /api/api/allocationevents/{scope}/{code}/reverse | [EXPERIMENTAL] ReverseAllocationEvent: Reverse an Allocation Event.
[**unbook_allocation_event**](AllocationEventsApi.md#unbook_allocation_event) | **POST** /api/api/allocationevents/{scope}/{code}/unbook | [EXPERIMENTAL] UnbookAllocationEvent: Unbook an Allocation Event.
[**upsert_allocation_event**](AllocationEventsApi.md#upsert_allocation_event) | **PUT** /api/api/allocationevents/{scope}/{code} | [EXPERIMENTAL] UpsertAllocationEvent: Upsert an Allocation Event.


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.allocation_events_api import AllocationEventsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(AllocationEventsApi)
```

---

# **book_allocation_event**
> AllocationEvent bookAllocationEvent = book_allocation_event(scope, code, allocation_event_book_request, effective_at=effective_at)

[EXPERIMENTAL] BookAllocationEvent: Book an Allocation Event.

Freeze a computed Allocation Event under a booking reference, from an effective datetime. Once booked the  event can no longer be replaced or reallocated. Booking again under the same reference returns the event  unchanged; booking under a different reference is refused.

### Example

```python
api_instance = api_client_factory.build(AllocationEventsApi)
scope = 'scope_example' # str
code = 'code_example' # str
allocation_event_book_request = AllocationEventBookRequest()
effective_at = 'effective_at_example' # str (optional)
api_response = api_instance.book_allocation_event(scope, code, allocation_event_book_request, effective_at=effective_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Allocation Event. | [required] 
 **code** | **str**| The code of the Allocation Event. Together with the scope this uniquely identifies the Allocation Event. | [required] 
 **allocation_event_book_request** | [**AllocationEventBookRequest**](../model/AllocationEventBookRequest.md)| The booking reference to freeze the event under. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to read the Allocation Event to book. The booking is recorded on the version in force at that time, from that version&#39;s own effective date. Defaults to the current LUSID system datetime if not specified. | [optional] 

### Return type

[**AllocationEvent**](../model/AllocationEvent.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The booked Allocation Event. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **create_allocation_event**
> AllocationEvent createAllocationEvent = create_allocation_event(scope, allocation_event_request)

[EXPERIMENTAL] CreateAllocationEvent: Create an Allocation Event.

Raise a new Allocation Event. The scope is provided in the route and the code in the request body. The event  names the Allocation Map it is shared by, the kind of event, the amount and the date. Its per-investor shares  are computed on creation from the map as it stood on the event date, so the response comes back Computed.

### Example

```python
api_instance = api_client_factory.build(AllocationEventsApi)
scope = 'scope_example' # str
allocation_event_request = AllocationEventRequest()
api_response = api_instance.create_allocation_event(scope, allocation_event_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Allocation Event. | [required] 
 **allocation_event_request** | [**AllocationEventRequest**](../model/AllocationEventRequest.md)| The definition of the Allocation Event. | [required] 

### Return type

[**AllocationEvent**](../model/AllocationEvent.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created Allocation Event. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_allocation_event**
> DeletedEntityResponse deleteAllocationEvent = delete_allocation_event(scope, code, effective_at=effective_at)

[EXPERIMENTAL] DeleteAllocationEvent: Delete an Allocation Event.

Delete an Allocation Event. Given an effective datetime, the Allocation Event is deleted from that datetime  and remains retrievable at earlier effective datetimes. Given none, an Allocation Event that was created  without an effective datetime is removed from the beginning of time, so that its code can be reused;  otherwise it is deleted from the current LUSID system datetime. Only an Allocation Event that has not been  booked can be deleted.

### Example

```python
api_instance = api_client_factory.build(AllocationEventsApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
api_response = api_instance.delete_allocation_event(scope, code, effective_at=effective_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Allocation Event. | [required] 
 **code** | **str**| The code of the Allocation Event. Together with the scope this uniquely identifies the Allocation Event. | [required] 
 **effective_at** | **str**| The effective datetime or cut label from which to delete the Allocation Event. If not specified, an Allocation Event created without an effective datetime is removed from the beginning of time; any other is deleted from the current LUSID system datetime. | [optional] 

### Return type

[**DeletedEntityResponse**](../model/DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the Allocation Event was deleted. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_allocation_event**
> AllocationEvent getAllocationEvent = get_allocation_event(scope, code, effective_at=effective_at, as_at=as_at)

[EXPERIMENTAL] GetAllocationEvent: Get an Allocation Event.

Retrieve a particular Allocation Event at an effective and asAt datetime, including its computed  per-investor shares and, once booked, its booking reference.

### Example

```python
api_instance = api_client_factory.build(AllocationEventsApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_allocation_event(scope, code, effective_at=effective_at, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Allocation Event. | [required] 
 **code** | **str**| The code of the Allocation Event. Together with the scope this uniquely identifies the Allocation Event. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the Allocation Event. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Allocation Event. Defaults to returning the latest version if not specified. | [optional] 

### Return type

[**AllocationEvent**](../model/AllocationEvent.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Allocation Event. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_allocation_event_notices**
> ResourceListOfAllocationEventNotice getAllocationEventNotices = get_allocation_event_notices(scope, code, investor_record_id=investor_record_id, include_zero=include_zero, as_at=as_at)

[EARLY ACCESS] GetAllocationEventNotices: [EARLY ACCESS] GetAllocationEventNotices: Get the notices an allocation event issues to its partners.

One notice per partner allocation, listing the ILPA transaction lines, the net amount due, the partner's  unfunded commitment reconciliation across the event and their cumulative position alongside the general  partner's. Notices carry a DRAFT watermark until the event is booked.

### Example

```python
api_instance = api_client_factory.build(AllocationEventsApi)
scope = 'scope_example' # str
code = 'code_example' # str
investor_record_id = 'investor_record_id_example' # str (optional)
include_zero = False # bool (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_allocation_event_notices(scope, code, investor_record_id=investor_record_id, include_zero=include_zero, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Allocation Event. | [required] 
 **code** | **str**| The code of the Allocation Event. Together with the scope this uniquely identifies the Allocation Event. | [required] 
 **investor_record_id** | **str**| Restrict the notices to this partner&#39;s investor record. | [optional] 
 **include_zero** | **bool**| Whether to include notices whose every line is zero. Defaults to false. | [optional] [default to False]
 **as_at** | **datetime**| The asAt datetime at which to read the event. Defaults to returning the latest version if not specified. | [optional] 

### Return type

[**ResourceListOfAllocationEventNotice**](../model/ResourceListOfAllocationEventNotice.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The notices the allocation event issues. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_allocation_event_receivables**
> AllocationReceivablesAgeing getAllocationEventReceivables = get_allocation_event_receivables(scope, code, effective_at=effective_at, as_at=as_at)

[EXPERIMENTAL] GetAllocationEventReceivables: Get the receivables of an Allocation Event.

What each investor still owes on a booked capital call as of the effective datetime, with how many days past  due it is and the ageing bucket that puts it in.

### Example

```python
api_instance = api_client_factory.build(AllocationEventsApi)
scope = 'scope_example' # str
code = 'code_example' # str
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_allocation_event_receivables(scope, code, effective_at=effective_at, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Allocation Event. | [required] 
 **code** | **str**| The code of the Allocation Event. Together with the scope this uniquely identifies the Allocation Event. | [required] 
 **effective_at** | **str**| The effective datetime or cut label as of which to age the receivables. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to read the Allocation Event. Defaults to returning the latest version if not specified. | [optional] 

### Return type

[**AllocationReceivablesAgeing**](../model/AllocationReceivablesAgeing.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The aged receivables of the Allocation Event. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_allocation_events**
> PagedResourceListOfAllocationEvent listAllocationEvents = list_allocation_events(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

[EXPERIMENTAL] ListAllocationEvents: List Allocation Events.

List all the Allocation Events matching a particular criteria.

### Example

```python
api_instance = api_client_factory.build(AllocationEventsApi)
effective_at = 'effective_at_example' # str (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
filter = 'filter_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
api_response = api_instance.list_allocation_events(effective_at=effective_at, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effective datetime or cut label at which to list the Allocation Events. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the Allocation Events. Defaults to returning the latest version of each Allocation Event if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Allocation Events; this value is returned from the previous call.              If a pagination token is provided, the filter, effectiveAt and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. For example, to filter on the Allocation Event status, specify \&quot;status eq &#39;Booked&#39;\&quot;.              For more information about filtering LUSID results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **sort_by** | [**List[str]**](../model/str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 

### Return type

[**PagedResourceListOfAllocationEvent**](../model/PagedResourceListOfAllocationEvent.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Allocation Events. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_allocation_payment_holds**
> ResourceListOfAllocationPaymentHold listAllocationPaymentHolds = list_allocation_payment_holds(scope, code, investor_record_id)

[EARLY ACCESS] ListAllocationPaymentHolds: [EARLY ACCESS] ListAllocationPaymentHolds: List the holds placed on a partner's payment.

Every hold placed on the partner's payment against the event, newest first, including released ones.

### Example

```python
api_instance = api_client_factory.build(AllocationEventsApi)
scope = 'scope_example' # str
code = 'code_example' # str
investor_record_id = 'investor_record_id_example' # str
api_response = api_instance.list_allocation_payment_holds(scope, code, investor_record_id)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Allocation Event. | [required] 
 **code** | **str**| The code of the Allocation Event. Together with the scope this uniquely identifies the Allocation Event. | [required] 
 **investor_record_id** | **str**| The investor record of the partner whose holds are listed. | [required] 

### Return type

[**ResourceListOfAllocationPaymentHold**](../model/ResourceListOfAllocationPaymentHold.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The holds placed on the partner&#39;s payment. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **plan_allocation_event_booking**
> AllocationPostingPlan planAllocationEventBooking = plan_allocation_event_booking(scope, code, allocation_event_book_request, effective_at=effective_at)

[EXPERIMENTAL] PlanAllocationEventBooking: Plan the booking of an Allocation Event.

Show everything booking a computed Allocation Event under a booking reference would write, validated as the  booking itself would be, without writing any of it: the investors' lines, the roll-ups above them through the  fund structure and the fund-side transactions. A booking that would be refused fails here with every problem  listed; warnings the map's policy lets through come back on the plan.

### Example

```python
api_instance = api_client_factory.build(AllocationEventsApi)
scope = 'scope_example' # str
code = 'code_example' # str
allocation_event_book_request = AllocationEventBookRequest()
effective_at = 'effective_at_example' # str (optional)
api_response = api_instance.plan_allocation_event_booking(scope, code, allocation_event_book_request, effective_at=effective_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Allocation Event. | [required] 
 **code** | **str**| The code of the Allocation Event. Together with the scope this uniquely identifies the Allocation Event. | [required] 
 **allocation_event_book_request** | [**AllocationEventBookRequest**](../model/AllocationEventBookRequest.md)| The booking reference the plan is drawn up under. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to plan the booking. Defaults to the current LUSID system datetime if not specified. | [optional] 

### Return type

[**AllocationPostingPlan**](../model/AllocationPostingPlan.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The postings the booking would write. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **put_allocation_payment_hold**
> AllocationPaymentHold putAllocationPaymentHold = put_allocation_payment_hold(scope, code, investor_record_id, allocation_payment_hold_request)

[EARLY ACCESS] PutAllocationPaymentHold: [EARLY ACCESS] PutAllocationPaymentHold: Place, move or release a hold on a partner's payment.

A Blocked or Escrow hold stops the partner's allocation being received against the event until it is  Released. A hold may only be released by a user other than the one who placed it.

### Example

```python
api_instance = api_client_factory.build(AllocationEventsApi)
scope = 'scope_example' # str
code = 'code_example' # str
investor_record_id = 'investor_record_id_example' # str
allocation_payment_hold_request = AllocationPaymentHoldRequest()
api_response = api_instance.put_allocation_payment_hold(scope, code, investor_record_id, allocation_payment_hold_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Allocation Event. | [required] 
 **code** | **str**| The code of the Allocation Event. Together with the scope this uniquely identifies the Allocation Event. | [required] 
 **investor_record_id** | **str**| The investor record of the partner whose payment is held. | [required] 
 **allocation_payment_hold_request** | [**AllocationPaymentHoldRequest**](../model/AllocationPaymentHoldRequest.md)| The hold to record: its status, and optionally a reason and an external reference. | [required] 

### Return type

[**AllocationPaymentHold**](../model/AllocationPaymentHold.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The hold as recorded. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **reallocate_allocation_event**
> AllocationEvent reallocateAllocationEvent = reallocate_allocation_event(scope, code, allocation_event_reallocate_request, effective_at=effective_at)

[EXPERIMENTAL] ReallocateAllocationEvent: Reallocate an Allocation Event.

Recompute the per-investor shares of an unbooked Allocation Event against its map, from an effective  datetime, recording the reason. Any basis values supplied replace those used before. A booked Allocation  Event cannot be reallocated.

### Example

```python
api_instance = api_client_factory.build(AllocationEventsApi)
scope = 'scope_example' # str
code = 'code_example' # str
allocation_event_reallocate_request = AllocationEventReallocateRequest()
effective_at = 'effective_at_example' # str (optional)
api_response = api_instance.reallocate_allocation_event(scope, code, allocation_event_reallocate_request, effective_at=effective_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Allocation Event. | [required] 
 **code** | **str**| The code of the Allocation Event. Together with the scope this uniquely identifies the Allocation Event. | [required] 
 **allocation_event_reallocate_request** | [**AllocationEventReallocateRequest**](../model/AllocationEventReallocateRequest.md)| The reason for the reallocation and any basis values to use. | [required] 
 **effective_at** | **str**| The effective datetime or cut label from which the reallocation applies. If not specified, the version in force now is recomputed in place from its own effective date. | [optional] 

### Return type

[**AllocationEvent**](../model/AllocationEvent.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The reallocated Allocation Event. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **receive_allocation_event**
> AllocationEvent receiveAllocationEvent = receive_allocation_event(scope, code, allocation_event_receipt_request, effective_at=effective_at)

[EXPERIMENTAL] ReceiveAllocationEvent: Record a receipt against an Allocation Event.

Record cash received from an investor against a booked capital call. The receipt is applied to what the  investor owes on the call; anything over is recorded as a refund payable, so the outstanding amount never  goes negative. A bank charge is borne by the partner or the fund as the map's policy says, and a receipt in  another currency is converted at the rate given.

### Example

```python
api_instance = api_client_factory.build(AllocationEventsApi)
scope = 'scope_example' # str
code = 'code_example' # str
allocation_event_receipt_request = AllocationEventReceiptRequest()
effective_at = 'effective_at_example' # str (optional)
api_response = api_instance.receive_allocation_event(scope, code, allocation_event_receipt_request, effective_at=effective_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Allocation Event. | [required] 
 **code** | **str**| The code of the Allocation Event. Together with the scope this uniquely identifies the Allocation Event. | [required] 
 **allocation_event_receipt_request** | [**AllocationEventReceiptRequest**](../model/AllocationEventReceiptRequest.md)| The investor, amount and date of the receipt. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to read the Allocation Event receiving cash. The receipt is recorded on the version in force at that time, from that version&#39;s own effective date; the receipt postings are dated by the request. Defaults to the current LUSID system datetime if not specified. | [optional] 

### Return type

[**AllocationEvent**](../model/AllocationEvent.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Allocation Event with the receipt recorded. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **reverse_allocation_event**
> AllocationEvent reverseAllocationEvent = reverse_allocation_event(scope, code, allocation_event_reverse_request, effective_at=effective_at)

[EXPERIMENTAL] ReverseAllocationEvent: Reverse an Allocation Event.

Reverse a booked Allocation Event: every posting the booking wrote is mirrored under the reversal reference and  the event is left Reversed. A reversal falling in a closed period posts in the current period unless it is  marked backdated. A reversal cannot itself be reversed; raise a new event naming the reversed one in its  replaces field to put corrected shares in the books.

### Example

```python
api_instance = api_client_factory.build(AllocationEventsApi)
scope = 'scope_example' # str
code = 'code_example' # str
allocation_event_reverse_request = AllocationEventReverseRequest()
effective_at = 'effective_at_example' # str (optional)
api_response = api_instance.reverse_allocation_event(scope, code, allocation_event_reverse_request, effective_at=effective_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Allocation Event. | [required] 
 **code** | **str**| The code of the Allocation Event. Together with the scope this uniquely identifies the Allocation Event. | [required] 
 **allocation_event_reverse_request** | [**AllocationEventReverseRequest**](../model/AllocationEventReverseRequest.md)| The reason for the reversal and, optionally, when it should take effect. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to read the Allocation Event to reverse. The reversed status is recorded on the version in force at that time, from that version&#39;s own effective date; the mirror postings are dated by the request. Defaults to the current LUSID system datetime if not specified. | [optional] 

### Return type

[**AllocationEvent**](../model/AllocationEvent.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The reversed Allocation Event. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **unbook_allocation_event**
> AllocationEvent unbookAllocationEvent = unbook_allocation_event(scope, code, allocation_event_unbook_request, effective_at=effective_at)

[EXPERIMENTAL] UnbookAllocationEvent: Unbook an Allocation Event.

Take an Allocation Event whose booking stopped half way back to Computed, cancelling every posting the  booking wrote, and record why. Only an event in the Booking status can be unbooked: one that is Booked is  reversed instead.

### Example

```python
api_instance = api_client_factory.build(AllocationEventsApi)
scope = 'scope_example' # str
code = 'code_example' # str
allocation_event_unbook_request = AllocationEventUnbookRequest()
effective_at = 'effective_at_example' # str (optional)
api_response = api_instance.unbook_allocation_event(scope, code, allocation_event_unbook_request, effective_at=effective_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Allocation Event. | [required] 
 **code** | **str**| The code of the Allocation Event. Together with the scope this uniquely identifies the Allocation Event. | [required] 
 **allocation_event_unbook_request** | [**AllocationEventUnbookRequest**](../model/AllocationEventUnbookRequest.md)| The reason the booking is being taken back. | [required] 
 **effective_at** | **str**| The effective datetime or cut label at which to read the Allocation Event to unbook. The unbooking is recorded on the version in force at that time, from that version&#39;s own effective date. Defaults to the current LUSID system datetime if not specified. | [optional] 

### Return type

[**AllocationEvent**](../model/AllocationEvent.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Allocation Event, back at Computed. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_allocation_event**
> AllocationEvent upsertAllocationEvent = upsert_allocation_event(scope, code, allocation_event_request)

[EXPERIMENTAL] UpsertAllocationEvent: Upsert an Allocation Event.

Update or insert an Allocation Event. If the Allocation Event does not exist it is created, otherwise it is  replaced and its shares recomputed. The code in the request body must match the code in the route. A booked  Allocation Event is frozen and cannot be replaced.

### Example

```python
api_instance = api_client_factory.build(AllocationEventsApi)
scope = 'scope_example' # str
code = 'code_example' # str
allocation_event_request = AllocationEventRequest()
api_response = api_instance.upsert_allocation_event(scope, code, allocation_event_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Allocation Event. | [required] 
 **code** | **str**| The code of the Allocation Event. Together with the scope this uniquely identifies the Allocation Event. | [required] 
 **allocation_event_request** | [**AllocationEventRequest**](../model/AllocationEventRequest.md)| The definition of the Allocation Event. | [required] 

### Return type

[**AllocationEvent**](../model/AllocationEvent.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The upserted Allocation Event. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

