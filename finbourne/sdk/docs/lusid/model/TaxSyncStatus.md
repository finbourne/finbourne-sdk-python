# TaxSyncStatus

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **portfolios** | [List[TaxPortfolioSyncStatus]](TaxPortfolioSyncStatus.md) | Required | The sync position of each portfolio in the Fund. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TaxSyncStatus import TaxSyncStatus

instance = TaxSyncStatus(
    portfolios=[]  # required — The sync position of each portfolio in the Fund.
)
```


## Related Models

- [TaxPortfolioSyncStatus](TaxPortfolioSyncStatus.md) — used in `portfolios`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

