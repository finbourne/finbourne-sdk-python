# DisputeMarginCallRequest

Disputes a margin call: moves the agreed amount now and leaves the rest of the demand in dispute.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **agreed_amount** | **float** | Required | The amount to move now; the rest of the counterparty&#39;s demand is left in dispute. |
| **reason** | **str** | Required | Why the call is disputed. |
| **owner** | **str** | Optional | Who owns the dispute. Defaults to the caller if not specified. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.DisputeMarginCallRequest import DisputeMarginCallRequest

instance = DisputeMarginCallRequest(
    agreed_amount=0.0,  # required — The amount to move now; the rest of the counterparty&#39;s demand is left in dispute.
    reason="...",  # required — Why the call is disputed.
    owner="..."  # optional — Who owns the dispute. Defaults to the caller if not specified.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

