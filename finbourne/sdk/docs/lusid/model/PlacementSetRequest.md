# PlacementSetRequest

A request to create or update multiple Placements.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **requests** | [List[PlacementRequest]](PlacementRequest.md) | Optional | A collection of PlacementRequests. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PlacementSetRequest import PlacementSetRequest

instance = PlacementSetRequest(
    requests=[]  # optional — A collection of PlacementRequests.
)
```


## Related Models

- [PlacementRequest](PlacementRequest.md) — used in `requests`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

