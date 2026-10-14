# FundPartner

A register line of a partnership fund: one partner's commitment and its capital balances at an effective date.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **investor_record_id** | **str** | Required | The identifier of the investor record this register line belongs to. |
| **display_name** | **str** | Optional | The display name of the partner. |
| **commitment_line_id** | **str** | Required | The identifier of the commitment (register) line. |
| **lusid_instrument_id** | **str** | Required | The LUSID instrument identifier of the register line&#39;s capital-interest instrument. |
| **portfolio_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **is_vehicle** | **bool** | Required | Whether the partner is a vehicle (for example a feeder or parallel fund) rather than an end investor. |
| **partner_role** | **str** | Required | The role of the register line. Available values: GPRegister, LPInvestment. |
| **commitment_currency** | **str** | Required | The currency of the partner&#39;s commitment. |
| **balances** | [FundPartnerBalances](FundPartnerBalances.md) | Required | *No description available.* |
| **share_of_commitments** | **float** | Required | The partner&#39;s committed capital as a decimal fraction of the fund&#39;s total commitments. |
| **admitted_on** | **datetime** | Optional | The date the partner was admitted, being the date of their first commitment. |
| **totals** | [FundPartnersTotals](FundPartnersTotals.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundPartner import FundPartner

instance = FundPartner(
    investor_record_id="...",  # required — The identifier of the investor record this register line belongs to.
    display_name="...",  # optional — The display name of the partner.
    commitment_line_id="...",  # required — The identifier of the commitment (register) line.
    lusid_instrument_id="...",  # required — The LUSID instrument identifier of the register line&#39;s capital-interest instrument.
    portfolio_id=ResourceId(...),  # required
    is_vehicle=True,  # required — Whether the partner is a vehicle (for example a feeder or parallel fund) rather than an end investor.
    partner_role="...",  # required — The role of the register line. Available values: GPRegister, LPInvestment.
    commitment_currency="...",  # required — The currency of the partner&#39;s commitment.
    balances=FundPartnerBalances(...),  # required
    share_of_commitments=0.0,  # required — The partner&#39;s committed capital as a decimal fraction of the fund&#39;s total commitments.
    admitted_on=datetime.now(),  # optional — The date the partner was admitted, being the date of their first commitment.
    totals=FundPartnersTotals(...)  # required
)
```

- [ResourceId](ResourceId.md)
- [FundPartnerBalances](FundPartnerBalances.md)
- [FundPartnersTotals](FundPartnersTotals.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

