# AggregateSpec

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **key** | **str** | Required | The key that uniquely identifies a queryable address in Lusid. |
| **op** | **str** | Required | The available values are: Sum, DefaultSum, Proportion, Average, Count, Min, Max, Value, SumOfPositiveValues, SumOfNegativeValues, SumOfAbsoluteValues, ProportionOfAbsoluteValues, SumCumulativeInAdvance, SumCumulativeInArrears |
| **options** | **Dict[str, Optional[object]]** | Optional | Additional options to apply when performing computations. Options that do not apply to the Key will be  ignored. Option values can be boolean, numeric, string or date-time. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AggregateSpec import AggregateSpec

instance = AggregateSpec(
    key="...",  # required — The key that uniquely identifies a queryable address in Lusid.
    op="...",  # required — The available values are: Sum, DefaultSum, Proportion, Average, Count, Min, Max, Value, SumOfPositiveValues, SumOfNegativeValues, SumOfAbsoluteValues, ProportionOfAbsoluteValues, SumCumulativeInAdvance, SumCumulativeInArrears
    options=  # optional — Additional options to apply when performing computations. Options that do not apply to the Key will be  ignored. Option values can be boolean, numeric, string or date-time.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

