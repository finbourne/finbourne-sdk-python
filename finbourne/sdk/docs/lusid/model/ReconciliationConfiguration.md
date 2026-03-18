# ReconciliationConfiguration

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **left** | [ReconciliationSideConfiguration](ReconciliationSideConfiguration.md) | Optional | *No description available.* |
| **right** | [ReconciliationSideConfiguration](ReconciliationSideConfiguration.md) | Optional | *No description available.* |
| **mapping_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ReconciliationConfiguration import ReconciliationConfiguration

instance = ReconciliationConfiguration(
    left=ReconciliationSideConfiguration(...),  # optional
    right=ReconciliationSideConfiguration(...),  # optional
    mapping_id=ResourceId(...)  # optional
)
```


## Related Models

- [ReconciliationSideConfiguration](ReconciliationSideConfiguration.md)
- [ReconciliationSideConfiguration](ReconciliationSideConfiguration.md)
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

