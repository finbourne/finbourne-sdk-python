# DataTypeSummary

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type_value_range** | **str** | Required | Indicates the range of data acceptable by a data type. The available values are: Open, Closed |
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **display_name** | **str** | Required | The display name of the data type. |
| **description** | **str** | Required | The description of the data type. |
| **value_type** | **str** | Required | The expected type of the values. The available values are: String, Int, Decimal, DateTime, Boolean, Map, List, PropertyArray, Percentage, Code, Id, Uri, CurrencyAndAmount, TradePrice, Currency, MetricValue, ResourceId, ResultValue, CutLocalTime, DateOrCutLabel, UnindexedText |
| **acceptable_values** | **List[str]** | Optional | The acceptable set of values for this data type. Only applies to &#39;open&#39; value type range. |
| **unit_schema** | **str** | Optional | The schema of the data type&#39;s units. The available values are: NoUnits, Basic, Iso4217Currency |
| **acceptable_units** | [List[IUnitDefinitionDto]](IUnitDefinitionDto.md) | Optional | The definitions of the acceptable units. |
| **version** | [Version](Version.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.DataTypeSummary import DataTypeSummary

instance = DataTypeSummary(
    type_value_range="...",  # required — Indicates the range of data acceptable by a data type. The available values are: Open, Closed
    id=ResourceId(...),  # required
    display_name="...",  # required — The display name of the data type.
    description="...",  # required — The description of the data type.
    value_type="...",  # required — The expected type of the values. The available values are: String, Int, Decimal, DateTime, Boolean, Map, List, PropertyArray, Percentage, Code, Id, Uri, CurrencyAndAmount, TradePrice, Currency, MetricValue, ResourceId, ResultValue, CutLocalTime, DateOrCutLabel, UnindexedText
    acceptable_values=,  # optional — The acceptable set of values for this data type. Only applies to &#39;open&#39; value type range.
    unit_schema="...",  # optional — The schema of the data type&#39;s units. The available values are: NoUnits, Basic, Iso4217Currency
    acceptable_units=[],  # optional — The definitions of the acceptable units.
    version=Version(...)  # optional
)
```

- [ResourceId](ResourceId.md)
- [IUnitDefinitionDto](IUnitDefinitionDto.md) — used in `acceptable_units`
- [Version](Version.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

