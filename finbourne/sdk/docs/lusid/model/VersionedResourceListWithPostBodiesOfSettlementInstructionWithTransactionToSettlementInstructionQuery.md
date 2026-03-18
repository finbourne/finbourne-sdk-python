# VersionedResourceListWithPostBodiesOfSettlementInstructionWithTransactionToSettlementInstructionQuery

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **version** | [Version](Version.md) | Required | *No description available.* |
| **values** | [List[SettlementInstructionWithTransaction]](SettlementInstructionWithTransaction.md) | Required | The resources to list. |
| **href** | **str** | Optional | The URI of the resource list. |
| **post_body** | [SettlementInstructionQuery](SettlementInstructionQuery.md) | Optional | *No description available.* |
| **next_page** | [SettlementInstructionQuery](SettlementInstructionQuery.md) | Optional | *No description available.* |
| **previous_page** | [SettlementInstructionQuery](SettlementInstructionQuery.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.VersionedResourceListWithPostBodiesOfSettlementInstructionWithTransactionToSettlementInstructionQuery import VersionedResourceListWithPostBodiesOfSettlementInstructionWithTransactionToSettlementInstructionQuery

instance = VersionedResourceListWithPostBodiesOfSettlementInstructionWithTransactionToSettlementInstructionQuery(
    version=Version(...),  # required
    values=[],  # required — The resources to list.
    href="...",  # optional — The URI of the resource list.
    post_body=SettlementInstructionQuery(...),  # optional
    next_page=SettlementInstructionQuery(...),  # optional
    previous_page=SettlementInstructionQuery(...),  # optional
    links=[]  # optional
)
```


## Related Models

- [Version](Version.md)
- [SettlementInstructionWithTransaction](SettlementInstructionWithTransaction.md) — used in `values`
- [SettlementInstructionQuery](SettlementInstructionQuery.md)
- [SettlementInstructionQuery](SettlementInstructionQuery.md)
- [SettlementInstructionQuery](SettlementInstructionQuery.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

