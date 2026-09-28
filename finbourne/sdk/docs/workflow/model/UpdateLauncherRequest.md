# UpdateLauncherRequest

Contains information for updating a Launcher on a Workflow.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **display_name** | **str** | Required | Human-readable name |
| **description** | **str** | Optional | Human-readable description |
| **status** | **str** | Required | The current status of the Launcher. One of - Active, Inactive |
| **launcher_details** | [LauncherDetails](LauncherDetails.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.UpdateLauncherRequest import UpdateLauncherRequest

instance = UpdateLauncherRequest(
    display_name="...",  # required — Human-readable name
    description="...",  # optional — Human-readable description
    status="...",  # required — The current status of the Launcher. One of - Active, Inactive
    launcher_details=LauncherDetails(...)  # required
)
```

- [LauncherDetails](LauncherDetails.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

