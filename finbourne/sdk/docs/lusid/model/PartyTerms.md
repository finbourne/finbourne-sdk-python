# PartyTerms

What one party posts under a margin item.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **threshold** | **float** | Optional | The exposure that is tolerated before margin is called. Empty means no threshold. |
| **independent_amount** | **float** | Required | The independent amount posted in addition to variation margin. |
| **cash_interest** | [CashInterest](CashInterest.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PartyTerms import PartyTerms

instance = PartyTerms(
    threshold=0.0,  # optional — The exposure that is tolerated before margin is called. Empty means no threshold.
    independent_amount=0.0,  # required — The independent amount posted in addition to variation margin.
    cash_interest=CashInterest(...)  # optional
)
```

- [CashInterest](CashInterest.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

