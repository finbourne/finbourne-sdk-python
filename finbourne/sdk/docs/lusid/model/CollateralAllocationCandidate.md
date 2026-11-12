# CollateralAllocationCandidate

One holding the allocation considered for a margin call, with its figures as far as they could be computed and  either its rank or the constraint that excluded it.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instrument_id** | **str** | Required | The LUSID instrument identifier of the asset, or CCY_ and the currency code for cash. |
| **instrument_identifiers** | **Dict[str, Optional[str]]** | Required | The instrument identifiers a transaction for the line is booked against. |
| **portfolio_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **custodian_account** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **asset_kind** | **str** | Required | Cash or Security. |
| **currency** | **str** | Optional | The currency the asset is denominated in, when known. |
| **units_free** | **float** | Required | Units not in a margin account and not promised to an earlier call of the run. |
| **lot_size** | **float** | Required | The smallest number of units the asset is delivered in. |
| **price** | **float** | Optional | The market value per unit in the base currency, before any haircut. Null when the asset could not be priced. |
| **eligibility_seq** | **int** | Optional | The one-based position of the schedule row that admits the asset. Null when no row does. |
| **valuation_percentage** | **float** | Optional | The fraction of market value the schedule row counts as collateral. |
| **fx_haircut** | **float** | Optional | The further fraction deducted because the asset is not in the base currency. Zero when it is. |
| **effective_value_per_unit** | **float** | Optional | Price times the valuation percentage, less the FX haircut: what one unit counts for as collateral. |
| **opportunity_rate** | **float** | Optional | The annual rate the fund gives up by locking the asset up: funding less the agreement&#39;s cash interest for cash, the lending fee it would otherwise earn for a security. |
| **cost_per_unit_of_value** | **float** | Optional | The ranking key: the annual cost of one unit of collateral value from this asset. |
| **concentration_cap** | **float** | Optional | The collateral value the schedule&#39;s concentration limit still allows from the asset&#39;s group. Null when the row sets no limit. |
| **settlement_date** | **datetime** | Optional | When the movement would settle under the agreement&#39;s settlement lag, counting weekdays. |
| **rank** | **int** | Optional | The asset&#39;s position in the ranking, cheapest first. Null when excluded. |
| **exclusion_reason** | **str** | Optional | The constraint the asset failed, when it did. One of NotEligible, NoFreeUnits, MissingPrice, MissingRate, MissesDeadline, BelowMinimumLot or ConcentrationExhausted. Null when it passed. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CollateralAllocationCandidate import CollateralAllocationCandidate

instance = CollateralAllocationCandidate(
    instrument_id="...",  # required — The LUSID instrument identifier of the asset, or CCY_ and the currency code for cash.
    instrument_identifiers=,  # required — The instrument identifiers a transaction for the line is booked against.
    portfolio_id=ResourceId(...),  # required
    custodian_account=ResourceId(...),  # optional
    asset_kind="...",  # required — Cash or Security.
    currency="...",  # optional — The currency the asset is denominated in, when known.
    units_free=0.0,  # required — Units not in a margin account and not promised to an earlier call of the run.
    lot_size=0.0,  # required — The smallest number of units the asset is delivered in.
    price=0.0,  # optional — The market value per unit in the base currency, before any haircut. Null when the asset could not be priced.
    eligibility_seq=0,  # optional — The one-based position of the schedule row that admits the asset. Null when no row does.
    valuation_percentage=0.0,  # optional — The fraction of market value the schedule row counts as collateral.
    fx_haircut=0.0,  # optional — The further fraction deducted because the asset is not in the base currency. Zero when it is.
    effective_value_per_unit=0.0,  # optional — Price times the valuation percentage, less the FX haircut: what one unit counts for as collateral.
    opportunity_rate=0.0,  # optional — The annual rate the fund gives up by locking the asset up: funding less the agreement&#39;s cash interest for cash, the lending fee it would otherwise earn for a security.
    cost_per_unit_of_value=0.0,  # optional — The ranking key: the annual cost of one unit of collateral value from this asset.
    concentration_cap=0.0,  # optional — The collateral value the schedule&#39;s concentration limit still allows from the asset&#39;s group. Null when the row sets no limit.
    settlement_date=datetime.now(),  # optional — When the movement would settle under the agreement&#39;s settlement lag, counting weekdays.
    rank=0,  # optional — The asset&#39;s position in the ranking, cheapest first. Null when excluded.
    exclusion_reason="..."  # optional — The constraint the asset failed, when it did. One of NotEligible, NoFreeUnits, MissingPrice, MissingRate, MissesDeadline, BelowMinimumLot or ConcentrationExhausted. Null when it passed.
)
```

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

