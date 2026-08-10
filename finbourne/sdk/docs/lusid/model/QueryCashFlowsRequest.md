# QueryCashFlowsRequest

Query for cashflows from one or more portfolios
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **as_at** | **datetime** | Optional | The time of the system at which to query for cashflows. |
| **window_start** | **datetime** | Required | The start date of the window. |
| **window_end** | **datetime** | Required | The end date of the window. |
| **portfolio_entity_ids** | [../model/List[PortfolioEntityId]](PortfolioEntityId.md) | Required | The set of portfolios and portfolio groups to which the instrument events must belong. |
| **recipe_id** | [../model/ResourceId](ResourceId.md) | Required | *No description available.* |
| **effective_at** | **datetime** | Required | The Effective date used in the valuation of the cashflows. |
| **cash_flow_calculation_version** | **str** | Optional | The version of the cash flow calculation logic to use. Defaults to &#39;1&#39; if not specified. Valid values are &#39;1&#39; and &#39;2&#39;.  &#39;1&#39; is the current production behaviour: cash flows booked as transactions are de-duplicated against the  instrument cash flows by identifier, and movements are treated as factual when they settle on or before the effective date.  &#39;2&#39; resolves cash flows via a deterministic source waterfall (structured result store &gt; transaction &gt; instrument),  classifies cash flows as factual by the transaction trade date (so trades dealt on or before the effective date  that settle afterwards are factual), and applies corporate action date filtering.  Bucketed responses calculated under version &#39;2&#39; always include the bucket interval metadata columns  (&#39;Valuation/Bucket/Start&#39;, &#39;Valuation/Bucket/End&#39;, &#39;Valuation/Bucket/StartInclusive&#39;, &#39;Valuation/Bucket/EndInclusive&#39;),  which are the required input of the bucket cash flow drill-down endpoint. Without a border configuration the  metadata describes the window-clamped interval of cash flow dates that the rounding method allocates to each bucket point. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.QueryCashFlowsRequest import QueryCashFlowsRequest

instance = QueryCashFlowsRequest(
    as_at=datetime.now(),  # optional — The time of the system at which to query for cashflows.
    window_start=datetime.now(),  # required — The start date of the window.
    window_end=datetime.now(),  # required — The end date of the window.
    portfolio_entity_ids=[],  # required — The set of portfolios and portfolio groups to which the instrument events must belong.
    recipe_id=ResourceId(...),  # required
    effective_at=datetime.now(),  # required — The Effective date used in the valuation of the cashflows.
    cash_flow_calculation_version="..."  # optional — The version of the cash flow calculation logic to use. Defaults to &#39;1&#39; if not specified. Valid values are &#39;1&#39; and &#39;2&#39;.  &#39;1&#39; is the current production behaviour: cash flows booked as transactions are de-duplicated against the  instrument cash flows by identifier, and movements are treated as factual when they settle on or before the effective date.  &#39;2&#39; resolves cash flows via a deterministic source waterfall (structured result store &gt; transaction &gt; instrument),  classifies cash flows as factual by the transaction trade date (so trades dealt on or before the effective date  that settle afterwards are factual), and applies corporate action date filtering.  Bucketed responses calculated under version &#39;2&#39; always include the bucket interval metadata columns  (&#39;Valuation/Bucket/Start&#39;, &#39;Valuation/Bucket/End&#39;, &#39;Valuation/Bucket/StartInclusive&#39;, &#39;Valuation/Bucket/EndInclusive&#39;),  which are the required input of the bucket cash flow drill-down endpoint. Without a border configuration the  metadata describes the window-clamped interval of cash flow dates that the rounding method allocates to each bucket point.
)
```

- [PortfolioEntityId](PortfolioEntityId.md) — used in `portfolio_entity_ids`
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

