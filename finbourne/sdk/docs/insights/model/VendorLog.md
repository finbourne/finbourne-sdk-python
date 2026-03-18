# VendorLog

Holds logged information about a request made to an external vendor.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | **str** | Required | The identifier of a log entry. |
| **provider** | **str** | Required | The provider or service name. |
| **timestamp** | **datetime** | Required | Timestamp of when the log was generated. |
| **type** | **str** | Required | Type of log. Possible values: HttpResponse. |
| **destination_url** | **str** | Required | The destination URL of the task. |
| **operation** | **str** | Required | The operation performed. Possible values: Evaluate. |
| **outcome** | **str** | Required | The outcome of the operation. Possible values: Success, Failure. |
| **duration** | **float** | Required | The duration of the operation in ms. |
| **http_status_code** | **int** | Required | The status code of the operation. |
| **user_id** | **str** | Required | The user that made the request to LUSID. |
| **request_id** | **str** | Required | The ID of the request to LUSID. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.insights.models.VendorLog import VendorLog

instance = VendorLog(
    id="...",  # required — The identifier of a log entry.
    provider="...",  # required — The provider or service name.
    timestamp=datetime.now(),  # required — Timestamp of when the log was generated.
    type="...",  # required — Type of log. Possible values: HttpResponse.
    destination_url="...",  # required — The destination URL of the task.
    operation="...",  # required — The operation performed. Possible values: Evaluate.
    outcome="...",  # required — The outcome of the operation. Possible values: Success, Failure.
    duration=0.0,  # required — The duration of the operation in ms.
    http_status_code=0,  # required — The status code of the operation.
    user_id="...",  # required — The user that made the request to LUSID.
    request_id="...",  # required — The ID of the request to LUSID.
    links=[]  # optional
)
```

- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

