# Fund

A Fund entity.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **display_name** | **str** | Optional | The name of the Fund. |
| **description** | **str** | Optional | A description for the Fund. |
| **base_currency** | **str** | Optional | The base currency of the Fund in ISO 4217 currency code format. All portfolios must be of a matching base currency. |
| **investor_structure** | **str** | Required | The Investor structure to be used by the Fund. Supported values are &#39;NonUnitised&#39; and &#39;Classes&#39;. |
| **portfolio_ids** | [List[PortfolioEntityIdWithDetails]](PortfolioEntityIdWithDetails.md) | Optional | A list of the portfolios on the fund, which are part of the Fund. Note: These must all have the same base currency, which must also much the Fund Base Currency. |
| **fund_configuration_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **abor_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **share_class_instruments** | [List[InstrumentResolutionDetail]](InstrumentResolutionDetail.md) | Optional | Details the user-provided instrument identifiers and the instrument resolved from them. These would be decommissioned in favour of the new AllocationGroups and ShareClasses structures. |
| **type** | **str** | Optional | The type of fund; &#39;Standalone&#39;, &#39;Master&#39; or &#39;Feeder&#39; |
| **inception_date** | **datetime** | Required | Inception date of the Fund |
| **decimal_places** | **int** | Optional | Number of decimal places for reporting |
| **year_end_date** | [DayMonth](DayMonth.md) | Optional | *No description available.* |
| **primary_nav_type** | [NavType](NavType.md) | Optional | *No description available.* |
| **additional_nav_types** | [List[NavType]](NavType.md) | Optional | The definitions for any additional NAVs on the Fund. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of properties for the Fund. |
| **create_instrument** | **bool** | Optional | Whether to create instruments for the Fund&#39;s share classes, series, or partner classes upon creation. Defaults to false. |
| **apportionment_method_property** | [ApportionmentMethodProperty](ApportionmentMethodProperty.md) | Optional | *No description available.* |
| **allocation_groups** | [List[AllocationGroup]](AllocationGroup.md) | Optional | An optional list of Allocation Group definitions for the Fund. |
| **share_classes** | [List[ShareClass]](ShareClass.md) | Optional | An optional list of Share Class definitions for the Fund. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.Fund import Fund

instance = Fund(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    id=ResourceId(...),  # required
    display_name="...",  # optional — The name of the Fund.
    description="...",  # optional — A description for the Fund.
    base_currency="...",  # optional — The base currency of the Fund in ISO 4217 currency code format. All portfolios must be of a matching base currency.
    investor_structure="...",  # required — The Investor structure to be used by the Fund. Supported values are &#39;NonUnitised&#39; and &#39;Classes&#39;.
    portfolio_ids=[],  # optional — A list of the portfolios on the fund, which are part of the Fund. Note: These must all have the same base currency, which must also much the Fund Base Currency.
    fund_configuration_id=ResourceId(...),  # optional
    abor_id=ResourceId(...),  # optional
    share_class_instruments=[],  # optional — Details the user-provided instrument identifiers and the instrument resolved from them. These would be decommissioned in favour of the new AllocationGroups and ShareClasses structures.
    type="...",  # optional — The type of fund; &#39;Standalone&#39;, &#39;Master&#39; or &#39;Feeder&#39;
    inception_date=datetime.now(),  # required — Inception date of the Fund
    decimal_places=0,  # optional — Number of decimal places for reporting
    year_end_date=DayMonth(...),  # optional
    primary_nav_type=NavType(...),  # optional
    additional_nav_types=[],  # optional — The definitions for any additional NAVs on the Fund.
    properties=ModelProperty(...),  # optional — A set of properties for the Fund.
    create_instrument=True,  # optional — Whether to create instruments for the Fund&#39;s share classes, series, or partner classes upon creation. Defaults to false.
    apportionment_method_property=ApportionmentMethodProperty(...),  # optional
    allocation_groups=[],  # optional — An optional list of Allocation Group definitions for the Fund.
    share_classes=[],  # optional — An optional list of Share Class definitions for the Fund.
    version=Version(...),  # optional
    links=[]  # optional
)
```

- [ResourceId](ResourceId.md)
- [PortfolioEntityIdWithDetails](PortfolioEntityIdWithDetails.md) — used in `portfolio_ids`
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [InstrumentResolutionDetail](InstrumentResolutionDetail.md) — used in `share_class_instruments`
- [DayMonth](DayMonth.md)
- [NavType](NavType.md)
- [NavType](NavType.md) — used in `additional_nav_types`
- [ModelProperty](ModelProperty.md) — used in `properties`
- [ApportionmentMethodProperty](ApportionmentMethodProperty.md)
- [AllocationGroup](AllocationGroup.md) — used in `allocation_groups`
- [ShareClass](ShareClass.md) — used in `share_classes`
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

