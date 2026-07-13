# GetSubscriptionResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | *No description available.* |
| **value** | [SubscriptionDefinition](SubscriptionDefinition.md) | Optional | *No description available.* |
| **failed** | [ErrorDetail](ErrorDetail.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.GetSubscriptionResponse import GetSubscriptionResponse

instance = GetSubscriptionResponse(
    href="...",  # optional
    value=SubscriptionDefinition(...),  # optional
    failed=ErrorDetail(...),  # optional
    links=[]  # optional
)
```

- [SubscriptionDefinition](SubscriptionDefinition.md)
- [ErrorDetail](ErrorDetail.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

