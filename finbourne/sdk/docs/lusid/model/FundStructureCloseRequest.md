# FundStructureCloseRequest

The request to close a fund structure: finalise the named valuation point on every member, members first.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **valuation_point_code** | **str** | Required | The code of the valuation point to finalise on every member fund. |
| **nav_type_code** | **str** | Optional | The NAV type to finalise under. Defaults to each fund&#39;s primary NAV type. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundStructureCloseRequest import FundStructureCloseRequest

instance = FundStructureCloseRequest(
    valuation_point_code="...",  # required — The code of the valuation point to finalise on every member fund.
    nav_type_code="..."  # optional — The NAV type to finalise under. Defaults to each fund&#39;s primary NAV type.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

