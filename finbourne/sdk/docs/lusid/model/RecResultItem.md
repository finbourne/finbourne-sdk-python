# RecResultItem

An individual item that makes up (one side of) a rec result. Polymorphic by itemType; each value has a  corresponding inherited class.

## oneOf Type

`RecResultItem` can be one of the following types:

* [RecResultExternalIdentifiersItem](./RecResultExternalIdentifiersItem.md)
* [RecResultHoldingItem](./RecResultHoldingItem.md)
* [RecResultRelationalDataItem](./RecResultRelationalDataItem.md)
* [RecResultResourceIdItem](./RecResultResourceIdItem.md)
* [RecResultSettlementActivityItem](./RecResultSettlementActivityItem.md)
* [RecResultTransactionItem](./RecResultTransactionItem.md)

## Usage

### Creating from a compatible type

```python
from finbourne.sdk.services.lusid.models.RecResultItem import RecResultItem

# Construct using any of the compatible types above
rec_result_external_identifiers_item_instance = lusid.models.rec_result_external_identifiers_item.RecResultExternalIdentifiersItem(
                        entity_scope = '', 
                        entity_unique_id = '', 
                        entity_display_name = '', 
                        identifiers = {
                            'key' : ''
                            }, 
                        item_type = '', 
                        rule_and_attribute_values = {
                            'key' : ''
                            }, 
                        writeback_suggestions = [
                            null
                            ], )

instance = RecResultItem(rec_result_external_identifiers_item_instance)
```

## Related Models

- [RecResultExternalIdentifiersItem](./RecResultExternalIdentifiersItem.md)
- [RecResultHoldingItem](./RecResultHoldingItem.md)
- [RecResultRelationalDataItem](./RecResultRelationalDataItem.md)
- [RecResultResourceIdItem](./RecResultResourceIdItem.md)
- [RecResultSettlementActivityItem](./RecResultSettlementActivityItem.md)
- [RecResultTransactionItem](./RecResultTransactionItem.md)

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

