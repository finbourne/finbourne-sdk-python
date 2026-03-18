# notifications.SubscriptionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_subscription**](SubscriptionsApi.md#create_subscription) | **POST** /notifications/api/subscriptions | CreateSubscription: Create a new subscription.
[**delete_subscription**](SubscriptionsApi.md#delete_subscription) | **DELETE** /notifications/api/subscriptions/{scope}/{code} | DeleteSubscription: Delete a subscription.
[**get_subscription**](SubscriptionsApi.md#get_subscription) | **GET** /notifications/api/subscriptions/{scope}/{code} | GetSubscription: Get a subscription.
[**list_subscriptions**](SubscriptionsApi.md#list_subscriptions) | **GET** /notifications/api/subscriptions | ListSubscriptions: List subscriptions.
[**update_subscription**](SubscriptionsApi.md#update_subscription) | **PUT** /notifications/api/subscriptions/{scope}/{code} | UpdateSubscription: Update an existing subscription.


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.notifications.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.notifications.api.subscriptions_api import SubscriptionsApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(SubscriptionsApi)
```

---

# **create_subscription**
> Subscription createSubscription = create_subscription(create_subscription)

CreateSubscription: Create a new subscription.

### Example

```python
api_instance = api_client_factory.build(SubscriptionsApi)
create_subscription = CreateSubscription()
api_response = api_instance.create_subscription(create_subscription)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_subscription** | [**CreateSubscription**](CreateSubscription.md)| The data to create a subscription | [required] 

### Return type

[**Subscription**](Subscription.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **delete_subscription**
> deleteSubscription = delete_subscription(scope, code)

DeleteSubscription: Delete a subscription.

### Example

```python
api_instance = api_client_factory.build(SubscriptionsApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_instance.delete_subscription(scope, code)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a subscription | [required] 
 **code** | **str**| The code that identifies a subscription | [required] 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | The details of the input related failure |  -  |
**404** | No subscription exists in current scope |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **get_subscription**
> Subscription getSubscription = get_subscription(scope, code)

GetSubscription: Get a subscription.

### Example

```python
api_instance = api_client_factory.build(SubscriptionsApi)
scope = 'scope_example' # str
code = 'code_example' # str
api_response = api_instance.get_subscription(scope, code)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a subscription | [required] 
 **code** | **str**| The code that identifies a subscription | [required] 

### Return type

[**Subscription**](Subscription.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | No subscription exists in current scope |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_subscriptions**
> ResourceListOfSubscription listSubscriptions = list_subscriptions(filter=filter, sort_by=sort_by, page=page, limit=limit)

ListSubscriptions: List subscriptions.

### Example

```python
api_instance = api_client_factory.build(SubscriptionsApi)
filter = 'filter_example' # str (optional)
sort_by = 'sort_by_example' # str (optional)
page = 'page_example' # str (optional)
limit = 56 # int (optional)
api_response = api_instance.list_subscriptions(filter=filter, sort_by=sort_by, page=page, limit=limit)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Expression to filter the result set. Read more about &lt;a href&#x3D;\&quot;https://support.lusid.com/filtering-results-from-lusid\&quot;&gt; filtering results from LUSID&lt;/a&gt;. | [optional] 
 **sort_by** | **str**| Fields to order the result set. Read more about &lt;a href&#x3D;\&quot;https://support.lusid.com/filtering-results-from-lusid\&quot;&gt; filtering results from LUSID&lt;/a&gt; | [optional] 
 **page** | **str**| Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied the filter  field should not be supplied. | [optional] 
 **limit** | **int**| The maximum number of subscriptions to retrieve. | [optional] 

### Return type

[**ResourceListOfSubscription**](ResourceListOfSubscription.md)

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

# **update_subscription**
> Subscription updateSubscription = update_subscription(scope, code, update_subscription)

UpdateSubscription: Update an existing subscription.

### Example

```python
api_instance = api_client_factory.build(SubscriptionsApi)
scope = 'scope_example' # str
code = 'code_example' # str
update_subscription = UpdateSubscription()
api_response = api_instance.update_subscription(scope, code, update_subscription)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a subscription | [required] 
 **code** | **str**| The code that identifies a subscription | [required] 
 **update_subscription** | [**UpdateSubscription**](UpdateSubscription.md)| The data to update a subscription | [required] 

### Return type

[**Subscription**](Subscription.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | No subscription exists in current scope |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

