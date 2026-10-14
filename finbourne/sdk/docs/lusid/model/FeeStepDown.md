# FeeStepDown

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **trigger** | **str** | Required | Available values: EndOfInvestmentPeriod, Date, Closing. |
| **step_down_date** | **datetime** | Optional | *No description available.* |
| **closing_id** | **str** | Optional | *No description available.* |
| **rate** | **float** | Optional | *No description available.* |
| **basis** | **str** | Optional | Available values: CommittedCapital, InvestedCapital, NetInvestedCapital, Nav. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FeeStepDown import FeeStepDown

instance = FeeStepDown(
    trigger="...",  # required — Available values: EndOfInvestmentPeriod, Date, Closing.
    step_down_date=datetime.now(),  # optional
    closing_id="...",  # optional
    rate=0.0,  # optional
    basis="..."  # optional — Available values: CommittedCapital, InvestedCapital, NetInvestedCapital, Nav.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

