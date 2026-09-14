# CurrencyGroupMinorUnit

A minor unit currency within a currency group.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **currency** | **str** | Required | The three-letter, case-sensitive currency code of the minor unit, e.g. GBX. |
| **fraction_of_major** | **float** | Required | The fraction of the major unit that one minor unit is worth, greater than zero and no more than one, e.g. 0.01 for GBX against GBP. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CurrencyGroupMinorUnit import CurrencyGroupMinorUnit

instance = CurrencyGroupMinorUnit(
    currency="...",  # required — The three-letter, case-sensitive currency code of the minor unit, e.g. GBX.
    fraction_of_major=0.0  # required — The fraction of the major unit that one minor unit is worth, greater than zero and no more than one, e.g. 0.01 for GBX against GBP.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

