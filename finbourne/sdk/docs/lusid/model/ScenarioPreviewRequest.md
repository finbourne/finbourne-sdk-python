# ScenarioPreviewRequest

Request to preview a scenario against a portfolio's market data without running a valuation: the  portfolio's market data dependencies are resolved and the scenario's shifts applied, and the  response reports which targets each shift changed (with values before and after) and which market  data was skipped. Supply either a reference to a stored scenario or inline shift definitions  (for previewing a definition before saving it), not both.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **recipe_id** | [../model/ResourceId](ResourceId.md) | Required | *No description available.* |
| **portfolio_entity_ids** | [../model/List[PortfolioEntityId]](PortfolioEntityId.md) | Required | The portfolios whose market data dependencies the scenario is previewed against. |
| **effective_at** | **datetime** | Required | The effective date to resolve market data at. |
| **as_at** | **datetime** | Optional | The as-at time to resolve at. Defaults to the latest. |
| **scenario** | [../model/ScenarioReference](ScenarioReference.md) | Optional | *No description available.* |
| **shifts** | [../model/List[ScenarioShiftDefinition]](ScenarioShiftDefinition.md) | Optional | Inline shift definitions to preview without saving a scenario, e.g. to test what a definition  would match while authoring it. Mutually exclusive with supplying a stored scenario reference. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ScenarioPreviewRequest import ScenarioPreviewRequest

instance = ScenarioPreviewRequest(
    recipe_id=ResourceId(...),  # required
    portfolio_entity_ids=[],  # required — The portfolios whose market data dependencies the scenario is previewed against.
    effective_at=datetime.now(),  # required — The effective date to resolve market data at.
    as_at=datetime.now(),  # optional — The as-at time to resolve at. Defaults to the latest.
    scenario=ScenarioReference(...),  # optional
    shifts=[]  # optional — Inline shift definitions to preview without saving a scenario, e.g. to test what a definition  would match while authoring it. Mutually exclusive with supplying a stored scenario reference.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [PortfolioEntityId](PortfolioEntityId.md) — used in `portfolio_entity_ids`
- [ScenarioReference](ScenarioReference.md)
- [ScenarioShiftDefinition](ScenarioShiftDefinition.md) — used in `shifts`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

