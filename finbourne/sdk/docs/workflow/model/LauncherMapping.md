# LauncherMapping

A value a Launcher either gives as it is or takes from somewhere.              Exactly one of Finbourne.Workflow.WebApi.Common.Dto.Json.Launchers.LauncherMapping.SetTo or Finbourne.Workflow.WebApi.Common.Dto.Json.Launchers.LauncherMapping.MapFrom must be given. Only an Event Launcher has an event to take a value from, so a Schedule Launcher can only use Finbourne.Workflow.WebApi.Common.Dto.Json.Launchers.LauncherMapping.SetTo
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **set_to** | **str** | Optional | The value to use, given as it is |
| **map_from** | **str** | Optional | The path the value is taken from, for example header.userId |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.LauncherMapping import LauncherMapping

instance = LauncherMapping(
    set_to="...",  # optional — The value to use, given as it is
    map_from="..."  # optional — The path the value is taken from, for example header.userId
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

