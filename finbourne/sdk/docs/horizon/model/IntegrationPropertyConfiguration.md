# IntegrationPropertyConfiguration

Response containing the description of an integration.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Required | The Integration this property configuration applies to |
| **properties** | [List[PropertyMapping]](PropertyMapping.md) | Required | The mandatory and optional properties available in this integration |
| **fields** | [List[FieldMapping]](FieldMapping.md) | Required | The fields available in this integration |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.IntegrationPropertyConfiguration import IntegrationPropertyConfiguration

instance = IntegrationPropertyConfiguration(
    type="...",  # required — The Integration this property configuration applies to
    properties=[],  # required — The mandatory and optional properties available in this integration
    fields=[]  # required — The fields available in this integration
)
```

- [PropertyMapping](PropertyMapping.md) — used in `properties`
- [FieldMapping](FieldMapping.md) — used in `fields`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

