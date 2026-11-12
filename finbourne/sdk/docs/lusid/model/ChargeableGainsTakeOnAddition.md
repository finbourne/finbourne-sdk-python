# ChargeableGainsTakeOnAddition

One acquisition added to a taken-on 1982 holding since 31 March 1982, carried as its own record inside the holding
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **var_date** | **datetime** | Required | *No description available.* |
| **cost** | **float** | Required | *No description available.* |
| **indexation** | **float** | Required | *No description available.* |
| **paid_cost** | **float** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ChargeableGainsTakeOnAddition import ChargeableGainsTakeOnAddition

instance = ChargeableGainsTakeOnAddition(
    var_date=datetime.now(),  # required
    cost=0.0,  # required
    indexation=0.0,  # required
    paid_cost=0.0  # optional
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

