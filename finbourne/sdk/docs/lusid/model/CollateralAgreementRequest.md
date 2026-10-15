# CollateralAgreementRequest

The request used to create a Collateral Agreement.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Required | The code of the Collateral Agreement. |
| **counterparty_id** | [CounterpartyIdentifier](CounterpartyIdentifier.md) | Required | *No description available.* |
| **applicability_filter** | **str** | Required | A filter selecting the portfolios and trades the agreement covers. Checked for structure only when the agreement is stored. |
| **base_currency** | **str** | Required | The currency margin is calculated and called in. Filterable. |
| **cut_label** | **str** | Required | The cut label naming the market data that margin is valued at. |
| **recipe_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **minimum_transfer_amount** | **float** | Optional | The smallest margin movement that is called. Optional. |
| **rounding** | [MarginRounding](MarginRounding.md) | Required | *No description available.* |
| **settlement_lag** | [MarginSettlementLag](MarginSettlementLag.md) | Required | *No description available.* |
| **match_tolerance** | **float** | Optional | The tolerance within which our margin figure and the counterparty&#39;s are considered to match. Optional. |
| **variation_margin** | [List[MarginItem]](MarginItem.md) | Optional | The variation margin arrangements under the agreement. |
| **initial_margin** | [List[MarginItem]](MarginItem.md) | Optional | The initial margin arrangements under the agreement. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of properties to decorate onto the Collateral Agreement. Filterable. |
| **effective_at** | **datetime** | Optional | The effective datetime from which the Collateral Agreement applies. Defaults to the beginning of time if not specified, so that the agreement is visible at every effective datetime. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CollateralAgreementRequest import CollateralAgreementRequest

instance = CollateralAgreementRequest(
    code="...",  # required — The code of the Collateral Agreement.
    counterparty_id=CounterpartyIdentifier(...),  # required
    applicability_filter="...",  # required — A filter selecting the portfolios and trades the agreement covers. Checked for structure only when the agreement is stored.
    base_currency="...",  # required — The currency margin is calculated and called in. Filterable.
    cut_label="...",  # required — The cut label naming the market data that margin is valued at.
    recipe_id=ResourceId(...),  # required
    minimum_transfer_amount=0.0,  # optional — The smallest margin movement that is called. Optional.
    rounding=MarginRounding(...),  # required
    settlement_lag=MarginSettlementLag(...),  # required
    match_tolerance=0.0,  # optional — The tolerance within which our margin figure and the counterparty&#39;s are considered to match. Optional.
    variation_margin=[],  # optional — The variation margin arrangements under the agreement.
    initial_margin=[],  # optional — The initial margin arrangements under the agreement.
    properties=ModelProperty(...),  # optional — A set of properties to decorate onto the Collateral Agreement. Filterable.
    effective_at=datetime.now()  # optional — The effective datetime from which the Collateral Agreement applies. Defaults to the beginning of time if not specified, so that the agreement is visible at every effective datetime.
)
```

- [CounterpartyIdentifier](CounterpartyIdentifier.md)
- [ResourceId](ResourceId.md)
- [MarginRounding](MarginRounding.md)
- [MarginSettlementLag](MarginSettlementLag.md)
- [MarginItem](MarginItem.md) — used in `variation_margin`
- [MarginItem](MarginItem.md) — used in `initial_margin`
- [ModelProperty](ModelProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

