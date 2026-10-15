# MarginSettlementLag

Business days between a margin call and settlement, by asset kind.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **cash** | **int** | Required | The business days between a cash margin call and settlement. |
| **securities** | **int** | Required | The business days between a securities margin call and settlement. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.MarginSettlementLag import MarginSettlementLag

instance = MarginSettlementLag(
    cash=0,  # required — The business days between a cash margin call and settlement.
    securities=0  # required — The business days between a securities margin call and settlement.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

