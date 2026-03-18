# CustomEntityField

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Required | The name of the field in the custom entity type definition. |
| **value** | **object** | Optional | The value for the field. |
| **effective_from** | **datetime** | Optional | The effective datetime from which the field&#39;s value is valid. For timeVariant fields, this defaults to the beginning of time. |
| **effective_until** | **datetime** | Optional | The effective datetime until which the field&#39;s value is valid. If not supplied, the value will be valid indefinitely or until the next “effectiveFrom” date of the field. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CustomEntityField import CustomEntityField

instance = CustomEntityField(
    name="...",  # required — The name of the field in the custom entity type definition.
    value=,  # optional — The value for the field.
    effective_from=datetime.now(),  # optional — The effective datetime from which the field&#39;s value is valid. For timeVariant fields, this defaults to the beginning of time.
    effective_until=datetime.now()  # optional — The effective datetime until which the field&#39;s value is valid. If not supplied, the value will be valid indefinitely or until the next “effectiveFrom” date of the field.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

