# SideDefinitionRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **security** | **str** | Required | The field or property key defining the side&#39;s security, or instrument. |
| **currency** | **str** | Required | The field or property key defining the side&#39;s currency. |
| **rate** | **str** | Required | The field or property key defining the side&#39;s rate. |
| **units** | **str** | Required | The value, field or property key defining the side&#39;s units. |
| **amount** | **str** | Required | The value, field or property key defining the side&#39;s amount |
| **notional_amount** | **str** | Optional | The value, field or property key defining the side&#39;s notional amount |
| **current_face** | **str** | Optional | The value, field or property key defining the side&#39;s current face / outstanding notional. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SideDefinitionRequest import SideDefinitionRequest

instance = SideDefinitionRequest(
    security="...",  # required — The field or property key defining the side&#39;s security, or instrument.
    currency="...",  # required — The field or property key defining the side&#39;s currency.
    rate="...",  # required — The field or property key defining the side&#39;s rate.
    units="...",  # required — The value, field or property key defining the side&#39;s units.
    amount="...",  # required — The value, field or property key defining the side&#39;s amount
    notional_amount="...",  # optional — The value, field or property key defining the side&#39;s notional amount
    current_face="..."  # optional — The value, field or property key defining the side&#39;s current face / outstanding notional.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

