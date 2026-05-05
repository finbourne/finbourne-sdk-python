# OrderGraphBlock

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **block** | [Block](Block.md) | Required | *No description available.* |
| **ordered** | [OrderGraphBlockOrderSynopsis](OrderGraphBlockOrderSynopsis.md) | Required | *No description available.* |
| **placed** | [OrderGraphBlockPlacementSynopsis](OrderGraphBlockPlacementSynopsis.md) | Required | *No description available.* |
| **executed** | [OrderGraphBlockExecutionSynopsis](OrderGraphBlockExecutionSynopsis.md) | Required | *No description available.* |
| **allocated** | [OrderGraphBlockAllocationSynopsis](OrderGraphBlockAllocationSynopsis.md) | Required | *No description available.* |
| **booked** | [OrderGraphBlockTransactionSynopsis](OrderGraphBlockTransactionSynopsis.md) | Required | *No description available.* |
| **derived_state** | **str** | Required | A simple description of the overall state of a block. |
| **derived_compliance_state** | **str** | Required | The overall compliance state of a block, derived from the block&#39;s orders. Available values: Pending, Failed, Passed, ManuallyApproved, PartiallyOverridden, Warning. |
| **derived_approval_state** | **str** | Required | The overall approval state of a block, derived from approval of the block&#39;s orders. Available values: Pending, Rejected, Approved. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.OrderGraphBlock import OrderGraphBlock

instance = OrderGraphBlock(
    block=Block(...),  # required
    ordered=OrderGraphBlockOrderSynopsis(...),  # required
    placed=OrderGraphBlockPlacementSynopsis(...),  # required
    executed=OrderGraphBlockExecutionSynopsis(...),  # required
    allocated=OrderGraphBlockAllocationSynopsis(...),  # required
    booked=OrderGraphBlockTransactionSynopsis(...),  # required
    derived_state="...",  # required — A simple description of the overall state of a block.
    derived_compliance_state="...",  # required — The overall compliance state of a block, derived from the block&#39;s orders. Available values: Pending, Failed, Passed, ManuallyApproved, PartiallyOverridden, Warning.
    derived_approval_state="..."  # required — The overall approval state of a block, derived from approval of the block&#39;s orders. Available values: Pending, Rejected, Approved.
)
```


## Related Models

- [Block](Block.md)
- [OrderGraphBlockOrderSynopsis](OrderGraphBlockOrderSynopsis.md)
- [OrderGraphBlockPlacementSynopsis](OrderGraphBlockPlacementSynopsis.md)
- [OrderGraphBlockExecutionSynopsis](OrderGraphBlockExecutionSynopsis.md)
- [OrderGraphBlockAllocationSynopsis](OrderGraphBlockAllocationSynopsis.md)
- [OrderGraphBlockTransactionSynopsis](OrderGraphBlockTransactionSynopsis.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

