# PaymentDetailsSeriesIdentifiers

The two hardcoded series identifier keys that uniquely identify a Payment Details data series.  The currency value must match the top-level currency field on the Payment Instruction.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **payment_type** | **str** | Required | The type of payment series. |
| **currency** | **str** | Required | ISO 4217 currency code identifying the currency-specific series row. Must match the top-level currency field. |
| **custodian_account_scope** | **str** | Optional | Optional. The scope of the custodian account on the portfolio. Only permitted when the applicable entity is a Portfolio. |
| **custodian_account_code** | **str** | Optional | Optional. The code of the custodian account on the portfolio. Only permitted when the applicable entity is a Portfolio. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PaymentDetailsSeriesIdentifiers import PaymentDetailsSeriesIdentifiers

instance = PaymentDetailsSeriesIdentifiers(
    payment_type="...",  # required — The type of payment series.
    currency="...",  # required — ISO 4217 currency code identifying the currency-specific series row. Must match the top-level currency field.
    custodian_account_scope="...",  # optional — Optional. The scope of the custodian account on the portfolio. Only permitted when the applicable entity is a Portfolio.
    custodian_account_code="..."  # optional — Optional. The code of the custodian account on the portfolio. Only permitted when the applicable entity is a Portfolio.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

