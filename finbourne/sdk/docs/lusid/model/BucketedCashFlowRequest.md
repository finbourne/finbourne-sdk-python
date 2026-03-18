# BucketedCashFlowRequest

Specification class consisting of parameters for BucketedCashFlow endpoint.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **rounding_method** | **str** | Required | When bucketing, there is not a unique way to allocate the bucket points.  RoundingMethod Supported string (enumeration) values are: [RoundDown, RoundUp]. |
| **bucketing_dates** | **List[datetime]** | Optional | A list of dates to perform cashflow bucketing upon.  If this is provided, the list of tenors for bucketing should be empty. |
| **bucket_tenors** | **List[str]** | Optional | A list of tenors to perform cashflow bucketing upon.  If this is provided, the list of dates for bucketing should be empty. |
| **effective_at** | **str** | Optional | The valuation (pricing) effective datetime or cut label (inclusive) at which to evaluate the cashflows.  This determines whether cashflows are evaluated in a historic or forward looking context and will, for certain models, affect where data is looked up.  For example, on a swap if the effectiveAt is in the middle of the window, cashflows before it will be historic and resets assumed to exist where if the effectiveAt  is before the start of the range they are forward looking and will be expectations assuming the model supports that.  There is evidently a presumption here about availability of data and that the effectiveAt is realistically on or before the real-world today. |
| **window_start** | **str** | Optional | The lower bound effective datetime or cut label (inclusive) from which to retrieve the cashflows.  There is no lower bound if this is not specified. |
| **window_end** | **str** | Optional | The upper bound effective datetime or cut label (inclusive) from which to retrieve the cashflows.  The upper bound defaults to &#39;today&#39; if it is not specified |
| **recipe_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **report_currency** | **str** | Optional | Three letter ISO currency string indicating what currency to report in for ReportCurrency denominated queries. |
| **group_by** | **List[str]** | Optional | The set of items by which to perform grouping. This primarily matters when one or more of the metric operators is a mapping  that reduces set size, e.g. sum or proportion. The group-by statement determines the set of keys by which to break the results out. |
| **addresses** | **List[str]** | Optional | The set of items that the user wishes to see in the results. If empty, will be defaulted to standard ones. |
| **equip_with_subtotals** | **bool** | Optional | Flag directing the Valuation call to populate the results with subtotals of aggregates. |
| **as_at** | **datetime** | Optional | The time of the system at which to query for bucketed cashflows. |
| **exclude_unsettled_trades** | **bool** | Optional | Flag directing the Valuation call to exclude cashflows from unsettled trades.  If absent or set to false, cashflows will returned based on trade date - more specifically, cashflows from any unsettled trades will be included in the results. If set to true, unsettled trades will be excluded from the result set. |
| **cash_flow_type** | **str** | Optional | Indicate the requested cash flow representation InstrumentCashFlows or PortfolioCashFlows (GetCashLadder uses this)  Options: [InstrumentCashFlow, PortfolioCashFlow] |
| **bucketing_schedule** | [BucketingSchedule](BucketingSchedule.md) | Optional | *No description available.* |
| **filter** | **str** | Optional |  |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BucketedCashFlowRequest import BucketedCashFlowRequest

instance = BucketedCashFlowRequest(
    rounding_method="...",  # required — When bucketing, there is not a unique way to allocate the bucket points.  RoundingMethod Supported string (enumeration) values are: [RoundDown, RoundUp].
    bucketing_dates=,  # optional — A list of dates to perform cashflow bucketing upon.  If this is provided, the list of tenors for bucketing should be empty.
    bucket_tenors=,  # optional — A list of tenors to perform cashflow bucketing upon.  If this is provided, the list of dates for bucketing should be empty.
    effective_at="...",  # optional — The valuation (pricing) effective datetime or cut label (inclusive) at which to evaluate the cashflows.  This determines whether cashflows are evaluated in a historic or forward looking context and will, for certain models, affect where data is looked up.  For example, on a swap if the effectiveAt is in the middle of the window, cashflows before it will be historic and resets assumed to exist where if the effectiveAt  is before the start of the range they are forward looking and will be expectations assuming the model supports that.  There is evidently a presumption here about availability of data and that the effectiveAt is realistically on or before the real-world today.
    window_start="...",  # optional — The lower bound effective datetime or cut label (inclusive) from which to retrieve the cashflows.  There is no lower bound if this is not specified.
    window_end="...",  # optional — The upper bound effective datetime or cut label (inclusive) from which to retrieve the cashflows.  The upper bound defaults to &#39;today&#39; if it is not specified
    recipe_id=ResourceId(...),  # optional
    report_currency="...",  # optional — Three letter ISO currency string indicating what currency to report in for ReportCurrency denominated queries.
    group_by=,  # optional — The set of items by which to perform grouping. This primarily matters when one or more of the metric operators is a mapping  that reduces set size, e.g. sum or proportion. The group-by statement determines the set of keys by which to break the results out.
    addresses=,  # optional — The set of items that the user wishes to see in the results. If empty, will be defaulted to standard ones.
    equip_with_subtotals=True,  # optional — Flag directing the Valuation call to populate the results with subtotals of aggregates.
    as_at=datetime.now(),  # optional — The time of the system at which to query for bucketed cashflows.
    exclude_unsettled_trades=True,  # optional — Flag directing the Valuation call to exclude cashflows from unsettled trades.  If absent or set to false, cashflows will returned based on trade date - more specifically, cashflows from any unsettled trades will be included in the results. If set to true, unsettled trades will be excluded from the result set.
    cash_flow_type="...",  # optional — Indicate the requested cash flow representation InstrumentCashFlows or PortfolioCashFlows (GetCashLadder uses this)  Options: [InstrumentCashFlow, PortfolioCashFlow]
    bucketing_schedule=BucketingSchedule(...),  # optional
    filter="..."  # optional — 
)
```

- [ResourceId](ResourceId.md)
- [BucketingSchedule](BucketingSchedule.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

