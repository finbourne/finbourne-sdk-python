# RecClosedPeriods

References to the closed periods created on the left and right timelines when a Closed Period  instance is locked.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **left** | [RecClosedPeriodReference](RecClosedPeriodReference.md) | Required | *No description available.* |
| **right** | [RecClosedPeriodReference](RecClosedPeriodReference.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecClosedPeriods import RecClosedPeriods

instance = RecClosedPeriods(
    left=RecClosedPeriodReference(...),  # required
    right=RecClosedPeriodReference(...)  # required
)
```


## Related Models

- [RecClosedPeriodReference](RecClosedPeriodReference.md)
- [RecClosedPeriodReference](RecClosedPeriodReference.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

