# lusid.OrderGraphApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_order_graph_blocks**](OrderGraphApi.md#list_order_graph_blocks) | **GET** /api/api/ordergraph/blocks | ListOrderGraphBlocks: Lists blocks that pass the filter provided, and builds a summary picture of the state of their associated order entities.
[**list_order_graph_placement_children**](OrderGraphApi.md#list_order_graph_placement_children) | **GET** /api/api/ordergraph/placementchildren/{scope}/{code} | [EARLY ACCESS] ListOrderGraphPlacementChildren: Lists all placements for the parent placement specified by the scope and code, and builds a summary picture of the state of their associated order entities.
[**list_order_graph_placements**](OrderGraphApi.md#list_order_graph_placements) | **GET** /api/api/ordergraph/placements | ListOrderGraphPlacements: Lists placements that pass the filter provided, and builds a summary picture of the state of their associated order entities.


### Example

```python
from finbourne.sdk.exceptions import ApiException
from finbourne.sdk.extensions.configuration_options import ConfigurationOptions
from finbourne.sdk.services.lusid.models import *

from finbourne.sdk.extensions import (
  SyncApiClientFactory
)

from finbourne.sdk.services.lusid.api.order_graph_api import OrderGraphApi

# opts = ConfigurationOptions()
# opts.total_timeout_ms = 30_000

# uncomment the below to use an api client factory with overrides
# api_client_factory = SyncApiClientFactory(opts=opts)

api_client_factory = SyncApiClientFactory()
api_instance = api_client_factory.build(OrderGraphApi)
```

---

# **list_order_graph_blocks**
> PagedResourceListOfOrderGraphBlock listOrderGraphBlocks = list_order_graph_blocks(as_at=as_at, pagination_token=pagination_token, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys, use_compliance_v2=use_compliance_v2)

ListOrderGraphBlocks: Lists blocks that pass the filter provided, and builds a summary picture of the state of their associated order entities.

Lists all blocks of orders, subject to the filter, along with the IDs of orders, placements, allocations and  executions in the block, the total quantities of each, and a simple text field describing the overall state.

### Example

```python
api_instance = api_client_factory.build(OrderGraphApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
pagination_token = 'pagination_token_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
limit = 56 # int (optional)
filter = '' # str (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
use_compliance_v2 = False # bool (optional)
api_response = api_instance.list_order_graph_blocks(as_at=as_at, pagination_token=pagination_token, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys, use_compliance_v2=use_compliance_v2)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| See https://support.lusid.com/knowledgebase/article/KA-01832/ | [optional] 
 **pagination_token** | **str**| See https://support.lusid.com/knowledgebase/article/KA-01915/ | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **limit** | **int**| See https://support.lusid.com/knowledgebase/article/KA-01915/ | [optional] 
 **filter** | **str**| See https://support.lusid.com/knowledgebase/article/KA-01914/ | [optional] [default to &#39;&#39;]
 **property_keys** | [**List[str]**](str.md)| Must be block-level properties. See https://support.lusid.com/knowledgebase/article/KA-01855/ | [optional] 
 **use_compliance_v2** | **bool**| Whether to use the V2 compliance engine when deriving compliance statuses for orders. (default: false) | [optional] [default to False]

### Return type

[**PagedResourceListOfOrderGraphBlock**](PagedResourceListOfOrderGraphBlock.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Blocks in scope. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_order_graph_placement_children**
> PagedResourceListOfOrderGraphPlacement listOrderGraphPlacementChildren = list_order_graph_placement_children(scope, code, as_at=as_at, pagination_token=pagination_token, sort_by=sort_by, limit=limit, property_keys=property_keys)

[EARLY ACCESS] ListOrderGraphPlacementChildren: Lists all placements for the parent placement specified by the scope and code, and builds a summary picture of the state of their associated order entities.

Lists all child order placements, for the specified parent placement, along with the IDs of the block and order that the  placement is for, each placement's quantity, the IDs of all allocations and executions in the placement  and the total quantities of those, and a simple text field describing the overall state of the placement.

### Example

```python
api_instance = api_client_factory.build(OrderGraphApi)
scope = 'scope_example' # str
code = 'code_example' # str
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
pagination_token = 'pagination_token_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
limit = 56 # int (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.list_order_graph_placement_children(scope, code, as_at=as_at, pagination_token=pagination_token, sort_by=sort_by, limit=limit, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The parent placement&#39;s scope | [required] 
 **code** | **str**| The parent placement&#39;s code | [required] 
 **as_at** | **datetime**| See https://support.lusid.com/knowledgebase/article/KA-01832/ | [optional] 
 **pagination_token** | **str**| See https://support.lusid.com/knowledgebase/article/KA-01915/ | [optional] 
 **sort_by** | [**List[str]**](str.md)| Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName. | [optional] 
 **limit** | **int**| See https://support.lusid.com/knowledgebase/article/KA-01915/ | [optional] 
 **property_keys** | [**List[str]**](str.md)| Must be placement properties. See https://support.lusid.com/knowledgebase/article/KA-01855/ | [optional] 

### Return type

[**PagedResourceListOfOrderGraphPlacement**](PagedResourceListOfOrderGraphPlacement.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List all child Placements for the specified Placement. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

---

# **list_order_graph_placements**
> PagedResourceListOfOrderGraphPlacement listOrderGraphPlacements = list_order_graph_placements(as_at=as_at, pagination_token=pagination_token, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys)

ListOrderGraphPlacements: Lists placements that pass the filter provided, and builds a summary picture of the state of their associated order entities.

Lists all order placements, subject to the filter, along with the IDs of the block and order that the  placement is for, each placement's quantity, the IDs of all allocations and executions in the placement  and the total quantities of those, and a simple text field describing the overall state of the placement.

### Example

```python
api_instance = api_client_factory.build(OrderGraphApi)
as_at = '2013-10-20T19:20:30+01:00' # datetime (optional)
pagination_token = 'pagination_token_example' # str (optional)
sort_by = ['sort_by_example'] # List[str] (optional)
limit = 56 # int (optional)
filter = '' # str (optional)
property_keys = ['property_keys_example'] # List[str] (optional)
api_response = api_instance.list_order_graph_placements(as_at=as_at, pagination_token=pagination_token, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys)
pprint(api_response)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| See https://support.lusid.com/knowledgebase/article/KA-01832/ | [optional] 
 **pagination_token** | **str**| See https://support.lusid.com/knowledgebase/article/KA-01915/ | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **limit** | **int**| See https://support.lusid.com/knowledgebase/article/KA-01915/ | [optional] 
 **filter** | **str**| See https://support.lusid.com/knowledgebase/article/KA-01914/ | [optional] [default to &#39;&#39;]
 **property_keys** | [**List[str]**](str.md)| Must be placement properties. See https://support.lusid.com/knowledgebase/article/KA-01855/ | [optional] 

### Return type

[**PagedResourceListOfOrderGraphPlacement**](PagedResourceListOfOrderGraphPlacement.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Placements in scope. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../README.md)

