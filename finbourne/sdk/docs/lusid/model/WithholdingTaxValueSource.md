# WithholdingTaxValueSource

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **dimension** | **str** | Required | The name of the matching dimension this declaration populates, as it appears in the dataset field schema. A declaration naming a dimension neither dataset has is rejected. |
| **source** | **str** | Required | The LUSID field the engine reads the dimension&#39;s value from, addressed in the same syntax used to filter results: a property key in the form Properties[{domain}/{scope}/{code}], such as Properties[Instrument/WithholdingTax/AssetClass] or Properties[Transaction/WithholdingTax/Custodian]; or the name of a field on the entity itself, such as Transaction.SettlementCurrency. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.WithholdingTaxValueSource import WithholdingTaxValueSource

instance = WithholdingTaxValueSource(
    dimension="...",  # required — The name of the matching dimension this declaration populates, as it appears in the dataset field schema. A declaration naming a dimension neither dataset has is rejected.
    source="..."  # required — The LUSID field the engine reads the dimension&#39;s value from, addressed in the same syntax used to filter results: a property key in the form Properties[{domain}/{scope}/{code}], such as Properties[Instrument/WithholdingTax/AssetClass] or Properties[Transaction/WithholdingTax/Custodian]; or the name of a field on the entity itself, such as Transaction.SettlementCurrency.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

