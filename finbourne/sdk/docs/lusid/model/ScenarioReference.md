# ScenarioReference

A reference to a stored Scenario, identified by scope and code, optionally pinned to an AsAt version.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **scope** | **str** | Required | The scope of the scenario to apply. |
| **code** | **str** | Required | The code of the scenario to apply. |
| **as_at** | **datetime** | Optional | The AsAt of the scenario version to apply. If not supplied, the latest version is used. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ScenarioReference import ScenarioReference

instance = ScenarioReference(
    scope="...",  # required — The scope of the scenario to apply.
    code="...",  # required — The code of the scenario to apply.
    as_at=datetime.now()  # optional — The AsAt of the scenario version to apply. If not supplied, the latest version is used.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

