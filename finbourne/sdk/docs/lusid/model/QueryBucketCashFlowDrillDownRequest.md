# QueryBucketCashFlowDrillDownRequest

Query for the individual cashflows inside a single cashflow bucket, with their source lineage.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **as_at** | **datetime** | Optional | The time of the system at which to query for cashflows. |
| **bucket_start** | **datetime** | Required | The lower bound effective datetime of the bucket from which to retrieve the cashflows. |
| **bucket_end** | **datetime** | Required | The upper bound effective datetime of the bucket from which to retrieve the cashflows. |
| **start_inclusive** | **bool** | Optional | Whether a cashflow paid exactly on the bucket start is included in the bucket. Defaults to true. |
| **end_inclusive** | **bool** | Optional | Whether a cashflow paid exactly on the bucket end is included in the bucket. Defaults to true. |
| **portfolio_entity_ids** | [../model/List[PortfolioEntityId]](PortfolioEntityId.md) | Required | The set of portfolios and portfolio groups to which the cashflows must belong. |
| **effective_at** | **datetime** | Required | The valuation (pricing) effective datetime or cut label (inclusive) at which to evaluate the cashflows.  This determines whether cashflows are evaluated in a historic or forward looking context and will, for certain models, affect where data is looked up. |
| **recipe_id** | [../model/ResourceId](ResourceId.md) | Required | *No description available.* |
| **report_currency** | **str** | Required | Three letter ISO currency string indicating what currency to report in for ReportCurrency denominated queries. |
| **exclude_unsettled_trades** | **bool** | Optional | If set to true, unsettled trades are excluded from the result set. Set this to match the value used on the bucketed cash flow query being drilled into, so the individual cash flows reconcile with the bucket. |
| **haircut_rules** | [../model/List[CashFlowHaircutRule]](CashFlowHaircutRule.md) | Optional | Optional ordered haircut rules applied to cashflow inflows; the first matching rule wins and a rule with no criteria acts as a catch-all. When supplied, each returned cashflow carries its gross amount, haircut fraction, net amount and the rule that was applied; with no rules those fields are omitted and the results are unchanged. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.QueryBucketCashFlowDrillDownRequest import QueryBucketCashFlowDrillDownRequest

instance = QueryBucketCashFlowDrillDownRequest(
    as_at=datetime.now(),  # optional — The time of the system at which to query for cashflows.
    bucket_start=datetime.now(),  # required — The lower bound effective datetime of the bucket from which to retrieve the cashflows.
    bucket_end=datetime.now(),  # required — The upper bound effective datetime of the bucket from which to retrieve the cashflows.
    start_inclusive=True,  # optional — Whether a cashflow paid exactly on the bucket start is included in the bucket. Defaults to true.
    end_inclusive=True,  # optional — Whether a cashflow paid exactly on the bucket end is included in the bucket. Defaults to true.
    portfolio_entity_ids=[],  # required — The set of portfolios and portfolio groups to which the cashflows must belong.
    effective_at=datetime.now(),  # required — The valuation (pricing) effective datetime or cut label (inclusive) at which to evaluate the cashflows.  This determines whether cashflows are evaluated in a historic or forward looking context and will, for certain models, affect where data is looked up.
    recipe_id=ResourceId(...),  # required
    report_currency="...",  # required — Three letter ISO currency string indicating what currency to report in for ReportCurrency denominated queries.
    exclude_unsettled_trades=True,  # optional — If set to true, unsettled trades are excluded from the result set. Set this to match the value used on the bucketed cash flow query being drilled into, so the individual cash flows reconcile with the bucket.
    haircut_rules=[]  # optional — Optional ordered haircut rules applied to cashflow inflows; the first matching rule wins and a rule with no criteria acts as a catch-all. When supplied, each returned cashflow carries its gross amount, haircut fraction, net amount and the rule that was applied; with no rules those fields are omitted and the results are unchanged.
)
```

- [PortfolioEntityId](PortfolioEntityId.md) — used in `portfolio_entity_ids`
- [ResourceId](ResourceId.md)
- [CashFlowHaircutRule](CashFlowHaircutRule.md) — used in `haircut_rules`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

