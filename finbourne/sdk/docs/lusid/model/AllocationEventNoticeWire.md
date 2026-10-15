# AllocationEventNoticeWire

Wire instructions for the payment a notice asks for or announces, from the investor record's payment  instructions. Absent when the investor record holds none.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **bank_name** | **str** | Optional | The name of the bank. |
| **account_name** | **str** | Optional | The name on the account. |
| **account_number** | **str** | Optional | The account number or IBAN. |
| **bic** | **str** | Optional | The bank identifier code. |
| **reference** | **str** | Optional | The payment reference. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationEventNoticeWire import AllocationEventNoticeWire

instance = AllocationEventNoticeWire(
    bank_name="...",  # optional — The name of the bank.
    account_name="...",  # optional — The name on the account.
    account_number="...",  # optional — The account number or IBAN.
    bic="...",  # optional — The bank identifier code.
    reference="..."  # optional — The payment reference.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

