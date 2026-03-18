# FeeAccrual

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **effective_at** | **datetime** | Required | The effective date for which the fee accrual has been calculated. |
| **code** | **str** | Required | The code of the fee for which the accrual has been calculated. |
| **name** | **str** | Required | The name of the fee for which the accrual has been calculated. |
| **calculation_base** | **float** | Optional | The result of the evaluating the fee&#39;s calculation base expression. |
| **amount** | **float** | Optional | The result of applying the fee to the calculation base, and scaled down to a day. |
| **previous_accrual** | **float** | Optional | The previous valuation point&#39;s total accrual. |
| **previous_total_accrual** | **float** | Optional | The previous valuation point&#39;s total accrual. |
| **total_accrual** | **float** | Optional | The sum of the PreviousAccrual and Amount. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FeeAccrual import FeeAccrual

instance = FeeAccrual(
    effective_at=datetime.now(),  # required — The effective date for which the fee accrual has been calculated.
    code="...",  # required — The code of the fee for which the accrual has been calculated.
    name="...",  # required — The name of the fee for which the accrual has been calculated.
    calculation_base=0.0,  # optional — The result of the evaluating the fee&#39;s calculation base expression.
    amount=0.0,  # optional — The result of applying the fee to the calculation base, and scaled down to a day.
    previous_accrual=0.0,  # optional — The previous valuation point&#39;s total accrual.
    previous_total_accrual=0.0,  # optional — The previous valuation point&#39;s total accrual.
    total_accrual=0.0,  # optional — The sum of the PreviousAccrual and Amount.
    links=[]  # optional
)
```

- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

