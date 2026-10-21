# MarginRunIssue

Something a margin run could not do for some of its agreements, and why.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **agreements** | [List[ResourceId]](ResourceId.md) | Required | The collateral agreements the issue concerns. |
| **detail** | **str** | Required | What prevented the agreements from being valued. |
| **shard_id** | **str** | Optional | The shard the issue arose in, when it arose while valuing. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.MarginRunIssue import MarginRunIssue

instance = MarginRunIssue(
    agreements=[],  # required — The collateral agreements the issue concerns.
    detail="...",  # required — What prevented the agreements from being valued.
    shard_id="..."  # optional — The shard the issue arose in, when it arose while valuing.
)
```


## Related Models

- [ResourceId](ResourceId.md) — used in `agreements`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

