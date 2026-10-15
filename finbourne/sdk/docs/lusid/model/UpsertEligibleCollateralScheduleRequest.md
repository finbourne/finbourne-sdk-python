# UpsertEligibleCollateralScheduleRequest

The request used to create or replace the definition of an Eligible Collateral Schedule from an effective date.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **description** | **str** | Optional | A description of the Eligible Collateral Schedule. Optional. |
| **rows** | [List[EligibleCollateralRowRequest]](EligibleCollateralRowRequest.md) | Required | The classes of collateral that may be posted, each with the valuation percentage it is accepted at. At least one and at most 200 rows. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of properties to decorate onto the Eligible Collateral Schedule. Filterable. |
| **effective_at** | **datetime** | Optional | The effective datetime or cut label from which the change applies. Defaults to the current LUSID system datetime if not specified. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertEligibleCollateralScheduleRequest import UpsertEligibleCollateralScheduleRequest

instance = UpsertEligibleCollateralScheduleRequest(
    description="...",  # optional — A description of the Eligible Collateral Schedule. Optional.
    rows=[],  # required — The classes of collateral that may be posted, each with the valuation percentage it is accepted at. At least one and at most 200 rows.
    properties=ModelProperty(...),  # optional — A set of properties to decorate onto the Eligible Collateral Schedule. Filterable.
    effective_at=datetime.now()  # optional — The effective datetime or cut label from which the change applies. Defaults to the current LUSID system datetime if not specified.
)
```

- [EligibleCollateralRowRequest](EligibleCollateralRowRequest.md) — used in `rows`
- [ModelProperty](ModelProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

