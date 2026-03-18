# PortfolioDetails

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **origin_portfolio_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **version** | [Version](Version.md) | Required | *No description available.* |
| **base_currency** | **str** | Required | The base currency of the transaction portfolio. |
| **corporate_action_source_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **sub_holding_keys** | **List[str]** | Optional | *No description available.* |
| **instrument_scopes** | **List[str]** | Optional | The resolution strategy used to resolve instruments of transactions/holdings upserted to the transaction portfolio. |
| **accounting_method** | **str** | Optional | . The available values are: Default, AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst, ProRateByUnits, ProRateByCost, ProRateByCostPortfolioCurrency, IntraDayThenFirstInFirstOut, LongTermHighestCostFirst, LongTermHighestCostFirstPortfolioCurrency, HighestCostFirstPortfolioCurrency, LowestCostFirstPortfolioCurrency, MaximumLossMinimumGain, MaximumLossMinimumGainPortfolioCurrency |
| **amortisation_method** | **str** | Optional | The amortisation method used by the portfolio for the calculation. The available values are: NoAmortisation, StraightLine, EffectiveYield, StraightLineSettlementDate, EffectiveYieldSettlementDate |
| **transaction_type_scope** | **str** | Optional | The scope of the transaction types. |
| **cash_gain_loss_calculation_date** | **str** | Optional | The option when the Cash Gain Loss to be calulated, TransactionDate/SettlementDate. Defaults to SettlementDate. |
| **instrument_event_configuration** | [InstrumentEventConfiguration](InstrumentEventConfiguration.md) | Optional | *No description available.* |
| **amortisation_rule_set_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **tax_rule_set_scope** | **str** | Optional | The scope of the tax rule sets for this portfolio. |
| **settlement_configuration** | [PortfolioSettlementConfiguration](PortfolioSettlementConfiguration.md) | Optional | *No description available.* |
| **staged_modifications** | [StagedModificationsInfo](StagedModificationsInfo.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PortfolioDetails import PortfolioDetails

instance = PortfolioDetails(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    origin_portfolio_id=ResourceId(...),  # required
    version=Version(...),  # required
    base_currency="...",  # required — The base currency of the transaction portfolio.
    corporate_action_source_id=ResourceId(...),  # optional
    sub_holding_keys=,  # optional
    instrument_scopes=,  # optional — The resolution strategy used to resolve instruments of transactions/holdings upserted to the transaction portfolio.
    accounting_method="...",  # optional — . The available values are: Default, AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst, ProRateByUnits, ProRateByCost, ProRateByCostPortfolioCurrency, IntraDayThenFirstInFirstOut, LongTermHighestCostFirst, LongTermHighestCostFirstPortfolioCurrency, HighestCostFirstPortfolioCurrency, LowestCostFirstPortfolioCurrency, MaximumLossMinimumGain, MaximumLossMinimumGainPortfolioCurrency
    amortisation_method="...",  # optional — The amortisation method used by the portfolio for the calculation. The available values are: NoAmortisation, StraightLine, EffectiveYield, StraightLineSettlementDate, EffectiveYieldSettlementDate
    transaction_type_scope="...",  # optional — The scope of the transaction types.
    cash_gain_loss_calculation_date="...",  # optional — The option when the Cash Gain Loss to be calulated, TransactionDate/SettlementDate. Defaults to SettlementDate.
    instrument_event_configuration=InstrumentEventConfiguration(...),  # optional
    amortisation_rule_set_id=ResourceId(...),  # optional
    tax_rule_set_scope="...",  # optional — The scope of the tax rule sets for this portfolio.
    settlement_configuration=PortfolioSettlementConfiguration(...),  # optional
    staged_modifications=StagedModificationsInfo(...),  # optional
    links=[]  # optional
)
```

- [ResourceId](ResourceId.md)
- [Version](Version.md)
- [ResourceId](ResourceId.md)
- [InstrumentEventConfiguration](InstrumentEventConfiguration.md)
- [ResourceId](ResourceId.md)
- [PortfolioSettlementConfiguration](PortfolioSettlementConfiguration.md)
- [StagedModificationsInfo](StagedModificationsInfo.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

