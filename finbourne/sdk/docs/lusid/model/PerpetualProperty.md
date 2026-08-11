# PerpetualProperty

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **key** | **str** | Required | The key of the property. This takes the format {domain}/{scope}/{code} e.g. &#39;Instrument/system/Name&#39; or &#39;Transaction/strategy/quantsignal&#39;. |
| **value** | [PropertyValue](PropertyValue.md) | Optional | *No description available.* |
| **reference_data** | [Dict[str, PropertyReferenceDataValue]](PropertyReferenceDataValue.md) | Optional | The ReferenceData linked to the value of the property. The ReferenceData is taken from the DataType on the PropertyDefinition that defines the property. *(read-only)* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PerpetualProperty import PerpetualProperty

instance = PerpetualProperty(
    key="...",  # required — The key of the property. This takes the format {domain}/{scope}/{code} e.g. &#39;Instrument/system/Name&#39; or &#39;Transaction/strategy/quantsignal&#39;.
    value=PropertyValue(...),  # optional
    reference_data=PropertyReferenceDataValue(...)  # optional — The ReferenceData linked to the value of the property. The ReferenceData is taken from the DataType on the PropertyDefinition that defines the property.
)
```

- [PropertyValue](PropertyValue.md)
- [PropertyReferenceDataValue](PropertyReferenceDataValue.md) — used in `reference_data`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

