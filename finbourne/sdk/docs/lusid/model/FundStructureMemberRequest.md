# FundStructureMemberRequest

A member to add to a Fund Structure: the node, and the links that join it to members already in the structure.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **node** | [FundStructureNode](FundStructureNode.md) | Required | *No description available.* |
| **edges** | [List[FundStructureEdge]](FundStructureEdge.md) | Optional | The links joining the new node to members already in the structure. May be empty for a member that is linked later. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundStructureMemberRequest import FundStructureMemberRequest

instance = FundStructureMemberRequest(
    node=FundStructureNode(...),  # required
    edges=[]  # optional — The links joining the new node to members already in the structure. May be empty for a member that is linked later.
)
```


## Related Models

- [FundStructureNode](FundStructureNode.md)
- [FundStructureEdge](FundStructureEdge.md) — used in `edges`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

