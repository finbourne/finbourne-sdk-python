# FundStructureRequest

The request used to create a Fund Structure.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Required | The code of the Fund Structure. |
| **name** | **str** | Required | The display name of the Fund Structure. |
| **description** | **str** | Optional | An optional description for the Fund Structure. |
| **existing_funds** | [List[ResourceId]](ResourceId.md) | Optional | An optional list of existing funds to be incorporated as part of the structure. |
| **allocation_groups** | [List[AllocationGroup]](AllocationGroup.md) | Optional | An optional list of Allocation Groups that can apply across a Fund Structure. A group may span the share classes of a member and the members that invest into it through dedicated share class links. |
| **nodes** | [List[FundStructureNode]](FundStructureNode.md) | Optional | The list of nodes that make up the Fund Structure, each referencing a Fund and defining its role. May be empty on create, with members added later through the members endpoint. |
| **edges** | [List[FundStructureEdge]](FundStructureEdge.md) | Optional | The list of edges that define how the members of the structure are linked: a member investing into a dedicated share class of another, or holding an equity, GP, LP or carry interest in another through an instrument. |
| **effective_at** | **datetime** | Optional | The effective datetime from which the Fund Structure applies. Defaults to the beginning of time if not specified, so that the structure is visible at every effective datetime. |
| **role_data_type_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **nav_type_codes** | **List[str]** | Required | The NAV types every member of the structure produces, by code. Declaring them once here gives the structure a shared Timeline. At least one is required, and every member fund must define a NAV type with each of these codes. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of properties to decorate onto the Fund Structure. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundStructureRequest import FundStructureRequest

instance = FundStructureRequest(
    code="...",  # required — The code of the Fund Structure.
    name="...",  # required — The display name of the Fund Structure.
    description="...",  # optional — An optional description for the Fund Structure.
    existing_funds=[],  # optional — An optional list of existing funds to be incorporated as part of the structure.
    allocation_groups=[],  # optional — An optional list of Allocation Groups that can apply across a Fund Structure. A group may span the share classes of a member and the members that invest into it through dedicated share class links.
    nodes=[],  # optional — The list of nodes that make up the Fund Structure, each referencing a Fund and defining its role. May be empty on create, with members added later through the members endpoint.
    edges=[],  # optional — The list of edges that define how the members of the structure are linked: a member investing into a dedicated share class of another, or holding an equity, GP, LP or carry interest in another through an instrument.
    effective_at=datetime.now(),  # optional — The effective datetime from which the Fund Structure applies. Defaults to the beginning of time if not specified, so that the structure is visible at every effective datetime.
    role_data_type_id=ResourceId(...),  # optional
    nav_type_codes=,  # required — The NAV types every member of the structure produces, by code. Declaring them once here gives the structure a shared Timeline. At least one is required, and every member fund must define a NAV type with each of these codes.
    properties=ModelProperty(...)  # optional — A set of properties to decorate onto the Fund Structure.
)
```

- [ResourceId](ResourceId.md) — used in `existing_funds`
- [AllocationGroup](AllocationGroup.md) — used in `allocation_groups`
- [FundStructureNode](FundStructureNode.md) — used in `nodes`
- [FundStructureEdge](FundStructureEdge.md) — used in `edges`
- [ResourceId](ResourceId.md)
- [ModelProperty](ModelProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

