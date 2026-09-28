# FundStructure

Definition of the structure of a fund
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **name** | **str** | Required | The display name of the Fund Structure. |
| **description** | **str** | Optional | An optional description for the Fund Structure. |
| **funds** | [List[Fund]](Fund.md) | Optional | An optional list of existing funds to be incorporated as part of the structure. |
| **allocation_groups** | [List[AllocationGroup]](AllocationGroup.md) | Optional | An optional list of Allocation Groups that can apply across a Fund Structure. A group may span the share classes of a member and the members that invest into it through dedicated share class links. |
| **nodes** | [List[FundStructureNode]](FundStructureNode.md) | Required | The list of nodes that make up the Fund Structure, each referencing a Fund and defining its role. May be empty on create, with members added later through the members endpoint. |
| **edges** | [List[FundStructureEdge]](FundStructureEdge.md) | Required | The list of edges that define how the members of the structure are linked: a member investing into a dedicated share class of another, or holding an equity, GP, LP or carry interest in another through an instrument. |
| **role_data_type_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **nav_type_codes** | **List[str]** | Optional | The NAV types every member of the structure produces, by code. Declaring them once here gives the structure a shared Timeline. At least one is required, and every member fund must define a NAV type with each of these codes. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of properties to decorate onto the Fund Structure. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


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
    allocation_groups=[],  # optional — An optional list of Allocation Groups that can apply across a Fund Structure. A group may span the share classes of a member and the members that invest into it through dedicated share class links.
    nodes=[],  # required — The list of nodes that make up the Fund Structure, each referencing a Fund and defining its role. May be empty on create, with members added later through the members endpoint.
    edges=[],  # required — The list of edges that define how the members of the structure are linked: a member investing into a dedicated share class of another, or holding an equity, GP, LP or carry interest in another through an instrument.
    role_data_type_id=ResourceId(...),  # optional
    nav_type_codes=,  # optional — The NAV types every member of the structure produces, by code. Declaring them once here gives the structure a shared Timeline. At least one is required, and every member fund must define a NAV type with each of these codes.
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
- [ResourceId](ResourceId.md)
- [Version](Version.md)
- [ModelProperty](ModelProperty.md) — used in `properties`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

