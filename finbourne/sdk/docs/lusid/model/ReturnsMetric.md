# ReturnsMetric

A metric requested from the aggregated-returns (TWR) endpoint. Supports only the  period `Return` (the grid granularity is set on the request via Period, not per metric);  `Alias` is the key the metric appears under in the response's metricsValue dictionary.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Optional | Available values: Return. |
| **alias** | **str** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ReturnsMetric import ReturnsMetric

instance = ReturnsMetric(
    type="...",  # optional — Available values: Return.
    alias="..."  # optional
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

