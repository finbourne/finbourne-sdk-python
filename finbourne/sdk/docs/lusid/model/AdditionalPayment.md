# AdditionalPayment

Record describing additional payment entity.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **amount** | **float** | Required | The payment amount. |
| **currency** | **str** | Required | The payment currency. |
| **pay_date** | **datetime** | Required | Date when the payment is made. |
| **pay_receive** | **str** | Required | Is it pay or receive.    Supported string (enumeration) values are: [Pay, Receive]. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AdditionalPayment import AdditionalPayment

instance = AdditionalPayment(
    amount=0.0,  # required — The payment amount.
    currency="...",  # required — The payment currency.
    pay_date=datetime.now(),  # required — Date when the payment is made.
    pay_receive="..."  # required — Is it pay or receive.    Supported string (enumeration) values are: [Pay, Receive].
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

