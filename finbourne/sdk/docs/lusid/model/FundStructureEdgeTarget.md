# FundStructureEdgeTarget

The member a link points at, and for a dedicated share class link the share class on that member.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **node** | **str** | Required | The node code of the member the link points at. |
| **share_class_short_code** | **str** | Optional | The short code of the share class on the target member that the source invests into. Required for a DedicatedShareClass link and not allowed on any other. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundStructureEdgeTarget import FundStructureEdgeTarget

instance = FundStructureEdgeTarget(
    node="...",  # required — The node code of the member the link points at.
    share_class_short_code="..."  # optional — The short code of the share class on the target member that the source invests into. Required for a DedicatedShareClass link and not allowed on any other.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

