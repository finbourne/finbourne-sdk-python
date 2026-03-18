# HoldingContext

Holding context node.  Contains settings that control how LUSID handles holdings within portfolios.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **tax_lot_level_holdings** | **bool** | Optional | Whether or not to expand the holdings to return the underlying tax-lots. Defaults to True. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.HoldingContext import HoldingContext

instance = HoldingContext(
    tax_lot_level_holdings=True  # optional — Whether or not to expand the holdings to return the underlying tax-lots. Defaults to True.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

