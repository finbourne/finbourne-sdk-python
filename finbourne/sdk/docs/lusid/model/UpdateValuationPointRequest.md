# UpdateValuationPointRequest

A definition for the period you wish to close
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **diary_entry_code** | **str** | Required | Unique code for the Valuation Point. |
| **diary_entry_variant** | **str** | Required | Optional variant code. Only required when it is necessary to choose between scenarios with multiple estimates. |
| **name** | **str** | Optional | Identifiable Name assigned to the Valuation Point. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of properties for the diary entry. |
| **apply_clear_down** | **bool** | Optional | Defaults to false. Set to true if you want that the closed period to have the clear down applied. |
| **update_inclusion_date_nav_adjustments** | **bool** | Optional | Defaults to false. Set to true if you have the required licence and want the InclusionDate property values to be used to determine whether items should be automatically included in the post close activities. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpdateValuationPointRequest import UpdateValuationPointRequest

instance = UpdateValuationPointRequest(
    diary_entry_code="...",  # required — Unique code for the Valuation Point.
    diary_entry_variant="...",  # required — Optional variant code. Only required when it is necessary to choose between scenarios with multiple estimates.
    name="...",  # optional — Identifiable Name assigned to the Valuation Point.
    properties=ModelProperty(...),  # optional — A set of properties for the diary entry.
    apply_clear_down=True,  # optional — Defaults to false. Set to true if you want that the closed period to have the clear down applied.
    update_inclusion_date_nav_adjustments=True  # optional — Defaults to false. Set to true if you have the required licence and want the InclusionDate property values to be used to determine whether items should be automatically included in the post close activities.
)
```

- [ModelProperty](ModelProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

