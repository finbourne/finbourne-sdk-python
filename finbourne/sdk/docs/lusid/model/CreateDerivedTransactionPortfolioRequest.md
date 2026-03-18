# CreateDerivedTransactionPortfolioRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **display_name** | **str** | Required | The name of the derived transaction portfolio. |
| **description** | **str** | Optional | A description for the derived transaction portfolio. |
| **code** | **str** | Required | The code of the derived transaction portfolio. Together with the scope this uniquely identifies the derived transaction portfolio. |
| **parent_portfolio_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **created** | **datetime** | Optional | This will be auto-populated to be the parent portfolio creation date. |
| **corporate_action_source_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **accounting_method** | **str** | Optional | . The available values are: Default, AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst, ProRateByUnits, ProRateByCost, ProRateByCostPortfolioCurrency, IntraDayThenFirstInFirstOut, LongTermHighestCostFirst, LongTermHighestCostFirstPortfolioCurrency, HighestCostFirstPortfolioCurrency, LowestCostFirstPortfolioCurrency, MaximumLossMinimumGain, MaximumLossMinimumGainPortfolioCurrency |
| **sub_holding_keys** | **List[str]** | Optional | A set of unique transaction properties to group the derived transaction portfolio&#39;s holdings by, perhaps for strategy tagging. Each property must be from the &#39;Transaction&#39; domain and identified by a key in the format {domain}/{scope}/{code}, for example &#39;Transaction/strategies/quantsignal&#39;. See https://support.lusid.com/knowledgebase/article/KA-01879/en-us for more information. |
| **instrument_scopes** | **List[str]** | Optional | The resolution strategy used to resolve instruments of transactions/holdings upserted to this derived portfolio. |
| **amortisation_method** | **str** | Optional | The amortisation method used by the portfolio for the calculation. The available values are: NoAmortisation, StraightLine, EffectiveYield, StraightLineSettlementDate, EffectiveYieldSettlementDate |
| **transaction_type_scope** | **str** | Optional | The scope of the transaction types. |
| **cash_gain_loss_calculation_date** | **str** | Optional | The option when the Cash Gain Loss to be calulated, TransactionDate/SettlementDate. Defaults to SettlementDate. |
| **amortisation_rule_set_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **instrument_event_configuration** | [InstrumentEventConfiguration](InstrumentEventConfiguration.md) | Optional | *No description available.* |
| **settlement_configuration** | [PortfolioSettlementConfiguration](PortfolioSettlementConfiguration.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CreateDerivedTransactionPortfolioRequest import CreateDerivedTransactionPortfolioRequest

instance = CreateDerivedTransactionPortfolioRequest(
    display_name="...",  # required — The name of the derived transaction portfolio.
    description="...",  # optional — A description for the derived transaction portfolio.
    code="...",  # required — The code of the derived transaction portfolio. Together with the scope this uniquely identifies the derived transaction portfolio.
    parent_portfolio_id=ResourceId(...),  # required
    created=datetime.now(),  # optional — This will be auto-populated to be the parent portfolio creation date.
    corporate_action_source_id=ResourceId(...),  # optional
    accounting_method="...",  # optional — . The available values are: Default, AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst, ProRateByUnits, ProRateByCost, ProRateByCostPortfolioCurrency, IntraDayThenFirstInFirstOut, LongTermHighestCostFirst, LongTermHighestCostFirstPortfolioCurrency, HighestCostFirstPortfolioCurrency, LowestCostFirstPortfolioCurrency, MaximumLossMinimumGain, MaximumLossMinimumGainPortfolioCurrency
    sub_holding_keys=,  # optional — A set of unique transaction properties to group the derived transaction portfolio&#39;s holdings by, perhaps for strategy tagging. Each property must be from the &#39;Transaction&#39; domain and identified by a key in the format {domain}/{scope}/{code}, for example &#39;Transaction/strategies/quantsignal&#39;. See https://support.lusid.com/knowledgebase/article/KA-01879/en-us for more information.
    instrument_scopes=,  # optional — The resolution strategy used to resolve instruments of transactions/holdings upserted to this derived portfolio.
    amortisation_method="...",  # optional — The amortisation method used by the portfolio for the calculation. The available values are: NoAmortisation, StraightLine, EffectiveYield, StraightLineSettlementDate, EffectiveYieldSettlementDate
    transaction_type_scope="...",  # optional — The scope of the transaction types.
    cash_gain_loss_calculation_date="...",  # optional — The option when the Cash Gain Loss to be calulated, TransactionDate/SettlementDate. Defaults to SettlementDate.
    amortisation_rule_set_id=ResourceId(...),  # optional
    instrument_event_configuration=InstrumentEventConfiguration(...),  # optional
    settlement_configuration=PortfolioSettlementConfiguration(...)  # optional
)
```

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [InstrumentEventConfiguration](InstrumentEventConfiguration.md)
- [PortfolioSettlementConfiguration](PortfolioSettlementConfiguration.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

