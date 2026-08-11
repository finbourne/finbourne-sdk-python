# Response

DTO of Finbourne.AspNetCore.Http.TrackingEntry.ResponseInformation.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **headers** | **Dict[str, List[str]]** | Optional | The headers |
| **content_length** | **int** | Optional | The actual length of the body, which may be larger than the data recorded in Finbourne.Insights.WebApi.Dtos.Response.Body (e.g. if actual Body is large, or not convertible to a string) |
| **content_type** | **str** | Optional | The content type |
| **body** | **str** | Optional | The recorded content. |
| **body_was_truncated** | **bool** | Optional | Determines if the recorded body was truncated. |
| **status_code** | **int** | Optional | Http Status Code of the request. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.insights.models.Response import Response

instance = Response(
    headers=,  # optional — The headers
    content_length=0,  # optional — The actual length of the body, which may be larger than the data recorded in Finbourne.Insights.WebApi.Dtos.Response.Body (e.g. if actual Body is large, or not convertible to a string)
    content_type="...",  # optional — The content type
    body="...",  # optional — The recorded content.
    body_was_truncated=True,  # optional — Determines if the recorded body was truncated.
    status_code=0,  # optional — Http Status Code of the request.
    links=[]  # optional
)
```

- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

