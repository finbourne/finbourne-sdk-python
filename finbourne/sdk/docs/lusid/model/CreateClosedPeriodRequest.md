# CreateClosedPeriodRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **closed_period_id** | **str** | Required | The unique Id of the Closed Period. The ClosedPeriodId, together with the Timeline Scope and Code, uniquely identifies a Closed Period |
| **effective_end** | **datetime** | Optional | The effective end of the Closed Period |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | The Closed Periods properties. These will be from the &#39;ClosedPeriod&#39; domain. |
| **as_at_closed** | **datetime** | Optional | The asAt closed datetime for the Closed Period |
| **display_name** | **str** | Optional | The name of the Closed Period. |
| **description** | **str** | Optional | A description for the Closed Period. |
| **holdings_as_at_closed_override** | **datetime** | Optional | The optional AsAtClosed Override to use for building holdings in the Closed Period.If not specified, the AsAtClosed on the Closed Period will be used. |
| **valuation_as_at_closed_override** | **datetime** | Optional | The optional AsAtClosed Override to use for performing valuations in the Closed Period.If not specified, the AsAtClosed on the Closed Period will be used. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CreateClosedPeriodRequest import CreateClosedPeriodRequest

instance = CreateClosedPeriodRequest(
    closed_period_id="...",  # required — The unique Id of the Closed Period. The ClosedPeriodId, together with the Timeline Scope and Code, uniquely identifies a Closed Period
    effective_end=datetime.now(),  # optional — The effective end of the Closed Period
    properties=ModelProperty(...),  # optional — The Closed Periods properties. These will be from the &#39;ClosedPeriod&#39; domain.
    as_at_closed=datetime.now(),  # optional — The asAt closed datetime for the Closed Period
    display_name="...",  # optional — The name of the Closed Period.
    description="...",  # optional — A description for the Closed Period.
    holdings_as_at_closed_override=datetime.now(),  # optional — The optional AsAtClosed Override to use for building holdings in the Closed Period.If not specified, the AsAtClosed on the Closed Period will be used.
    valuation_as_at_closed_override=datetime.now()  # optional — The optional AsAtClosed Override to use for performing valuations in the Closed Period.If not specified, the AsAtClosed on the Closed Period will be used.
)
```

- [ModelProperty](ModelProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

