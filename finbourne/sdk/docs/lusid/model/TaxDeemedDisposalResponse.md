# TaxDeemedDisposalResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | **str** | Optional | The deterministic identifier of the deemed disposal, derived from the holding and date. |
| **holding_id** | **str** | Optional | The identifier of the holding. For a company this is the pooled LUSID instrument identifier, for a fund the portfolio code and instrument identifier. |
| **instrument_id** | **str** | Optional | The LUSID unique identifier of the instrument. |
| **instrument_name** | **str** | Optional | The name of the instrument. |
| **portfolio_code** | **str** | Optional | The code of the portfolio the holding sits in, or the pooled marker for a company. |
| **var_date** | **datetime** | Optional | The date the deemed disposal arises, the end of the period. |
| **units** | **float** | Optional | The units disposed of. |
| **cost** | **float** | Optional | The allowable cost of the units disposed of. |
| **market_value** | **float** | Optional | The market value of the holding at the deemed-disposal date. |
| **net_amount** | **float** | Optional | The net deemed amount, gains less losses. |
| **notional** | **bool** | Optional | True when the deemed disposal is notional, as it is for a member fund, rather than an actual deemed disposal at company level. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TaxDeemedDisposalResponse import TaxDeemedDisposalResponse

instance = TaxDeemedDisposalResponse(
    id="...",  # optional — The deterministic identifier of the deemed disposal, derived from the holding and date.
    holding_id="...",  # optional — The identifier of the holding. For a company this is the pooled LUSID instrument identifier, for a fund the portfolio code and instrument identifier.
    instrument_id="...",  # optional — The LUSID unique identifier of the instrument.
    instrument_name="...",  # optional — The name of the instrument.
    portfolio_code="...",  # optional — The code of the portfolio the holding sits in, or the pooled marker for a company.
    var_date=datetime.now(),  # optional — The date the deemed disposal arises, the end of the period.
    units=0.0,  # optional — The units disposed of.
    cost=0.0,  # optional — The allowable cost of the units disposed of.
    market_value=0.0,  # optional — The market value of the holding at the deemed-disposal date.
    net_amount=0.0,  # optional — The net deemed amount, gains less losses.
    notional=True  # optional — True when the deemed disposal is notional, as it is for a member fund, rather than an actual deemed disposal at company level.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

