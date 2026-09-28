# RecResultHoldingImpact

One holding, and where known the tax lot within it, that a transaction or settlement activity item impacted.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **holding_id** | **str** | Required | The impacted holding, at holding level: the id a holding item over it carries. |
| **tax_lot_id** | **str** | Optional | The impacted tax lot within the holding, where the source states one; null when the impact is known at holding level only. Opaque: compare it whole, do not parse it. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecResultHoldingImpact import RecResultHoldingImpact

instance = RecResultHoldingImpact(
    holding_id="...",  # required — The impacted holding, at holding level: the id a holding item over it carries.
    tax_lot_id="..."  # optional — The impacted tax lot within the holding, where the source states one; null when the impact is known at holding level only. Opaque: compare it whole, do not parse it.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

