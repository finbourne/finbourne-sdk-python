# SettlementCycle

The settlement cycle for an instrument
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **business_day_offset** | **int** | Required | *No description available.* |
| **calendars** | [List[ResourceId]](ResourceId.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SettlementCycle import SettlementCycle

instance = SettlementCycle(
    business_day_offset=0,  # required
    calendars=[]  # required
)
```

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

