# TaxAccountingPeriod

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **label** | **str** | Optional | The label of the period, for example the four-digit year. |
| **start** | **datetime** | Optional | The first day of the period, inclusive. |
| **end** | **datetime** | Optional | The last day of the period, inclusive. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TaxAccountingPeriod import TaxAccountingPeriod

instance = TaxAccountingPeriod(
    label="...",  # optional — The label of the period, for example the four-digit year.
    start=datetime.now(),  # optional — The first day of the period, inclusive.
    end=datetime.now()  # optional — The last day of the period, inclusive.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

