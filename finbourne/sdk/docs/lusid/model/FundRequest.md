# FundRequest

The request used to create a Fund.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Required | The code given for the Fund. |
| **display_name** | **str** | Optional | The name of the Fund. |
| **description** | **str** | Optional | A description for the Fund. |
| **fund_configuration_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **abor_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **share_class_instrument_scopes** | **List[str]** | Optional | The scopes in which the instruments lie, currently limited to one. |
| **share_class_instruments** | [List[InstrumentResolutionDetail]](InstrumentResolutionDetail.md) | Optional | Details the user-provided instrument identifiers and the instrument resolved from them. These would be decommissioned in favour of the new AllocationGroups and ShareClasses structures. |
| **type** | **str** | Required | The type of fund; &#39;Standalone&#39;, &#39;Master&#39; or &#39;Feeder&#39; |
| **inception_date** | **datetime** | Required | Inception date of the Fund |
| **decimal_places** | **int** | Optional | Number of decimal places for reporting |
| **year_end_date** | [DayMonth](DayMonth.md) | Required | *No description available.* |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of properties for the Fund. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundRequest import FundRequest

instance = FundRequest(
    code="...",  # required — The code given for the Fund.
    display_name="...",  # optional — The name of the Fund.
    description="...",  # optional — A description for the Fund.
    fund_configuration_id=ResourceId(...),  # required
    abor_id=ResourceId(...),  # required
    share_class_instrument_scopes=,  # optional — The scopes in which the instruments lie, currently limited to one.
    share_class_instruments=[],  # optional — Details the user-provided instrument identifiers and the instrument resolved from them. These would be decommissioned in favour of the new AllocationGroups and ShareClasses structures.
    type="...",  # required — The type of fund; &#39;Standalone&#39;, &#39;Master&#39; or &#39;Feeder&#39;
    inception_date=datetime.now(),  # required — Inception date of the Fund
    decimal_places=0,  # optional — Number of decimal places for reporting
    year_end_date=DayMonth(...),  # required
    properties=ModelProperty(...)  # optional — A set of properties for the Fund.
)
```

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [InstrumentResolutionDetail](InstrumentResolutionDetail.md) — used in `share_class_instruments`
- [DayMonth](DayMonth.md)
- [ModelProperty](ModelProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

