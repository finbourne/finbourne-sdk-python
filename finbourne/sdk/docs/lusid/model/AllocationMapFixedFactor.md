# AllocationMapFixedFactor

The weight of one investor record under a FixedPercentage basis.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **investor_record_id** | **str** | Required | The investor record the factor belongs to. |
| **factor** | **float** | Required | The weight of the investor record. Weights are normalised over the participants that receive the remainder, so they need not sum to 1. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationMapFixedFactor import AllocationMapFixedFactor

instance = AllocationMapFixedFactor(
    investor_record_id="...",  # required — The investor record the factor belongs to.
    factor=0.0  # required — The weight of the investor record. Weights are normalised over the participants that receive the remainder, so they need not sum to 1.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

