# ComponentTransaction

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **display_name** | **str** | Required | *No description available.* |
| **condition** | **str** | Optional | *No description available.* |
| **transaction_field_map** | [TransactionFieldMap](TransactionFieldMap.md) | Required | *No description available.* |
| **transaction_property_map** | [List[TransactionPropertyMap]](TransactionPropertyMap.md) | Required | *No description available.* |
| **preserve_tax_lot_structure** | **bool** | Optional | Controls if tax lot structure should be preserved when cost base is transferred to a new holding. For example in Spin Off instrument events. |
| **market_open_time_adjustments** | **List[str]** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ComponentTransaction import ComponentTransaction

instance = ComponentTransaction(
    display_name="...",  # required
    condition="...",  # optional
    transaction_field_map=TransactionFieldMap(...),  # required
    transaction_property_map=[],  # required
    preserve_tax_lot_structure=True,  # optional — Controls if tax lot structure should be preserved when cost base is transferred to a new holding. For example in Spin Off instrument events.
    market_open_time_adjustments=  # optional
)
```

- [TransactionFieldMap](TransactionFieldMap.md)
- [TransactionPropertyMap](TransactionPropertyMap.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

