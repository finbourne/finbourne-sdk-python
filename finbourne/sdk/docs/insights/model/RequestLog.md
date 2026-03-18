# RequestLog

Holds logged information about a request performed on an API.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **timestamp** | **datetime** | Required | The timestamp of the request. |
| **application** | **str** | Required | The name of the application that the request was made to. |
| **id** | **str** | Required | The identifier of the request. |
| **session_id** | **str** | Optional | The identifier of the session that the request was made in. |
| **verb** | **str** | Required | The HTTP verb of the request. |
| **url** | **str** | Required | The URL of the request. |
| **domain** | **str** | Optional | The domain of the request. |
| **user** | **str** | Required | The user who made the request. |
| **user_type** | **str** | Optional | The type of the user who made the request. |
| **operation** | **str** | Optional | The API operation invoked by the request. |
| **outcome** | **str** | Required | The outcome of the request: Completed, Errored or Failed. |
| **duration** | **float** | Required | The duration of the request in milliseconds. |
| **http_status_code** | **int** | Required | The status code of the request. |
| **error_code** | **str** | Optional | Error code, if the request had a failure or error. |
| **sdk_language** | **str** | Optional | The language of the SDK used. |
| **sdk_version** | **str** | Optional | The version of the SDK used. |
| **source_application** | **str** | Optional | The name of the application that made the request. |
| **correlation_id** | **List[str]** | Optional | The chain of requestIds preceding this request |
| **impersonating_user** | **str** | Optional | The impersonating user. Only present if the request is an impersonated one |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.insights.models.RequestLog import RequestLog

instance = RequestLog(
    timestamp=datetime.now(),  # required — The timestamp of the request.
    application="...",  # required — The name of the application that the request was made to.
    id="...",  # required — The identifier of the request.
    session_id="...",  # optional — The identifier of the session that the request was made in.
    verb="...",  # required — The HTTP verb of the request.
    url="...",  # required — The URL of the request.
    domain="...",  # optional — The domain of the request.
    user="...",  # required — The user who made the request.
    user_type="...",  # optional — The type of the user who made the request.
    operation="...",  # optional — The API operation invoked by the request.
    outcome="...",  # required — The outcome of the request: Completed, Errored or Failed.
    duration=0.0,  # required — The duration of the request in milliseconds.
    http_status_code=0,  # required — The status code of the request.
    error_code="...",  # optional — Error code, if the request had a failure or error.
    sdk_language="...",  # optional — The language of the SDK used.
    sdk_version="...",  # optional — The version of the SDK used.
    source_application="...",  # optional — The name of the application that made the request.
    correlation_id=,  # optional — The chain of requestIds preceding this request
    impersonating_user="...",  # optional — The impersonating user. Only present if the request is an impersonated one
    links=[]  # optional
)
```

- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

