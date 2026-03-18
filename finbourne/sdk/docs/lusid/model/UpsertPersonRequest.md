# UpsertPersonRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **identifiers** | [Dict[str, ModelProperty]](ModelProperty.md) | Required | The identifiers the person will be upserted with.The provided keys should be idTypeScope, idTypeCode, code |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of properties associated to the Person. There can be multiple properties associated with a property key. |
| **display_name** | **str** | Required | The display name of the Person |
| **description** | **str** | Optional | The description of the Person |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertPersonRequest import UpsertPersonRequest

instance = UpsertPersonRequest(
    identifiers=ModelProperty(...),  # required — The identifiers the person will be upserted with.The provided keys should be idTypeScope, idTypeCode, code
    properties=ModelProperty(...),  # optional — A set of properties associated to the Person. There can be multiple properties associated with a property key.
    display_name="...",  # required — The display name of the Person
    description="..."  # optional — The description of the Person
)
```


## Related Models

- [ModelProperty](ModelProperty.md) — used in `identifiers`
- [ModelProperty](ModelProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

