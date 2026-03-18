# SettlementSchedule

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **trade_id** | **str** | Optional | *No description available.* |
| **settlement_date** | **datetime** | Optional | *No description available.* |
| **units** | **float** | Optional | *No description available.* |
| **bond_interest** | **float** | Optional | *No description available.* |
| **movement_name** | **str** | Optional | *No description available.* |
| **movement_type** | **str** | Optional | *No description available.* |
| **unsettled_units** | **float** | Optional | *No description available.* |
| **overdue_units** | **float** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SettlementSchedule import SettlementSchedule

instance = SettlementSchedule(
    trade_id="...",  # optional
    settlement_date=datetime.now(),  # optional
    units=0.0,  # optional
    bond_interest=0.0,  # optional
    movement_name="...",  # optional
    movement_type="...",  # optional
    unsettled_units=0.0,  # optional
    overdue_units=0.0  # optional
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

