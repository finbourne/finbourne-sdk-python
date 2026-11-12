# PricingMethodologyAudit

The working behind a share class's dealing price: the net cashflow it was decided on, the spread applied and  what the methodology alone proposed, with how any Market swing triggers were evaluated.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **net_cashflow** | **float** | Required | The fund&#39;s net dealing cashflow for the valuation point, in the fund currency. An inflow is positive and an outflow negative. |
| **net_cashflow_pct_of_nav** | **float** | Optional | The net cashflow as a percentage of the previous valuation point&#39;s NAV. Absent when there is no previous NAV to measure it against. |
| **spreads_applied** | [SwingSpreadApplied](SwingSpreadApplied.md) | Optional | *No description available.* |
| **engine_proposal** | [PricingMethodologyEngineProposal](PricingMethodologyEngineProposal.md) | Required | *No description available.* |
| **override** | [PricingMethodologyOverride](PricingMethodologyOverride.md) | Optional | *No description available.* |
| **inflow_trigger** | [SwingTriggerEvaluation](SwingTriggerEvaluation.md) | Optional | *No description available.* |
| **outflow_trigger** | [SwingTriggerEvaluation](SwingTriggerEvaluation.md) | Optional | *No description available.* |
| **dealing_flows** | [DealingFlowSummary](DealingFlowSummary.md) | Optional | *No description available.* |
| **estimate_valuation** | [EstimateValuation](EstimateValuation.md) | Optional | *No description available.* |
| **approval_status** | **str** | Optional | Where a manually approved swing decision stands. Pending until a manager approves or overrides the engine&#39;s proposal, or when the proposal has changed since the decision was taken; Approved when the decision equals the proposal; Overridden when it differs. Absent when the swing policy approves automatically. |
| **dealing_lines_not_valued** | [List[DealingLineNotValued]](DealingLineNotValued.md) | Optional | The dealing lines read for the swing decision that could not be valued into the share class currency: an amount in a currency that is neither the fund&#39;s nor any share class&#39;s, or a weight-only line. While any are present and no pricingMethodologyOverride has been submitted, no swing decision is taken, the dealing price is absent and the valuation point cannot be finalised; under an override the override&#39;s price stands and the lines remain listed here. Absent when every line was valued or the methodology does not swing. |
| **completeness** | [DealingBookCompleteness](DealingBookCompleteness.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PricingMethodologyAudit import PricingMethodologyAudit

instance = PricingMethodologyAudit(
    net_cashflow=0.0,  # required — The fund&#39;s net dealing cashflow for the valuation point, in the fund currency. An inflow is positive and an outflow negative.
    net_cashflow_pct_of_nav=0.0,  # optional — The net cashflow as a percentage of the previous valuation point&#39;s NAV. Absent when there is no previous NAV to measure it against.
    spreads_applied=SwingSpreadApplied(...),  # optional
    engine_proposal=PricingMethodologyEngineProposal(...),  # required
    override=PricingMethodologyOverride(...),  # optional
    inflow_trigger=SwingTriggerEvaluation(...),  # optional
    outflow_trigger=SwingTriggerEvaluation(...),  # optional
    dealing_flows=DealingFlowSummary(...),  # optional
    estimate_valuation=EstimateValuation(...),  # optional
    approval_status="...",  # optional — Where a manually approved swing decision stands. Pending until a manager approves or overrides the engine&#39;s proposal, or when the proposal has changed since the decision was taken; Approved when the decision equals the proposal; Overridden when it differs. Absent when the swing policy approves automatically.
    dealing_lines_not_valued=[],  # optional — The dealing lines read for the swing decision that could not be valued into the share class currency: an amount in a currency that is neither the fund&#39;s nor any share class&#39;s, or a weight-only line. While any are present and no pricingMethodologyOverride has been submitted, no swing decision is taken, the dealing price is absent and the valuation point cannot be finalised; under an override the override&#39;s price stands and the lines remain listed here. Absent when every line was valued or the methodology does not swing.
    completeness=DealingBookCompleteness(...)  # optional
)
```

- [SwingSpreadApplied](SwingSpreadApplied.md)
- [PricingMethodologyEngineProposal](PricingMethodologyEngineProposal.md)
- [PricingMethodologyOverride](PricingMethodologyOverride.md)
- [SwingTriggerEvaluation](SwingTriggerEvaluation.md)
- [SwingTriggerEvaluation](SwingTriggerEvaluation.md)
- [DealingFlowSummary](DealingFlowSummary.md)
- [EstimateValuation](EstimateValuation.md)
- [DealingLineNotValued](DealingLineNotValued.md) — used in `dealing_lines_not_valued`
- [DealingBookCompleteness](DealingBookCompleteness.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

