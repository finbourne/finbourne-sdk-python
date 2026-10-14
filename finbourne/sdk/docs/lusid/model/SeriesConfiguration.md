# SeriesConfiguration

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **share_class_short_code** | **str** | Required | *No description available.* |
| **series_launch_price** | **float** | Optional | *No description available.* |
| **distribution_series_selection** | **str** | Optional | Available values: ProRataByNav, FIFO, SpecifiedSeries. |
| **deal_linked_series** | **bool** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SeriesConfiguration import SeriesConfiguration

instance = SeriesConfiguration(
    share_class_short_code="...",  # required
    series_launch_price=0.0,  # optional
    distribution_series_selection="...",  # optional — Available values: ProRataByNav, FIFO, SpecifiedSeries.
    deal_linked_series=True  # optional
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

