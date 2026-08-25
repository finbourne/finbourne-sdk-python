# PortfolioHoldingResult

Represents holding details for a data quality check result, where LusidEntityResult represents a scope-and-code  or identifier-addressed entity. A holding has no scope and code of its own, so it is identified by the portfolio  it came from plus what distinguishes it within that portfolio.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **entity_type** | **str** | Optional | The type of the entity. Always \&quot;Holding\&quot;. |
| **as_at** | **datetime** | Optional | The as-at timestamp for the holding |
| **effective_at** | **datetime** | Optional | The effective-at timestamp for the holding |
| **source_portfolio_scope** | **str** | Optional | The scope of the portfolio this holding came from |
| **source_portfolio_code** | **str** | Optional | The code of the portfolio this holding came from |
| **source_portfolio_entity_unique_id** | **str** | Optional | The unique identifier of the portfolio this holding came from |
| **source_portfolio_display_name** | **str** | Optional | The display name of the portfolio this holding came from |
| **holding_id** | **str** | Optional | The holding&#39;s identifier within its portfolio |
| **taxlot_id** | **str** | Optional | The tax lot identifier, where the holding was expanded to tax lots. Null otherwise. |
| **sub_entity_id** | **str** | Optional | Identifies the holding to the derived property explain API: the holding id on its own, or the holding id  and tax lot id colon-separated where a tax lot is present. |
| **lusid_instrument_id** | **str** | Optional | The LUSID instrument identifier of the instrument held |
| **instrument_display_name** | **str** | Optional | The name of the instrument held |
| **holding_type_name** | **str** | Optional | The kind of holding, e.g. Position, Balance |
| **currency** | **str** | Optional | The currency of the holding |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PortfolioHoldingResult import PortfolioHoldingResult

instance = PortfolioHoldingResult(
    entity_type="...",  # optional — The type of the entity. Always \&quot;Holding\&quot;.
    as_at=datetime.now(),  # optional — The as-at timestamp for the holding
    effective_at=datetime.now(),  # optional — The effective-at timestamp for the holding
    source_portfolio_scope="...",  # optional — The scope of the portfolio this holding came from
    source_portfolio_code="...",  # optional — The code of the portfolio this holding came from
    source_portfolio_entity_unique_id="...",  # optional — The unique identifier of the portfolio this holding came from
    source_portfolio_display_name="...",  # optional — The display name of the portfolio this holding came from
    holding_id="...",  # optional — The holding&#39;s identifier within its portfolio
    taxlot_id="...",  # optional — The tax lot identifier, where the holding was expanded to tax lots. Null otherwise.
    sub_entity_id="...",  # optional — Identifies the holding to the derived property explain API: the holding id on its own, or the holding id  and tax lot id colon-separated where a tax lot is present.
    lusid_instrument_id="...",  # optional — The LUSID instrument identifier of the instrument held
    instrument_display_name="...",  # optional — The name of the instrument held
    holding_type_name="...",  # optional — The kind of holding, e.g. Position, Balance
    currency="..."  # optional — The currency of the holding
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

