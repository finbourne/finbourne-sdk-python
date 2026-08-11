# MappingRule

An individual mapping rule, for mapping between a left and right field/property.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **left** | **str** | Optional | The name of the field/property in the left resource (e.g. a transaction) |
| **right** | **str** | Optional | The name of the field/property in the right resource (e.g. a transaction) |
| **comparison_type** | **str** | Optional | The type of comparison to be performed |
| **comparison_value** | **float** | Optional | The (optional) value used with ComparisonType. |
| **weight** | **float** | Optional | A factor used to influence the importance of this item. |
| **mapped_strings** | [List[MappedString]](MappedString.md) | Optional | The (optional) value used to map string values. |
| **is_case_sensitive** | **bool** | Optional | Should string comparisons take case into account, defaults to &#x60;false&#x60;. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.MappingRule import MappingRule

instance = MappingRule(
    left="...",  # optional — The name of the field/property in the left resource (e.g. a transaction)
    right="...",  # optional — The name of the field/property in the right resource (e.g. a transaction)
    comparison_type="...",  # optional — The type of comparison to be performed
    comparison_value=0.0,  # optional — The (optional) value used with ComparisonType.
    weight=0.0,  # optional — A factor used to influence the importance of this item.
    mapped_strings=[],  # optional — The (optional) value used to map string values.
    is_case_sensitive=True  # optional — Should string comparisons take case into account, defaults to &#x60;false&#x60;.
)
```

- [MappedString](MappedString.md) — used in `mapped_strings`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

