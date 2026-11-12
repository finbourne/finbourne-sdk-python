# NettingRecommendation

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **run_id** | **str** | Required | The run the recommendation was made from. Filterable. |
| **source_agreement_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **source_item** | **str** | Required | The initial-margin item the trades would leave. Filterable. |
| **target_agreement_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **target_item** | **str** | Required | The initial-margin item the trades would join. Filterable. |
| **transfer** | **str** | Required | How the trades would get there: Redesignation when both agreements face one counterparty, Novation otherwise. Filterable. |
| **instrument_type** | **str** | Optional | LUSID&#39;s type for the instruments in the cluster. Filterable. |
| **currency** | **str** | Optional | The currency the cluster&#39;s trades are denominated in. Filterable. |
| **maturity_bucket** | **str** | Optional | The residual-maturity bucket the cluster&#39;s trades fall in on the run date; empty for instruments without a maturity. Filterable. |
| **trades** | [List[TradeReference]](TradeReference.md) | Required | The holdings that would move. |
| **saving_per_day** | **float** | Required | What we would no longer fund each day across both sets, in the sets&#39; base currency. Filterable. |
| **one_off_cost** | **float** | Required | The novation cost when the transfer is one; zero for a re-designation. Filterable. |
| **payback_days** | **float** | Required | How many days of saving cover the one-off cost. Filterable. |
| **initial_margin_change** | **float** | Required | The sum over both sets of what we would post after the move less what we post today. Filterable. |
| **source** | [InitialMarginChange](InitialMarginChange.md) | Required | *No description available.* |
| **target** | [InitialMarginChange](InitialMarginChange.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.NettingRecommendation import NettingRecommendation

instance = NettingRecommendation(
    run_id="...",  # required — The run the recommendation was made from. Filterable.
    source_agreement_id=ResourceId(...),  # required
    source_item="...",  # required — The initial-margin item the trades would leave. Filterable.
    target_agreement_id=ResourceId(...),  # required
    target_item="...",  # required — The initial-margin item the trades would join. Filterable.
    transfer="...",  # required — How the trades would get there: Redesignation when both agreements face one counterparty, Novation otherwise. Filterable.
    instrument_type="...",  # optional — LUSID&#39;s type for the instruments in the cluster. Filterable.
    currency="...",  # optional — The currency the cluster&#39;s trades are denominated in. Filterable.
    maturity_bucket="...",  # optional — The residual-maturity bucket the cluster&#39;s trades fall in on the run date; empty for instruments without a maturity. Filterable.
    trades=[],  # required — The holdings that would move.
    saving_per_day=0.0,  # required — What we would no longer fund each day across both sets, in the sets&#39; base currency. Filterable.
    one_off_cost=0.0,  # required — The novation cost when the transfer is one; zero for a re-designation. Filterable.
    payback_days=0.0,  # required — How many days of saving cover the one-off cost. Filterable.
    initial_margin_change=0.0,  # required — The sum over both sets of what we would post after the move less what we post today. Filterable.
    source=InitialMarginChange(...),  # required
    target=InitialMarginChange(...)  # required
)
```

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [TradeReference](TradeReference.md) — used in `trades`
- [InitialMarginChange](InitialMarginChange.md)
- [InitialMarginChange](InitialMarginChange.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

