# HealthCheck

Configuration for a Worker that performs a GET against a given Url.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Required | The type of worker |
| **url** | **str** | Required | The URL to check, eg: https://www.google.com/ |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.HealthCheck import HealthCheck

instance = HealthCheck(
    type="...",  # required — The type of worker
    url="..."  # required — The URL to check, eg: https://www.google.com/
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

