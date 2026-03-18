# CurrencyAndAmount

An amount of a specific currency, specifying a value and an associated unit
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **amount** | **float** | Optional | *No description available.* |
| **currency** | **str** | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CurrencyAndAmount import CurrencyAndAmount

instance = CurrencyAndAmount(
    amount=0.0,  # optional
    currency="..."  # required
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

