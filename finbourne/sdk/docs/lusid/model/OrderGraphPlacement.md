# OrderGraphPlacement

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **placement** | [Placement](Placement.md) | Required | *No description available.* |
| **block_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **ordered** | [OrderGraphPlacementOrderSynopsis](OrderGraphPlacementOrderSynopsis.md) | Required | *No description available.* |
| **placed** | [OrderGraphPlacementPlacementSynopsis](OrderGraphPlacementPlacementSynopsis.md) | Required | *No description available.* |
| **executed** | [OrderGraphPlacementExecutionSynopsis](OrderGraphPlacementExecutionSynopsis.md) | Required | *No description available.* |
| **allocated** | [OrderGraphPlacementAllocationSynopsis](OrderGraphPlacementAllocationSynopsis.md) | Required | *No description available.* |
| **derived_state** | **str** | Required | A simple description of the overall state of a placement. |
| **calculated_average_price** | **float** | Optional | Average price realised on executions for a given placement |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.OrderGraphPlacement import OrderGraphPlacement

instance = OrderGraphPlacement(
    placement=Placement(...),  # required
    block_id=ResourceId(...),  # required
    ordered=OrderGraphPlacementOrderSynopsis(...),  # required
    placed=OrderGraphPlacementPlacementSynopsis(...),  # required
    executed=OrderGraphPlacementExecutionSynopsis(...),  # required
    allocated=OrderGraphPlacementAllocationSynopsis(...),  # required
    derived_state="...",  # required — A simple description of the overall state of a placement.
    calculated_average_price=0.0  # optional — Average price realised on executions for a given placement
)
```


## Related Models

- [Placement](Placement.md)
- [ResourceId](ResourceId.md)
- [OrderGraphPlacementOrderSynopsis](OrderGraphPlacementOrderSynopsis.md)
- [OrderGraphPlacementPlacementSynopsis](OrderGraphPlacementPlacementSynopsis.md)
- [OrderGraphPlacementExecutionSynopsis](OrderGraphPlacementExecutionSynopsis.md)
- [OrderGraphPlacementAllocationSynopsis](OrderGraphPlacementAllocationSynopsis.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

