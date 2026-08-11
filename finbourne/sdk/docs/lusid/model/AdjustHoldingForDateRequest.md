# AdjustHoldingForDateRequest

This request specifies target holdings. i.e. holding data that the  system should match. When processed by the movement  engine, it will create 'true-up' adjustments on the fly.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **effective_at** | **str** | Required | The Effective date that the target holding will be adjusted at. |
| **instrument_identifiers** | **Dict[str, Optional[str]]** | Required | A set of instrument identifiers that can resolve the holding adjustment to a unique instrument. |
| **sub_holding_keys** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | Set of unique transaction properties and associated values to store with the holding adjustment transaction automatically created by LUSID. Each property must be from the &#39;Transaction&#39; domain. |
| **properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | Set of unique holding properties and associated values to store with the target holding. Each property must be from the &#39;Holding&#39; domain. |
| **tax_lots** | [List[TargetTaxLotRequest]](TargetTaxLotRequest.md) | Required | The tax-lots that together make up the target holding. |
| **currency** | **str** | Optional | The Holding currency. This needs to be equal with the one on the TaxLot -&gt; cost if one is specified |
| **custodian_account_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AdjustHoldingForDateRequest import AdjustHoldingForDateRequest

instance = AdjustHoldingForDateRequest(
    effective_at="...",  # required — The Effective date that the target holding will be adjusted at.
    instrument_identifiers=,  # required — A set of instrument identifiers that can resolve the holding adjustment to a unique instrument.
    sub_holding_keys=PerpetualProperty(...),  # optional — Set of unique transaction properties and associated values to store with the holding adjustment transaction automatically created by LUSID. Each property must be from the &#39;Transaction&#39; domain.
    properties=PerpetualProperty(...),  # optional — Set of unique holding properties and associated values to store with the target holding. Each property must be from the &#39;Holding&#39; domain.
    tax_lots=[],  # required — The tax-lots that together make up the target holding.
    currency="...",  # optional — The Holding currency. This needs to be equal with the one on the TaxLot -&gt; cost if one is specified
    custodian_account_id=ResourceId(...)  # optional
)
```

- [PerpetualProperty](PerpetualProperty.md) — used in `sub_holding_keys`
- [PerpetualProperty](PerpetualProperty.md) — used in `properties`
- [TargetTaxLotRequest](TargetTaxLotRequest.md) — used in `tax_lots`
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

