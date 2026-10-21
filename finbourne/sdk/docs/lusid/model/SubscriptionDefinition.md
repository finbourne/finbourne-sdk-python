# SubscriptionDefinition

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **scope** | **str** | Required | *No description available.* |
| **code** | **str** | Required | *No description available.* |
| **display_name** | **str** | Optional | *No description available.* |
| **description** | **str** | Optional | *No description available.* |
| **portfolio_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **timeline_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **timeline_property** | **str** | Optional | A portfolio property key (Portfolio/scope/code) naming a perpetual portfolio property whose value  (scope/code) identifies the timeline for each portfolio. Mutually exclusive with timelineId.  The property must be defined, with a data type of value type ResourceId or String. |
| **portfolio_filter** | **str** | Optional | A filter, in the syntax of the list portfolios filter, that narrows a wildcard portfolioId to the portfolios  of the scope that match it. Only valid when portfolioId.code is \&quot;*\&quot;. It may use the portfolio&#39;s own fields and  its perpetual Portfolio properties; time-variant and derived properties and relationships are not supported.  A portfolio that starts or stops matching joins or leaves the subscription. |
| **address_keys** | **List[str]** | Optional | The set of addresses the subscriber wishes to receive. |
| **by_tax_lots** | **bool** | Optional | *No description available.* |
| **subscription_type** | **str** | Required | Required. The kind of data the subscription streams: before/after effects per  holding (holdings), the transactions themselves (transactions), or each changed holding&#39;s  complete current state (positions). Address keys and byTaxLots are not valid for a  transactions subscription. Available values: Holdings, Transactions, Positions. |
| **start_effective_at** | **datetime** | Optional | *No description available.* |
| **end_effective_at** | **datetime** | Optional | Deprecated and no longer honoured: a fixed forward date stops being a forward view once  the live edge passes it. Use effectiveForwardDays instead. Still accepted and echoed back  so existing subscriptions keep round-tripping. |
| **effective_forward_days** | **int** | Optional | How far forward the subscription reports, as a number of calendar days past the live  edge — a rolling forward view that advances as time passes. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SubscriptionDefinition import SubscriptionDefinition

instance = SubscriptionDefinition(
    scope="...",  # required
    code="...",  # required
    display_name="...",  # optional
    description="...",  # optional
    portfolio_id=ResourceId(...),  # required
    timeline_id=ResourceId(...),  # optional
    timeline_property="...",  # optional — A portfolio property key (Portfolio/scope/code) naming a perpetual portfolio property whose value  (scope/code) identifies the timeline for each portfolio. Mutually exclusive with timelineId.  The property must be defined, with a data type of value type ResourceId or String.
    portfolio_filter="...",  # optional — A filter, in the syntax of the list portfolios filter, that narrows a wildcard portfolioId to the portfolios  of the scope that match it. Only valid when portfolioId.code is \&quot;*\&quot;. It may use the portfolio&#39;s own fields and  its perpetual Portfolio properties; time-variant and derived properties and relationships are not supported.  A portfolio that starts or stops matching joins or leaves the subscription.
    address_keys=,  # optional — The set of addresses the subscriber wishes to receive.
    by_tax_lots=True,  # optional
    subscription_type="...",  # required — Required. The kind of data the subscription streams: before/after effects per  holding (holdings), the transactions themselves (transactions), or each changed holding&#39;s  complete current state (positions). Address keys and byTaxLots are not valid for a  transactions subscription. Available values: Holdings, Transactions, Positions.
    start_effective_at=datetime.now(),  # optional
    end_effective_at=datetime.now(),  # optional — Deprecated and no longer honoured: a fixed forward date stops being a forward view once  the live edge passes it. Use effectiveForwardDays instead. Still accepted and echoed back  so existing subscriptions keep round-tripping.
    effective_forward_days=0  # optional — How far forward the subscription reports, as a number of calendar days past the live  edge — a rolling forward view that advances as time passes.
)
```

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

