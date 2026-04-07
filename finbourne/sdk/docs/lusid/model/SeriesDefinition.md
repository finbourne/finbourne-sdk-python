# SeriesDefinition

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **series_identifier** | **str** | Required | The identifier that uniquely identifies this Series within the Share Class. |
| **series_type** | **str** | Required | The type of the Series. Valid values are: Lead, Standard. |
| **launch_date** | **datetime** | Required | The date on which the Series was launched. |
| **launch_price_type** | **str** | Required | The type of launch price for the Series. Valid values are: Manual, Calculated. |
| **dom_ccy** | **str** | Required | The denomination currency of the Series. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | An optional set of properties to associate with the Series. Only applied if createInstrument is set to true on the parent Fund. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SeriesDefinition import SeriesDefinition

instance = SeriesDefinition(
    series_identifier="...",  # required — The identifier that uniquely identifies this Series within the Share Class.
    series_type="...",  # required — The type of the Series. Valid values are: Lead, Standard.
    launch_date=datetime.now(),  # required — The date on which the Series was launched.
    launch_price_type="...",  # required — The type of launch price for the Series. Valid values are: Manual, Calculated.
    dom_ccy="...",  # required — The denomination currency of the Series.
    properties=ModelProperty(...)  # optional — An optional set of properties to associate with the Series. Only applied if createInstrument is set to true on the parent Fund.
)
```

- [ModelProperty](ModelProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

