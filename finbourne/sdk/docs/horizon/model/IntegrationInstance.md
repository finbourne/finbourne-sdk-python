# IntegrationInstance

Response containing an integration instance.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | **str** | Required | Identifies the instance within the integration. |
| **integration_type** | **str** | Required | The integration type. |
| **name** | **str** | Required | Name of the instance. |
| **description** | **str** | Required | Description of the instance. |
| **enabled** | **bool** | Required | If true the instance will be executed if its trigger is satisfied. |
| **triggers** | [List[Trigger]](Trigger.md) | Required | Defines what triggers execution of the instance. |
| **details** | **object** | Required | Base DTO type of an integration configuration specific to the integration type.              N.B. ASP.NET Core model validation is normally applied automatically when [ApiController] is added to a controller, however it doesn&#39;t work here with the polymorphic integration subtypes of this class (see https://github.com/dotnet/aspnetcore/issues/27882). The workaround here is to implement the IValidatableObject interface and each subtype must call Validate() or ValidateContents() on its properties (the validation is not recursive).  Located in Horizon.Integrations.Web so both specific integration projects and Horizon.WebApi can reference it. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.IntegrationInstance import IntegrationInstance

instance = IntegrationInstance(
    id="...",  # required — Identifies the instance within the integration.
    integration_type="...",  # required — The integration type.
    name="...",  # required — Name of the instance.
    description="...",  # required — Description of the instance.
    enabled=True,  # required — If true the instance will be executed if its trigger is satisfied.
    triggers=[],  # required — Defines what triggers execution of the instance.
    details=  # required — Base DTO type of an integration configuration specific to the integration type.              N.B. ASP.NET Core model validation is normally applied automatically when [ApiController] is added to a controller, however it doesn&#39;t work here with the polymorphic integration subtypes of this class (see https://github.com/dotnet/aspnetcore/issues/27882). The workaround here is to implement the IValidatableObject interface and each subtype must call Validate() or ValidateContents() on its properties (the validation is not recursive).  Located in Horizon.Integrations.Web so both specific integration projects and Horizon.WebApi can reference it.
)
```

- [Trigger](Trigger.md) — used in `triggers`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

