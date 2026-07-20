# FundStructureNode

A node in a Fund Structure, representing a Fund and its role within the structure.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **node_code** | **str** | Required | A unique identifier for this node within the Fund Structure. |
| **fund_scope** | **str** | Required | The scope of the Fund referenced by this node. |
| **fund_code** | **str** | Required | The code of the Fund referenced by this node. |
| **role** | **str** | Required | The role of this node within the structure. Available values: Master, Feeder. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundStructureNode import FundStructureNode

instance = FundStructureNode(
    node_code="...",  # required — A unique identifier for this node within the Fund Structure.
    fund_scope="...",  # required — The scope of the Fund referenced by this node.
    fund_code="...",  # required — The code of the Fund referenced by this node.
    role="..."  # required — The role of this node within the structure. Available values: Master, Feeder.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

