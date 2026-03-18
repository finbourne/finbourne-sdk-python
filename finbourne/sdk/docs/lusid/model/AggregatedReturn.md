# AggregatedReturn

A list of Aggregated Returns.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **effective_at** | **datetime** | Required | The effectiveAt for the return. |
| **end_of_period** | **datetime** | Required | The end of period date. For the monthly period this will be the Month End Date. |
| **opening_market_value** | **float** | Optional | The opening market value. |
| **closing_market_value** | **float** | Optional | The closing market value. |
| **metrics_value** | **Dict[str, float]** | Required | The value for the specified metric. |
| **frequency** | **str** | Optional | Show the aggregated output returns on a Daily or Monthly period. |
| **composite_members** | **int** | Optional | The number of members in the Composite on the given day. |
| **composite_members_without_return** | [List[ResourceId]](ResourceId.md) | Optional | List containing Composite members which post no return on the given day. |
| **warnings** | **List[str]** | Optional | List of the warnings about the calculation of the aggregated return. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AggregatedReturn import AggregatedReturn

instance = AggregatedReturn(
    effective_at=datetime.now(),  # required — The effectiveAt for the return.
    end_of_period=datetime.now(),  # required — The end of period date. For the monthly period this will be the Month End Date.
    opening_market_value=0.0,  # optional — The opening market value.
    closing_market_value=0.0,  # optional — The closing market value.
    metrics_value=,  # required — The value for the specified metric.
    frequency="...",  # optional — Show the aggregated output returns on a Daily or Monthly period.
    composite_members=0,  # optional — The number of members in the Composite on the given day.
    composite_members_without_return=[],  # optional — List containing Composite members which post no return on the given day.
    warnings=  # optional — List of the warnings about the calculation of the aggregated return.
)
```

- [ResourceId](ResourceId.md) — used in `composite_members_without_return`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

