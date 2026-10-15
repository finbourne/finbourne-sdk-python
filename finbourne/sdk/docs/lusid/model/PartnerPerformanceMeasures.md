# PartnerPerformanceMeasures

One set of performance measures: the multiples, the net IRR and the cash flows it was solved from.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
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


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PartnerPerformanceMeasures import PartnerPerformanceMeasures

instance = PartnerPerformanceMeasures(
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
    residual_value_date=datetime.now()  # required — The date the residual value is taken as at.
)
```

- [PartnerPerformanceCashFlow](PartnerPerformanceCashFlow.md) — used in `cash_flows`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

