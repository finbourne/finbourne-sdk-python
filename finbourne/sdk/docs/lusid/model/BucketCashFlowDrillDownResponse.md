# BucketCashFlowDrillDownResponse

The cash flows of a range of effective dates, split into periods by a BucketingSchedule: for each period, member portfolio,  payment currency and sub-holding key combination, its opening balance, the cash flows that make up its activity, and its  closing balance. Each balance and each cash flow appears once, in its bucket.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **report_currency** | **str** | Optional | The report currency the cash flows&#39; converted fields are in; absent when none was requested. |
| **window_start** | **datetime** | Required | The window start the buckets&#39; balances run from: where the first bucket&#39;s opening balance is taken. |
| **buckets** | [List[BucketCashFlowBucket]](BucketCashFlowBucket.md) | Required | One bucket per period of the schedule, per member portfolio, payment currency and sub-holding key combination, each with its  opening balance, activity and closing balance. |
| **currency_subtotals** | [List[BucketCurrencySubtotal]](BucketCurrencySubtotal.md) | Required | The buckets summed across portfolios and sub-holding keys, one per period and payment currency. |
| **issues** | **List[str]** | Optional | What the balances do not cover, for example that they are in the payment currency only and gross of haircut; absent when there is nothing to report. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BucketCashFlowDrillDownResponse import BucketCashFlowDrillDownResponse

instance = BucketCashFlowDrillDownResponse(
    report_currency="...",  # optional — The report currency the cash flows&#39; converted fields are in; absent when none was requested.
    window_start=datetime.now(),  # required — The window start the buckets&#39; balances run from: where the first bucket&#39;s opening balance is taken.
    buckets=[],  # required — One bucket per period of the schedule, per member portfolio, payment currency and sub-holding key combination, each with its  opening balance, activity and closing balance.
    currency_subtotals=[],  # required — The buckets summed across portfolios and sub-holding keys, one per period and payment currency.
    issues=,  # optional — What the balances do not cover, for example that they are in the payment currency only and gross of haircut; absent when there is nothing to report.
    links=[]  # optional
)
```

- [BucketCashFlowBucket](BucketCashFlowBucket.md) — used in `buckets`
- [BucketCurrencySubtotal](BucketCurrencySubtotal.md) — used in `currency_subtotals`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

