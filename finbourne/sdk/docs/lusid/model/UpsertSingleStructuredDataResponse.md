# UpsertSingleStructuredDataResponse

Response from upserting structured data document
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **value** | **datetime** | Optional | The value that was successfully retrieved. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertSingleStructuredDataResponse import UpsertSingleStructuredDataResponse

instance = UpsertSingleStructuredDataResponse(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    value=datetime.now(),  # optional — The value that was successfully retrieved.
    links=[]  # optional
)
```

- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

