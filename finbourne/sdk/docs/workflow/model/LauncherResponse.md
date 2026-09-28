# LauncherResponse

A Launcher, which starts a run of one Workflow either at the times a schedule gives or when a matching event arrives
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **workflow_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **launcher_id** | **str** | Required | The identifier of this Launcher inside its Workflow |
| **display_name** | **str** | Required | Human-readable name |
| **description** | **str** | Optional | Human-readable description |
| **status** | **str** | Required | The current status of the Launcher. One of - Active, Inactive |
| **launcher_details** | [LauncherDetailsResponse](LauncherDetailsResponse.md) | Required | *No description available.* |
| **summaries** | [LauncherSummaries](LauncherSummaries.md) | Optional | *No description available.* |
| **version** | [VersionInfo](VersionInfo.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.LauncherResponse import LauncherResponse

instance = LauncherResponse(
    workflow_id=ResourceId(...),  # required
    launcher_id="...",  # required — The identifier of this Launcher inside its Workflow
    display_name="...",  # required — Human-readable name
    description="...",  # optional — Human-readable description
    status="...",  # required — The current status of the Launcher. One of - Active, Inactive
    launcher_details=LauncherDetailsResponse(...),  # required
    summaries=LauncherSummaries(...),  # optional
    version=VersionInfo(...)  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [LauncherDetailsResponse](LauncherDetailsResponse.md)
- [LauncherSummaries](LauncherSummaries.md)
- [VersionInfo](VersionInfo.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

