# ReturnsEntity

Returns entity, used for configuring the calculation of aggregated returns.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **recipe_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **recipe_entity** | **str** | Optional | Entity a recipe is retrieved from for use in the aggregated returns calculation. Either RecipeId or RecipeEntity must be specified. |
| **fee_handling** | **str** | Optional | Configures how fees are handled in the aggregated returns calculation. |
| **flow_handling** | **str** | Optional | Configures how flows are handled in the aggregated returns calculation. |
| **business_calendar** | **str** | Optional | Calendar used in the aggregated returns calculation. |
| **handle_flow_discrepancy** | **str** | Optional | Configures handling for the case where net flows do not match the sum of tagged flows. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ReturnsEntity import ReturnsEntity

instance = ReturnsEntity(
    id=ResourceId(...),  # required
    recipe_id=ResourceId(...),  # optional
    recipe_entity="...",  # optional — Entity a recipe is retrieved from for use in the aggregated returns calculation. Either RecipeId or RecipeEntity must be specified.
    fee_handling="...",  # optional — Configures how fees are handled in the aggregated returns calculation.
    flow_handling="...",  # optional — Configures how flows are handled in the aggregated returns calculation.
    business_calendar="...",  # optional — Calendar used in the aggregated returns calculation.
    handle_flow_discrepancy="..."  # optional — Configures handling for the case where net flows do not match the sum of tagged flows.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

