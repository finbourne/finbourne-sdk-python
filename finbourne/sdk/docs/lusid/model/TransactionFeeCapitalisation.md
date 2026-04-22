# TransactionFeeCapitalisation

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **capitalisation** | **str** | Optional | Whether the transaction fee should be capitalised, not capitalised, or conditionally capitalised. The allowed values are Capitalised, NonCapitalised, Conditional. |
| **capitalised_condition** | **str** | Optional | The condition that determines whether the fee is capitalised when applied to the transaction. Required only when Capitalisation is &#39;Conditional&#39;. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TransactionFeeCapitalisation import TransactionFeeCapitalisation

instance = TransactionFeeCapitalisation(
    capitalisation="...",  # optional — Whether the transaction fee should be capitalised, not capitalised, or conditionally capitalised. The allowed values are Capitalised, NonCapitalised, Conditional.
    capitalised_condition="..."  # optional — The condition that determines whether the fee is capitalised when applied to the transaction. Required only when Capitalisation is &#39;Conditional&#39;.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

