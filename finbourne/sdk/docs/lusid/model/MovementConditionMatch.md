# MovementConditionMatch

The outcome of one movement's condition for a transaction. Reported per movement rather than keyed by  movement, because a transaction type may configure several movements that share a side and have no name.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **movement_name** | **str** | Optional | The name of the movement, or null if the movement is unnamed. |
| **side** | **str** | Required | The side the movement is configured against. |
| **condition_matched** | **bool** | Optional | Whether the movement&#39;s condition was satisfied by this transaction. A movement with no condition always matches. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.MovementConditionMatch import MovementConditionMatch

instance = MovementConditionMatch(
    movement_name="...",  # optional — The name of the movement, or null if the movement is unnamed.
    side="...",  # required — The side the movement is configured against.
    condition_matched=True  # optional — Whether the movement&#39;s condition was satisfied by this transaction. A movement with no condition always matches.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

