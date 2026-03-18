# UpdateCutLabelDefinitionRequest

This request specifies a new Cut Label Definition
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **display_name** | **str** | Required | *No description available.* |
| **description** | **str** | Optional | *No description available.* |
| **cut_local_time** | [CutLocalTime](CutLocalTime.md) | Required | *No description available.* |
| **time_zone** | **str** | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpdateCutLabelDefinitionRequest import UpdateCutLabelDefinitionRequest

instance = UpdateCutLabelDefinitionRequest(
    display_name="...",  # required
    description="...",  # optional
    cut_local_time=CutLocalTime(...),  # required
    time_zone="..."  # required
)
```

- [CutLocalTime](CutLocalTime.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

