# PerpetualProperty

A perpetual property (i.e. without effective dates) on a Workflow. A property is deleted by supplying a null Finbourne.Workflow.WebApi.Common.Dto.Json.Properties.PerpetualProperty.Value.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **key** | **str** | Required | The property key in the form {domain}/{scope}/{code}. The domain must be &#39;Workflow&#39;. |
| **value** | [PropertyValue](PropertyValue.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.PerpetualProperty import PerpetualProperty

instance = PerpetualProperty(
    key="...",  # required — The property key in the form {domain}/{scope}/{code}. The domain must be &#39;Workflow&#39;.
    value=PropertyValue(...)  # optional
)
```

- [PropertyValue](PropertyValue.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

