# ApplicableEntityTypes

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **applicable_entity_types_to_add** | **List[str]** | Optional | The types of entities this relational dataset definition can be applied to (e.g. Instrument, Portfolio, etc.). |
| **applicable_entity_types_to_remove** | **List[str]** | Optional | The types of entities this relational dataset definition can be applied to (e.g. Instrument, Portfolio, etc.). |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ApplicableEntityTypes import ApplicableEntityTypes

instance = ApplicableEntityTypes(
    applicable_entity_types_to_add=,  # optional — The types of entities this relational dataset definition can be applied to (e.g. Instrument, Portfolio, etc.).
    applicable_entity_types_to_remove=  # optional — The types of entities this relational dataset definition can be applied to (e.g. Instrument, Portfolio, etc.).
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

