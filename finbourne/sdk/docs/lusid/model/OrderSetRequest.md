# OrderSetRequest

A request to create or update multiple Orders.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **order_requests** | [List[OrderRequest]](OrderRequest.md) | Optional | A collection of OrderRequests. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.OrderSetRequest import OrderSetRequest

instance = OrderSetRequest(
    order_requests=[]  # optional — A collection of OrderRequests.
)
```


## Related Models

- [OrderRequest](OrderRequest.md) — used in `order_requests`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

