# TransactionDiagnostics

Represents a set of diagnostics per transaction, where applicable.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **transaction_display_name** | **str** | Required | *No description available.* |
| **error_details** | **List[str]** | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TransactionDiagnostics import TransactionDiagnostics

instance = TransactionDiagnostics(
    transaction_display_name="...",  # required
    error_details=  # required
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

