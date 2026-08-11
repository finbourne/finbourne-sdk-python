# ReconciliationSideConfiguration

Specification for one side of a valuations/positions scheduled reconciliation
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **recipe_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **effective_at** | **datetime** | Optional | *No description available.* |
| **as_at** | **datetime** | Optional | *No description available.* |
| **currency** | **str** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ReconciliationSideConfiguration import ReconciliationSideConfiguration

instance = ReconciliationSideConfiguration(
    recipe_id=ResourceId(...),  # optional
    effective_at=datetime.now(),  # optional
    as_at=datetime.now(),  # optional
    currency="..."  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

