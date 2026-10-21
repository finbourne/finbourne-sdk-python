# AcceptMarginCallRequest

Accepts a margin call, at its default agreed amount or the amount given.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **agreed_amount** | **float** | Optional | The amount to accept. Optional when the call is matched or within tolerance, when our call or the counterparty&#39;s demand is taken; required when the demand breaks tolerance or has not been recorded. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AcceptMarginCallRequest import AcceptMarginCallRequest

instance = AcceptMarginCallRequest(
    agreed_amount=0.0  # optional — The amount to accept. Optional when the call is matched or within tolerance, when our call or the counterparty&#39;s demand is taken; required when the demand breaks tolerance or has not been recorded.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

