# MembershipAmendmentResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **custom_data_model_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **entity_type** | **str** | Required | The type of the entity that was added or removed from the Custom Data Model. |
| **entity_unique_id** | **str** | Required | The entity unique identifier of the entity that was added or removed from the Custom Data Model. |
| **operation** | **str** | Required | The operation that was performed on the entity&#39;s membership in the Custom Data Model. Either &#39;Add&#39; or &#39;Remove&#39;. |
| **entity_display_name** | **str** | Required | The display name of the entity that was added or removed from the Custom Data Model. |
| **data_model_membership** | [DataModelMembership](DataModelMembership.md) | Optional | *No description available.* |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **staged_modifications** | [StagedModificationsInfo](StagedModificationsInfo.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.MembershipAmendmentResponse import MembershipAmendmentResponse

instance = MembershipAmendmentResponse(
    custom_data_model_id=ResourceId(...),  # required
    entity_type="...",  # required — The type of the entity that was added or removed from the Custom Data Model.
    entity_unique_id="...",  # required — The entity unique identifier of the entity that was added or removed from the Custom Data Model.
    operation="...",  # required — The operation that was performed on the entity&#39;s membership in the Custom Data Model. Either &#39;Add&#39; or &#39;Remove&#39;.
    entity_display_name="...",  # required — The display name of the entity that was added or removed from the Custom Data Model.
    data_model_membership=DataModelMembership(...),  # optional
    version=Version(...),  # optional
    staged_modifications=StagedModificationsInfo(...)  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [DataModelMembership](DataModelMembership.md)
- [Version](Version.md)
- [StagedModificationsInfo](StagedModificationsInfo.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

