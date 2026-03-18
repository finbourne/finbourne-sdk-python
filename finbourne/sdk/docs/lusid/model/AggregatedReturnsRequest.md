# AggregatedReturnsRequest

The request used in the AggregatedReturns.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **metrics** | [List[PerformanceReturnsMetric]](PerformanceReturnsMetric.md) | Required | A list of metrics to calculate in the AggregatedReturns. |
| **return_ids** | [List[ResourceId]](ResourceId.md) | Optional | The Scope and code of the returns. |
| **recipe_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **composite_method** | **str** | Optional | The method used to calculate the Portfolio performance: Equal/Asset. |
| **period** | **str** | Optional | The type of the returns used to calculate the aggregation result: Daily/Monthly. |
| **output_frequency** | **str** | Optional | The type of calculated output: Daily/Weekly/Monthly/Quarterly/Half-Yearly/Yearly. |
| **alternative_inception_date** | **str** | Optional | Optional - either a date, or the key for a portfolio property containing a date. If provided, the given date will override the inception date for this request. |
| **holiday_calendars** | **List[str]** | Optional | The holiday calendar(s) that should be used in determining the date schedule. Holiday calendar(s) are supplied by their codes, for example, &#39;CoppClark&#39;. Note that when the calendars are not available (e.g. when the user has insufficient permissions), a recipe setting will be used to determine whether the whole batch should then fail or whether the calendar not being available should simply be ignored. |
| **currency** | **str** | Optional | Optional - either a string or a property. If provided, the results will be converted to the specified currency |
| **run_mode** | **str** | Optional | The dates the AggregatedReturns output will be calculated: ReturnData/WeekDays/AllDays/MonthEnd. Defaults to ReturnData. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AggregatedReturnsRequest import AggregatedReturnsRequest

instance = AggregatedReturnsRequest(
    metrics=[],  # required — A list of metrics to calculate in the AggregatedReturns.
    return_ids=[],  # optional — The Scope and code of the returns.
    recipe_id=ResourceId(...),  # optional
    composite_method="...",  # optional — The method used to calculate the Portfolio performance: Equal/Asset.
    period="...",  # optional — The type of the returns used to calculate the aggregation result: Daily/Monthly.
    output_frequency="...",  # optional — The type of calculated output: Daily/Weekly/Monthly/Quarterly/Half-Yearly/Yearly.
    alternative_inception_date="...",  # optional — Optional - either a date, or the key for a portfolio property containing a date. If provided, the given date will override the inception date for this request.
    holiday_calendars=,  # optional — The holiday calendar(s) that should be used in determining the date schedule. Holiday calendar(s) are supplied by their codes, for example, &#39;CoppClark&#39;. Note that when the calendars are not available (e.g. when the user has insufficient permissions), a recipe setting will be used to determine whether the whole batch should then fail or whether the calendar not being available should simply be ignored.
    currency="...",  # optional — Optional - either a string or a property. If provided, the results will be converted to the specified currency
    run_mode="..."  # optional — The dates the AggregatedReturns output will be calculated: ReturnData/WeekDays/AllDays/MonthEnd. Defaults to ReturnData.
)
```


## Related Models

- [PerformanceReturnsMetric](PerformanceReturnsMetric.md) — used in `metrics`
- [ResourceId](ResourceId.md) — used in `return_ids`
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

