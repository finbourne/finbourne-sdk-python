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
| **details** | **object** | Required | *No description available.* |


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
    details=  # required
)
```

- [Trigger](Trigger.md) — used in `triggers`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

