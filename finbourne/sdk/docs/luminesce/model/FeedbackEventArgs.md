# FeedbackEventArgs

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **when** | **datetime** | Optional | *No description available.* |
| **session_id** | **UUID** | Optional | *No description available.* |
| **execution_id** | **UUID** | Optional | *No description available.* |
| **level** | [FeedbackLevel](FeedbackLevel.md) | Optional | *No description available.* |
| **sender** | **str** | Optional | *No description available.* |
| **state_id** | **int** | Optional | *No description available.* |
| **message_template** | **str** | Optional | *No description available.* |
| **property_values** | **List[object]** | Optional | *No description available.* |
| **message** | **str** | Optional | *No description available.* *(read-only)* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.FeedbackEventArgs import FeedbackEventArgs

instance = FeedbackEventArgs(
    when=datetime.now(),  # optional
    session_id="...",  # optional
    execution_id="...",  # optional
    level=FeedbackLevel(...),  # optional
    sender="...",  # optional
    state_id=0,  # optional
    message_template="...",  # optional
    property_values=,  # optional
    message="..."  # optional
)
```

- [FeedbackLevel](FeedbackLevel.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

