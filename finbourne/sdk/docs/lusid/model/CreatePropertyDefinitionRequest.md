# CreatePropertyDefinitionRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **domain** | **str** | Required | The domain that the property exists in. Available values: Transaction, Portfolio, Holding, ReferenceHolding, TransactionConfiguration, Instrument, PortfolioGroup, Person, Order, Allocation, Calendar, LegalEntity, InvestorRecord, InvestmentAccount, Placement, Execution, Block, Participation, Package, OrderInstruction, CustomEntity, InstrumentEvent, Account, ChartOfAccounts, CustodianAccount, CheckDefinition, Abor, AborConfiguration, Fund, FundConfiguration, Fee, Reconciliation, PropertyDefinition, Compliance, DiaryEntry, Leg, DerivedValuation, Timeline, ClosedPeriod, IdentifierDefinition, SettlementInstruction, TransactionFee. |
| **scope** | **str** | Required | The scope that the property exists in. |
| **code** | **str** | Required | The code of the property. Together with the domain and scope this uniquely identifies the property. |
| **value_required** | **bool** | Optional | This field is not implemented and should be disregarded. |
| **display_name** | **str** | Required | The display name of the property. |
| **data_type_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **life_time** | **str** | Optional | Describes how the property&#39;s values can change over time. Available values: Perpetual, TimeVariant. |
| **constraint_style** | **str** | Optional | Describes the uniqueness and cardinality of the property for entity objects under the property domain specified in Key. Defaults to \&quot;Property\&quot; if not specified. Valid values for this field are: Property, Collection or Identifier. |
| **property_description** | **str** | Optional | Describes the property |
| **collection_type** | **str** | Optional | Describes whether a collection property should behave as a Set or as an Array. Available values: Set, Array. |
| **custom_entity_types** | **List[str]** | Optional | The custom entity types that properties relating to this property definition can be applied to. |
| **value_format** | **str** | Optional | The format in which values for this property definition should be represented. Available values: Text, Html. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CreatePropertyDefinitionRequest import CreatePropertyDefinitionRequest

instance = CreatePropertyDefinitionRequest(
    domain="...",  # required — The domain that the property exists in. Available values: Transaction, Portfolio, Holding, ReferenceHolding, TransactionConfiguration, Instrument, PortfolioGroup, Person, Order, Allocation, Calendar, LegalEntity, InvestorRecord, InvestmentAccount, Placement, Execution, Block, Participation, Package, OrderInstruction, CustomEntity, InstrumentEvent, Account, ChartOfAccounts, CustodianAccount, CheckDefinition, Abor, AborConfiguration, Fund, FundConfiguration, Fee, Reconciliation, PropertyDefinition, Compliance, DiaryEntry, Leg, DerivedValuation, Timeline, ClosedPeriod, IdentifierDefinition, SettlementInstruction, TransactionFee.
    scope="...",  # required — The scope that the property exists in.
    code="...",  # required — The code of the property. Together with the domain and scope this uniquely identifies the property.
    value_required=True,  # optional — This field is not implemented and should be disregarded.
    display_name="...",  # required — The display name of the property.
    data_type_id=ResourceId(...),  # required
    life_time="...",  # optional — Describes how the property&#39;s values can change over time. Available values: Perpetual, TimeVariant.
    constraint_style="...",  # optional — Describes the uniqueness and cardinality of the property for entity objects under the property domain specified in Key. Defaults to \&quot;Property\&quot; if not specified. Valid values for this field are: Property, Collection or Identifier.
    property_description="...",  # optional — Describes the property
    collection_type="...",  # optional — Describes whether a collection property should behave as a Set or as an Array. Available values: Set, Array.
    custom_entity_types=,  # optional — The custom entity types that properties relating to this property definition can be applied to.
    value_format="..."  # optional — The format in which values for this property definition should be represented. Available values: Text, Html.
)
```

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

