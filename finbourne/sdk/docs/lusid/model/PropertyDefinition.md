# PropertyDefinition

A list of property definitions.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **key** | **str** | Optional | The property key which uniquely identifies the property. The format for the property key is {domain}/{scope}/{code}, e.g. &#39;Portfolio/Manager/Id&#39;. |
| **value_type** | **str** | Optional | The type of values that can be associated with this property. This is defined by the property&#39;s data type. The available values are: String, Int, Decimal, DateTime, Boolean, Map, List, PropertyArray, Percentage, Code, Id, Uri, CurrencyAndAmount, TradePrice, Currency, MetricValue, ResourceId, ResultValue, CutLocalTime, DateOrCutLabel, UnindexedText |
| **display_name** | **str** | Optional | The display name of the property. |
| **data_type_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **type** | **str** | Optional | The type of the property. The available values are: Label, Metric, Information |
| **unit_schema** | **str** | Optional | The units that can be associated with the property&#39;s values. This is defined by the property&#39;s data type. The available values are: NoUnits, Basic, Iso4217Currency |
| **domain** | **str** | Optional | The domain that the property exists in. The available values are: NotDefined, Transaction, Portfolio, Holding, ReferenceHolding, TransactionConfiguration, Instrument, CutLabelDefinition, Analytic, PortfolioGroup, Person, AccessMetadata, Order, UnitResult, MarketData, ConfigurationRecipe, Allocation, Calendar, LegalEntity, InvestorRecord, InvestmentAccount, Placement, Execution, Block, Participation, Package, OrderInstruction, NextBestAction, CustomEntity, InstrumentEvent, Account, ChartOfAccounts, CustodianAccount, CheckDefinition, Abor, AborConfiguration, Fund, FundConfiguration, Fee, Reconciliation, PropertyDefinition, Compliance, DiaryEntry, Leg, DerivedValuation, Timeline, ClosedPeriod, AddressKeyDefinition, AmortisationRuleSet, AnalyticsSetInventory, AtomUnitResult, CleardownModule, ComplexMarketData, ComplianceRunSummary, ComplianceRule, ComplianceRunInfo, CorporateActionSource, CounterpartyAgreement, CustomEntityDefinition, DataType, Dialect, EventHandler, GeneralLedgerProfile, PostingModule, Quote, RecipeComposer, ReconciliationRunBreak, ReferenceList, RelationDefinition, ReturnBlockIndex, SRSDocument, SRSIndex, TransactionTemplate, TransactionTemplateScope, TransactionType, TransactionTypeConfig, TranslationScript, TaskDefinition, TaskInstance, Worker, StagingRuleSet, IdentifierDefinition, SettlementInstruction, TransactionFee |
| **scope** | **str** | Optional | The scope that the property exists in. *(read-only)* |
| **code** | **str** | Optional | The code of the property. Together with the domain and scope this uniquely identifies the property. *(read-only)* |
| **value_required** | **bool** | Optional | This field is not implemented and should be disregarded. |
| **life_time** | **str** | Optional | Describes how the property&#39;s values can change over time. The available values are: Perpetual, TimeVariant |
| **constraint_style** | **str** | Optional | Describes the uniqueness and cardinality of the property for entity objects under the property domain specified in Key. |
| **property_definition_type** | **str** | Optional | The definition type (DerivedDefinition or Definition). The available values are: ValueProperty, DerivedDefinition |
| **property_description** | **str** | Optional | A brief description of what a property of this property definition contains. |
| **derivation_formula** | **str** | Optional | The rule that defines how data is composed for a derived property. |
| **collection_type** | **str** | Optional | Describes whether a collection property should behave as a set or as an array. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | Set of unique property definition properties and associated values to store with the property definition. Each property must be from the &#39;PropertyDefinition&#39; domain. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **staged_modifications** | [StagedModificationsInfo](StagedModificationsInfo.md) | Optional | *No description available.* |
| **is_filterable** | **bool** | Optional | Bool indicating whether the values of this property are fitlerable, this is true for all non-derived property defintions.  For a derived definition this must be set true to enable filtering. |
| **custom_entity_types** | **List[str]** | Optional | The custom entity types that properties relating to this property definition can be applied to. |
| **value_format** | **str** | Optional | The format in which values for this property definition should be represented. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PropertyDefinition import PropertyDefinition

instance = PropertyDefinition(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    key="...",  # optional — The property key which uniquely identifies the property. The format for the property key is {domain}/{scope}/{code}, e.g. &#39;Portfolio/Manager/Id&#39;.
    value_type="...",  # optional — The type of values that can be associated with this property. This is defined by the property&#39;s data type. The available values are: String, Int, Decimal, DateTime, Boolean, Map, List, PropertyArray, Percentage, Code, Id, Uri, CurrencyAndAmount, TradePrice, Currency, MetricValue, ResourceId, ResultValue, CutLocalTime, DateOrCutLabel, UnindexedText
    display_name="...",  # optional — The display name of the property.
    data_type_id=ResourceId(...),  # optional
    type="...",  # optional — The type of the property. The available values are: Label, Metric, Information
    unit_schema="...",  # optional — The units that can be associated with the property&#39;s values. This is defined by the property&#39;s data type. The available values are: NoUnits, Basic, Iso4217Currency
    domain="...",  # optional — The domain that the property exists in. The available values are: NotDefined, Transaction, Portfolio, Holding, ReferenceHolding, TransactionConfiguration, Instrument, CutLabelDefinition, Analytic, PortfolioGroup, Person, AccessMetadata, Order, UnitResult, MarketData, ConfigurationRecipe, Allocation, Calendar, LegalEntity, InvestorRecord, InvestmentAccount, Placement, Execution, Block, Participation, Package, OrderInstruction, NextBestAction, CustomEntity, InstrumentEvent, Account, ChartOfAccounts, CustodianAccount, CheckDefinition, Abor, AborConfiguration, Fund, FundConfiguration, Fee, Reconciliation, PropertyDefinition, Compliance, DiaryEntry, Leg, DerivedValuation, Timeline, ClosedPeriod, AddressKeyDefinition, AmortisationRuleSet, AnalyticsSetInventory, AtomUnitResult, CleardownModule, ComplexMarketData, ComplianceRunSummary, ComplianceRule, ComplianceRunInfo, CorporateActionSource, CounterpartyAgreement, CustomEntityDefinition, DataType, Dialect, EventHandler, GeneralLedgerProfile, PostingModule, Quote, RecipeComposer, ReconciliationRunBreak, ReferenceList, RelationDefinition, ReturnBlockIndex, SRSDocument, SRSIndex, TransactionTemplate, TransactionTemplateScope, TransactionType, TransactionTypeConfig, TranslationScript, TaskDefinition, TaskInstance, Worker, StagingRuleSet, IdentifierDefinition, SettlementInstruction, TransactionFee
    scope="...",  # optional — The scope that the property exists in.
    code="...",  # optional — The code of the property. Together with the domain and scope this uniquely identifies the property.
    value_required=True,  # optional — This field is not implemented and should be disregarded.
    life_time="...",  # optional — Describes how the property&#39;s values can change over time. The available values are: Perpetual, TimeVariant
    constraint_style="...",  # optional — Describes the uniqueness and cardinality of the property for entity objects under the property domain specified in Key.
    property_definition_type="...",  # optional — The definition type (DerivedDefinition or Definition). The available values are: ValueProperty, DerivedDefinition
    property_description="...",  # optional — A brief description of what a property of this property definition contains.
    derivation_formula="...",  # optional — The rule that defines how data is composed for a derived property.
    collection_type="...",  # optional — Describes whether a collection property should behave as a set or as an array.
    properties=ModelProperty(...),  # optional — Set of unique property definition properties and associated values to store with the property definition. Each property must be from the &#39;PropertyDefinition&#39; domain.
    version=Version(...),  # optional
    staged_modifications=StagedModificationsInfo(...),  # optional
    is_filterable=True,  # optional — Bool indicating whether the values of this property are fitlerable, this is true for all non-derived property defintions.  For a derived definition this must be set true to enable filtering.
    custom_entity_types=,  # optional — The custom entity types that properties relating to this property definition can be applied to.
    value_format="...",  # optional — The format in which values for this property definition should be represented.
    links=[]  # optional
)
```

- [ResourceId](ResourceId.md)
- [ModelProperty](ModelProperty.md) — used in `properties`
- [Version](Version.md)
- [StagedModificationsInfo](StagedModificationsInfo.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

