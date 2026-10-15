# EligibleCollateralScheduleRequest

The request used to create an Eligible Collateral Schedule.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Required | The code of the Eligible Collateral Schedule. |
| **description** | **str** | Optional | A description of the Eligible Collateral Schedule. Optional. |
| **rows** | [List[EligibleCollateralRowRequest]](EligibleCollateralRowRequest.md) | Required | The classes of collateral that may be posted, each with the valuation percentage it is accepted at. At least one and at most 200 rows. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of properties to decorate onto the Eligible Collateral Schedule. Filterable. |
| **effective_at** | **datetime** | Optional | The effective datetime from which the Eligible Collateral Schedule applies. Defaults to the beginning of time if not specified, so that the schedule is visible at every effective datetime. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.EligibleCollateralScheduleRequest import EligibleCollateralScheduleRequest

instance = EligibleCollateralScheduleRequest(
    code="...",  # required — The code of the Eligible Collateral Schedule.
    description="...",  # optional — A description of the Eligible Collateral Schedule. Optional.
    rows=[],  # required — The classes of collateral that may be posted, each with the valuation percentage it is accepted at. At least one and at most 200 rows.
    properties=ModelProperty(...),  # optional — A set of properties to decorate onto the Eligible Collateral Schedule. Filterable.
    effective_at=datetime.now()  # optional — The effective datetime from which the Eligible Collateral Schedule applies. Defaults to the beginning of time if not specified, so that the schedule is visible at every effective datetime.
)
```

- [EligibleCollateralRowRequest](EligibleCollateralRowRequest.md) — used in `rows`
- [ModelProperty](ModelProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

