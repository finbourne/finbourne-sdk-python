# ResolveTenorsResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **start_date** | **datetime** | Required | *No description available.* |
| **spot_date** | **datetime** | Required | *No description available.* |
| **eom_rule_applied** | **bool** | Required | *No description available.* |
| **dates** | **Dict[str, datetime]** | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ResolveTenorsResponse import ResolveTenorsResponse

instance = ResolveTenorsResponse(
    start_date=datetime.now(),  # required
    spot_date=datetime.now(),  # required
    eom_rule_applied=True,  # required
    dates=  # required
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

