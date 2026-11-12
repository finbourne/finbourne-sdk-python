# TaxClassificationFieldVersion

One stored value of a classification input or override and the bitemporal window it held for.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **var_field** | **str** | Required | The name of the classification input or override the version belongs to. |
| **value** | **str** | Optional | The value of the field over the version&#39;s effective and asAt window. |
| **effective_from** | **datetime** | Required | The start of the effective window the value applies from. |
| **effective_until** | **datetime** | Required | The end of the effective window the value applies until. |
| **as_at_from** | **datetime** | Required | The asAt time the value was recorded. |
| **as_at_until** | **datetime** | Optional | The asAt time the value was superseded, if it has been. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TaxClassificationFieldVersion import TaxClassificationFieldVersion

instance = TaxClassificationFieldVersion(
    var_field="...",  # required — The name of the classification input or override the version belongs to.
    value="...",  # optional — The value of the field over the version&#39;s effective and asAt window.
    effective_from=datetime.now(),  # required — The start of the effective window the value applies from.
    effective_until=datetime.now(),  # required — The end of the effective window the value applies until.
    as_at_from=datetime.now(),  # required — The asAt time the value was recorded.
    as_at_until=datetime.now()  # optional — The asAt time the value was superseded, if it has been.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

