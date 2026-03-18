# TransactionType

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **aliases** | [List[TransactionTypeAlias]](TransactionTypeAlias.md) | Required | List of transaction types that map to this specific transaction configuration |
| **movements** | [List[TransactionTypeMovement]](TransactionTypeMovement.md) | Required | Movement data for the transaction type |
| **properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | Properties attached to the transaction type |
| **calculations** | [List[TransactionTypeCalculation]](TransactionTypeCalculation.md) | Optional | Calculations to be performed for the transaction type |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TransactionType import TransactionType

instance = TransactionType(
    aliases=[],  # required — List of transaction types that map to this specific transaction configuration
    movements=[],  # required — Movement data for the transaction type
    properties=PerpetualProperty(...),  # optional — Properties attached to the transaction type
    calculations=[],  # optional — Calculations to be performed for the transaction type
    links=[]  # optional
)
```


## Related Models

- [TransactionTypeAlias](TransactionTypeAlias.md) — used in `aliases`
- [TransactionTypeMovement](TransactionTypeMovement.md) — used in `movements`
- [PerpetualProperty](PerpetualProperty.md) — used in `properties`
- [TransactionTypeCalculation](TransactionTypeCalculation.md) — used in `calculations`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

