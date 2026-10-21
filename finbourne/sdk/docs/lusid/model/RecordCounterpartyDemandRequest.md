# RecordCounterpartyDemandRequest

The counterparty's figure for a margin call, to match against ours.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **amount** | **float** | Required | The counterparty&#39;s figure for the call, signed as the call. |
| **received_at** | **datetime** | Optional | When the demand was received. Defaults to the current LUSID system datetime if not specified. |
| **statement_reference** | **str** | Optional | A reference to the counterparty&#39;s statement, such as a Drive path. Optional. |
| **note** | **str** | Optional | A note to record with the demand. Optional. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecordCounterpartyDemandRequest import RecordCounterpartyDemandRequest

instance = RecordCounterpartyDemandRequest(
    amount=0.0,  # required — The counterparty&#39;s figure for the call, signed as the call.
    received_at=datetime.now(),  # optional — When the demand was received. Defaults to the current LUSID system datetime if not specified.
    statement_reference="...",  # optional — A reference to the counterparty&#39;s statement, such as a Drive path. Optional.
    note="..."  # optional — A note to record with the demand. Optional.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

