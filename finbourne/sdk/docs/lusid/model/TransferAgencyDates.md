# TransferAgencyDates

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **price_date** | **datetime** | Optional | The date at which the fund is priced, for the order received on ReceivedDate. Can be passed into the request instead of the ReceivedDate to calculate the TransactionDate and ExpectedPaymentDate. If both the received date and price date are given, a failure is returned. |
| **transaction_date** | **datetime** | Optional | The date at which the transaction into or out of the fund is made. |
| **expected_payment_date** | **datetime** | Optional | The date by which the cash is expected to be paid to or from the fund. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TransferAgencyDates import TransferAgencyDates

instance = TransferAgencyDates(
    price_date=datetime.now(),  # optional — The date at which the fund is priced, for the order received on ReceivedDate. Can be passed into the request instead of the ReceivedDate to calculate the TransactionDate and ExpectedPaymentDate. If both the received date and price date are given, a failure is returned.
    transaction_date=datetime.now(),  # optional — The date at which the transaction into or out of the fund is made.
    expected_payment_date=datetime.now(),  # optional — The date by which the cash is expected to be paid to or from the fund.
    links=[]  # optional
)
```

- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

