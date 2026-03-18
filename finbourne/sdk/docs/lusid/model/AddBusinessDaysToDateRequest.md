# AddBusinessDaysToDateRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **business_day_offset** | **int** | Required | *No description available.* |
| **holiday_codes** | **List[str]** | Required | *No description available.* |
| **start_date** | **datetime** | Optional | *No description available.* |
| **as_at** | **datetime** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AddBusinessDaysToDateRequest import AddBusinessDaysToDateRequest

instance = AddBusinessDaysToDateRequest(
    business_day_offset=0,  # required
    holiday_codes=,  # required
    start_date=datetime.now(),  # optional
    as_at=datetime.now()  # optional
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

