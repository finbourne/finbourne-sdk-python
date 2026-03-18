# OpenFigiSearchResult

Response coming back from a search request to OpenFIGI
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **results** | [List[OpenFigiData]](OpenFigiData.md) | Required | Enumerable list of OpenFIGI results |
| **perm_id_uri** | **str** | Optional | URI of the related PermID response, if requested |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.OpenFigiSearchResult import OpenFigiSearchResult

instance = OpenFigiSearchResult(
    results=[],  # required — Enumerable list of OpenFIGI results
    perm_id_uri="..."  # optional — URI of the related PermID response, if requested
)
```


## Related Models

- [OpenFigiData](OpenFigiData.md) — used in `results`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

