# CreateInstanceRequest

A request to add a new instance to an integration.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instance_optional_props** | [Dict[str, LusidPropertyDefinitionOverridesByType]](LusidPropertyDefinitionOverridesByType.md) | Optional | *No description available.* |
| **integration_type** | **str** | Required | *No description available.* |
| **name** | **str** | Required | *No description available.* |
| **description** | **str** | Required | *No description available.* |
| **enabled** | **bool** | Required | *No description available.* |
| **triggers** | [List[Trigger]](Trigger.md) | Required | *No description available.* |
| **details** | **object** | Required | Base DTO type of an integration configuration specific to the integration type.              N.B. ASP.NET Core model validation is normally applied automatically when [ApiController] is added to a controller, however it doesn&#39;t work here with the polymorphic integration subtypes of this class (see https://github.com/dotnet/aspnetcore/issues/27882). The workaround here is to implement the IValidatableObject interface and each subtype must call Validate() or ValidateContents() on its properties (the validation is not recursive).  Located in Horizon.Integrations.Web so both specific integration projects and Horizon.WebApi can reference it. |
| **post_process_tasks** | [List[PostProcessTask]](PostProcessTask.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.CreateInstanceRequest import CreateInstanceRequest

instance = CreateInstanceRequest(
    instance_optional_props=LusidPropertyDefinitionOverridesByType(...),  # optional
    integration_type="...",  # required
    name="...",  # required
    description="...",  # required
    enabled=True,  # required
    triggers=[],  # required
    details=,  # required — Base DTO type of an integration configuration specific to the integration type.              N.B. ASP.NET Core model validation is normally applied automatically when [ApiController] is added to a controller, however it doesn&#39;t work here with the polymorphic integration subtypes of this class (see https://github.com/dotnet/aspnetcore/issues/27882). The workaround here is to implement the IValidatableObject interface and each subtype must call Validate() or ValidateContents() on its properties (the validation is not recursive).  Located in Horizon.Integrations.Web so both specific integration projects and Horizon.WebApi can reference it.
    post_process_tasks=[]  # required
)
```


## Related Models

- [LusidPropertyDefinitionOverridesByType](LusidPropertyDefinitionOverridesByType.md)
- [Trigger](Trigger.md)
- [PostProcessTask](PostProcessTask.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

