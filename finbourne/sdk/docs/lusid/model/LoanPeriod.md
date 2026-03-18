# LoanPeriod

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **payment_date** | **datetime** | Required | *No description available.* |
| **notional** | **float** | Required | *No description available.* |
| **interest_amount** | **float** | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.LoanPeriod import LoanPeriod

instance = LoanPeriod(
    payment_date=datetime.now(),  # required
    notional=0.0,  # required
    interest_amount=0.0  # required
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

