# UpsertValuationPointRequest

A definition for the period you wish to close
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **diary_entry_code** | **str** | Required | Unique code for the Valuation Point. |
| **diary_entry_variant** | **str** | Optional | Optional variant code. Only required when it is necessary to choose between scenarios with multiple estimates. |
| **name** | **str** | Optional | Identifiable Name assigned to the Valuation Point. |
| **effective_at** | **datetime** | Required | The effective time of the diary entry. |
| **query_as_at** | **datetime** | Optional | The query time of the diary entry. Defaults to latest. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of properties for the diary entry. |
| **apply_clear_down** | **bool** | Optional | Defaults to false. Set to true if you want that the closed period to have the clear down applied. |
| **holdings_as_at_override** | **datetime** | Optional | The optional AsAt Override to use for building holdings in the Valuation Point. Defaults to Latest. |
| **valuations_as_at_override** | **datetime** | Optional | The optional AsAt Override to use for performing valuations in the Valuation Point. Defaults to Latest. |
| **update_inclusion_date_nav_adjustments** | **bool** | Optional | Defaults to false. Set to true if you have the required licence and want the InclusionDate property values to be used to determine whether items should be automatically included in the post close activities. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertValuationPointRequest import UpsertValuationPointRequest

instance = UpsertValuationPointRequest(
    diary_entry_code="...",  # required — Unique code for the Valuation Point.
    diary_entry_variant="...",  # optional — Optional variant code. Only required when it is necessary to choose between scenarios with multiple estimates.
    name="...",  # optional — Identifiable Name assigned to the Valuation Point.
    effective_at=datetime.now(),  # required — The effective time of the diary entry.
    query_as_at=datetime.now(),  # optional — The query time of the diary entry. Defaults to latest.
    properties=ModelProperty(...),  # optional — A set of properties for the diary entry.
    apply_clear_down=True,  # optional — Defaults to false. Set to true if you want that the closed period to have the clear down applied.
    holdings_as_at_override=datetime.now(),  # optional — The optional AsAt Override to use for building holdings in the Valuation Point. Defaults to Latest.
    valuations_as_at_override=datetime.now(),  # optional — The optional AsAt Override to use for performing valuations in the Valuation Point. Defaults to Latest.
    update_inclusion_date_nav_adjustments=True  # optional — Defaults to false. Set to true if you have the required licence and want the InclusionDate property values to be used to determine whether items should be automatically included in the post close activities.
)
```

- [ModelProperty](ModelProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

