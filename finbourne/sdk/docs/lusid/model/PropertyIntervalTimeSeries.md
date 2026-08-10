# PropertyIntervalTimeSeries

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **key** | **str** | Required | The property key that this time series belongs to. |
| **values** | [../model/List[PropertyInterval]](PropertyInterval.md) | Required | The complete time series (history) of intervals for the property key. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PropertyIntervalTimeSeries import PropertyIntervalTimeSeries

instance = PropertyIntervalTimeSeries(
    key="...",  # required — The property key that this time series belongs to.
    values=[]  # required — The complete time series (history) of intervals for the property key.
)
```

- [PropertyInterval](PropertyInterval.md) — used in `values`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

