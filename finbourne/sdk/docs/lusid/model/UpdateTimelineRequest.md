# UpdateTimelineRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **display_name** | **str** | Required | The name of the Timeline. |
| **description** | **str** | Optional | A description for the Timeline. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | The Timelines properties. These will be from the &#39;Timeline&#39; domain. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpdateTimelineRequest import UpdateTimelineRequest

instance = UpdateTimelineRequest(
    display_name="...",  # required — The name of the Timeline.
    description="...",  # optional — A description for the Timeline.
    properties=ModelProperty(...)  # optional — The Timelines properties. These will be from the &#39;Timeline&#39; domain.
)
```

- [ModelProperty](ModelProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

