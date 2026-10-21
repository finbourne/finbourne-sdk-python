# MarginCallKey

The parts that identify a margin call: its run and the call's business key.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **run_id** | **str** | Required | The run the call belongs to. |
| **agreement_scope** | **str** | Required | The scope of the call&#39;s collateral agreement. |
| **agreement_code** | **str** | Required | The code of the call&#39;s collateral agreement. |
| **item** | **str** | Required | The margin item of the call. |
| **margin_type** | **str** | Required | The margin type of the call. Currently VariationMargin. |
| **direction** | **str** | Required | Who posts under the call: WePost, TheyPost or None. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.MarginCallKey import MarginCallKey

instance = MarginCallKey(
    run_id="...",  # required — The run the call belongs to.
    agreement_scope="...",  # required — The scope of the call&#39;s collateral agreement.
    agreement_code="...",  # required — The code of the call&#39;s collateral agreement.
    item="...",  # required — The margin item of the call.
    margin_type="...",  # required — The margin type of the call. Currently VariationMargin.
    direction="..."  # required — Who posts under the call: WePost, TheyPost or None.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

