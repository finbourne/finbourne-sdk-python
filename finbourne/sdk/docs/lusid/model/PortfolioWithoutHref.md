# PortfolioWithoutHref

A list of portfolios.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **type** | **str** | Required | The type of the portfolio. The available values are: Transaction, Reference, DerivedTransaction, SimplePosition |
| **display_name** | **str** | Required | The name of the portfolio. |
| **description** | **str** | Optional | The long form description of the portfolio. |
| **created** | **datetime** | Required | The effective datetime at which the portfolio was created. No transactions or constituents can be added to the portfolio before this date. |
| **parent_portfolio_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **staged_modifications** | [StagedModificationsInfo](StagedModificationsInfo.md) | Optional | *No description available.* |
| **is_derived** | **bool** | Optional | Whether or not this is a derived portfolio. |
| **base_currency** | **str** | Optional | The base currency of the portfolio. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | The requested portfolio properties. These will be from the &#39;Portfolio&#39; domain. |
| **relationships** | [List[Relationship]](Relationship.md) | Optional | A set of relationships associated to the portfolio. |
| **instrument_scopes** | **List[str]** | Optional | The instrument scope resolution strategy of this portfolio. |
| **accounting_method** | **str** | Optional | . The available values are: Default, AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst, ProRateByUnits, ProRateByCost, ProRateByCostPortfolioCurrency, IntraDayThenFirstInFirstOut, LongTermHighestCostFirst, LongTermHighestCostFirstPortfolioCurrency, HighestCostFirstPortfolioCurrency, LowestCostFirstPortfolioCurrency, MaximumLossMinimumGain, MaximumLossMinimumGainPortfolioCurrency |
| **amortisation_method** | **str** | Optional | The amortisation method used by the portfolio for the calculation. The available values are: NoAmortisation, StraightLine, EffectiveYield, StraightLineSettlementDate, EffectiveYieldSettlementDate |
| **transaction_type_scope** | **str** | Optional | The scope of the transaction types. |
| **cash_gain_loss_calculation_date** | **str** | Optional | The scope of the transaction types. |
| **instrument_event_configuration** | [InstrumentEventConfiguration](InstrumentEventConfiguration.md) | Optional | *No description available.* |
| **amortisation_rule_set_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **tax_rule_set_scope** | **str** | Optional | The scope of the tax rule sets for this portfolio. |
| **settlement_configuration** | [PortfolioSettlementConfiguration](PortfolioSettlementConfiguration.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PortfolioWithoutHref import PortfolioWithoutHref

instance = PortfolioWithoutHref(
    id=ResourceId(...),  # required
    type="...",  # required — The type of the portfolio. The available values are: Transaction, Reference, DerivedTransaction, SimplePosition
    display_name="...",  # required — The name of the portfolio.
    description="...",  # optional — The long form description of the portfolio.
    created=datetime.now(),  # required — The effective datetime at which the portfolio was created. No transactions or constituents can be added to the portfolio before this date.
    parent_portfolio_id=ResourceId(...),  # optional
    version=Version(...),  # optional
    staged_modifications=StagedModificationsInfo(...),  # optional
    is_derived=True,  # optional — Whether or not this is a derived portfolio.
    base_currency="...",  # optional — The base currency of the portfolio.
    properties=ModelProperty(...),  # optional — The requested portfolio properties. These will be from the &#39;Portfolio&#39; domain.
    relationships=[],  # optional — A set of relationships associated to the portfolio.
    instrument_scopes=,  # optional — The instrument scope resolution strategy of this portfolio.
    accounting_method="...",  # optional — . The available values are: Default, AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst, ProRateByUnits, ProRateByCost, ProRateByCostPortfolioCurrency, IntraDayThenFirstInFirstOut, LongTermHighestCostFirst, LongTermHighestCostFirstPortfolioCurrency, HighestCostFirstPortfolioCurrency, LowestCostFirstPortfolioCurrency, MaximumLossMinimumGain, MaximumLossMinimumGainPortfolioCurrency
    amortisation_method="...",  # optional — The amortisation method used by the portfolio for the calculation. The available values are: NoAmortisation, StraightLine, EffectiveYield, StraightLineSettlementDate, EffectiveYieldSettlementDate
    transaction_type_scope="...",  # optional — The scope of the transaction types.
    cash_gain_loss_calculation_date="...",  # optional — The scope of the transaction types.
    instrument_event_configuration=InstrumentEventConfiguration(...),  # optional
    amortisation_rule_set_id=ResourceId(...),  # optional
    tax_rule_set_scope="...",  # optional — The scope of the tax rule sets for this portfolio.
    settlement_configuration=PortfolioSettlementConfiguration(...),  # optional
    links=[]  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [Version](Version.md)
- [StagedModificationsInfo](StagedModificationsInfo.md)
- [ModelProperty](ModelProperty.md) — used in `properties`
- [Relationship](Relationship.md) — used in `relationships`
- [InstrumentEventConfiguration](InstrumentEventConfiguration.md)
- [ResourceId](ResourceId.md)
- [PortfolioSettlementConfiguration](PortfolioSettlementConfiguration.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

