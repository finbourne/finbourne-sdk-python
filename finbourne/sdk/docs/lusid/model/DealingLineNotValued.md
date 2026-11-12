# DealingLineNotValued

A dealing line read for a swing decision that could not be valued into its share class currency, and why.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **order_id** | **str** | Required | The identifier of the dealing order that could not be valued, as scope/code. |
| **share_class** | **str** | Optional | The share class the order deals in, keyed as the valuation point&#39;s share classes are. |
| **currency** | **str** | Optional | The currency the order&#39;s amount is in. Absent when the line carries no amount. |
| **reason** | **str** | Required | Why the line could not be valued into the share class currency. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.DealingLineNotValued import DealingLineNotValued

instance = DealingLineNotValued(
    order_id="...",  # required — The identifier of the dealing order that could not be valued, as scope/code.
    share_class="...",  # optional — The share class the order deals in, keyed as the valuation point&#39;s share classes are.
    currency="...",  # optional — The currency the order&#39;s amount is in. Absent when the line carries no amount.
    reason="..."  # required — Why the line could not be valued into the share class currency.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

