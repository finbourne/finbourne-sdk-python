# PaymentRecordReference

Identifies a Payment Record attached to a specific transaction within a portfolio.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **portfolio_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **transaction_id** | **str** | Required | The ID of the cash transaction within the portfolio to which the Payment Record is attached. |
| **payment_record_id** | **str** | Required | The unique identifier of the Payment Record attached to the above transaction. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PaymentRecordReference import PaymentRecordReference

instance = PaymentRecordReference(
    portfolio_id=ResourceId(...),  # required
    transaction_id="...",  # required — The ID of the cash transaction within the portfolio to which the Payment Record is attached.
    payment_record_id="..."  # required — The unique identifier of the Payment Record attached to the above transaction.
)
```


## Related Models

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

