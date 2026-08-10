# FundStructureRequest

The request used to create a Fund Structure.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Required | The code of the Fund Structure. |
| **name** | **str** | Required | The display name of the Fund Structure. |
| **description** | **str** | Optional | An optional description for the Fund Structure. |
| **existing_funds** | [../model/List[ResourceId]](ResourceId.md) | Optional | An optional list of existing funds to be incorporated as part of the structure. |
| **new_funds** | [../model/List[FundDefinitionRequest]](FundDefinitionRequest.md) | Optional | An optional list of Fund definitions to be created inline as part of the structure. |
| **allocation_groups** | [../model/List[AllocationGroup]](AllocationGroup.md) | Optional | An optional list of Allocation Groups that can apply across a Fund Structure. Only classes and feeder funds linked to the master fund specified are allowed. |
| **nodes** | [../model/List[FundStructureNode]](FundStructureNode.md) | Required | The list of nodes that make up the Fund Structure, each referencing a Fund and defining its role. |
| **edges** | [../model/List[FundStructureEdge]](FundStructureEdge.md) | Required | The list of edges that define the relationships between feeder and master nodes in the structure. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundStructureRequest import FundStructureRequest

instance = FundStructureRequest(
    code="...",  # required — The code of the Fund Structure.
    name="...",  # required — The display name of the Fund Structure.
    description="...",  # optional — An optional description for the Fund Structure.
    existing_funds=[],  # optional — An optional list of existing funds to be incorporated as part of the structure.
    new_funds=[],  # optional — An optional list of Fund definitions to be created inline as part of the structure.
    allocation_groups=[],  # optional — An optional list of Allocation Groups that can apply across a Fund Structure. Only classes and feeder funds linked to the master fund specified are allowed.
    nodes=[],  # required — The list of nodes that make up the Fund Structure, each referencing a Fund and defining its role.
    edges=[]  # required — The list of edges that define the relationships between feeder and master nodes in the structure.
)
```

- [ResourceId](ResourceId.md) — used in `existing_funds`
- [FundDefinitionRequest](FundDefinitionRequest.md) — used in `new_funds`
- [AllocationGroup](AllocationGroup.md) — used in `allocation_groups`
- [FundStructureNode](FundStructureNode.md) — used in `nodes`
- [FundStructureEdge](FundStructureEdge.md) — used in `edges`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

