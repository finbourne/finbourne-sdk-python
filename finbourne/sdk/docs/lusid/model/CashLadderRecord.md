# CashLadderRecord

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **effective_date** | **datetime** | Optional | *No description available.* |
| **open** | **float** | Required | *No description available.* |
| **activities** | **Dict[str, float]** | Required | *No description available.* |
| **close** | **float** | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CashLadderRecord import CashLadderRecord

instance = CashLadderRecord(
    effective_date=datetime.now(),  # optional
    open=0.0,  # required
    activities=,  # required
    close=0.0  # required
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

