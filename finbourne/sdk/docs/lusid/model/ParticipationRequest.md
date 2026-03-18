# ParticipationRequest

A request to create or update a Participation.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **placement_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **order_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ParticipationRequest import ParticipationRequest

instance = ParticipationRequest(
    id=ResourceId(...),  # required
    placement_id=ResourceId(...),  # required
    order_id=ResourceId(...)  # required
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

