# TraceLog

Holds metadata for a trace.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **trace_id** | **str** | Required | The identifier of the trace. |
| **created_at** | **datetime** | Required | The datetime at which the trace was created. |
| **user_id** | **str** | Required | The id of the user who created the trace. |
| **description** | **str** | Optional | The description of the trace. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.insights.models.TraceLog import TraceLog

instance = TraceLog(
    trace_id="...",  # required — The identifier of the trace.
    created_at=datetime.now(),  # required — The datetime at which the trace was created.
    user_id="...",  # required — The id of the user who created the trace.
    description="...",  # optional — The description of the trace.
    links=[]  # optional
)
```

- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

