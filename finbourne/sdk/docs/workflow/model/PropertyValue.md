# PropertyValue

The value of a property. Exactly one of Finbourne.Workflow.WebApi.Common.Dto.Json.Properties.PropertyValue.LabelValue, Finbourne.Workflow.WebApi.Common.Dto.Json.Properties.PropertyValue.MetricValue or Finbourne.Workflow.WebApi.Common.Dto.Json.Properties.PropertyValue.LabelValueSet should be supplied.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **label_value** | **str** | Optional | The value of a text property. |
| **metric_value** | [MetricValue](MetricValue.md) | Optional | *No description available.* |
| **label_value_set** | [LabelValueSet](LabelValueSet.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.PropertyValue import PropertyValue

instance = PropertyValue(
    label_value="...",  # optional — The value of a text property.
    metric_value=MetricValue(...),  # optional
    label_value_set=LabelValueSet(...)  # optional
)
```

- [MetricValue](MetricValue.md)
- [LabelValueSet](LabelValueSet.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

