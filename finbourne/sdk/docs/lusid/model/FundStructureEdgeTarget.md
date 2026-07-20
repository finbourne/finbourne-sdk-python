# FundStructureEdgeTarget

The target of a Fund Structure edge, identifying the master node and share class the feeder invests into.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **node** | **str** | Required | The node code of the master node that is the target of this relationship. |
| **share_class_short_code** | **str** | Required | The short code of the share class on the master fund that the feeder invests into. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundStructureEdgeTarget import FundStructureEdgeTarget

instance = FundStructureEdgeTarget(
    node="...",  # required — The node code of the master node that is the target of this relationship.
    share_class_short_code="..."  # required — The short code of the share class on the master fund that the feeder invests into.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

