# TaxReconciliationBridgeRow

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **label** | **str** | Optional | The label of the period, for example the four-digit year. |
| **amount** | **float** | Optional | The amount, in pounds. |
| **running_total** | **float** | Optional | The running total after this step of the bridge. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TaxReconciliationBridgeRow import TaxReconciliationBridgeRow

instance = TaxReconciliationBridgeRow(
    label="...",  # optional — The label of the period, for example the four-digit year.
    amount=0.0,  # optional — The amount, in pounds.
    running_total=0.0  # optional — The running total after this step of the bridge.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

