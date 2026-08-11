# BlockSetRequest

A request to create or update multiple Blocks.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **requests** | [List[BlockRequest]](BlockRequest.md) | Optional | A collection of BlockRequests. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BlockSetRequest import BlockSetRequest

instance = BlockSetRequest(
    requests=[]  # optional — A collection of BlockRequests.
)
```


## Related Models

- [BlockRequest](BlockRequest.md) — used in `requests`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

