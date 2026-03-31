# FundDefinitionRequest

The request used to create a Fund.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Required | The code given for the Fund. |
| **display_name** | **str** | Required | The name of the Fund. |
| **description** | **str** | Optional | A description for the Fund. |
| **base_currency** | **str** | Required | The base currency of the Fund in ISO 4217 currency code format. All portfolios must be of a matching base currency. |
| **investor_structure** | **str** | Optional | The Investor structure to be used by the Fund. Supported values are &#39;NonUnitised&#39; and &#39;Classes&#39;. |
| **portfolio_ids** | [List[PortfolioEntityId]](PortfolioEntityId.md) | Required | A list of the Portfolio IDs associated with the fund, which are part of the Fund. Note: These must all have the same base currency, which must also much the Fund Base Currency. |
| **fund_configuration_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **share_class_instrument_scopes** | **List[str]** | Optional | The scopes in which the instruments lie, currently limited to one. |
| **share_class_instruments** | [List[InstrumentResolutionDetail]](InstrumentResolutionDetail.md) | Optional | Details the user-provided instrument identifiers and the instrument resolved from them. These would be decommissioned in favour of the new AllocationGroups and ShareClasses structures. |
| **type** | **str** | Optional | The type of fund; &#39;Standalone&#39;, &#39;Master&#39; or &#39;Feeder&#39; |
| **inception_date** | **datetime** | Required | Inception date of the Fund |
| **decimal_places** | **int** | Optional | Number of decimal places for reporting |
| **primary_nav_type** | [NavTypeDefinition](NavTypeDefinition.md) | Required | *No description available.* |
| **additional_nav_types** | [List[NavTypeDefinition]](NavTypeDefinition.md) | Optional | The definitions for any additional NAVs on the Fund. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of properties for the Fund. |
| **create_instrument** | **bool** | Optional | Whether to create instruments for the Fund&#39;s share classes, series, or partner classes upon creation. Defaults to false. |
| **apportionment_method_property** | [ApportionmentMethodProperty](ApportionmentMethodProperty.md) | Optional | *No description available.* |
| **share_classes** | [List[ShareClassDefinition]](ShareClassDefinition.md) | Optional | An optional list of Share Class definitions for the Fund. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundDefinitionRequest import FundDefinitionRequest

instance = FundDefinitionRequest(
    code="...",  # required — The code given for the Fund.
    display_name="...",  # required — The name of the Fund.
    description="...",  # optional — A description for the Fund.
    base_currency="...",  # required — The base currency of the Fund in ISO 4217 currency code format. All portfolios must be of a matching base currency.
    investor_structure="...",  # optional — The Investor structure to be used by the Fund. Supported values are &#39;NonUnitised&#39; and &#39;Classes&#39;.
    portfolio_ids=[],  # required — A list of the Portfolio IDs associated with the fund, which are part of the Fund. Note: These must all have the same base currency, which must also much the Fund Base Currency.
    fund_configuration_id=ResourceId(...),  # required
    share_class_instrument_scopes=,  # optional — The scopes in which the instruments lie, currently limited to one.
    share_class_instruments=[],  # optional — Details the user-provided instrument identifiers and the instrument resolved from them. These would be decommissioned in favour of the new AllocationGroups and ShareClasses structures.
    type="...",  # optional — The type of fund; &#39;Standalone&#39;, &#39;Master&#39; or &#39;Feeder&#39;
    inception_date=datetime.now(),  # required — Inception date of the Fund
    decimal_places=0,  # optional — Number of decimal places for reporting
    primary_nav_type=NavTypeDefinition(...),  # required
    additional_nav_types=[],  # optional — The definitions for any additional NAVs on the Fund.
    properties=ModelProperty(...),  # optional — A set of properties for the Fund.
    create_instrument=True,  # optional — Whether to create instruments for the Fund&#39;s share classes, series, or partner classes upon creation. Defaults to false.
    apportionment_method_property=ApportionmentMethodProperty(...),  # optional
    share_classes=[]  # optional — An optional list of Share Class definitions for the Fund.
)
```

- [PortfolioEntityId](PortfolioEntityId.md) — used in `portfolio_ids`
- [ResourceId](ResourceId.md)
- [InstrumentResolutionDetail](InstrumentResolutionDetail.md) — used in `share_class_instruments`
- [NavTypeDefinition](NavTypeDefinition.md)
- [NavTypeDefinition](NavTypeDefinition.md) — used in `additional_nav_types`
- [ModelProperty](ModelProperty.md) — used in `properties`
- [ApportionmentMethodProperty](ApportionmentMethodProperty.md)
- [ShareClassDefinition](ShareClassDefinition.md) — used in `share_classes`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

