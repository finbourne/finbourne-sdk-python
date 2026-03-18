# CashFlowLineage

Lineage for cash flow value
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instrument_type** | **str** | Optional | The instrument type of the instrument to which the cash flow belongs to. When upserting CashFlowValues, this  should be null. |
| **cash_flow_type** | **str** | Optional | The cashflow type.When upserting CashFlowValues, this should be null, or one of [Unknown, Coupon, Notional,  Premium, Principal, Protection, Cash] |
| **instrument_id** | **str** | Optional | The LUID of the instrument to which the cash flow belongs to. When upserting this should be null. |
| **leg_id** | **str** | Optional | The leg id to which the cash flow belongs to. |
| **source_transaction_id** | **str** | Optional | The source transaction of the instrument to which the cash flow belongs to. When upserting this should be null |
| **pay_receive** | **str** | Optional | Does the cash flow belong to the Pay or Receive leg. When upserting this should either be null or one of [Pay, Receive, NotApplicable] |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CashFlowLineage import CashFlowLineage

instance = CashFlowLineage(
    instrument_type="...",  # optional — The instrument type of the instrument to which the cash flow belongs to. When upserting CashFlowValues, this  should be null.
    cash_flow_type="...",  # optional — The cashflow type.When upserting CashFlowValues, this should be null, or one of [Unknown, Coupon, Notional,  Premium, Principal, Protection, Cash]
    instrument_id="...",  # optional — The LUID of the instrument to which the cash flow belongs to. When upserting this should be null.
    leg_id="...",  # optional — The leg id to which the cash flow belongs to.
    source_transaction_id="...",  # optional — The source transaction of the instrument to which the cash flow belongs to. When upserting this should be null
    pay_receive="..."  # optional — Does the cash flow belong to the Pay or Receive leg. When upserting this should either be null or one of [Pay, Receive, NotApplicable]
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

