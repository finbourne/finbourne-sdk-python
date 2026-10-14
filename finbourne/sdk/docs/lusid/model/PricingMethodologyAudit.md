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
    dealing_flows=DealingFlowSummary(...)  # optional
)
```

- [SwingSpreadApplied](SwingSpreadApplied.md)
- [PricingMethodologyEngineProposal](PricingMethodologyEngineProposal.md)
- [PricingMethodologyOverride](PricingMethodologyOverride.md)
- [SwingTriggerEvaluation](SwingTriggerEvaluation.md)
- [SwingTriggerEvaluation](SwingTriggerEvaluation.md)
- [DealingFlowSummary](DealingFlowSummary.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

