# MarginRunRequest

A request to value collateral agreements for a business date and publish their margin calls.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **effective_at** | **str** | Required | The business date, datetime or cut label to value the agreements at. |
| **as_at** | **datetime** | Optional | The asAt datetime to read agreements, portfolios and market data at. Defaults to the current LUSID system datetime if not specified. |
| **agreement_filter** | **str** | Optional | An expression selecting the collateral agreements to run, in the same syntax as listing collateral agreements. Every agreement the caller may calculate margin for is run if not specified. |
| **scenario** | [ResourceId](ResourceId.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.MarginRunRequest import MarginRunRequest

instance = MarginRunRequest(
    effective_at="...",  # required — The business date, datetime or cut label to value the agreements at.
    as_at=datetime.now(),  # optional — The asAt datetime to read agreements, portfolios and market data at. Defaults to the current LUSID system datetime if not specified.
    agreement_filter="...",  # optional — An expression selecting the collateral agreements to run, in the same syntax as listing collateral agreements. Every agreement the caller may calculate margin for is run if not specified.
    scenario=ResourceId(...)  # optional
)
```

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

