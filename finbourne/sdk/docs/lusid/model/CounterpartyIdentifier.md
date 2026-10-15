# CounterpartyIdentifier

The legal entity a collateral agreement is made with.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id_type_scope** | **str** | Required | The scope of the identifier type, e.g. the scope of the LEI identifier. |
| **id_type_code** | **str** | Required | The code of the identifier type, e.g. LEI. |
| **code** | **str** | Required | The value of the identifier. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CounterpartyIdentifier import CounterpartyIdentifier

instance = CounterpartyIdentifier(
    id_type_scope="...",  # required — The scope of the identifier type, e.g. the scope of the LEI identifier.
    id_type_code="...",  # required — The code of the identifier type, e.g. LEI.
    code="..."  # required — The value of the identifier.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

