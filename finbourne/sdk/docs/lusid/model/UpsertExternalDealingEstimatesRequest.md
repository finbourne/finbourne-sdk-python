# UpsertExternalDealingEstimatesRequest

One dealing point's dealing estimates for the fund named in the route, as a third-party transfer agent sends them.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **dealing_point** | **datetime** | Required | *No description available.* |
| **source** | [ExternalDealingEstimateSource](ExternalDealingEstimateSource.md) | Required | *No description available.* |
| **complete** | **bool** | Optional | *No description available.* |
| **sent_at** | **datetime** | Optional | *No description available.* |
| **lines** | [Dict[str, ExternalDealingEstimateLine]](ExternalDealingEstimateLine.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertExternalDealingEstimatesRequest import UpsertExternalDealingEstimatesRequest

instance = UpsertExternalDealingEstimatesRequest(
    dealing_point=datetime.now(),  # required
    source=ExternalDealingEstimateSource(...),  # required
    complete=True,  # optional
    sent_at=datetime.now(),  # optional
    lines=ExternalDealingEstimateLine(...)  # required
)
```

- [ExternalDealingEstimateSource](ExternalDealingEstimateSource.md)
- [ExternalDealingEstimateLine](ExternalDealingEstimateLine.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

