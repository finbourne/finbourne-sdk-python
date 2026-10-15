# CollateralAgreement

A collateral agreement: who it covers, how exposure is valued, and the variation and initial margin  arrangements collateral is called and returned under.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **counterparty_id** | [CounterpartyIdentifier](CounterpartyIdentifier.md) | Optional | *No description available.* |
| **applicability_filter** | **str** | Optional | A filter selecting the portfolios and trades the agreement covers. Checked for structure only when the agreement is stored. |
| **base_currency** | **str** | Optional | The currency margin is calculated and called in. Filterable. |
| **cut_label** | **str** | Optional | The cut label naming the market data that margin is valued at. |
| **recipe_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **minimum_transfer_amount** | **float** | Optional | The smallest margin movement that is called. Optional. |
| **rounding** | [MarginRounding](MarginRounding.md) | Optional | *No description available.* |
| **settlement_lag** | [MarginSettlementLag](MarginSettlementLag.md) | Optional | *No description available.* |
| **match_tolerance** | **float** | Optional | The tolerance within which our margin figure and the counterparty&#39;s are considered to match. Optional. |
| **variation_margin** | [List[MarginItem]](MarginItem.md) | Optional | The variation margin arrangements under the agreement. |
| **initial_margin** | [List[MarginItem]](MarginItem.md) | Optional | The initial margin arrangements under the agreement. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of properties to decorate onto the Collateral Agreement. Filterable. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CollateralAgreement import CollateralAgreement

instance = CollateralAgreement(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    id=ResourceId(...),  # required
    counterparty_id=CounterpartyIdentifier(...),  # optional
    applicability_filter="...",  # optional — A filter selecting the portfolios and trades the agreement covers. Checked for structure only when the agreement is stored.
    base_currency="...",  # optional — The currency margin is calculated and called in. Filterable.
    cut_label="...",  # optional — The cut label naming the market data that margin is valued at.
    recipe_id=ResourceId(...),  # optional
    minimum_transfer_amount=0.0,  # optional — The smallest margin movement that is called. Optional.
    rounding=MarginRounding(...),  # optional
    settlement_lag=MarginSettlementLag(...),  # optional
    match_tolerance=0.0,  # optional — The tolerance within which our margin figure and the counterparty&#39;s are considered to match. Optional.
    variation_margin=[],  # optional — The variation margin arrangements under the agreement.
    initial_margin=[],  # optional — The initial margin arrangements under the agreement.
    version=Version(...),  # optional
    properties=ModelProperty(...),  # optional — A set of properties to decorate onto the Collateral Agreement. Filterable.
    links=[]  # optional
)
```

- [ResourceId](ResourceId.md)
- [CounterpartyIdentifier](CounterpartyIdentifier.md)
- [ResourceId](ResourceId.md)
- [MarginRounding](MarginRounding.md)
- [MarginSettlementLag](MarginSettlementLag.md)
- [MarginItem](MarginItem.md) — used in `variation_margin`
- [MarginItem](MarginItem.md) — used in `initial_margin`
- [Version](Version.md)
- [ModelProperty](ModelProperty.md) — used in `properties`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

