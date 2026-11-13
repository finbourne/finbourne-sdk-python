# TaxReturnDisposalRow

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **holding_id** | **str** | Optional | The identifier of the holding. For a company this is the pooled LUSID instrument identifier, for a fund the portfolio code and instrument identifier. |
| **instrument_id** | **str** | Optional | The LUSID unique identifier of the instrument. |
| **instrument_name** | **str** | Optional | The name of the instrument. |
| **portfolio_code** | **str** | Optional | The code of the portfolio the holding sits in, or the pooled marker for a company. |
| **disposal_date** | **datetime** | Optional | The date of the disposal. |
| **units** | **float** | Optional | The units disposed of. |
| **cost** | **float** | Optional | The allowable cost of the units disposed of. |
| **indexation_allowance_taken** | **float** | Optional | The indexation allowance deducted when arriving at the chargeable gain. |
| **chargeable_gain** | **float** | Optional | The chargeable gain or allowable loss on the disposal, negative for a loss. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TaxReturnDisposalRow import TaxReturnDisposalRow

instance = TaxReturnDisposalRow(
    holding_id="...",  # optional — The identifier of the holding. For a company this is the pooled LUSID instrument identifier, for a fund the portfolio code and instrument identifier.
    instrument_id="...",  # optional — The LUSID unique identifier of the instrument.
    instrument_name="...",  # optional — The name of the instrument.
    portfolio_code="...",  # optional — The code of the portfolio the holding sits in, or the pooled marker for a company.
    disposal_date=datetime.now(),  # optional — The date of the disposal.
    units=0.0,  # optional — The units disposed of.
    cost=0.0,  # optional — The allowable cost of the units disposed of.
    indexation_allowance_taken=0.0,  # optional — The indexation allowance deducted when arriving at the chargeable gain.
    chargeable_gain=0.0  # optional — The chargeable gain or allowable loss on the disposal, negative for a loss.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

