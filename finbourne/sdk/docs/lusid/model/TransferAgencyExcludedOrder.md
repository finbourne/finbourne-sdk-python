# TransferAgencyExcludedOrder

An order left out of the sizing an estimate was struck from, with the reason it was left out.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **order_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **reason** | **str** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TransferAgencyExcludedOrder import TransferAgencyExcludedOrder

instance = TransferAgencyExcludedOrder(
    order_id=ResourceId(...),  # optional
    reason="..."  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

