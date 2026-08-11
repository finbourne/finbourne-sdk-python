# HoldingContributor

A list of transactions contributed to a holding.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **transaction** | [Transaction](Transaction.md) | Required | *No description available.* |
| **holding_id** | **int** | Optional | The unique holding identifier |
| **movements** | [List[MovementSettlementSummary]](MovementSettlementSummary.md) | Optional | Movements contributed to holding |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.HoldingContributor import HoldingContributor

instance = HoldingContributor(
    transaction=Transaction(...),  # required
    holding_id=0,  # optional — The unique holding identifier
    movements=[]  # optional — Movements contributed to holding
)
```


## Related Models

- [Transaction](Transaction.md)
- [MovementSettlementSummary](MovementSettlementSummary.md) — used in `movements`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

