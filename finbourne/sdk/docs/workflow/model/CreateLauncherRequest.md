# CreateLauncherRequest

Contains information for creating a Launcher on a Workflow.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **launcher_id** | **str** | Required | The identifier of the Launcher inside its Workflow |
| **display_name** | **str** | Required | Human-readable name |
| **description** | **str** | Optional | Human-readable description |
| **status** | **str** | Required | The current status of the Launcher. One of - Active, Inactive |
| **launcher_details** | [LauncherDetails](LauncherDetails.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.CreateLauncherRequest import CreateLauncherRequest

instance = CreateLauncherRequest(
    launcher_id="...",  # required — The identifier of the Launcher inside its Workflow
    display_name="...",  # required — Human-readable name
    description="...",  # optional — Human-readable description
    status="...",  # required — The current status of the Launcher. One of - Active, Inactive
    launcher_details=LauncherDetails(...)  # required
)
```

- [LauncherDetails](LauncherDetails.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

