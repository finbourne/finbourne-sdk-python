# QuantityInstructed

The quantity of the event that was instructed, represented either as a percentage of the overall holdings or the number of units instructed.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Required | The type of quantity instructed, either Percentage or Units. |
| **amount** | **float** | Required | The actual amount instructed. For Type Percentage, this is between 0 and 100. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.QuantityInstructed import QuantityInstructed

instance = QuantityInstructed(
    type="...",  # required — The type of quantity instructed, either Percentage or Units.
    amount=0.0  # required — The actual amount instructed. For Type Percentage, this is between 0 and 100.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

