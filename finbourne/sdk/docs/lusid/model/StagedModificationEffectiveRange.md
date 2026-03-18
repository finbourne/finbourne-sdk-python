# StagedModificationEffectiveRange

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **from_date** | **datetime** | Optional | The datetime that this requested change is effective from. |
| **until_date** | **datetime** | Optional | The datetime that this requested change is effective until. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.StagedModificationEffectiveRange import StagedModificationEffectiveRange

instance = StagedModificationEffectiveRange(
    from_date=datetime.now(),  # optional — The datetime that this requested change is effective from.
    until_date=datetime.now()  # optional — The datetime that this requested change is effective until.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

