# PerformanceReturn

A list of Returns.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **effective_at** | **datetime** | Required | The effectiveAt for the return. |
| **rate_of_return** | **float** | Required | The return number. |
| **opening_market_value** | **float** | Optional | The opening market value. |
| **closing_market_value** | **float** | Optional | The closing market value. |
| **period** | **str** | Optional | Upsert the returns on a Daily or Monthly period. Defaults to Daily. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PerformanceReturn import PerformanceReturn

instance = PerformanceReturn(
    effective_at=datetime.now(),  # required — The effectiveAt for the return.
    rate_of_return=0.0,  # required — The return number.
    opening_market_value=0.0,  # optional — The opening market value.
    closing_market_value=0.0,  # optional — The closing market value.
    period="..."  # optional — Upsert the returns on a Daily or Monthly period. Defaults to Daily.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

