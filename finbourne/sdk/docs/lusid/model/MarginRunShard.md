# MarginRunShard

One valuation shard of a margin run: the agreements it values with one recipe, and how far it has got.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | **str** | Required | The identifier of the shard within the run. |
| **recipe_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **agreements** | [List[ResourceId]](ResourceId.md) | Required | The collateral agreements the shard values. |
| **status** | **str** | Required | The status of the shard. One of Pending, Running, Completed or Failed. |
| **call_count** | **int** | Required | The number of margin calls the shard published. |
| **line_count** | **int** | Required | The number of margin lines the shard published. |
| **detail** | **str** | Optional | Why the shard failed, or which of its netting sets it completed without figures and why. |
| **as_at** | **datetime** | Optional | When the shard was valued: the run&#39;s as-at, or the time of the retry that valued it. Null until the shard has finished. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.MarginRunShard import MarginRunShard

instance = MarginRunShard(
    id="...",  # required — The identifier of the shard within the run.
    recipe_id=ResourceId(...),  # optional
    agreements=[],  # required — The collateral agreements the shard values.
    status="...",  # required — The status of the shard. One of Pending, Running, Completed or Failed.
    call_count=0,  # required — The number of margin calls the shard published.
    line_count=0,  # required — The number of margin lines the shard published.
    detail="...",  # optional — Why the shard failed, or which of its netting sets it completed without figures and why.
    as_at=datetime.now()  # optional — When the shard was valued: the run&#39;s as-at, or the time of the retry that valued it. Null until the shard has finished.
)
```

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md) — used in `agreements`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

