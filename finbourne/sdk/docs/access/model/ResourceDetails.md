# ResourceDetails

Details about the resource being requested that may be pertinent to the entitlement evaluation
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | **Dict[str, str]** | Required | The identifier of the resource being evaluated |
| **metadata** | **Dict[str, Optional[List[EntitlementMetadata]]]** | Optional | Any metadata associated with the resource being requested |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.access.models.ResourceDetails import ResourceDetails

instance = ResourceDetails(
    id=,  # required — The identifier of the resource being evaluated
    metadata=  # optional — Any metadata associated with the resource being requested
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

