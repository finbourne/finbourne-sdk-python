# PropertyValue

The value of the property.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **label_value** | **str** | Optional | The text value of a property defined as having the &#39;Label&#39; type. |
| **metric_value** | [MetricValue](MetricValue.md) | Optional | *No description available.* |
| **label_value_set** | [LabelValueSet](LabelValueSet.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PropertyValue import PropertyValue

instance = PropertyValue(
    label_value="...",  # optional — The text value of a property defined as having the &#39;Label&#39; type.
    metric_value=MetricValue(...),  # optional
    label_value_set=LabelValueSet(...)  # optional
)
```

- [MetricValue](MetricValue.md)
- [LabelValueSet](LabelValueSet.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

