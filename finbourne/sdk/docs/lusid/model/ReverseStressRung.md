# ReverseStressRung

One evaluated factor and what the portfolio was worth under it.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **scale** | **float** | Optional | The factor the scenario&#39;s shifts were multiplied by. |
| **value** | **float** | Optional | The value of the measure under the scaled scenario. |
| **pnl** | **float** | Optional | The change from the unstressed value. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ReverseStressRung import ReverseStressRung

instance = ReverseStressRung(
    scale=0.0,  # optional — The factor the scenario&#39;s shifts were multiplied by.
    value=0.0,  # optional — The value of the measure under the scaled scenario.
    pnl=0.0  # optional — The change from the unstressed value.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

