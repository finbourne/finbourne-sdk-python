# MarginCalculation

How the margin requirement for an item is calculated. The method field selects the method and the  remaining fields are the ones that method uses.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **method** | **str** | Required | The calculation method. One of NetMtm, Ccp, GmraExposure, GmslaRcv, HouseRules, Simm, RegulatoryGrid or CcpIngested. Available values: NetMtm, Ccp, GmraExposure, GmslaRcv, HouseRules, Simm, RegulatoryGrid, CcpIngested. |
| **exposure_method** | **str** | Optional | For GmraExposure, the exposure method. One of Gmra2011A or Gmra2011B. Available values: Gmra2011A, Gmra2011B. |
| **repricing_permitted** | **bool** | Optional | For GmraExposure, whether repricing is permitted. |
| **margin_percentage** | **float** | Optional | For GmslaRcv, the margin percentage applied to the loan value. |
| **lending_fee_bps** | **int** | Optional | For GmslaRcv, the lending fee in basis points. |
| **credit_line** | **float** | Optional | For HouseRules, the credit line extended to the counterparty. |
| **threshold_allocation** | [ThresholdAllocation](ThresholdAllocation.md) | Optional | *No description available.* |
| **ccp** | **str** | Optional | For CcpIngested, the name of the central counterparty. |
| **fcm_add_on** | **float** | Optional | For CcpIngested, the add-on charged by the futures commission merchant. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.MarginCalculation import MarginCalculation

instance = MarginCalculation(
    method="...",  # required — The calculation method. One of NetMtm, Ccp, GmraExposure, GmslaRcv, HouseRules, Simm, RegulatoryGrid or CcpIngested. Available values: NetMtm, Ccp, GmraExposure, GmslaRcv, HouseRules, Simm, RegulatoryGrid, CcpIngested.
    exposure_method="...",  # optional — For GmraExposure, the exposure method. One of Gmra2011A or Gmra2011B. Available values: Gmra2011A, Gmra2011B.
    repricing_permitted=True,  # optional — For GmraExposure, whether repricing is permitted.
    margin_percentage=0.0,  # optional — For GmslaRcv, the margin percentage applied to the loan value.
    lending_fee_bps=0,  # optional — For GmslaRcv, the lending fee in basis points.
    credit_line=0.0,  # optional — For HouseRules, the credit line extended to the counterparty.
    threshold_allocation=ThresholdAllocation(...),  # optional
    ccp="...",  # optional — For CcpIngested, the name of the central counterparty.
    fcm_add_on=0.0  # optional — For CcpIngested, the add-on charged by the futures commission merchant.
)
```

- [ThresholdAllocation](ThresholdAllocation.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

