# ModelProperty

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **key** | **str** | Required | The key of the property. This takes the format {domain}/{scope}/{code} e.g. &#39;Instrument/system/Name&#39; or &#39;Transaction/strategy/quantsignal&#39;. |
| **value** | [PropertyValue](PropertyValue.md) | Optional | *No description available.* |
| **effective_from** | **datetime** | Optional | The effective datetime from which the property is valid. |
| **effective_until** | **datetime** | Optional | The effective datetime until which the property is valid. If not supplied this will be valid indefinitely, or until the next &#39;effectiveFrom&#39; datetime of the property. |
| **reference_data** | [Dict[str, PropertyReferenceDataValue]](PropertyReferenceDataValue.md) | Optional | The ReferenceData linked to the value of the property. The ReferenceData is taken from the DataType on the PropertyDefinition that defines the property. *(read-only)* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ModelProperty import ModelProperty

instance = ModelProperty(
    key="...",  # required — The key of the property. This takes the format {domain}/{scope}/{code} e.g. &#39;Instrument/system/Name&#39; or &#39;Transaction/strategy/quantsignal&#39;.
    value=PropertyValue(...),  # optional
    effective_from=datetime.now(),  # optional — The effective datetime from which the property is valid.
    effective_until=datetime.now(),  # optional — The effective datetime until which the property is valid. If not supplied this will be valid indefinitely, or until the next &#39;effectiveFrom&#39; datetime of the property.
    reference_data=PropertyReferenceDataValue(...)  # optional — The ReferenceData linked to the value of the property. The ReferenceData is taken from the DataType on the PropertyDefinition that defines the property.
)
```

- [PropertyValue](PropertyValue.md)
- [PropertyReferenceDataValue](PropertyReferenceDataValue.md) — used in `reference_data`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

