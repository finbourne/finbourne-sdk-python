# TransactionTypeDetails

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **scope** | **str** | Required | The scope in which the TransactionType was resolved. If the portfolio has a TransactionTypeScope, this will have been used. Otherwise the default scope will have been used. |
| **source** | **str** | Required | The source in which the TransactionType was resolved. |
| **type** | **str** | Required | The resolved TransactionType. More information on TransactionType resolution can be found at https://support.lusid.com/docs/how-does-lusid-resolve-transactions-to-transaction-types |
| **movement_condition_matches** | [List[MovementConditionMatch]](MovementConditionMatch.md) | Optional | One entry for each movement on the resolved TransactionType, in the order the movements are configured, recording whether that movement&#39;s condition was satisfied by this transaction. Empty for transaction versions that generate no movements, such as cancelled and amended versions. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TransactionTypeDetails import TransactionTypeDetails

instance = TransactionTypeDetails(
    scope="...",  # required — The scope in which the TransactionType was resolved. If the portfolio has a TransactionTypeScope, this will have been used. Otherwise the default scope will have been used.
    source="...",  # required — The source in which the TransactionType was resolved.
    type="...",  # required — The resolved TransactionType. More information on TransactionType resolution can be found at https://support.lusid.com/docs/how-does-lusid-resolve-transactions-to-transaction-types
    movement_condition_matches=[]  # optional — One entry for each movement on the resolved TransactionType, in the order the movements are configured, recording whether that movement&#39;s condition was satisfied by this transaction. Empty for transaction versions that generate no movements, such as cancelled and amended versions.
)
```

- [MovementConditionMatch](MovementConditionMatch.md) — used in `movement_condition_matches`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

