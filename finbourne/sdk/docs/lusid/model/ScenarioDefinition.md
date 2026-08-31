# ScenarioDefinition

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **scope** | **str** | Required | *No description available.* |
| **code** | **str** | Required | *No description available.* |
| **display_name** | **str** | Optional | *No description available.* |
| **description** | **str** | Optional | *No description available.* |
| **short_code** | **str** | Optional | A short, memorable identifier for the scenario, for use in reporting. Optional on upsert:  when omitted, reads return a value inferred from the display name (falling back to the  code) rather than null; the inferred value is computed fresh on every read and is never  persisted. When supplied, the value is stored and returned verbatim. Independent of  scenarioType. |
| **scenario_type** | **str** | Required | Classifies the scenario. Required on upsert; supported string (enumeration) values are:  [Historical, Regulatory, Hypothetical]. Independent of shortCode. Available values: Historical, Regulatory, Hypothetical. |
| **shifts** | [List[ScenarioShiftDefinition]](ScenarioShiftDefinition.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ScenarioDefinition import ScenarioDefinition

instance = ScenarioDefinition(
    scope="...",  # required
    code="...",  # required
    display_name="...",  # optional
    description="...",  # optional
    short_code="...",  # optional — A short, memorable identifier for the scenario, for use in reporting. Optional on upsert:  when omitted, reads return a value inferred from the display name (falling back to the  code) rather than null; the inferred value is computed fresh on every read and is never  persisted. When supplied, the value is stored and returned verbatim. Independent of  scenarioType.
    scenario_type="...",  # required — Classifies the scenario. Required on upsert; supported string (enumeration) values are:  [Historical, Regulatory, Hypothetical]. Independent of shortCode. Available values: Historical, Regulatory, Hypothetical.
    shifts=[]  # optional
)
```

- [ScenarioShiftDefinition](ScenarioShiftDefinition.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

