# EstimateVariant

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **variant** | **str** | Optional | The Variant of the Calendar Entry. Together with the valuation point code marks the unique branch for the NavType. |
| **display_name** | **str** | Required | The name of the Fund Calendar entry. |
| **description** | **str** | Optional | A description for the Fund Calendar entry. |
| **as_at** | **datetime** | Required | The asAt datetime for the Calendar Entry. |
| **holdings_as_at_override** | **datetime** | Optional | The optional AsAt Override to use for building holdings in the Valuation Point. Defaults to QueryAsAt. |
| **valuations_as_at_override** | **datetime** | Optional | The optional AsAt Override to use for performing valuations in the Valuation Point. Defaults to QueryAsAt. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | The properties for the Calendar Entry. These will be from the &#39;ClosedPeriod&#39; domain. |
| **version** | [Version](Version.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.EstimateVariant import EstimateVariant

instance = EstimateVariant(
    variant="...",  # optional — The Variant of the Calendar Entry. Together with the valuation point code marks the unique branch for the NavType.
    display_name="...",  # required — The name of the Fund Calendar entry.
    description="...",  # optional — A description for the Fund Calendar entry.
    as_at=datetime.now(),  # required — The asAt datetime for the Calendar Entry.
    holdings_as_at_override=datetime.now(),  # optional — The optional AsAt Override to use for building holdings in the Valuation Point. Defaults to QueryAsAt.
    valuations_as_at_override=datetime.now(),  # optional — The optional AsAt Override to use for performing valuations in the Valuation Point. Defaults to QueryAsAt.
    properties=ModelProperty(...),  # optional — The properties for the Calendar Entry. These will be from the &#39;ClosedPeriod&#39; domain.
    version=Version(...)  # required
)
```

- [ModelProperty](ModelProperty.md) — used in `properties`
- [Version](Version.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

