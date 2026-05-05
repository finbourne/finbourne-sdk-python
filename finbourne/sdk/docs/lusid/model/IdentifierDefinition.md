# IdentifierDefinition

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **domain** | **str** | Required | The type of entity to which the identifier can be attached. Available values: Transaction, Portfolio, Holding, ReferenceHolding, TransactionConfiguration, Instrument, PortfolioGroup, Person, Order, Allocation, Calendar, LegalEntity, InvestorRecord, InvestmentAccount, Placement, Execution, Block, Participation, Package, OrderInstruction, CustomEntity, InstrumentEvent, Account, ChartOfAccounts, CustodianAccount, CheckDefinition, Abor, AborConfiguration, Fund, FundConfiguration, Fee, Reconciliation, PropertyDefinition, Compliance, DiaryEntry, Leg, DerivedValuation, Timeline, ClosedPeriod, IdentifierDefinition, SettlementInstruction, TransactionFee. |
| **identifier_scope** | **str** | Required | The scope that the identifier definition exists in. |
| **identifier_type** | **str** | Required | What the identifier represents. Together with \&quot;domain\&quot; and \&quot;identifierScope\&quot; this uniquely identifies the identifier definition. |
| **life_time** | **str** | Required | Describes whether an identifier value is associated with an entity for all effective dates or applies within a specified effective date range. Available values: Perpetual, TimeVariant. |
| **hierarchy_usage** | **str** | Optional | MasterIdentifier (aka unique) An entity can have one value for this identifier definition on a given effective date. A value for this identifier definition can only be associated with one entity (in a given scope) on a given effective date. ParentIdentifier (aka non-unique) An entity can have one value for this identifier definition on a given effective date. A value for this identifier definition can be associated with many entities (in a given scope) on a given effective date. Default value: MasterIdentifier. Available values: MasterIdentifier, ParentIdentifier. |
| **hierarchy_level** | **str** | Optional | Optional metadata associated with the identifier definition. |
| **display_name** | **str** | Optional | A display name for the identifier. E.g. Figi. |
| **description** | **str** | Optional | An optional description for the identifier. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of properties for the identifier definition. |
| **version** | [Version](Version.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.IdentifierDefinition import IdentifierDefinition

instance = IdentifierDefinition(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    domain="...",  # required — The type of entity to which the identifier can be attached. Available values: Transaction, Portfolio, Holding, ReferenceHolding, TransactionConfiguration, Instrument, PortfolioGroup, Person, Order, Allocation, Calendar, LegalEntity, InvestorRecord, InvestmentAccount, Placement, Execution, Block, Participation, Package, OrderInstruction, CustomEntity, InstrumentEvent, Account, ChartOfAccounts, CustodianAccount, CheckDefinition, Abor, AborConfiguration, Fund, FundConfiguration, Fee, Reconciliation, PropertyDefinition, Compliance, DiaryEntry, Leg, DerivedValuation, Timeline, ClosedPeriod, IdentifierDefinition, SettlementInstruction, TransactionFee.
    identifier_scope="...",  # required — The scope that the identifier definition exists in.
    identifier_type="...",  # required — What the identifier represents. Together with \&quot;domain\&quot; and \&quot;identifierScope\&quot; this uniquely identifies the identifier definition.
    life_time="...",  # required — Describes whether an identifier value is associated with an entity for all effective dates or applies within a specified effective date range. Available values: Perpetual, TimeVariant.
    hierarchy_usage="...",  # optional — MasterIdentifier (aka unique) An entity can have one value for this identifier definition on a given effective date. A value for this identifier definition can only be associated with one entity (in a given scope) on a given effective date. ParentIdentifier (aka non-unique) An entity can have one value for this identifier definition on a given effective date. A value for this identifier definition can be associated with many entities (in a given scope) on a given effective date. Default value: MasterIdentifier. Available values: MasterIdentifier, ParentIdentifier.
    hierarchy_level="...",  # optional — Optional metadata associated with the identifier definition.
    display_name="...",  # optional — A display name for the identifier. E.g. Figi.
    description="...",  # optional — An optional description for the identifier.
    properties=ModelProperty(...),  # optional — A set of properties for the identifier definition.
    version=Version(...)  # optional
)
```

- [ModelProperty](ModelProperty.md) — used in `properties`
- [Version](Version.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

