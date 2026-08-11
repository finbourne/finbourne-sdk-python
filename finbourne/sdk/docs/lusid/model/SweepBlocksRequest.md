# SweepBlocksRequest

A request to sweep specified blocks.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **block_ids** | [Dict[str, ResourceId]](ResourceId.md) | Required | A dictionary mapping ephemeral identifiers, which live as long as the request, to specific blocks to sweep. |
| **latest_allowable_modification_time** | **str** | Required | Timestamp or cut label which the  block or related entities must not have been updated after. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SweepBlocksRequest import SweepBlocksRequest

instance = SweepBlocksRequest(
    block_ids=ResourceId(...),  # required — A dictionary mapping ephemeral identifiers, which live as long as the request, to specific blocks to sweep.
    latest_allowable_modification_time="..."  # required — Timestamp or cut label which the  block or related entities must not have been updated after.
)
```


## Related Models

- [ResourceId](ResourceId.md) — used in `block_ids`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

