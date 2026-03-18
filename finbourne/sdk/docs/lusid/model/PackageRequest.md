# PackageRequest

A request to create or update a Package.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **order_ids** | [List[ResourceId]](ResourceId.md) | Required | Related order ids. |
| **order_instruction_ids** | [List[ResourceId]](ResourceId.md) | Required | Related order instruction ids. |
| **properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | Client-defined properties associated with this execution. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PackageRequest import PackageRequest

instance = PackageRequest(
    id=ResourceId(...),  # required
    order_ids=[],  # required — Related order ids.
    order_instruction_ids=[],  # required — Related order instruction ids.
    properties=PerpetualProperty(...)  # optional — Client-defined properties associated with this execution.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md) — used in `order_ids`
- [ResourceId](ResourceId.md) — used in `order_instruction_ids`
- [PerpetualProperty](PerpetualProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

