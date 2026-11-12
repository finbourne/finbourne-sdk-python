# UpsertExternalDealingEstimateResult

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **fund_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **dealing_point** | **datetime** | Optional | *No description available.* |
| **late** | **bool** | Optional | *No description available.* |
| **upserted_estimates** | [List[ResourceId]](ResourceId.md) | Optional | *No description available.* |
| **deleted_estimates** | [List[ResourceId]](ResourceId.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertExternalDealingEstimateResult import UpsertExternalDealingEstimateResult

instance = UpsertExternalDealingEstimateResult(
    fund_id=ResourceId(...),  # optional
    dealing_point=datetime.now(),  # optional
    late=True,  # optional
    upserted_estimates=[],  # optional
    deleted_estimates=[]  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

