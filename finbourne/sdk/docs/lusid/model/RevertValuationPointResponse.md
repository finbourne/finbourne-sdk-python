# RevertValuationPointResponse

A Valuation Point reverted to Estimate, with all of its variants. Any variant that finalising the Valuation Point  had rejected is brought back as an Estimate by the revert, and is reported here alongside it.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **valuation_point_code** | **str** | Optional | The code of the Valuation Point. |
| **nav_type_code** | **str** | Optional | The navTypeCode of the Fund Calendar Entry. This is the code of the NAV type that this Calendar Entry is associated with. |
| **status** | **str** | Required | The status of the Valuation Point. Available values: Undefined, Estimate, Final, Candidate, Rejected, Unofficial. |
| **apply_clear_down** | **bool** | Optional | Indicates whether a clear down was applied when the Valuation Point was created. |
| **effective_at** | **datetime** | Required | The effective time of the Valuation Point. |
| **previous** | [PreviousValuationPoint](PreviousValuationPoint.md) | Optional | *No description available.* |
| **variants** | [List[EstimateVariant]](EstimateVariant.md) | Optional | The variants of the Estimate Valuation Point.  |
| **staged_modifications** | [StagedModificationsInfo](StagedModificationsInfo.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RevertValuationPointResponse import RevertValuationPointResponse

instance = RevertValuationPointResponse(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    valuation_point_code="...",  # optional — The code of the Valuation Point.
    nav_type_code="...",  # optional — The navTypeCode of the Fund Calendar Entry. This is the code of the NAV type that this Calendar Entry is associated with.
    status="...",  # required — The status of the Valuation Point. Available values: Undefined, Estimate, Final, Candidate, Rejected, Unofficial.
    apply_clear_down=True,  # optional — Indicates whether a clear down was applied when the Valuation Point was created.
    effective_at=datetime.now(),  # required — The effective time of the Valuation Point.
    previous=PreviousValuationPoint(...),  # optional
    variants=[],  # optional — The variants of the Estimate Valuation Point. 
    staged_modifications=StagedModificationsInfo(...),  # optional
    links=[]  # optional
)
```

- [PreviousValuationPoint](PreviousValuationPoint.md)
- [EstimateVariant](EstimateVariant.md) — used in `variants`
- [StagedModificationsInfo](StagedModificationsInfo.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

