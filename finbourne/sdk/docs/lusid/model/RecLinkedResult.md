# RecLinkedResult

A rec result of a different rec type in the same rec instance whose items share an identifier with this  result's items, and the keys that established the link. Links are symmetric: the linked result carries one back.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | **str** | Required | The id of the linked result, as carried in that result&#39;s own id field. |
| **rec_type** | **str** | Required | The rec type of the linked result. Always differs from this result&#39;s rec type. Available values: Holding, CashHolding, Valuation, InputTransaction, OutputTransaction, SettlementActivity. |
| **linked_by** | [RecLinkedBy](RecLinkedBy.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecLinkedResult import RecLinkedResult

instance = RecLinkedResult(
    id="...",  # required — The id of the linked result, as carried in that result&#39;s own id field.
    rec_type="...",  # required — The rec type of the linked result. Always differs from this result&#39;s rec type. Available values: Holding, CashHolding, Valuation, InputTransaction, OutputTransaction, SettlementActivity.
    linked_by=RecLinkedBy(...)  # required
)
```

- [RecLinkedBy](RecLinkedBy.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

