# DataType

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type_value_range** | **str** | Required | The available values are: Open, Closed |
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **display_name** | **str** | Required | *No description available.* |
| **description** | **str** | Required | *No description available.* |
| **value_type** | **str** | Required | The available values are: String, Int, Decimal, DateTime, Boolean, Map, List, PropertyArray, Percentage, Code, Id, Uri, CurrencyAndAmount, TradePrice, Currency, MetricValue, ResourceId, ResultValue, CutLocalTime, DateOrCutLabel, UnindexedText |
| **acceptable_values** | **List[str]** | Optional | *No description available.* |
| **unit_schema** | **str** | Optional | The available values are: NoUnits, Basic, Iso4217Currency |
| **acceptable_units** | [List[IUnitDefinitionDto]](IUnitDefinitionDto.md) | Optional | *No description available.* |
| **reference_data** | [ReferenceData](ReferenceData.md) | Optional | *No description available.* |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **staged_modifications** | [StagedModificationsInfo](StagedModificationsInfo.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.DataType import DataType

instance = DataType(
    type_value_range="...",  # required — The available values are: Open, Closed
    id=ResourceId(...),  # required
    display_name="...",  # required
    description="...",  # required
    value_type="...",  # required — The available values are: String, Int, Decimal, DateTime, Boolean, Map, List, PropertyArray, Percentage, Code, Id, Uri, CurrencyAndAmount, TradePrice, Currency, MetricValue, ResourceId, ResultValue, CutLocalTime, DateOrCutLabel, UnindexedText
    acceptable_values=,  # optional
    unit_schema="...",  # optional — The available values are: NoUnits, Basic, Iso4217Currency
    acceptable_units=[],  # optional
    reference_data=ReferenceData(...),  # optional
    version=Version(...),  # optional
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    staged_modifications=StagedModificationsInfo(...),  # optional
    links=[]  # optional
)
```

- [ResourceId](ResourceId.md)
- [IUnitDefinitionDto](IUnitDefinitionDto.md)
- [ReferenceData](ReferenceData.md)
- [Version](Version.md)
- [StagedModificationsInfo](StagedModificationsInfo.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

