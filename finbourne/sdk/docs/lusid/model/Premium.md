# Premium

A class containing information for a given premium payment.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **amount** | **float** | Required | Premium amount. |
| **currency** | **str** | Required | Premium currency. |
| **var_date** | **datetime** | Required | Date when premium paid. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.Premium import Premium

instance = Premium(
    amount=0.0,  # required — Premium amount.
    currency="...",  # required — Premium currency.
    var_date=datetime.now()  # required — Date when premium paid.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

