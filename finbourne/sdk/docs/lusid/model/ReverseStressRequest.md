# ReverseStressRequest

Request to solve a reverse stress test: instead of asking what a given market move does to a  portfolio, it asks how far the market has to move along a given direction to produce a given  loss. The direction is a stored scenario; the answer is the factor its shifts are multiplied by.                A single effective date is solved, not a schedule. \"How far must the market move to lose this  much\" has one answer per date, and returning a factor per date under one target would invite the  answer being read as a single portfolio-wide number when it is not.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **recipe_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **portfolio_entity_ids** | [List[PortfolioEntityId]](PortfolioEntityId.md) | Required | The portfolios or portfolio groups whose value the target loss is measured against. |
| **effective_at** | **datetime** | Required | The effective date to value at. |
| **as_at** | **datetime** | Optional | The as-at time to read portfolios, instruments, market data and the scenario definition at.  Defaults to the latest. |
| **scenario** | [ScenarioReference](ScenarioReference.md) | Required | *No description available.* |
| **target_pnl** | **float** | Required | The change in value to solve for, signed and in the report currency: negative for a loss.  Expressed as an amount rather than a percentage so that the same target can be stated against  a portfolio whose base value is not known to the caller. |
| **metric** | **str** | Optional | The measure the target is expressed in. Defaults to Valuation/PV. Must be a measure that  supports scenario decoration, which the request is rejected for if it is not. |
| **report_currency** | **str** | Optional | Three to five letter currency string to report in. If absent the portfolio&#39;s own currency is used,  which makes the target ambiguous across a multi-currency portfolio group - supply it there. |
| **filters** | [List[PropertyFilter]](PropertyFilter.md) | Optional | Filters reducing the holdings the target is measured over, matching the valuation endpoint&#39;s. |
| **max_scale** | **float** | Optional | The largest factor to evaluate. A target beyond the loss reached at this factor is reported as  out of reach rather than extrapolated to: extrapolating past the evaluated range is exactly  where a locally linear P&amp;L stops being linear. |
| **ladder_points** | **int** | Optional | How many factors to evaluate between zero and MaxScale. All of them are valued in  one request - the rungs share market data resolution - so a finer ladder costs far less than  its rung count suggests, and a coarse one is the main source of a missed bracket. |
| **tolerance** | **float** | Optional | How close the achieved loss must be to the target, relative to the target&#39;s own size. Relative  rather than absolute because the same reverse stress is asked of books whose value differs by  orders of magnitude. |
| **max_iterations** | **int** | Optional | How many refinement rounds are allowed after the opening ladder. Each round costs one  valuation; on a near-linear P&amp;L the first interpolation is usually already inside tolerance,  so the default exists for the mildly curved case rather than the normal one. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ReverseStressRequest import ReverseStressRequest

instance = ReverseStressRequest(
    recipe_id=ResourceId(...),  # required
    portfolio_entity_ids=[],  # required — The portfolios or portfolio groups whose value the target loss is measured against.
    effective_at=datetime.now(),  # required — The effective date to value at.
    as_at=datetime.now(),  # optional — The as-at time to read portfolios, instruments, market data and the scenario definition at.  Defaults to the latest.
    scenario=ScenarioReference(...),  # required
    target_pnl=0.0,  # required — The change in value to solve for, signed and in the report currency: negative for a loss.  Expressed as an amount rather than a percentage so that the same target can be stated against  a portfolio whose base value is not known to the caller.
    metric="...",  # optional — The measure the target is expressed in. Defaults to Valuation/PV. Must be a measure that  supports scenario decoration, which the request is rejected for if it is not.
    report_currency="...",  # optional — Three to five letter currency string to report in. If absent the portfolio&#39;s own currency is used,  which makes the target ambiguous across a multi-currency portfolio group - supply it there.
    filters=[],  # optional — Filters reducing the holdings the target is measured over, matching the valuation endpoint&#39;s.
    max_scale=0.0,  # optional — The largest factor to evaluate. A target beyond the loss reached at this factor is reported as  out of reach rather than extrapolated to: extrapolating past the evaluated range is exactly  where a locally linear P&amp;L stops being linear.
    ladder_points=0,  # optional — How many factors to evaluate between zero and MaxScale. All of them are valued in  one request - the rungs share market data resolution - so a finer ladder costs far less than  its rung count suggests, and a coarse one is the main source of a missed bracket.
    tolerance=0.0,  # optional — How close the achieved loss must be to the target, relative to the target&#39;s own size. Relative  rather than absolute because the same reverse stress is asked of books whose value differs by  orders of magnitude.
    max_iterations=0  # optional — How many refinement rounds are allowed after the opening ladder. Each round costs one  valuation; on a near-linear P&amp;L the first interpolation is usually already inside tolerance,  so the default exists for the mildly curved case rather than the normal one.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [PortfolioEntityId](PortfolioEntityId.md) — used in `portfolio_entity_ids`
- [ScenarioReference](ScenarioReference.md)
- [PropertyFilter](PropertyFilter.md) — used in `filters`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

