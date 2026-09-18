# PortfolioTransactionResult

Represents transaction details for a data quality check result.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **entity_type** | **str** | Optional | The type of the entity. Always \&quot;Transaction\&quot;. |
| **transaction_view** | **str** | Optional | Whether this is an input or an output transaction |
| **as_at** | **datetime** | Optional | The as-at timestamp for the transaction |
| **transaction_date** | **datetime** | Optional | The transaction date |
| **transaction_id** | **str** | Optional | The transaction&#39;s identifier within its portfolio |
| **entity_unique_id** | **str** | Optional | The transaction&#39;s unique identifier across portfolios |
| **source_portfolio_scope** | **str** | Optional | The scope of the portfolio this transaction came from |
| **source_portfolio_code** | **str** | Optional | The code of the portfolio this transaction came from |
| **source_portfolio_entity_unique_id** | **str** | Optional | The unique identifier of the portfolio this transaction came from |
| **source_portfolio_display_name** | **str** | Optional | The display name of the portfolio this transaction came from |
| **lusid_instrument_id** | **str** | Optional | The LUSID instrument identifier of the instrument transacted |
| **instrument_display_name** | **str** | Optional | The name of the instrument transacted |
| **transaction_type** | **str** | Optional | The transaction type, e.g. Buy, Sell |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PortfolioTransactionResult import PortfolioTransactionResult

instance = PortfolioTransactionResult(
    entity_type="...",  # optional — The type of the entity. Always \&quot;Transaction\&quot;.
    transaction_view="...",  # optional — Whether this is an input or an output transaction
    as_at=datetime.now(),  # optional — The as-at timestamp for the transaction
    transaction_date=datetime.now(),  # optional — The transaction date
    transaction_id="...",  # optional — The transaction&#39;s identifier within its portfolio
    entity_unique_id="...",  # optional — The transaction&#39;s unique identifier across portfolios
    source_portfolio_scope="...",  # optional — The scope of the portfolio this transaction came from
    source_portfolio_code="...",  # optional — The code of the portfolio this transaction came from
    source_portfolio_entity_unique_id="...",  # optional — The unique identifier of the portfolio this transaction came from
    source_portfolio_display_name="...",  # optional — The display name of the portfolio this transaction came from
    lusid_instrument_id="...",  # optional — The LUSID instrument identifier of the instrument transacted
    instrument_display_name="...",  # optional — The name of the instrument transacted
    transaction_type="..."  # optional — The transaction type, e.g. Buy, Sell
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

