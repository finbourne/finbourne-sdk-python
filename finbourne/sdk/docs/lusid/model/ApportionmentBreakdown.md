# ApportionmentBreakdown

The apportionment result for one level - the fund (apportioning the non-class-specific P&L across all  share classes) or a single allocation group (apportioning its tagged P&L across its members) - with the  per-member base values and factors the method produced.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **apportionment_level** | **str** | Required | Whether this result is the fund-level apportionment (across all share classes) or an allocation group&#39;s (across its share classes). Available values: Fund, AllocationGroup. |
| **allocation_group_code** | **str** | Optional | The ShareClassShortCode identifying the allocation group this result is for, or null for the fund-level result. |
| **apportionment_method_property_key** | **str** | Required | The apportionment method property key that produced the factors. |
| **factors** | [../model/List[ApportionmentMemberFactor]](ApportionmentMemberFactor.md) | Required | The per-member base values and apportionment factors produced by the method. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ApportionmentBreakdown import ApportionmentBreakdown

instance = ApportionmentBreakdown(
    apportionment_level="...",  # required — Whether this result is the fund-level apportionment (across all share classes) or an allocation group&#39;s (across its share classes). Available values: Fund, AllocationGroup.
    allocation_group_code="...",  # optional — The ShareClassShortCode identifying the allocation group this result is for, or null for the fund-level result.
    apportionment_method_property_key="...",  # required — The apportionment method property key that produced the factors.
    factors=[]  # required — The per-member base values and apportionment factors produced by the method.
)
```

- [ApportionmentMemberFactor](ApportionmentMemberFactor.md) — used in `factors`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

