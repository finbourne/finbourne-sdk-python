# EstimateValuationDifference

How far apart the estimate-price and last-official-price valuations of the net dealing flow are.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **amount** | **float** | Required | The estimate-price net cashflow less the last-official-price net cashflow, in the fund currency. Negative when the last official price values the net flow higher. |
| **pct_of_nav** | **float** | Optional | The amount as a percentage of the fund&#39;s NAV at the previous valuation point. Absent when there is no previous NAV. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.EstimateValuationDifference import EstimateValuationDifference

instance = EstimateValuationDifference(
    amount=0.0,  # required — The estimate-price net cashflow less the last-official-price net cashflow, in the fund currency. Negative when the last official price values the net flow higher.
    pct_of_nav=0.0  # optional — The amount as a percentage of the fund&#39;s NAV at the previous valuation point. Absent when there is no previous NAV.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

