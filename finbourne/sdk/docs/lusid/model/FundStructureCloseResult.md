# FundStructureCloseResult

The outcome of closing a fund structure: one step per member in the order they were closed.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **structure_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **valuation_point_code** | **str** | Required | The code of the valuation point to finalise on every member fund. |
| **steps** | [List[FundStructureCloseStep]](FundStructureCloseStep.md) | Required | The finalisation of each member, in the order attempted. |
| **completed** | **bool** | Required | Whether every member finalised. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundStructureCloseResult import FundStructureCloseResult

instance = FundStructureCloseResult(
    structure_id=ResourceId(...),  # required
    valuation_point_code="...",  # required — The code of the valuation point to finalise on every member fund.
    steps=[],  # required — The finalisation of each member, in the order attempted.
    completed=True  # required — Whether every member finalised.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [FundStructureCloseStep](FundStructureCloseStep.md) — used in `steps`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

