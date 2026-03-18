# MovementSettlementSummary

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Optional | *No description available.* |
| **type** | **str** | Optional | *No description available.* |
| **lusid_instrument_id** | **str** | Optional | *No description available.* |
| **instrument_scope** | **str** | Optional | *No description available.* |
| **settlement_mode** | **str** | Optional | *No description available.* |
| **contractual_settlement_date** | **str** | Optional | *No description available.* |
| **units** | **float** | Optional | *No description available.* |
| **settled_units** | **float** | Optional | *No description available.* |
| **unsettled_units** | **float** | Optional | *No description available.* |
| **overdue_units** | **float** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.MovementSettlementSummary import MovementSettlementSummary

instance = MovementSettlementSummary(
    name="...",  # optional
    type="...",  # optional
    lusid_instrument_id="...",  # optional
    instrument_scope="...",  # optional
    settlement_mode="...",  # optional
    contractual_settlement_date="...",  # optional
    units=0.0,  # optional
    settled_units=0.0,  # optional
    unsettled_units=0.0,  # optional
    overdue_units=0.0  # optional
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

