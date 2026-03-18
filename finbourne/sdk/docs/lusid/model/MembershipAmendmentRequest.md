# MembershipAmendmentRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **custom_data_model_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **entity_type** | **str** | Required | The type of the entity that is being added or removed from the Custom Data Model. |
| **entity_unique_id** | **str** | Required | The entity unique identifier of the entity that is being added or removed from the Custom Data Model. |
| **operation** | **str** | Required | The operation to be performed on the entity&#39;s membership in the Custom Data Model. Either &#39;Add&#39; or &#39;Remove&#39;. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.MembershipAmendmentRequest import MembershipAmendmentRequest

instance = MembershipAmendmentRequest(
    custom_data_model_id=ResourceId(...),  # required
    entity_type="...",  # required — The type of the entity that is being added or removed from the Custom Data Model.
    entity_unique_id="...",  # required — The entity unique identifier of the entity that is being added or removed from the Custom Data Model.
    operation="..."  # required — The operation to be performed on the entity&#39;s membership in the Custom Data Model. Either &#39;Add&#39; or &#39;Remove&#39;.
)
```


## Related Models

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

