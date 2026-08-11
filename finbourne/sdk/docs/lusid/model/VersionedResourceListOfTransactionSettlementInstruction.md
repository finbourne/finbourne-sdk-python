# VersionedResourceListOfTransactionSettlementInstruction

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **version** | [Version](Version.md) | Required | *No description available.* |
| **values** | [List[TransactionSettlementInstruction]](TransactionSettlementInstruction.md) | Required | *No description available.* |
| **href** | **str** | Optional | *No description available.* |
| **next_page** | **str** | Optional | *No description available.* |
| **previous_page** | **str** | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.VersionedResourceListOfTransactionSettlementInstruction import VersionedResourceListOfTransactionSettlementInstruction

instance = VersionedResourceListOfTransactionSettlementInstruction(
    version=Version(...),  # required
    values=[],  # required
    href="...",  # optional
    next_page="...",  # optional
    previous_page="...",  # optional
    links=[]  # optional
)
```


## Related Models

- [Version](Version.md)
- [TransactionSettlementInstruction](TransactionSettlementInstruction.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

