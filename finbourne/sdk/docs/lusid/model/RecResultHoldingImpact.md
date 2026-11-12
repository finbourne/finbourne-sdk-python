# RecResultHoldingImpact

One holding, and where known the tax lot within it, that a transaction or settlement activity item impacted.  Also holds the display names of the holding's instrument.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **holding_id** | **str** | Required | The impacted holding, at holding level: the id a holding item over it carries. |
| **tax_lot_id** | **str** | Optional | The impacted tax lot within the holding, where the source states one; null when the impact is known at holding level only. Opaque: compare it whole, do not parse it. |
| **holding_instrument_scope** | **str** | Optional | The scope of the impacted holding&#39;s instrument. Null where the source does not state one. |
| **holding_lusid_instrument_id** | **str** | Optional | The LUID of the impacted holding&#39;s instrument. Null where the source does not state it. |
| **holding_instrument_name** | **str** | Optional | The name of the impacted holding&#39;s instrument, as it stood at the asAt the run read its data. Null where the run did not resolve it. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecResultHoldingImpact import RecResultHoldingImpact

instance = RecResultHoldingImpact(
    holding_id="...",  # required — The impacted holding, at holding level: the id a holding item over it carries.
    tax_lot_id="...",  # optional — The impacted tax lot within the holding, where the source states one; null when the impact is known at holding level only. Opaque: compare it whole, do not parse it.
    holding_instrument_scope="...",  # optional — The scope of the impacted holding&#39;s instrument. Null where the source does not state one.
    holding_lusid_instrument_id="...",  # optional — The LUID of the impacted holding&#39;s instrument. Null where the source does not state it.
    holding_instrument_name="..."  # optional — The name of the impacted holding&#39;s instrument, as it stood at the asAt the run read its data. Null where the run did not resolve it.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

