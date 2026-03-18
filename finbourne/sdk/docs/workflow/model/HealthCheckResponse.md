# HealthCheckResponse

Readonly configuration for a Worker that performs a GET against a given Url.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Optional | The type of worker |
| **url** | **str** | Optional | The URL to check, eg: https://www.google.com/ |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.HealthCheckResponse import HealthCheckResponse

instance = HealthCheckResponse(
    type="...",  # optional — The type of worker
    url="..."  # optional — The URL to check, eg: https://www.google.com/
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

