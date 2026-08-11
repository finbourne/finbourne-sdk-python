# StagedModificationsRequestedChangeInterval

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **attribute_name** | **str** | Optional | Name of the property the change applies to. |
| **effective_range** | [StagedModificationEffectiveRange](StagedModificationEffectiveRange.md) | Optional | *No description available.* |
| **previous_value** | [PropertyValue](PropertyValue.md) | Optional | *No description available.* |
| **new_value** | [PropertyValue](PropertyValue.md) | Optional | *No description available.* |
| **as_at_basis** | **str** | Optional | Whether the change represents the modification when the request was made or the modification as it would be at the latest time. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.StagedModificationsRequestedChangeInterval import StagedModificationsRequestedChangeInterval

instance = StagedModificationsRequestedChangeInterval(
    attribute_name="...",  # optional — Name of the property the change applies to.
    effective_range=StagedModificationEffectiveRange(...),  # optional
    previous_value=PropertyValue(...),  # optional
    new_value=PropertyValue(...),  # optional
    as_at_basis="...",  # optional — Whether the change represents the modification when the request was made or the modification as it would be at the latest time.
    links=[]  # optional
)
```

- [StagedModificationEffectiveRange](StagedModificationEffectiveRange.md)
- [PropertyValue](PropertyValue.md)
- [PropertyValue](PropertyValue.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

