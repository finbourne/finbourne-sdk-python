# IntegrationInstanceResponse

Response representing an integration instance.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | **str** | Required | The unique identifier of the integration instance. |
| **integration_type** | **str** | Required | The type of the integration. |
| **name** | **str** | Required | The name of the integration instance. |
| **description** | **str** | Required | The description of the integration instance. |
| **enabled** | **bool** | Required | Whether the integration instance is enabled. |
| **triggers** | [List[Trigger]](Trigger.md) | Required | The triggers associated with the integration instance. |
| **details** | **object** | Required | Base DTO type of an integration configuration specific to the integration type.              N.B. ASP.NET Core model validation is normally applied automatically when [ApiController] is added to a controller, however it doesn&#39;t work here with the polymorphic integration subtypes of this class (see https://github.com/dotnet/aspnetcore/issues/27882). The workaround here is to implement the IValidatableObject interface and each subtype must call Validate() or ValidateContents() on its properties (the validation is not recursive).  Located in Horizon.Integrations.Web so both specific integration projects and Horizon.WebApi can reference it. |
| **post_process_tasks** | [List[PostProcessTask]](PostProcessTask.md) | Required | The post process tasks associated with the integration instance. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.IntegrationInstanceResponse import IntegrationInstanceResponse

instance = IntegrationInstanceResponse(
    id="...",  # required — The unique identifier of the integration instance.
    integration_type="...",  # required — The type of the integration.
    name="...",  # required — The name of the integration instance.
    description="...",  # required — The description of the integration instance.
    enabled=True,  # required — Whether the integration instance is enabled.
    triggers=[],  # required — The triggers associated with the integration instance.
    details=,  # required — Base DTO type of an integration configuration specific to the integration type.              N.B. ASP.NET Core model validation is normally applied automatically when [ApiController] is added to a controller, however it doesn&#39;t work here with the polymorphic integration subtypes of this class (see https://github.com/dotnet/aspnetcore/issues/27882). The workaround here is to implement the IValidatableObject interface and each subtype must call Validate() or ValidateContents() on its properties (the validation is not recursive).  Located in Horizon.Integrations.Web so both specific integration projects and Horizon.WebApi can reference it.
    post_process_tasks=[]  # required — The post process tasks associated with the integration instance.
)
```

- [Trigger](Trigger.md) — used in `triggers`
- [PostProcessTask](PostProcessTask.md) — used in `post_process_tasks`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

