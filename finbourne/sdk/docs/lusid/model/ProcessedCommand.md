# ProcessedCommand

The list of commands.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **description** | **str** | Required | The description of the command issued. |
| **path** | **str** | Optional | The unique identifier for the command including the request id. |
| **user_id** | [User](User.md) | Required | *No description available.* |
| **processed_time** | **datetime** | Required | The asAt datetime that the events published by the processing of this command were committed to LUSID. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ProcessedCommand import ProcessedCommand

instance = ProcessedCommand(
    description="...",  # required — The description of the command issued.
    path="...",  # optional — The unique identifier for the command including the request id.
    user_id=User(...),  # required
    processed_time=datetime.now()  # required — The asAt datetime that the events published by the processing of this command were committed to LUSID.
)
```

- [User](User.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

