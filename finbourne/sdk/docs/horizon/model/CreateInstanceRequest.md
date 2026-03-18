# CreateInstanceRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instance_optional_props** | [Dict[str, LusidPropertyDefinitionOverridesByType]](LusidPropertyDefinitionOverridesByType.md) | Optional | *No description available.* |
| **integration_type** | **str** | Required | *No description available.* |
| **name** | **str** | Required | *No description available.* |
| **description** | **str** | Required | *No description available.* |
| **enabled** | **bool** | Required | *No description available.* |
| **triggers** | [List[Trigger]](Trigger.md) | Required | *No description available.* |
| **details** | **object** | Required | *No description available.* |
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
    details=,  # required
    post_process_tasks=[]  # required
)
```


## Related Models

- [LusidPropertyDefinitionOverridesByType](LusidPropertyDefinitionOverridesByType.md)
- [Trigger](Trigger.md)
- [PostProcessTask](PostProcessTask.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

