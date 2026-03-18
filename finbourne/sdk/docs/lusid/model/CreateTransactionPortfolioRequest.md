# CreateTransactionPortfolioRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **display_name** | **str** | Required | The name of the transaction portfolio. |
| **description** | **str** | Optional | A description for the transaction portfolio. |
| **code** | **str** | Required | The code of the transaction portfolio. Together with the scope this uniquely identifies the transaction portfolio. |
| **created** | **datetime** | Optional | The effective datetime at which to create the transaction portfolio. No transactions can be added to the transaction portfolio before this date. Defaults to the current LUSID system datetime if not specified. |
| **base_currency** | **str** | Required | The base currency of the transaction portfolio in ISO 4217 currency code format. |
| **corporate_action_source_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **accounting_method** | **str** | Optional | . The available values are: Default, AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst, ProRateByUnits, ProRateByCost, ProRateByCostPortfolioCurrency, IntraDayThenFirstInFirstOut, LongTermHighestCostFirst, LongTermHighestCostFirstPortfolioCurrency, HighestCostFirstPortfolioCurrency, LowestCostFirstPortfolioCurrency, MaximumLossMinimumGain, MaximumLossMinimumGainPortfolioCurrency |
| **sub_holding_keys** | **List[str]** | Optional | A set of unique transaction properties to group the transaction portfolio&#39;s holdings by, perhaps for strategy tagging. Each property must be from the &#39;Transaction&#39; domain and identified by a key in the format {domain}/{scope}/{code}, for example &#39;Transaction/strategies/quantsignal&#39;. See https://support.lusid.com/knowledgebase/article/KA-01879/en-us for more information. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of unique portfolio properties to add custom data to the transaction portfolio. Each property must be from the &#39;Portfolio&#39; domain and identified by a key in the format {domain}/{scope}/{code}, for example &#39;Portfolio/Manager/Id&#39;. Note these properties must be pre-defined. |
| **instrument_scopes** | **List[str]** | Optional | The resolution strategy used to resolve instruments of transactions/holdings upserted to this portfolio. |
| **amortisation_method** | **str** | Optional | The amortisation method used by the portfolio for the calculation. The available values are: NoAmortisation, StraightLine, EffectiveYield, StraightLineSettlementDate, EffectiveYieldSettlementDate |
| **transaction_type_scope** | **str** | Optional | The scope of the transaction types. |
| **cash_gain_loss_calculation_date** | **str** | Optional | The option when the Cash Gain Loss to be calulated, TransactionDate/SettlementDate. Defaults to SettlementDate. |
| **instrument_event_configuration** | [InstrumentEventConfiguration](InstrumentEventConfiguration.md) | Optional | *No description available.* |
| **amortisation_rule_set_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **tax_rule_set_scope** | **str** | Optional | The scope of the tax rule sets for this portfolio. |
| **settlement_configuration** | [PortfolioSettlementConfiguration](PortfolioSettlementConfiguration.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CreateTransactionPortfolioRequest import CreateTransactionPortfolioRequest

instance = CreateTransactionPortfolioRequest(
    display_name="...",  # required — The name of the transaction portfolio.
    description="...",  # optional — A description for the transaction portfolio.
    code="...",  # required — The code of the transaction portfolio. Together with the scope this uniquely identifies the transaction portfolio.
    created=datetime.now(),  # optional — The effective datetime at which to create the transaction portfolio. No transactions can be added to the transaction portfolio before this date. Defaults to the current LUSID system datetime if not specified.
    base_currency="...",  # required — The base currency of the transaction portfolio in ISO 4217 currency code format.
    corporate_action_source_id=ResourceId(...),  # optional
    accounting_method="...",  # optional — . The available values are: Default, AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst, ProRateByUnits, ProRateByCost, ProRateByCostPortfolioCurrency, IntraDayThenFirstInFirstOut, LongTermHighestCostFirst, LongTermHighestCostFirstPortfolioCurrency, HighestCostFirstPortfolioCurrency, LowestCostFirstPortfolioCurrency, MaximumLossMinimumGain, MaximumLossMinimumGainPortfolioCurrency
    sub_holding_keys=,  # optional — A set of unique transaction properties to group the transaction portfolio&#39;s holdings by, perhaps for strategy tagging. Each property must be from the &#39;Transaction&#39; domain and identified by a key in the format {domain}/{scope}/{code}, for example &#39;Transaction/strategies/quantsignal&#39;. See https://support.lusid.com/knowledgebase/article/KA-01879/en-us for more information.
    properties=ModelProperty(...),  # optional — A set of unique portfolio properties to add custom data to the transaction portfolio. Each property must be from the &#39;Portfolio&#39; domain and identified by a key in the format {domain}/{scope}/{code}, for example &#39;Portfolio/Manager/Id&#39;. Note these properties must be pre-defined.
    instrument_scopes=,  # optional — The resolution strategy used to resolve instruments of transactions/holdings upserted to this portfolio.
    amortisation_method="...",  # optional — The amortisation method used by the portfolio for the calculation. The available values are: NoAmortisation, StraightLine, EffectiveYield, StraightLineSettlementDate, EffectiveYieldSettlementDate
    transaction_type_scope="...",  # optional — The scope of the transaction types.
    cash_gain_loss_calculation_date="...",  # optional — The option when the Cash Gain Loss to be calulated, TransactionDate/SettlementDate. Defaults to SettlementDate.
    instrument_event_configuration=InstrumentEventConfiguration(...),  # optional
    amortisation_rule_set_id=ResourceId(...),  # optional
    tax_rule_set_scope="...",  # optional — The scope of the tax rule sets for this portfolio.
    settlement_configuration=PortfolioSettlementConfiguration(...)  # optional
)
```

- [ResourceId](ResourceId.md)
- [ModelProperty](ModelProperty.md) — used in `properties`
- [InstrumentEventConfiguration](InstrumentEventConfiguration.md)
- [ResourceId](ResourceId.md)
- [PortfolioSettlementConfiguration](PortfolioSettlementConfiguration.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

