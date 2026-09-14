# AggregateSpec

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **key** | **str** | Required | The key that uniquely identifies a queryable address in Lusid. |
| **op** | **str** | Required | Available values: Sum, DefaultSum, Proportion, Average, Count, Min, Max, Value, SumOfPositiveValues, SumOfNegativeValues, SumOfAbsoluteValues, ProportionOfAbsoluteValues, SumCumulativeInAdvance, SumCumulativeInArrears. |
| **options** | **Dict[str, Optional[object]]** | Optional | Additional options to apply when performing computations. Options that do not apply to the Key will be  ignored. Option values can be boolean, numeric, string or date-time. |
| **return_as** | **str** | Optional | Optional client-chosen name for this metric. When supplied, the corresponding column in the returned  data is keyed by this name instead of the serialised address key (with options), letting callers  associate each requested metric with its result without reconstructing the key serialisation.  Names must be unique within a request, start with a letter and contain only letters, digits,  underscores or hyphens. When omitted, the column is keyed by the serialised address key as before. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AggregateSpec import AggregateSpec

instance = AggregateSpec(
    key="...",  # required — The key that uniquely identifies a queryable address in Lusid.
    op="...",  # required — Available values: Sum, DefaultSum, Proportion, Average, Count, Min, Max, Value, SumOfPositiveValues, SumOfNegativeValues, SumOfAbsoluteValues, ProportionOfAbsoluteValues, SumCumulativeInAdvance, SumCumulativeInArrears.
    options=,  # optional — Additional options to apply when performing computations. Options that do not apply to the Key will be  ignored. Option values can be boolean, numeric, string or date-time.
    return_as="..."  # optional — Optional client-chosen name for this metric. When supplied, the corresponding column in the returned  data is keyed by this name instead of the serialised address key (with options), letting callers  associate each requested metric with its result without reconstructing the key serialisation.  Names must be unique within a request, start with a letter and contain only letters, digits,  underscores or hyphens. When omitted, the column is keyed by the serialised address key as before.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

