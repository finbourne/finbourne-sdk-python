# VendorRequest

Details of a request made to a vendor service.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | **str** | Required | The ID of the log. |
| **request** | **str** | Required | The body of the request. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.insights.models.VendorRequest import VendorRequest

instance = VendorRequest(
    id="...",  # required — The ID of the log.
    request="...",  # required — The body of the request.
    links=[]  # optional
)
```

- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

