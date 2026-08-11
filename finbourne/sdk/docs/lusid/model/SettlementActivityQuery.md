# SettlementActivityQuery

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **as_at** | **datetime** | Optional | The asAt time at which to query settlement activity. Defaults to latest. |
| **portfolio_entity_ids** | [List[PortfolioEntityId]](PortfolioEntityId.md) | Optional | The portfolios and / or portfolio groups to query. At least one entry is required. |
| **start_activity_date** | **str** | Optional | Lower bound (inclusive) of the activity date range. If not set, no lower bound is applied. |
| **end_activity_date** | **str** | Optional | Upper bound (inclusive) of the activity date range. Defaults to the current date and time. Treated as effectiveAt. |
| **filter** | **str** | Optional | A LUSID standard filter expression. Supports traversal into transaction and settlementInstruction. |
| **settlement_instruction_property_keys** | **List[str]** | Optional | Settlement instruction property keys to populate on the response. Behaviour matches BuildSettlementInstructions. |
| **transaction_property_keys** | **List[str]** | Optional | Transaction property keys to populate on the response. Behaviour matches BuildSettlementInstructions. |
| **limit** | **int** | Optional | Page size limit; standard pagination control. Defaults to 5000. |
| **page** | **str** | Optional | Pagination cursor returned by a previous response. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SettlementActivityQuery import SettlementActivityQuery

instance = SettlementActivityQuery(
    as_at=datetime.now(),  # optional — The asAt time at which to query settlement activity. Defaults to latest.
    portfolio_entity_ids=[],  # optional — The portfolios and / or portfolio groups to query. At least one entry is required.
    start_activity_date="...",  # optional — Lower bound (inclusive) of the activity date range. If not set, no lower bound is applied.
    end_activity_date="...",  # optional — Upper bound (inclusive) of the activity date range. Defaults to the current date and time. Treated as effectiveAt.
    filter="...",  # optional — A LUSID standard filter expression. Supports traversal into transaction and settlementInstruction.
    settlement_instruction_property_keys=,  # optional — Settlement instruction property keys to populate on the response. Behaviour matches BuildSettlementInstructions.
    transaction_property_keys=,  # optional — Transaction property keys to populate on the response. Behaviour matches BuildSettlementInstructions.
    limit=0,  # optional — Page size limit; standard pagination control. Defaults to 5000.
    page="..."  # optional — Pagination cursor returned by a previous response.
)
```

- [PortfolioEntityId](PortfolioEntityId.md) — used in `portfolio_entity_ids`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

