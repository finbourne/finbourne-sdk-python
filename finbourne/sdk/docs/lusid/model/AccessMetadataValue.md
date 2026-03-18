# AccessMetadataValue

An access control value. Provider should only be used if you are a service provider licensing data. In that case  the provider value must match your domain.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **value** | **str** | Required | *No description available.* |
| **provider** | **str** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AccessMetadataValue import AccessMetadataValue

instance = AccessMetadataValue(
    value="...",  # required
    provider="..."  # optional
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

