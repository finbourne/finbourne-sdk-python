# RecResultItem

An individual item that makes up (one side of) a rec result. Polymorphic by rec type / item type.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **item_type** | **str** | Required | The polymorphic item-type discriminator (e.g. SettlementActivity, Holding, Transaction). Available values: SettlementActivity, Holding, Transaction. |
| **rule_and_attribute_values** | **Dict[str, Optional[str]]** | Optional | The core rule, aggregate rule and supplemental attribute values for the item, keyed by name. *(read-only)* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecResultItem import RecResultItem

instance = RecResultItem(
    item_type="...",  # required — The polymorphic item-type discriminator (e.g. SettlementActivity, Holding, Transaction). Available values: SettlementActivity, Holding, Transaction.
    rule_and_attribute_values=  # optional — The core rule, aggregate rule and supplemental attribute values for the item, keyed by name.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

