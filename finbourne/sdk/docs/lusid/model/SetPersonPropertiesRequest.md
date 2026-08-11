# SetPersonPropertiesRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Required | Properties to set for a Person. All time-variant properties must have same EffectiveFrom date. Properties not included in the request will not be amended. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SetPersonPropertiesRequest import SetPersonPropertiesRequest

instance = SetPersonPropertiesRequest(
    properties=ModelProperty(...)  # required — Properties to set for a Person. All time-variant properties must have same EffectiveFrom date. Properties not included in the request will not be amended.
)
```


## Related Models

- [ModelProperty](ModelProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

