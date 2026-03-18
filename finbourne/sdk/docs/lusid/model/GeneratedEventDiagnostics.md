# GeneratedEventDiagnostics

Represents a set of diagnostics per generatedEvent, where applicable.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instrument_event_id** | **str** | Required | *No description available.* |
| **type** | **str** | Required | *No description available.* |
| **detail** | **str** | Required | *No description available.* |
| **error_details** | **List[str]** | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.GeneratedEventDiagnostics import GeneratedEventDiagnostics

instance = GeneratedEventDiagnostics(
    instrument_event_id="...",  # required
    type="...",  # required
    detail="...",  # required
    error_details=  # required
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

