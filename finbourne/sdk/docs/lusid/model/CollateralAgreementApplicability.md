# CollateralAgreementApplicability

The portfolios a collateral agreement currently covers, according to its applicability filter.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **applicability_filter** | **str** | Required | The applicability filter that was evaluated. Only its clauses on portfolio fields are applied to select the portfolios returned. |
| **portfolios** | [List[ResourceId]](ResourceId.md) | Required | The portfolios matching the applicability filter, up to the requested limit. |
| **has_more_portfolios** | **bool** | Required | Whether more portfolios match the filter than were returned. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CollateralAgreementApplicability import CollateralAgreementApplicability

instance = CollateralAgreementApplicability(
    id=ResourceId(...),  # required
    applicability_filter="...",  # required — The applicability filter that was evaluated. Only its clauses on portfolio fields are applied to select the portfolios returned.
    portfolios=[],  # required — The portfolios matching the applicability filter, up to the requested limit.
    has_more_portfolios=True  # required — Whether more portfolios match the filter than were returned.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md) — used in `portfolios`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

