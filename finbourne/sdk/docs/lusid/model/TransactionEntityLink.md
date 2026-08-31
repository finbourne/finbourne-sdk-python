# TransactionEntityLink

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **entity_type** | **str** | Required | Available values: Transaction, Portfolio, Holding, ReferenceHolding, TransactionConfiguration, Instrument, PortfolioGroup, Person, Order, Allocation, Calendar, LegalEntity, InvestorRecord, InvestmentAccount, Placement, Execution, Block, Participation, Package, OrderInstruction, CustomEntity, InstrumentEvent, Account, ChartOfAccounts, CustodianAccount, CheckDefinition, Abor, AborConfiguration, Fund, FundConfiguration, FundStructure, Fee, Reconciliation, PropertyDefinition, Compliance, DiaryEntry, Leg, DerivedValuation, Timeline, ClosedPeriod, TaskDefinition, Workflow, IdentifierDefinition, SettlementInstruction, TransactionFeeType, PaymentInstruction, Transfer. |
| **entity_id_name** | **str** | Required | *No description available.* |
| **entity_id_value** | **str** | Required | *No description available.* |
| **restrict_editing** | **bool** | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TransactionEntityLink import TransactionEntityLink

instance = TransactionEntityLink(
    entity_type="...",  # required — Available values: Transaction, Portfolio, Holding, ReferenceHolding, TransactionConfiguration, Instrument, PortfolioGroup, Person, Order, Allocation, Calendar, LegalEntity, InvestorRecord, InvestmentAccount, Placement, Execution, Block, Participation, Package, OrderInstruction, CustomEntity, InstrumentEvent, Account, ChartOfAccounts, CustodianAccount, CheckDefinition, Abor, AborConfiguration, Fund, FundConfiguration, FundStructure, Fee, Reconciliation, PropertyDefinition, Compliance, DiaryEntry, Leg, DerivedValuation, Timeline, ClosedPeriod, TaskDefinition, Workflow, IdentifierDefinition, SettlementInstruction, TransactionFeeType, PaymentInstruction, Transfer.
    entity_id_name="...",  # required
    entity_id_value="...",  # required
    restrict_editing=True  # required
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

