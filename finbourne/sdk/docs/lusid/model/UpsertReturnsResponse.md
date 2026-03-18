# UpsertReturnsResponse

Response from upserting Returns
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **version** | [Version](Version.md) | Required | *No description available.* |
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **values** | **List[Dict[str, datetime]]** | Optional | The set of values that were successfully retrieved. |
| **failed** | **List[Dict[str, ErrorDetail]]** | Optional | The set of values that could not be retrieved due along with a reason for this, e.g badly formed request. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertReturnsResponse import UpsertReturnsResponse

instance = UpsertReturnsResponse(
    version=Version(...),  # required
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    values=,  # optional — The set of values that were successfully retrieved.
    failed=,  # optional — The set of values that could not be retrieved due along with a reason for this, e.g badly formed request.
    links=[]  # optional
)
```


## Related Models

- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

