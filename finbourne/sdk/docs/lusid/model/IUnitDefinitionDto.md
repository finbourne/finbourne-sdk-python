# IUnitDefinitionDto

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **var_schema** | **str** | Optional | The available values are: NoUnits, Basic, Iso4217Currency |
| **code** | **str** | Optional | *No description available.* *(read-only)* |
| **display_name** | **str** | Optional | *No description available.* *(read-only)* |
| **description** | **str** | Optional | *No description available.* *(read-only)* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.IUnitDefinitionDto import IUnitDefinitionDto

instance = IUnitDefinitionDto(
    var_schema="...",  # optional — The available values are: NoUnits, Basic, Iso4217Currency
    code="...",  # optional
    display_name="...",  # optional
    description="..."  # optional
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

