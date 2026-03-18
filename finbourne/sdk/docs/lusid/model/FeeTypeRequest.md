# FeeTypeRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Required |  |
| **display_name** | **str** | Required | The name of the fee type. |
| **description** | **str** | Optional | The description of the fee type. |
| **component_transactions** | [List[ComponentTransaction]](ComponentTransaction.md) | Required | A set of component transactions that relate to the fee type to be created. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FeeTypeRequest import FeeTypeRequest

instance = FeeTypeRequest(
    code="...",  # required — 
    display_name="...",  # required — The name of the fee type.
    description="...",  # optional — The description of the fee type.
    component_transactions=[]  # required — A set of component transactions that relate to the fee type to be created.
)
```

- [ComponentTransaction](ComponentTransaction.md) — used in `component_transactions`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

