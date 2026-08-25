# PortfolioHoldingDataset

Contains the run-time parameters that are appropriate for check definitions  with datasetSchema.type = \"PortfolioContents\"
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **as_at** | **datetime** | Optional | The asAt date to fetch the data. Nullable. Defaults to latest. |
| **effective_at** | **datetime** | Optional | The effectiveAt date to fetch the data. Nullable. Defaults to latest. |
| **portfolio_scope** | **str** | Optional | The scope of the portfolios whose holdings to check. Nullable. Every scope is checked if not provided. |
| **portfolio_selector_attribute** | **str** | Optional | An attribute (field name or propertyKey) to use to narrow down the portfolios whose holdings are checked. |
| **portfolio_selector_value** | **str** | Optional | The value of the above attribute used to narrow down the portfolios. |
| **holding_selector_attribute** | **str** | Optional | An attribute (field name, propertyKey or sub-holding key) to use to narrow down the holdings checked  within those portfolios. |
| **holding_selector_value** | **str** | Optional | The value of the above attribute used to narrow down the holdings. |
| **by_taxlots** | **bool** | Optional | Whether to expand holdings to their underlying tax lots. Defaults to false. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PortfolioHoldingDataset import PortfolioHoldingDataset

instance = PortfolioHoldingDataset(
    as_at=datetime.now(),  # optional — The asAt date to fetch the data. Nullable. Defaults to latest.
    effective_at=datetime.now(),  # optional — The effectiveAt date to fetch the data. Nullable. Defaults to latest.
    portfolio_scope="...",  # optional — The scope of the portfolios whose holdings to check. Nullable. Every scope is checked if not provided.
    portfolio_selector_attribute="...",  # optional — An attribute (field name or propertyKey) to use to narrow down the portfolios whose holdings are checked.
    portfolio_selector_value="...",  # optional — The value of the above attribute used to narrow down the portfolios.
    holding_selector_attribute="...",  # optional — An attribute (field name, propertyKey or sub-holding key) to use to narrow down the holdings checked  within those portfolios.
    holding_selector_value="...",  # optional — The value of the above attribute used to narrow down the holdings.
    by_taxlots=True  # optional — Whether to expand holdings to their underlying tax lots. Defaults to false.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

