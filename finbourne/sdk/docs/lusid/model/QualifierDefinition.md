# QualifierDefinition

A qualifier as returned on read: the request shape plus the value type resolved from its data type.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **key** | **str** | Optional | The key by which the qualifier is addressed, for example &#39;direction&#39;. Addressed in filters, sort orders and derivation formulae as Properties[{propertyKey}].Qualifiers[{qualifierKey}]. Validated under the same rules as a property code. |
| **display_name** | **str** | Optional | The display name of the qualifier. |
| **description** | **str** | Optional | Describes the qualifier. Optional; null where not supplied. |
| **data_type_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **value_type** | **str** | Optional | The type of value this qualifier carries, resolved from its data type. Available values: String, Int, Decimal, DateTime, Boolean, Map, List, PropertyArray, Percentage, Code, Id, Uri, CurrencyAndAmount, TradePrice, Currency, MetricValue, ResourceId, ResultValue, CutLocalTime, DateOrCutLabel, UnindexedText. |
| **is_required** | **bool** | Optional | Whether a value for this qualifier must be supplied when a value of the property is written. Defaults to false, and is returned as a boolean rather than as null. Validated on write only, so setting it true does not retroactively invalidate values stored before the change. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.QualifierDefinition import QualifierDefinition

instance = QualifierDefinition(
    key="...",  # optional — The key by which the qualifier is addressed, for example &#39;direction&#39;. Addressed in filters, sort orders and derivation formulae as Properties[{propertyKey}].Qualifiers[{qualifierKey}]. Validated under the same rules as a property code.
    display_name="...",  # optional — The display name of the qualifier.
    description="...",  # optional — Describes the qualifier. Optional; null where not supplied.
    data_type_id=ResourceId(...),  # optional
    value_type="...",  # optional — The type of value this qualifier carries, resolved from its data type. Available values: String, Int, Decimal, DateTime, Boolean, Map, List, PropertyArray, Percentage, Code, Id, Uri, CurrencyAndAmount, TradePrice, Currency, MetricValue, ResourceId, ResultValue, CutLocalTime, DateOrCutLabel, UnindexedText.
    is_required=True  # optional — Whether a value for this qualifier must be supplied when a value of the property is written. Defaults to false, and is returned as a boolean rather than as null. Validated on write only, so setting it true does not retroactively invalidate values stored before the change.
)
```

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

