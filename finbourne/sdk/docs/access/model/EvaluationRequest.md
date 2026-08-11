# EvaluationRequest

Specification for a server side evaluation of entitlement.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **request** | [RequestDetails](RequestDetails.md) | Required | *No description available.* |
| **resource** | [ResourceDetails](ResourceDetails.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.access.models.EvaluationRequest import EvaluationRequest

instance = EvaluationRequest(
    request=RequestDetails(...),  # required
    resource=ResourceDetails(...)  # required
)
```


## Related Models

- [RequestDetails](RequestDetails.md)
- [ResourceDetails](ResourceDetails.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

