# OrderBySpec

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **key** | **str** | Required | The key that uniquely identifies a queryable address in Lusid. |
| **sort_order** | **str** | Required | The available values are: Ascending, Descending |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.OrderBySpec import OrderBySpec

instance = OrderBySpec(
    key="...",  # required — The key that uniquely identifies a queryable address in Lusid.
    sort_order="..."  # required — The available values are: Ascending, Descending
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

