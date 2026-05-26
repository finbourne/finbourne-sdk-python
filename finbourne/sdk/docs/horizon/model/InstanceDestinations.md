# InstanceDestinations

record containing details of the destinations for an instance.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **destination_type** | **str** | Required | *No description available.* |
| **name** | **str** | Required | *No description available.* |
| **destination_path** | **str** | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.InstanceDestinations import InstanceDestinations

instance = InstanceDestinations(
    destination_type="...",  # required
    name="...",  # required
    destination_path="..."  # required
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

