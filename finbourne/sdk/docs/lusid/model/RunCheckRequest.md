# RunCheckRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **lusid_entity_dataset** | [LusidEntityDataset](LusidEntityDataset.md) | Optional | *No description available.* |
| **limit_individual_breaches_per_rule** | **int** | Optional | The maximum number of individual breaches to return per rule. Defaults to 100 if not specified. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RunCheckRequest import RunCheckRequest

instance = RunCheckRequest(
    lusid_entity_dataset=LusidEntityDataset(...),  # optional
    limit_individual_breaches_per_rule=0  # optional — The maximum number of individual breaches to return per rule. Defaults to 100 if not specified.
)
```


## Related Models

- [LusidEntityDataset](LusidEntityDataset.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

