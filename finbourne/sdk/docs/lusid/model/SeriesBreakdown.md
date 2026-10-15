# SeriesBreakdown

The valuation of one series within a share class at a valuation point.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **series_identifier** | **str** | Required | The identifier of the series within its share class. |
| **units** | **float** | Required | The units in issue in the series at the valuation point. |
| **nav** | **float** | Required | The series&#39; share of the share class NAV, in the fund currency. |
| **nav_per_unit** | **float** | Required | The series NAV per unit in the share class currency, rounded as the share class unit price is. |
| **capital_ratio** | **float** | Required | The series&#39; opening NAV as a proportion of the share class&#39;s opening NAV. Zero for a series with no units; sums to 1 across the series that hold units. |
| **pnl** | **float** | Required | The P&amp;L apportioned to the series in the period: its NAV less its opening NAV. |
| **previous_nav** | **float** | Required | The series NAV at the previous valuation point, in the fund currency. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SeriesBreakdown import SeriesBreakdown

instance = SeriesBreakdown(
    series_identifier="...",  # required — The identifier of the series within its share class.
    units=0.0,  # required — The units in issue in the series at the valuation point.
    nav=0.0,  # required — The series&#39; share of the share class NAV, in the fund currency.
    nav_per_unit=0.0,  # required — The series NAV per unit in the share class currency, rounded as the share class unit price is.
    capital_ratio=0.0,  # required — The series&#39; opening NAV as a proportion of the share class&#39;s opening NAV. Zero for a series with no units; sums to 1 across the series that hold units.
    pnl=0.0,  # required — The P&amp;L apportioned to the series in the period: its NAV less its opening NAV.
    previous_nav=0.0  # required — The series NAV at the previous valuation point, in the fund currency.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

