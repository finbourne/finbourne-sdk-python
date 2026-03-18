# SideConfigurationDataRequest

Configuration needed to define a side. Sides are referenced by Label. Beyond that, other properties  can be used to reference either transaction fields, or transaction properties.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **side** | **str** | Required | The side&#39;s label. |
| **security** | **str** | Required | The security, or instrument. |
| **currency** | **str** | Required | The currency. |
| **rate** | **str** | Required | The rate. |
| **units** | **str** | Required | The units. |
| **amount** | **str** | Required | The amount. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SideConfigurationDataRequest import SideConfigurationDataRequest

instance = SideConfigurationDataRequest(
    side="...",  # required — The side&#39;s label.
    security="...",  # required — The security, or instrument.
    currency="...",  # required — The currency.
    rate="...",  # required — The rate.
    units="...",  # required — The units.
    amount="..."  # required — The amount.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

