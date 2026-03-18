# ConstituentsAdjustmentHeader

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **effective_at** | **datetime** | Optional | There can be at most one holdings adjustment for a portfolio at a  specific effective time so this uniquely identifies the adjustment. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ConstituentsAdjustmentHeader import ConstituentsAdjustmentHeader

instance = ConstituentsAdjustmentHeader(
    effective_at=datetime.now(),  # optional — There can be at most one holdings adjustment for a portfolio at a  specific effective time so this uniquely identifies the adjustment.
    version=Version(...),  # optional
    links=[]  # optional
)
```

- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

