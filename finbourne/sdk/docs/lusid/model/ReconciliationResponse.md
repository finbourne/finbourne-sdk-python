# ReconciliationResponse

Class representing the set of comparisons that result from comparing holdings and their valuations between two separate evaluations.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **comparisons** | [List[ReconciliationLine]](ReconciliationLine.md) | Optional | List of comparisons of left to right hand sides. |
| **data_schema** | [ResultDataSchema](ResultDataSchema.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ReconciliationResponse import ReconciliationResponse

instance = ReconciliationResponse(
    comparisons=[],  # optional — List of comparisons of left to right hand sides.
    data_schema=ResultDataSchema(...)  # optional
)
```


## Related Models

- [ReconciliationLine](ReconciliationLine.md) — used in `comparisons`
- [ResultDataSchema](ResultDataSchema.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

