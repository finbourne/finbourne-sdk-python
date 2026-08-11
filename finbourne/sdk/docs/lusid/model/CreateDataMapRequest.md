# CreateDataMapRequest

Request to create a new data map
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [DataMapKey](DataMapKey.md) | Required | *No description available.* |
| **data** | [DataMapping](DataMapping.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CreateDataMapRequest import CreateDataMapRequest

instance = CreateDataMapRequest(
    id=DataMapKey(...),  # required
    data=DataMapping(...)  # optional
)
```


## Related Models

- [DataMapKey](DataMapKey.md)
- [DataMapping](DataMapping.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

