# PartnerPerformance

The ILPA performance measures for one partner, or for the fund as a whole: paid-in to commitment, the  distribution, residual value and total value multiples, and the net IRR, together with the cash flows the IRR  was solved from. When the fund financed deals through a subscription facility, the measures are also given  with the facility-funded calls re-dated to when the deals were actually funded.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **fund_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **investor_record_id** | **str** | Optional | The investor record identifier of the partner, or null when the figures are for the fund as a whole. |
| **currency** | **str** | Required | The currency the cash flows and residual value are expressed in. |
| **commitment** | **float** | Required | The total commitment the paid-in-capital ratio is measured against. |
| **paid_in** | **float** | Required | The contributions paid in to the fund. |
| **distributed** | **float** | Required | The distributions paid out of the fund. |
| **pic** | **float** | Optional | Paid-in capital as a multiple of commitment, or null when there is no commitment. |
| **dpi** | **float** | Optional | Distributions as a multiple of paid-in capital, or null when nothing has been paid in. |
| **rvpi** | **float** | Optional | Residual value as a multiple of paid-in capital, or null when nothing has been paid in. |
| **tvpi** | **float** | Optional | Total value as a multiple of paid-in capital, being DPI plus RVPI. |
| **net_irr** | **float** | Optional | The annualised net internal rate of return solved from the dated cash flows, or null when no rate can be solved. |
| **cash_flows** | [List[PartnerPerformanceCashFlow]](PartnerPerformanceCashFlow.md) | Required | The dated cash flows the net IRR was solved from, including the terminal residual value. |
| **residual_value** | **float** | Required | The partner&#39;s residual value in the fund at the valuation date. |
| **residual_value_date** | **datetime** | Required | The date the residual value is taken as at. |
| **with_facility** | [PartnerPerformanceMeasures](PartnerPerformanceMeasures.md) | Optional | *No description available.* |
| **without_facility** | [PartnerPerformanceMeasures](PartnerPerformanceMeasures.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PartnerPerformance import PartnerPerformance

instance = PartnerPerformance(
    fund_id=ResourceId(...),  # required
    investor_record_id="...",  # optional — The investor record identifier of the partner, or null when the figures are for the fund as a whole.
    currency="...",  # required — The currency the cash flows and residual value are expressed in.
    commitment=0.0,  # required — The total commitment the paid-in-capital ratio is measured against.
    paid_in=0.0,  # required — The contributions paid in to the fund.
    distributed=0.0,  # required — The distributions paid out of the fund.
    pic=0.0,  # optional — Paid-in capital as a multiple of commitment, or null when there is no commitment.
    dpi=0.0,  # optional — Distributions as a multiple of paid-in capital, or null when nothing has been paid in.
    rvpi=0.0,  # optional — Residual value as a multiple of paid-in capital, or null when nothing has been paid in.
    tvpi=0.0,  # optional — Total value as a multiple of paid-in capital, being DPI plus RVPI.
    net_irr=0.0,  # optional — The annualised net internal rate of return solved from the dated cash flows, or null when no rate can be solved.
    cash_flows=[],  # required — The dated cash flows the net IRR was solved from, including the terminal residual value.
    residual_value=0.0,  # required — The partner&#39;s residual value in the fund at the valuation date.
    residual_value_date=datetime.now(),  # required — The date the residual value is taken as at.
    with_facility=PartnerPerformanceMeasures(...),  # optional
    without_facility=PartnerPerformanceMeasures(...)  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [PartnerPerformanceCashFlow](PartnerPerformanceCashFlow.md) — used in `cash_flows`
- [PartnerPerformanceMeasures](PartnerPerformanceMeasures.md)
- [PartnerPerformanceMeasures](PartnerPerformanceMeasures.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

