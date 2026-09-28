# AllocationMapBasis

How an allocation event is weighted between the participants of an Allocation Map.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **kind** | **str** | Optional | How the event is weighted between the participants. ValueWeighted apportions pro rata to each participant&#39;s value; PropertyWeighted apportions pro rata to the property named in &#39;property&#39;; FixedPercentage apportions by the factors in fixedFactors. Available values: ValueWeighted, PropertyWeighted, FixedPercentage. |
| **var_property** | [ApportionmentMethodProperty](ApportionmentMethodProperty.md) | Optional | *No description available.* |
| **fixed_factors** | [List[AllocationMapFixedFactor]](AllocationMapFixedFactor.md) | Optional | For a FixedPercentage basis, the share of the amount each participating investor record takes. At least one is required under that kind, every factor must be positive, and the factors must sum to 1. |
| **scoped_to_member** | **bool** | Optional | Whether the basis is evaluated only over amounts booked against the structure member rather than fund-wide. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationMapBasis import AllocationMapBasis

instance = AllocationMapBasis(
    kind="...",  # optional — How the event is weighted between the participants. ValueWeighted apportions pro rata to each participant&#39;s value; PropertyWeighted apportions pro rata to the property named in &#39;property&#39;; FixedPercentage apportions by the factors in fixedFactors. Available values: ValueWeighted, PropertyWeighted, FixedPercentage.
    var_property=ApportionmentMethodProperty(...),  # optional
    fixed_factors=[],  # optional — For a FixedPercentage basis, the share of the amount each participating investor record takes. At least one is required under that kind, every factor must be positive, and the factors must sum to 1.
    scoped_to_member=True  # optional — Whether the basis is evaluated only over amounts booked against the structure member rather than fund-wide.
)
```

- [ApportionmentMethodProperty](ApportionmentMethodProperty.md)
- [AllocationMapFixedFactor](AllocationMapFixedFactor.md) — used in `fixed_factors`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

