# lusid.SubscriptionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_subscription**](SubscriptionsApi.md#delete_subscription) | **DELETE** /api/api/subscriptions/{scope}/{code} | [EARLY ACCESS] DeleteSubscription: Delete a Subscription, assuming that it is present.
[**get_subscription**](SubscriptionsApi.md#get_subscription) | **GET** /api/api/subscriptions/{scope}/{code} | [EARLY ACCESS] GetSubscription: Get Subscription
[**list_subscriptions**](SubscriptionsApi.md#list_subscriptions) | **GET** /api/api/subscriptions/{scope} | [EARLY ACCESS] ListSubscriptions: List the set of Subscription definitions
[**upsert_subscription**](SubscriptionsApi.md#upsert_subscription) | **POST** /api/api/subscriptions | [EARLY ACCESS] UpsertSubscription: Upsert a Subscription. This creates or updates the subscription definition in LUSID.


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.subscriptions_api import SubscriptionsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(SubscriptionsApi)
```

---

# **delete_subscription**
> AnnulSingleStructuredDataResponse deleteSubscription = delete_subscription(scope, code)

[EARLY ACCESS] DeleteSubscription: Delete a Subscription, assuming that it is present.

Delete the specified Subscription definition from a single scope.                The response will return either detail of the deleted item, or an explanation (failure) as to why this did not succeed.

### Example

```python
api_instance = api_client_factory.build(SubscriptionsApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.delete_subscription(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Subscription to delete. | [required] 
 **code** | **str**| The Subscription to delete. | [required] 

### Return type

[**AnnulSingleStructuredDataResponse**](../model/AnnulSingleStructuredDataResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The AsAt of deletion or failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_subscription**
> GetSubscriptionResponse getSubscription = get_subscription(scope, code, as_at=as_at)

[EARLY ACCESS] GetSubscription: Get Subscription

Get a Subscription definition from a single scope.                The response will return either the subscription that has been stored, or a failure explaining why the request was unsuccessful.

### Example

```python
api_instance = api_client_factory.build(SubscriptionsApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
api_response = api_instance.get_subscription(scope, code, as_at=as_at)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Subscription to retrieve. | [required] 
 **code** | **str**| The code of the Subscription to retrieve. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Subscription. Defaults to return the latest version if not specified. | [optional] 

### Return type

[**GetSubscriptionResponse**](../model/GetSubscriptionResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved Subscription or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_subscriptions**
> PagedResourceListOfGetSubscriptionResponse listSubscriptions = list_subscriptions(scope, as_at=as_at, filter=filter, limit=limit, page=page)

[EARLY ACCESS] ListSubscriptions: List the set of Subscription definitions

List the set of subscription definitions at the specified date/time and scope.

### Example

```python
api_instance = api_client_factory.build(SubscriptionsApi)
scope = 'scope_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
filter = 'filter_example' # str (optional)
limit = 56 # int (optional)
page = 'page_example' # str (optional)
api_response = api_instance.list_subscriptions(scope, as_at=as_at, filter=filter, limit=limit, page=page)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to list subscriptions for. | [required] 
 **as_at** | **datetime**| The asAt datetime at which to list the subscriptions. Defaults to latest if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. | [optional] 
 **limit** | **int**| Maximum number of results to return. Defaults to 100. | [optional] 
 **page** | **str**| Pagination token from a previous result to fetch the next page. | [optional] 

### Return type

[**PagedResourceListOfGetSubscriptionResponse**](../model/PagedResourceListOfGetSubscriptionResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested subscriptions |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **upsert_subscription**
> UpsertSingleStructuredDataResponse upsertSubscription = upsert_subscription(upsert_subscription_request)

[EARLY ACCESS] UpsertSubscription: Upsert a Subscription. This creates or updates the subscription definition in LUSID.

Update or insert one Subscription definition. An item will be updated if it already exists  and inserted if it does not.                The referenced portfolio (and timeline, when supplied) must exist and be readable by the caller.                The response will return the successfully updated or inserted subscription or failure message if unsuccessful.

### Example

```python
api_instance = api_client_factory.build(SubscriptionsApi)
upsert_subscription_request = UpsertSubscriptionRequest()
api_response = api_instance.upsert_subscription(upsert_subscription_request)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_subscription_request** | [**UpsertSubscriptionRequest**](../model/UpsertSubscriptionRequest.md)| The Subscription to update or insert | [required] 

### Return type

[**UpsertSingleStructuredDataResponse**](../model/UpsertSingleStructuredDataResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully updated or inserted item or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

