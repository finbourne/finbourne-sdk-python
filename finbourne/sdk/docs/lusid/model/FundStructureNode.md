# FundStructureNode

A node in a Fund Structure, representing a Fund and its role within the structure.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **node_code** | **str** | Required | A unique identifier for this node within the Fund Structure. |
| **fund_scope** | **str** | Required | The scope of the Fund referenced by this node. |
| **fund_code** | **str** | Required | The code of the Fund referenced by this node. |
| **role** | **str** | Required | The role of this node within the structure. Must be one of the acceptable values of the structure&#39;s role data type. |
| **allocation_basis** | [FundStructureAllocationBasis](FundStructureAllocationBasis.md) | Optional | *No description available.* |
| **pnl_flow_mode** | **str** | Optional | How profit and loss reaches this member from the members it holds. EquityPickup (the default) revalues the position in each held member; BucketFlowThrough receives one line per economic bucket, tagged with its origin; TransactionFlowThrough receives every line, tagged with its origin and path. Available values: EquityPickup, BucketFlowThrough, TransactionFlowThrough. |
| **allocation_map_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundStructureNode import FundStructureNode

instance = FundStructureNode(
    node_code="...",  # required — A unique identifier for this node within the Fund Structure.
    fund_scope="...",  # required — The scope of the Fund referenced by this node.
    fund_code="...",  # required — The code of the Fund referenced by this node.
    role="...",  # required — The role of this node within the structure. Must be one of the acceptable values of the structure&#39;s role data type.
    allocation_basis=FundStructureAllocationBasis(...),  # optional
    pnl_flow_mode="...",  # optional — How profit and loss reaches this member from the members it holds. EquityPickup (the default) revalues the position in each held member; BucketFlowThrough receives one line per economic bucket, tagged with its origin; TransactionFlowThrough receives every line, tagged with its origin and path. Available values: EquityPickup, BucketFlowThrough, TransactionFlowThrough.
    allocation_map_id=ResourceId(...)  # optional
)
```

- [FundStructureAllocationBasis](FundStructureAllocationBasis.md)
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

