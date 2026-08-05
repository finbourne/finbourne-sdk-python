# RecClosedPeriodReference

A reference to a closed period created on a timeline when the instance was locked.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **timeline_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **closed_period_id** | **str** | Required | The identifier of the closed period. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecClosedPeriodReference import RecClosedPeriodReference

instance = RecClosedPeriodReference(
    timeline_id=ResourceId(...),  # required
    closed_period_id="..."  # required — The identifier of the closed period.
)
```


## Related Models

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

