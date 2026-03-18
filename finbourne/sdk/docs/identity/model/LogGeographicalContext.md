# LogGeographicalContext

Represents a LogGeographicalContext resource in the Okta API
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **city** | **str** | Optional | *No description available.* |
| **state** | **str** | Optional | *No description available.* |
| **country** | **str** | Optional | *No description available.* |
| **postal_code** | **str** | Optional | *No description available.* |
| **geolocation** | [LogGeolocation](LogGeolocation.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.LogGeographicalContext import LogGeographicalContext

instance = LogGeographicalContext(
    city="...",  # optional
    state="...",  # optional
    country="...",  # optional
    postal_code="...",  # optional
    geolocation=LogGeolocation(...)  # optional
)
```

- [LogGeolocation](LogGeolocation.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

