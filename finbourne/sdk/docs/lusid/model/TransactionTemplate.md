# TransactionTemplate

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instrument_type** | **str** | Required | A value that represents the instrument type. |
| **instrument_event_type** | **str** | Required | A value that represents the instrument event type. |
| **description** | **str** | Required | The description of the transaction template. |
| **scope** | **str** | Required | The scope in which the transaction template resides. |
| **component_transactions** | [List[ComponentTransaction]](ComponentTransaction.md) | Required | A set of component transactions that relate to the template to be created. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TransactionTemplate import TransactionTemplate

instance = TransactionTemplate(
    instrument_type="...",  # required — A value that represents the instrument type.
    instrument_event_type="...",  # required — A value that represents the instrument event type.
    description="...",  # required — The description of the transaction template.
    scope="...",  # required — The scope in which the transaction template resides.
    component_transactions=[],  # required — A set of component transactions that relate to the template to be created.
    links=[]  # optional
)
```

- [ComponentTransaction](ComponentTransaction.md) — used in `component_transactions`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

