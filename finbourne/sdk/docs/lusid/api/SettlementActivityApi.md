# lusid.SettlementActivityApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_settlement_activity**](SettlementActivityApi.md#query_settlement_activity) | **POST** /api/api/settlementactivities/$query | [EARLY ACCESS] QuerySettlementActivity: Query Settlement Activity


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.settlement_activity_api import SettlementActivityApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(SettlementActivityApi)
```

---

# **query_settlement_activity**
> ResourceListWithPostBodiesOfSettlementActivityToSettlementActivityQuery querySettlementActivity = query_settlement_activity(settlement_activity_query)

[EARLY ACCESS] QuerySettlementActivity: Query Settlement Activity

Queries settlement activity (Expected and Settled) for the specified portfolios and/or portfolio groups.

### Example

```python
api_instance = api_client_factory.build(SettlementActivityApi)
settlement_activity_query = SettlementActivityQuery()
api_response = api_instance.query_settlement_activity(settlement_activity_query)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement_activity_query** | [**SettlementActivityQuery**](SettlementActivityQuery.md)| The query parameters controlling which settlement activity is returned. | [required] 

### Return type

[**ResourceListWithPostBodiesOfSettlementActivityToSettlementActivityQuery**](ResourceListWithPostBodiesOfSettlementActivityToSettlementActivityQuery.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested settlement activity for the specified portfolios and portfolio groups |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

