# EffectiveRange

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **from_date** | **datetime** | Optional | The effective from datetime that this range applies to. |
| **until_date** | **datetime** | Optional | The effective from datetime that this range applies to. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.EffectiveRange import EffectiveRange

instance = EffectiveRange(
    from_date=datetime.now(),  # optional — The effective from datetime that this range applies to.
    until_date=datetime.now()  # optional — The effective from datetime that this range applies to.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

