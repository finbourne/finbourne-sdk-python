# TransactionQueryParameters

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **start_date** | **str** | Required | The lower bound effective datetime or cut label (inclusive) from which to build the transactions. |
| **end_date** | **str** | Required | The upper bound effective datetime or cut label (inclusive) from which to retrieve transactions. |
| **query_mode** | **str** | Optional | The date to compare against the upper and lower bounds for the effective datetime or cut label. Default value: TradeDate. Available values: TradeDate, SettleDate. |
| **show_cancelled_transactions** | **bool** | Optional | Option to specify whether or not to include cancelled transactions in the output. Defaults to False if not specified. |
| **timeline_scope** | **str** | Optional | Scope of the Timeline for the Portfolio. The Timeline to be used while building transactions |
| **timeline_code** | **str** | Optional | Code of the Timeline for the Portfolio. The Timeline to be used while building transactions. This can optionally include a colon, followed by the Closed Period Id to use at the head of the timeline, for a timeline with unconfirmed periods. |
| **include_economics** | **bool** | Optional | By default is false. When set to true the Economics data would be populated in the response. |
| **include_settlement_status** | **bool** | Optional | By default is false. When set to true the Settlement Status data would be populated in the response. |
| **settlement_status_date** | **str** | Optional | Optional date used to specify end of an extended window for settlement information. When provided, transactions will be returned between start and end date, but settlement information between start date and this date will be included. When provided, the value must be greater than or equal to end date. |
| **return_excluded_transactions** | **bool** | Optional | Option to specify whether or not to include transactions that are marked as excluded by the portfolio&#39;s transaction exclusion filter. Excluded transactions do not affect holdings. Defaults to false if not specified. |
| **allocation_expansion** | **str** | Optional | How an input transaction that was split into allocation slices (strategy tag allocations or a prorated allocation method) is presented. &#39;Expanded&#39; (the default) returns one output transaction per slice. &#39;Combined&#39; returns one output transaction per input transaction with units, consideration and realised gain/loss summed over the slices, with every realised gain/loss record of each slice, including zero-realised ones, listed with its own transaction type and sub-holding key properties. For a prorated type with no units side the combined units are the total position the slices were prorated over, not the input&#39;s units. Transaction filters apply per slice, so a filter on a slice-level property combines only the matching slices. Sequence numbers are assigned after combining. Holdings and tax lots are identical in both modes. Available values: Expanded, Combined. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TransactionQueryParameters import TransactionQueryParameters

instance = TransactionQueryParameters(
    start_date="...",  # required — The lower bound effective datetime or cut label (inclusive) from which to build the transactions.
    end_date="...",  # required — The upper bound effective datetime or cut label (inclusive) from which to retrieve transactions.
    query_mode="...",  # optional — The date to compare against the upper and lower bounds for the effective datetime or cut label. Default value: TradeDate. Available values: TradeDate, SettleDate.
    show_cancelled_transactions=True,  # optional — Option to specify whether or not to include cancelled transactions in the output. Defaults to False if not specified.
    timeline_scope="...",  # optional — Scope of the Timeline for the Portfolio. The Timeline to be used while building transactions
    timeline_code="...",  # optional — Code of the Timeline for the Portfolio. The Timeline to be used while building transactions. This can optionally include a colon, followed by the Closed Period Id to use at the head of the timeline, for a timeline with unconfirmed periods.
    include_economics=True,  # optional — By default is false. When set to true the Economics data would be populated in the response.
    include_settlement_status=True,  # optional — By default is false. When set to true the Settlement Status data would be populated in the response.
    settlement_status_date="...",  # optional — Optional date used to specify end of an extended window for settlement information. When provided, transactions will be returned between start and end date, but settlement information between start date and this date will be included. When provided, the value must be greater than or equal to end date.
    return_excluded_transactions=True,  # optional — Option to specify whether or not to include transactions that are marked as excluded by the portfolio&#39;s transaction exclusion filter. Excluded transactions do not affect holdings. Defaults to false if not specified.
    allocation_expansion="..."  # optional — How an input transaction that was split into allocation slices (strategy tag allocations or a prorated allocation method) is presented. &#39;Expanded&#39; (the default) returns one output transaction per slice. &#39;Combined&#39; returns one output transaction per input transaction with units, consideration and realised gain/loss summed over the slices, with every realised gain/loss record of each slice, including zero-realised ones, listed with its own transaction type and sub-holding key properties. For a prorated type with no units side the combined units are the total position the slices were prorated over, not the input&#39;s units. Transaction filters apply per slice, so a filter on a slice-level property combines only the matching slices. Sequence numbers are assigned after combining. Holdings and tax lots are identical in both modes. Available values: Expanded, Combined.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

