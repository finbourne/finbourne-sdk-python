# ProcessorDescription

Represents a processor in the Horizon integration system.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Required | *No description available.* |
| **display_name** | **str** | Required | *No description available.* |
| **description** | **str** | Required | *No description available.* |
| **category** | **str** | Required | *No description available.* |
| **is_active** | **bool** | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.ProcessorDescription import ProcessorDescription

instance = ProcessorDescription(
    name="...",  # required
    display_name="...",  # required
    description="...",  # required
    category="...",  # required
    is_active=True  # required
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

