# RecRequiredApproval

An approval slot required for a result set, passed through from the rec definition's review configuration.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **approval_code** | **str** | Required | Client-defined identifier for the approval slot (e.g. &#39;Desk&#39;, &#39;Risk&#39;). |
| **description** | **str** | Optional | Human-readable label for the approval slot. |
| **current_user_can_decide** | **bool** | Optional | Whether the calling user may decide this approval slot, pre-evaluated at request time. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecRequiredApproval import RecRequiredApproval

instance = RecRequiredApproval(
    approval_code="...",  # required — Client-defined identifier for the approval slot (e.g. &#39;Desk&#39;, &#39;Risk&#39;).
    description="...",  # optional — Human-readable label for the approval slot.
    current_user_can_decide=True  # optional — Whether the calling user may decide this approval slot, pre-evaluated at request time.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

