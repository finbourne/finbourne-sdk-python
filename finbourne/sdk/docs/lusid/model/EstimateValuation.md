# EstimateValuation

The swing decision read at both unit prices the transfer agency's unit-denominated orders could be valued at: this valuation point's estimate price and the last official price, with which one the decision used and how far apart they are.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **decision_price** | **str** | Required | The unit price the swing decision was taken on. &#39;EstimatePrice&#39; is the price struck at this valuation point; &#39;LastOfficialPrice&#39; is the unit price the previous valuation point published or, for a share class that has not published one yet, the launch price the class was set up with. |
| **at_estimate_price** | [DealingFlowValuation](DealingFlowValuation.md) | Required | *No description available.* |
| **at_last_official_price** | [DealingFlowValuation](DealingFlowValuation.md) | Optional | *No description available.* |
| **difference** | [EstimateValuationDifference](EstimateValuationDifference.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.EstimateValuation import EstimateValuation

instance = EstimateValuation(
    decision_price="...",  # required — The unit price the swing decision was taken on. &#39;EstimatePrice&#39; is the price struck at this valuation point; &#39;LastOfficialPrice&#39; is the unit price the previous valuation point published or, for a share class that has not published one yet, the launch price the class was set up with.
    at_estimate_price=DealingFlowValuation(...),  # required
    at_last_official_price=DealingFlowValuation(...),  # optional
    difference=EstimateValuationDifference(...)  # optional
)
```

- [DealingFlowValuation](DealingFlowValuation.md)
- [DealingFlowValuation](DealingFlowValuation.md)
- [EstimateValuationDifference](EstimateValuationDifference.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

