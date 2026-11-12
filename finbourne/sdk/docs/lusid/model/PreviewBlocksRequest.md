# PreviewBlocksRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **orders** | [List[OrderRequest]](OrderRequest.md) | Required | The orders to group into blocks. Properties in the Block domain are taken as the block&#39;s properties and form part of the grouping key. |
| **grouping_mode** | **str** | Optional | How orders are grouped. None: one block per order. SameSide: orders sharing instrument, side, type, time in force, price (for Limit and Stop), basis, date and block properties share a block. CrossSide: as SameSide but ignoring side, so opposing orders may net into one block, provided each portfolio&#39;s net for the instrument has the same sign as the block&#39;s first portfolio. Available values: None, SameSide, CrossSide. |
| **block_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PreviewBlocksRequest import PreviewBlocksRequest

instance = PreviewBlocksRequest(
    orders=[],  # required — The orders to group into blocks. Properties in the Block domain are taken as the block&#39;s properties and form part of the grouping key.
    grouping_mode="...",  # optional — How orders are grouped. None: one block per order. SameSide: orders sharing instrument, side, type, time in force, price (for Limit and Stop), basis, date and block properties share a block. CrossSide: as SameSide but ignoring side, so opposing orders may net into one block, provided each portfolio&#39;s net for the instrument has the same sign as the block&#39;s first portfolio. Available values: None, SameSide, CrossSide.
    block_id=ResourceId(...)  # optional
)
```


## Related Models

- [OrderRequest](OrderRequest.md) — used in `orders`
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

