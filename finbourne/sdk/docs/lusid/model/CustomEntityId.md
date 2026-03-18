# CustomEntityId

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **identifier_scope** | **str** | Required | The scope the identifier resides in (the scope of the identifier property definition). |
| **identifier_type** | **str** | Required | What the identifier represents (the code of the identifier property definition). |
| **identifier_value** | **str** | Required | The value of the identifier for this entity. |
| **effective_from** | **datetime** | Optional | The effective datetime from which the identifier is valid. |
| **effective_until** | **datetime** | Optional | The effective datetime until which the identifier is valid. If not supplied this will be valid indefinitely, or until the next &#39;effectiveFrom&#39; datetime of the identifier. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CustomEntityId import CustomEntityId

instance = CustomEntityId(
    identifier_scope="...",  # required — The scope the identifier resides in (the scope of the identifier property definition).
    identifier_type="...",  # required — What the identifier represents (the code of the identifier property definition).
    identifier_value="...",  # required — The value of the identifier for this entity.
    effective_from=datetime.now(),  # optional — The effective datetime from which the identifier is valid.
    effective_until=datetime.now()  # optional — The effective datetime until which the identifier is valid. If not supplied this will be valid indefinitely, or until the next &#39;effectiveFrom&#39; datetime of the identifier.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

