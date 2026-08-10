# AllocationGroup

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **classes** | [../model/List[AllocationGroupClass]](AllocationGroupClass.md) | Optional | An optional list of share classes that belong to this group. Each entry must reference a ShareClass already present on the Fund. You can provide this or the Formula, but not both. |
| **name** | **str** | Required | The display name of the Allocation Group. |
| **description** | **str** | Optional | An optional description for the Allocation Group. |
| **share_class_short_code** | **str** | Required | The short code that identifies the Allocation Group. |
| **apportionment_method_property** | [../model/ApportionmentMethodProperty](ApportionmentMethodProperty.md) | Optional | *No description available.* |
| **formula** | **str** | Optional | An optional filter expression used to define which classes belong to this group, based on fund grouping criteria. You can provide this or the Classes, but not both. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationGroup import AllocationGroup

instance = AllocationGroup(
    classes=[],  # optional — An optional list of share classes that belong to this group. Each entry must reference a ShareClass already present on the Fund. You can provide this or the Formula, but not both.
    name="...",  # required — The display name of the Allocation Group.
    description="...",  # optional — An optional description for the Allocation Group.
    share_class_short_code="...",  # required — The short code that identifies the Allocation Group.
    apportionment_method_property=ApportionmentMethodProperty(...),  # optional
    formula="..."  # optional — An optional filter expression used to define which classes belong to this group, based on fund grouping criteria. You can provide this or the Classes, but not both.
)
```


## Related Models

- [AllocationGroupClass](AllocationGroupClass.md) — used in `classes`
- [ApportionmentMethodProperty](ApportionmentMethodProperty.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

