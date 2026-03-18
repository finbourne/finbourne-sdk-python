# TransactionQueryParameters

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **start_date** | **str** | Required | The lower bound effective datetime or cut label (inclusive) from which to build the transactions. |
| **end_date** | **str** | Required | The upper bound effective datetime or cut label (inclusive) from which to retrieve transactions. |
| **query_mode** | **str** | Optional | The date to compare against the upper and lower bounds for the effective datetime or cut label. Defaults to &#39;TradeDate&#39; if not specified. The available values are: TradeDate, SettleDate |
| **show_cancelled_transactions** | **bool** | Optional | Option to specify whether or not to include cancelled transactions in the output. Defaults to False if not specified. |
| **timeline_scope** | **str** | Optional | Scope of the Timeline for the Portfolio. The Timeline to be used while building transactions |
| **timeline_code** | **str** | Optional | Code of the Timeline for the Portfolio. The Timeline to be used while building transactions. This can optionally include a colon, followed by the Closed Period Id to use at the head of the timeline, for a timeline with unconfirmed periods. |
| **include_economics** | **bool** | Optional | By default is false. When set to true the Economics data would be populated in the response. |
| **include_settlement_status** | **bool** | Optional | By default is false. When set to true the Settlement Status data would be populated in the response. |
| **settlement_status_date** | **str** | Optional | Optional date used to specify end of an extended window for settlement information. When provided, transactions will be returned between start and end date, but settlement information between start date and this date will be included. When provided, the value must be greater than or equal to end date. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TransactionQueryParameters import TransactionQueryParameters

instance = TransactionQueryParameters(
    start_date="...",  # required — The lower bound effective datetime or cut label (inclusive) from which to build the transactions.
    end_date="...",  # required — The upper bound effective datetime or cut label (inclusive) from which to retrieve transactions.
    query_mode="...",  # optional — The date to compare against the upper and lower bounds for the effective datetime or cut label. Defaults to &#39;TradeDate&#39; if not specified. The available values are: TradeDate, SettleDate
    show_cancelled_transactions=True,  # optional — Option to specify whether or not to include cancelled transactions in the output. Defaults to False if not specified.
    timeline_scope="...",  # optional — Scope of the Timeline for the Portfolio. The Timeline to be used while building transactions
    timeline_code="...",  # optional — Code of the Timeline for the Portfolio. The Timeline to be used while building transactions. This can optionally include a colon, followed by the Closed Period Id to use at the head of the timeline, for a timeline with unconfirmed periods.
    include_economics=True,  # optional — By default is false. When set to true the Economics data would be populated in the response.
    include_settlement_status=True,  # optional — By default is false. When set to true the Settlement Status data would be populated in the response.
    settlement_status_date="..."  # optional — Optional date used to specify end of an extended window for settlement information. When provided, transactions will be returned between start and end date, but settlement information between start date and this date will be included. When provided, the value must be greater than or equal to end date.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

