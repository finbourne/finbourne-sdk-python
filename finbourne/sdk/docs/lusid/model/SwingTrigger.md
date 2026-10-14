# SwingTrigger

When a Market swing fires in one direction: the net cashflow measure and the size it must exceed.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Required | What the threshold measures: NetCashflowAbsolute, the size of the net cashflow in the fund currency, or NetCashflowPctOfNav, the net cashflow as a percentage of the previous valuation point&#39;s NAV. A NetCashflowPctOfNav trigger does not fire when there is no previous NAV. Available values: NetCashflowAbsolute, NetCashflowPctOfNav. |
| **threshold** | **float** | Required | The size of net cashflow, as a magnitude, the flow must be above for the trigger to fire. Above zero. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SwingTrigger import SwingTrigger

instance = SwingTrigger(
    type="...",  # required — What the threshold measures: NetCashflowAbsolute, the size of the net cashflow in the fund currency, or NetCashflowPctOfNav, the net cashflow as a percentage of the previous valuation point&#39;s NAV. A NetCashflowPctOfNav trigger does not fire when there is no previous NAV. Available values: NetCashflowAbsolute, NetCashflowPctOfNav.
    threshold=0.0  # required — The size of net cashflow, as a magnitude, the flow must be above for the trigger to fire. Above zero.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

