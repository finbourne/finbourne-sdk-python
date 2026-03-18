# MarketContextSuppliers

It is possible to control which supplier is used for a given asset class.  This field is deprecated in favour of market data rules, which subsumes its functionality.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **commodity** | **str** | Optional | *No description available.* |
| **credit** | **str** | Optional | *No description available.* |
| **equity** | **str** | Optional | *No description available.* |
| **fx** | **str** | Optional | *No description available.* |
| **rates** | **str** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.MarketContextSuppliers import MarketContextSuppliers

instance = MarketContextSuppliers(
    commodity="...",  # optional
    credit="...",  # optional
    equity="...",  # optional
    fx="...",  # optional
    rates="..."  # optional
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

