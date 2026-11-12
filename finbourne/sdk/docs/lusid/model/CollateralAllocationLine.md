# CollateralAllocationLine

One asset chosen for a margin call, with what a transaction moving it needs: the instrument, the portfolio and  account it leaves, the units, the price and the consideration. An override that fails a constraint is kept with  its exclusion reason and covers nothing.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instrument_id** | **str** | Required | The LUSID instrument identifier of the asset, or CCY_ and the currency code for cash. |
| **instrument_identifiers** | **Dict[str, Optional[str]]** | Required | The instrument identifiers a transaction for the line is booked against. |
| **portfolio_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **custodian_account** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **currency** | **str** | Optional | The currency the asset is denominated in, when known. |
| **units** | **float** | Required | The units to move. |
| **price** | **float** | Optional | The market value per unit in the base currency, before any haircut. Null when the asset could not be priced. |
| **consideration** | **float** | Optional | Units times price in the base currency: what a transaction for the line settles. Null when the asset could not be priced. |
| **effective_value_per_unit** | **float** | Optional | Price times the valuation percentage, less the FX haircut: what one unit counts for as collateral. |
| **collateral_value** | **float** | Required | The collateral value the line covers: units times the effective value per unit. |
| **cost_per_unit_of_value** | **float** | Optional | The ranking key: the annual cost of one unit of collateral value from this asset. |
| **settlement_date** | **datetime** | Optional | When the movement would settle under the agreement&#39;s settlement lag, counting weekdays. |
| **bound_by** | **str** | Required | Which limit decided the units. One of RemainingRequirement, FreeUnits, ConcentrationCap, LotRounding or Override. |
| **exclusion_reason** | **str** | Optional | The constraint the asset failed, when it did. One of NotEligible, NoFreeUnits, MissingPrice, MissingRate, MissesDeadline, BelowMinimumLot or ConcentrationExhausted. Null when it passed. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CollateralAllocationLine import CollateralAllocationLine

instance = CollateralAllocationLine(
    instrument_id="...",  # required — The LUSID instrument identifier of the asset, or CCY_ and the currency code for cash.
    instrument_identifiers=,  # required — The instrument identifiers a transaction for the line is booked against.
    portfolio_id=ResourceId(...),  # required
    custodian_account=ResourceId(...),  # optional
    currency="...",  # optional — The currency the asset is denominated in, when known.
    units=0.0,  # required — The units to move.
    price=0.0,  # optional — The market value per unit in the base currency, before any haircut. Null when the asset could not be priced.
    consideration=0.0,  # optional — Units times price in the base currency: what a transaction for the line settles. Null when the asset could not be priced.
    effective_value_per_unit=0.0,  # optional — Price times the valuation percentage, less the FX haircut: what one unit counts for as collateral.
    collateral_value=0.0,  # required — The collateral value the line covers: units times the effective value per unit.
    cost_per_unit_of_value=0.0,  # optional — The ranking key: the annual cost of one unit of collateral value from this asset.
    settlement_date=datetime.now(),  # optional — When the movement would settle under the agreement&#39;s settlement lag, counting weekdays.
    bound_by="...",  # required — Which limit decided the units. One of RemainingRequirement, FreeUnits, ConcentrationCap, LotRounding or Override.
    exclusion_reason="..."  # optional — The constraint the asset failed, when it did. One of NotEligible, NoFreeUnits, MissingPrice, MissingRate, MissesDeadline, BelowMinimumLot or ConcentrationExhausted. Null when it passed.
)
```

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

