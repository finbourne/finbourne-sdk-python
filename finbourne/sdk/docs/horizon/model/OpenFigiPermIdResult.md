# OpenFigiPermIdResult

A packed WebAPI OpenFigi DTO and PermId DTO
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **open_figi_result** | [OpenFigiData](OpenFigiData.md) | Required | *No description available.* |
| **perm_id_result** | [PermIdData](PermIdData.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.OpenFigiPermIdResult import OpenFigiPermIdResult

instance = OpenFigiPermIdResult(
    open_figi_result=OpenFigiData(...),  # required
    perm_id_result=PermIdData(...)  # optional
)
```


## Related Models

- [OpenFigiData](OpenFigiData.md)
- [PermIdData](PermIdData.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

