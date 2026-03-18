# LevelStep

Item which is stepped in level/quantity.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **var_date** | **datetime** | Required | The date from which the level should apply. |
| **quantity** | **float** | Required | The quantity which is applied. This might be an absolute, percentage, fractional or other value. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.LevelStep import LevelStep

instance = LevelStep(
    var_date=datetime.now(),  # required — The date from which the level should apply.
    quantity=0.0  # required — The quantity which is applied. This might be an absolute, percentage, fractional or other value.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

