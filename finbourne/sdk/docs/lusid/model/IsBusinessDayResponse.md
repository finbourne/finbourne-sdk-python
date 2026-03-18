# IsBusinessDayResponse

Whether or not a DateTimeOffset is a business DateTime
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **requested_date_time** | **datetime** | Required | *No description available.* |
| **is_business_day** | **bool** | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.IsBusinessDayResponse import IsBusinessDayResponse

instance = IsBusinessDayResponse(
    requested_date_time=datetime.now(),  # required
    is_business_day=True  # required
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

