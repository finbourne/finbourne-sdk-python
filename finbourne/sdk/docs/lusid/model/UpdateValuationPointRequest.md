# UpdateValuationPointRequest

A definition for the period you wish to close
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **valuation_point_code** | **str** | Required | Unique code for the Valuation Point. |
| **variant** | **str** | Optional | Optional variant code. Only required when it is necessary to choose between scenarios with multiple estimates. |
| **name** | **str** | Optional | Identifiable Name assigned to the Valuation Point. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of properties for the diary entry. |
| **apply_clear_down** | **bool** | Optional | Defaults to null. Set to true if you want the closed period to have the clear down applied. |
| **update_inclusion_date_nav_adjustments** | **bool** | Optional | Defaults to null. Set to true if you have the required licence and want the InclusionDate property values to be used to determine whether items should be automatically included in the post close activities. |
| **pricing_methodology_override** | [PricingMethodologyOverrideRequest](PricingMethodologyOverrideRequest.md) | Optional | *No description available.* |
| **bucket_set_seeds** | [List[BucketSetSeedRequest]](BucketSetSeedRequest.md) | Optional | Defaults to null. The closing balances to seed for bucket sets at this estimate valuation point, at most one per bucket set. They replace the seeds this variant of the valuation point had, and none removes them. Null leaves them as they are. While the valuation point is an estimate, each seeded bucket set&#39;s flow bucket values are its seed; finalising the valuation point stores them, and the next valuation point opens from them. A bucket set can only be seeded when the previous final valuation point has no values for it. The seed is trusted input: it is not reconciled to the share class NAVs. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpdateValuationPointRequest import UpdateValuationPointRequest

instance = UpdateValuationPointRequest(
    valuation_point_code="...",  # required — Unique code for the Valuation Point.
    variant="...",  # optional — Optional variant code. Only required when it is necessary to choose between scenarios with multiple estimates.
    name="...",  # optional — Identifiable Name assigned to the Valuation Point.
    properties=ModelProperty(...),  # optional — A set of properties for the diary entry.
    apply_clear_down=True,  # optional — Defaults to null. Set to true if you want the closed period to have the clear down applied.
    update_inclusion_date_nav_adjustments=True,  # optional — Defaults to null. Set to true if you have the required licence and want the InclusionDate property values to be used to determine whether items should be automatically included in the post close activities.
    pricing_methodology_override=PricingMethodologyOverrideRequest(...),  # optional
    bucket_set_seeds=[]  # optional — Defaults to null. The closing balances to seed for bucket sets at this estimate valuation point, at most one per bucket set. They replace the seeds this variant of the valuation point had, and none removes them. Null leaves them as they are. While the valuation point is an estimate, each seeded bucket set&#39;s flow bucket values are its seed; finalising the valuation point stores them, and the next valuation point opens from them. A bucket set can only be seeded when the previous final valuation point has no values for it. The seed is trusted input: it is not reconciled to the share class NAVs.
)
```

- [ModelProperty](ModelProperty.md) — used in `properties`
- [PricingMethodologyOverrideRequest](PricingMethodologyOverrideRequest.md)
- [BucketSetSeedRequest](BucketSetSeedRequest.md) — used in `bucket_set_seeds`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

