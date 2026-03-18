# HoldingsAdjustment

Full content of a holdings adjustment for a single portfolio and effective date.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **effective_at** | **datetime** | Required | The effective datetime from which the adjustment is valid. There can only be one holdings adjustment for a transaction portfolio at a specific effective datetime, so this uniquely identifies the adjustment. |
| **version** | [Version](Version.md) | Required | *No description available.* |
| **unmatched_holding_method** | **str** | Required | Describes how the holdings were adjusted. If &#39;PositionToZero&#39; the entire transaction portfolio&#39;s holdings were set via a call to &#39;Set holdings&#39;. If &#39;KeepTheSame&#39; only the specified holdings were adjusted via a call to &#39;Adjust holdings&#39;. The available values are: PositionToZero, KeepTheSame |
| **adjustments** | [List[HoldingAdjustment]](HoldingAdjustment.md) | Required | The holding adjustments. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.HoldingsAdjustment import HoldingsAdjustment

instance = HoldingsAdjustment(
    effective_at=datetime.now(),  # required — The effective datetime from which the adjustment is valid. There can only be one holdings adjustment for a transaction portfolio at a specific effective datetime, so this uniquely identifies the adjustment.
    version=Version(...),  # required
    unmatched_holding_method="...",  # required — Describes how the holdings were adjusted. If &#39;PositionToZero&#39; the entire transaction portfolio&#39;s holdings were set via a call to &#39;Set holdings&#39;. If &#39;KeepTheSame&#39; only the specified holdings were adjusted via a call to &#39;Adjust holdings&#39;. The available values are: PositionToZero, KeepTheSame
    adjustments=[],  # required — The holding adjustments.
    links=[]  # optional
)
```

- [Version](Version.md)
- [HoldingAdjustment](HoldingAdjustment.md) — used in `adjustments`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

