# TransactionDateWindows

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **left** | **str** | Required | Transaction Date Window for the left side of a reconciliation |
| **right** | **str** | Required | Transaction Date Window for the right side of a reconciliation |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TransactionDateWindows import TransactionDateWindows

instance = TransactionDateWindows(
    left="...",  # required — Transaction Date Window for the left side of a reconciliation
    right="..."  # required — Transaction Date Window for the right side of a reconciliation
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

