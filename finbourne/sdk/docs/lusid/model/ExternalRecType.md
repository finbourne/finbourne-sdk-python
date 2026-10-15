# ExternalRecType

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Required | The name for this external reconciliation describing source data. |
| **temporality** | **str** | Optional | How the reconciliation reads its data: PointInTime (the latest state as at the instance&#39;s effectiveAt, the default) or Activity (everything effective across the instance&#39;s activity window). Available values: PointInTime, Activity. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ExternalRecType import ExternalRecType

instance = ExternalRecType(
    name="...",  # required — The name for this external reconciliation describing source data.
    temporality="..."  # optional — How the reconciliation reads its data: PointInTime (the latest state as at the instance&#39;s effectiveAt, the default) or Activity (everything effective across the instance&#39;s activity window). Available values: PointInTime, Activity.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

