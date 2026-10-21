# RecDefCurrencies

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **left** | **str** | Optional | The currency used on the left side of the reconciliation. Required when the left side has portfolio sources; must be null when it draws on relational data. |
| **right** | **str** | Optional | The currency used on the right side of the reconciliation. Required when the right side has portfolio sources; must be null when it draws on relational data. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecDefCurrencies import RecDefCurrencies

instance = RecDefCurrencies(
    left="...",  # optional — The currency used on the left side of the reconciliation. Required when the left side has portfolio sources; must be null when it draws on relational data.
    right="..."  # optional — The currency used on the right side of the reconciliation. Required when the right side has portfolio sources; must be null when it draws on relational data.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

