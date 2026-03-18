# HoldingAdjustmentWithDate

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **effective_at** | **datetime** | Optional | The effective date of the holding adjustment |
| **instrument_identifiers** | **Dict[str, Optional[str]]** | Optional | A set of instrument identifiers that can resolve the holding adjustment to a unique instrument. |
| **instrument_scope** | **str** | Optional | The scope of the instrument that the holding adjustment is in. |
| **instrument_uid** | **str** | Required | The unique Lusid Instrument Id (LUID) of the instrument that the holding adjustment is in. |
| **sub_holding_keys** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | The set of unique transaction properties and associated values stored with the holding adjustment transactions automatically created by LUSID. Each property will be from the &#39;Transaction&#39; domain. |
| **properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | The set of unique holding properties and associated values stored with the target holding. Each property will be from the &#39;Holding&#39; domain. |
| **tax_lots** | [List[TargetTaxLot]](TargetTaxLot.md) | Required | The tax-lots that together make up the target holding. |
| **currency** | **str** | Optional | The Holding currency. |
| **custodian_account_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.HoldingAdjustmentWithDate import HoldingAdjustmentWithDate

instance = HoldingAdjustmentWithDate(
    effective_at=datetime.now(),  # optional — The effective date of the holding adjustment
    instrument_identifiers=,  # optional — A set of instrument identifiers that can resolve the holding adjustment to a unique instrument.
    instrument_scope="...",  # optional — The scope of the instrument that the holding adjustment is in.
    instrument_uid="...",  # required — The unique Lusid Instrument Id (LUID) of the instrument that the holding adjustment is in.
    sub_holding_keys=PerpetualProperty(...),  # optional — The set of unique transaction properties and associated values stored with the holding adjustment transactions automatically created by LUSID. Each property will be from the &#39;Transaction&#39; domain.
    properties=PerpetualProperty(...),  # optional — The set of unique holding properties and associated values stored with the target holding. Each property will be from the &#39;Holding&#39; domain.
    tax_lots=[],  # required — The tax-lots that together make up the target holding.
    currency="...",  # optional — The Holding currency.
    custodian_account_id=ResourceId(...)  # optional
)
```

- [PerpetualProperty](PerpetualProperty.md) — used in `sub_holding_keys`
- [PerpetualProperty](PerpetualProperty.md) — used in `properties`
- [TargetTaxLot](TargetTaxLot.md) — used in `tax_lots`
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

