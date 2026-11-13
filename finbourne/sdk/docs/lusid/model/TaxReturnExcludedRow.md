# TaxReturnExcludedRow

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **holding_id** | **str** | Optional | The identifier of the holding. For a company this is the pooled LUSID instrument identifier, for a fund the portfolio code and instrument identifier. |
| **instrument_id** | **str** | Optional | The LUSID unique identifier of the instrument. |
| **instrument_name** | **str** | Optional | The name of the instrument. |
| **portfolio_code** | **str** | Optional | The code of the portfolio the holding sits in, or the pooled marker for a company. |
| **reason** | **str** | Optional | Why the holding is outside the return. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TaxReturnExcludedRow import TaxReturnExcludedRow

instance = TaxReturnExcludedRow(
    holding_id="...",  # optional — The identifier of the holding. For a company this is the pooled LUSID instrument identifier, for a fund the portfolio code and instrument identifier.
    instrument_id="...",  # optional — The LUSID unique identifier of the instrument.
    instrument_name="...",  # optional — The name of the instrument.
    portfolio_code="...",  # optional — The code of the portfolio the holding sits in, or the pooled marker for a company.
    reason="..."  # optional — Why the holding is outside the return.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

