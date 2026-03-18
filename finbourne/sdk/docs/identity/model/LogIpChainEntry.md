# LogIpChainEntry

Represents a LogIpChainEntry resource in the Okta API
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **ip** | **str** | Optional | *No description available.* |
| **geographical_context** | [LogGeographicalContext](LogGeographicalContext.md) | Optional | *No description available.* |
| **version** | **str** | Optional | *No description available.* |
| **source** | **str** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.LogIpChainEntry import LogIpChainEntry

instance = LogIpChainEntry(
    ip="...",  # optional
    geographical_context=LogGeographicalContext(...),  # optional
    version="...",  # optional
    source="..."  # optional
)
```

- [LogGeographicalContext](LogGeographicalContext.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

