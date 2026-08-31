# BatchCreateClosedPeriodsRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **closed_periods** | [List[CreateClosedPeriodRequest]](CreateClosedPeriodRequest.md) | Required | The ordered set of Closed Periods to create. Each Closed Period&#39;s EffectiveStart is derived from the previous Closed Period&#39;s EffectiveEnd (or the current chain tail for the first item), so EffectiveEnd must be strictly increasing across the batch. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BatchCreateClosedPeriodsRequest import BatchCreateClosedPeriodsRequest

instance = BatchCreateClosedPeriodsRequest(
    closed_periods=[]  # required — The ordered set of Closed Periods to create. Each Closed Period&#39;s EffectiveStart is derived from the previous Closed Period&#39;s EffectiveEnd (or the current chain tail for the first item), so EffectiveEnd must be strictly increasing across the batch.
)
```


## Related Models

- [CreateClosedPeriodRequest](CreateClosedPeriodRequest.md) — used in `closed_periods`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

