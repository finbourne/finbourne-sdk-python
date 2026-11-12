# TaxPortfolioSyncStatus

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **portfolio_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **last_transaction_as_at** | **datetime** | Optional | The asAt the latest transaction was booked to the portfolio. Absent when the portfolio has no transactions. |
| **last_tax_as_at** | **datetime** | Optional | The asAt the tax engine last processed the Fund, taken from its latest valuation point. Absent when no valuation point has been run. |
| **in_sync** | **bool** | Required | True when the tax position is no older than the latest booked transaction, or the portfolio has no transactions. |
| **asset_class** | **str** | Optional | The asset class of the portfolio&#39;s holdings where the holding data carries one. Optional. |
| **country_of_domicile** | **str** | Optional | The country of domicile of the portfolio&#39;s holdings where the holding data carries one. Optional. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TaxPortfolioSyncStatus import TaxPortfolioSyncStatus

instance = TaxPortfolioSyncStatus(
    portfolio_id=ResourceId(...),  # required
    last_transaction_as_at=datetime.now(),  # optional — The asAt the latest transaction was booked to the portfolio. Absent when the portfolio has no transactions.
    last_tax_as_at=datetime.now(),  # optional — The asAt the tax engine last processed the Fund, taken from its latest valuation point. Absent when no valuation point has been run.
    in_sync=True,  # required — True when the tax position is no older than the latest booked transaction, or the portfolio has no transactions.
    asset_class="...",  # optional — The asset class of the portfolio&#39;s holdings where the holding data carries one. Optional.
    country_of_domicile="..."  # optional — The country of domicile of the portfolio&#39;s holdings where the holding data carries one. Optional.
)
```


## Related Models

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

