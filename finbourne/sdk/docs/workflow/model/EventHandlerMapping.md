# EventHandlerMapping

Defines a mapping for event handler properties
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **map_from** | **str** | Optional | The field to map from |
| **set_to** | **str** | Optional | The (constant) value to set |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.EventHandlerMapping import EventHandlerMapping

instance = EventHandlerMapping(
    map_from="...",  # optional — The field to map from
    set_to="..."  # optional — The (constant) value to set
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

