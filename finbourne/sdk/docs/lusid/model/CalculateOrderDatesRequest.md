# CalculateOrderDatesRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instrument_identifier_type** | **str** | Required | *No description available.* |
| **instrument_identifier** | **str** | Required | *No description available.* |
| **instrument_scope** | **str** | Optional | *No description available.* |
| **received_date** | **datetime** | Optional | *No description available.* |
| **price_date** | **datetime** | Optional | *No description available.* |
| **transaction_category** | **str** | Optional | *No description available.* |
| **liquidating_share_class_identifier** | **str** | Optional | *No description available.* |
| **liquidating_share_class_identifier_type** | **str** | Optional | *No description available.* |
| **liquidating_share_class_instrument_scope** | **str** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CalculateOrderDatesRequest import CalculateOrderDatesRequest

instance = CalculateOrderDatesRequest(
    instrument_identifier_type="...",  # required
    instrument_identifier="...",  # required
    instrument_scope="...",  # optional
    received_date=datetime.now(),  # optional
    price_date=datetime.now(),  # optional
    transaction_category="...",  # optional
    liquidating_share_class_identifier="...",  # optional
    liquidating_share_class_identifier_type="...",  # optional
    liquidating_share_class_instrument_scope="..."  # optional
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

