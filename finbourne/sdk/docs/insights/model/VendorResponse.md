# VendorResponse

Details of a response to a request made to a vendor service.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | **str** | Required | The ID of the log. |
| **response** | **str** | Required | The body of the response. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.insights.models.VendorResponse import VendorResponse

instance = VendorResponse(
    id="...",  # required — The ID of the log.
    response="...",  # required — The body of the response.
    links=[]  # optional
)
```

- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

