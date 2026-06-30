# MetricValue

The numeric value of a metric property, with an optional unit.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **value** | **float** | Optional | The numerical value of the property. |
| **unit** | **str** | Optional | The unit identifier for the value. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.MetricValue import MetricValue

instance = MetricValue(
    value=0.0,  # optional — The numerical value of the property.
    unit="..."  # optional — The unit identifier for the value.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

