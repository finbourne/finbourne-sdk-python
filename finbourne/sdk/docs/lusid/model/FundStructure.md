# FundStructure

Definition of the structure of a fund
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **id** | [../model/ResourceId](ResourceId.md) | Required | *No description available.* |
| **name** | **str** | Required | The display name of the Fund Structure. |
| **description** | **str** | Optional | An optional description for the Fund Structure. |
| **funds** | [../model/List[Fund]](Fund.md) | Optional | An optional list of existing funds to be incorporated as part of the structure. |
| **allocation_groups** | [../model/List[AllocationGroup]](AllocationGroup.md) | Optional | An optional list of Allocation Groups that can apply across a Fund Structure. Only classes and feeder funds linked to the master fund specified are allowed. |
| **nodes** | [../model/List[FundStructureNode]](FundStructureNode.md) | Required | The list of nodes that make up the Fund Structure, each referencing a Fund and defining its role. |
| **edges** | [../model/List[FundStructureEdge]](FundStructureEdge.md) | Required | The list of edges that define the relationships between feeder and master nodes in the structure. |
| **version** | [../model/Version](Version.md) | Optional | *No description available.* |
| **properties** | [../model/Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of properties to decorate onto the Fund Structure. |
| **links** | [../model/List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundStructure import FundStructure

instance = FundStructure(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    id=ResourceId(...),  # required
    name="...",  # required — The display name of the Fund Structure.
    description="...",  # optional — An optional description for the Fund Structure.
    funds=[],  # optional — An optional list of existing funds to be incorporated as part of the structure.
    allocation_groups=[],  # optional — An optional list of Allocation Groups that can apply across a Fund Structure. Only classes and feeder funds linked to the master fund specified are allowed.
    nodes=[],  # required — The list of nodes that make up the Fund Structure, each referencing a Fund and defining its role.
    edges=[],  # required — The list of edges that define the relationships between feeder and master nodes in the structure.
    version=Version(...),  # optional
    properties=ModelProperty(...),  # optional — A set of properties to decorate onto the Fund Structure.
    links=[]  # optional
)
```

- [ResourceId](ResourceId.md)
- [Fund](Fund.md) — used in `funds`
- [AllocationGroup](AllocationGroup.md) — used in `allocation_groups`
- [FundStructureNode](FundStructureNode.md) — used in `nodes`
- [FundStructureEdge](FundStructureEdge.md) — used in `edges`
- [Version](Version.md)
- [ModelProperty](ModelProperty.md) — used in `properties`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

