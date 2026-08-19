# RecDefSource

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **source_type** | **str** | Required | The type of entity that this source refers to. One of: Portfolio, PortfolioGroup, Fund. Available values: Portfolio, PortfolioGroup, Fund. |
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecDefSource import RecDefSource

instance = RecDefSource(
    source_type="...",  # required — The type of entity that this source refers to. One of: Portfolio, PortfolioGroup, Fund. Available values: Portfolio, PortfolioGroup, Fund.
    id=ResourceId(...)  # required
)
```

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

