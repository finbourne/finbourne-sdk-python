# TransactionTemplateRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **description** | **str** | Required | The description of the transaction template. |
| **component_transactions** | [List[ComponentTransaction]](ComponentTransaction.md) | Required | A set of component transactions that relate to the template to be created. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TransactionTemplateRequest import TransactionTemplateRequest

instance = TransactionTemplateRequest(
    description="...",  # required — The description of the transaction template.
    component_transactions=[]  # required — A set of component transactions that relate to the template to be created.
)
```

- [ComponentTransaction](ComponentTransaction.md) — used in `component_transactions`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

