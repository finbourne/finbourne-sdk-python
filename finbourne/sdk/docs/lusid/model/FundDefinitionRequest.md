# FundDefinitionRequest

The request used to create a Fund.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Required | The code given for the Fund. |
| **short_code** | **str** | Optional | A short code for the Fund. A fund structure tags journal entry lines with the short code of the member they originated from, so it should be unique across the funds of one structure. Optional. |
| **display_name** | **str** | Required | The name of the Fund. |
| **description** | **str** | Optional | A description for the Fund. |
| **base_currency** | **str** | Required | The base currency of the Fund in ISO 4217 currency code format. All portfolios must be of a matching base currency. |
| **investor_structure** | **str** | Optional | The Investor structure to be used by the Fund. Available values: NonUnitised, Classes. |
| **portfolio_ids** | [List[PortfolioEntityId]](PortfolioEntityId.md) | Required | A list of the Portfolio IDs associated with the fund, which are part of the Fund. Note: These must all have the same base currency, which must also match the Fund Base Currency. |
| **fund_configuration_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **share_class_instrument_scopes** | **List[str]** | Optional | The scopes in which the instruments lie, currently limited to one. |
| **share_class_instruments** | [List[InstrumentResolutionDetail]](InstrumentResolutionDetail.md) | Optional | Details the user-provided instrument identifiers and the instrument resolved from them. These would be decommissioned in favour of the new AllocationGroups and ShareClasses structures. |
| **type** | **str** | Optional | The kind of vehicle the fund is, one of the values of the system/fundVehicleType data type. Master and Feeder are deprecated: the structural role of a fund now lives on its fund structure node, and a fund with either type cannot be a member of a fund structure. Available values: Standalone, Master, Feeder, SPV, AIV, TaxBlocker, CarryVehicle, SponsorCommitmentVehicle, CoInvestVehicle, GPInterestHolder, SMA, CTA. |
| **tax_transparency** | **str** | Optional | Whether the Fund is looked through for tax: Transparent passes its income and gains to its holders as their own, Opaque is taxed in its own right. Optional; if not set, a TaxBlocker is Opaque and a CarryVehicle or GPInterestHolder is Transparent. A fund structure requires it on every SPV and AIV member. Available values: Transparent, Opaque. |
| **inception_date** | **datetime** | Required | Inception date of the Fund |
| **decimal_places** | **int** | Optional | Number of decimal places for reporting |
| **primary_nav_type** | [NavTypeDefinition](NavTypeDefinition.md) | Required | *No description available.* |
| **additional_nav_types** | [List[NavTypeDefinition]](NavTypeDefinition.md) | Optional | The definitions for any additional NAVs on the Fund. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of properties for the Fund. |
| **create_instrument** | **bool** | Optional | Whether to create instruments for the Fund&#39;s share classes, series, or partner classes upon creation. Defaults to false. |
| **share_classes** | [List[ShareClassDefinition]](ShareClassDefinition.md) | Optional | An optional list of Share Class definitions for the Fund. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundDefinitionRequest import FundDefinitionRequest

instance = FundDefinitionRequest(
    code="...",  # required — The code given for the Fund.
    short_code="...",  # optional — A short code for the Fund. A fund structure tags journal entry lines with the short code of the member they originated from, so it should be unique across the funds of one structure. Optional.
    display_name="...",  # required — The name of the Fund.
    description="...",  # optional — A description for the Fund.
    base_currency="...",  # required — The base currency of the Fund in ISO 4217 currency code format. All portfolios must be of a matching base currency.
    investor_structure="...",  # optional — The Investor structure to be used by the Fund. Available values: NonUnitised, Classes.
    portfolio_ids=[],  # required — A list of the Portfolio IDs associated with the fund, which are part of the Fund. Note: These must all have the same base currency, which must also match the Fund Base Currency.
    fund_configuration_id=ResourceId(...),  # required
    share_class_instrument_scopes=,  # optional — The scopes in which the instruments lie, currently limited to one.
    share_class_instruments=[],  # optional — Details the user-provided instrument identifiers and the instrument resolved from them. These would be decommissioned in favour of the new AllocationGroups and ShareClasses structures.
    type="...",  # optional — The kind of vehicle the fund is, one of the values of the system/fundVehicleType data type. Master and Feeder are deprecated: the structural role of a fund now lives on its fund structure node, and a fund with either type cannot be a member of a fund structure. Available values: Standalone, Master, Feeder, SPV, AIV, TaxBlocker, CarryVehicle, SponsorCommitmentVehicle, CoInvestVehicle, GPInterestHolder, SMA, CTA.
    tax_transparency="...",  # optional — Whether the Fund is looked through for tax: Transparent passes its income and gains to its holders as their own, Opaque is taxed in its own right. Optional; if not set, a TaxBlocker is Opaque and a CarryVehicle or GPInterestHolder is Transparent. A fund structure requires it on every SPV and AIV member. Available values: Transparent, Opaque.
    inception_date=datetime.now(),  # required — Inception date of the Fund
    decimal_places=0,  # optional — Number of decimal places for reporting
    primary_nav_type=NavTypeDefinition(...),  # required
    additional_nav_types=[],  # optional — The definitions for any additional NAVs on the Fund.
    properties=ModelProperty(...),  # optional — A set of properties for the Fund.
    create_instrument=True,  # optional — Whether to create instruments for the Fund&#39;s share classes, series, or partner classes upon creation. Defaults to false.
    share_classes=[]  # optional — An optional list of Share Class definitions for the Fund.
)
```

- [PortfolioEntityId](PortfolioEntityId.md) — used in `portfolio_ids`
- [ResourceId](ResourceId.md)
- [InstrumentResolutionDetail](InstrumentResolutionDetail.md) — used in `share_class_instruments`
- [NavTypeDefinition](NavTypeDefinition.md)
- [NavTypeDefinition](NavTypeDefinition.md) — used in `additional_nav_types`
- [ModelProperty](ModelProperty.md) — used in `properties`
- [ShareClassDefinition](ShareClassDefinition.md) — used in `share_classes`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

