# TraceEventLog

Holds information about a trace event.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **trace_event_id** | **str** | Required | The identifier of the trace event. |
| **trace_id** | **str** | Required | The identifier of the parent trace. |
| **created_at** | **datetime** | Required | The datetime at which the trace event was created. |
| **event_type** | **str** | Required | The type of the trace event. |
| **origin** | **str** | Required | Whether the event originated from the AI or the user |
| **content** | **str** | Required | The content of the trace event. |
| **agent_scope** | **str** | Required | The scope of the agent currently being interacted with |
| **agent_code** | **str** | Required | The code identifier of the agent currently being interacted with |
| **agent_version** | **int** | Required | The version of the circuit in which the trace event occurred. |
| **node_id** | **str** | Required | The ID of the circuit&#39;s node at which the trace event occured. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.insights.models.TraceEventLog import TraceEventLog

instance = TraceEventLog(
    trace_event_id="...",  # required — The identifier of the trace event.
    trace_id="...",  # required — The identifier of the parent trace.
    created_at=datetime.now(),  # required — The datetime at which the trace event was created.
    event_type="...",  # required — The type of the trace event.
    origin="...",  # required — Whether the event originated from the AI or the user
    content="...",  # required — The content of the trace event.
    agent_scope="...",  # required — The scope of the agent currently being interacted with
    agent_code="...",  # required — The code identifier of the agent currently being interacted with
    agent_version=0,  # required — The version of the circuit in which the trace event occurred.
    node_id="...",  # required — The ID of the circuit&#39;s node at which the trace event occured.
    links=[]  # optional
)
```

- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

