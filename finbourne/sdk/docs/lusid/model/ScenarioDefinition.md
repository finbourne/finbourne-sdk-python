# ScenarioDefinition

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **scope** | **str** | Required | *No description available.* |
| **code** | **str** | Required | *No description available.* |
| **display_name** | **str** | Optional | *No description available.* |
| **description** | **str** | Optional | *No description available.* |
| **shifts** | [../model/List[ScenarioShiftDefinition]](ScenarioShiftDefinition.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ScenarioDefinition import ScenarioDefinition

instance = ScenarioDefinition(
    scope="...",  # required
    code="...",  # required
    display_name="...",  # optional
    description="...",  # optional
    shifts=[]  # optional
)
```

- [ScenarioShiftDefinition](ScenarioShiftDefinition.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

