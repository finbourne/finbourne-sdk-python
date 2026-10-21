# WithholdingTaxRateSplit

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **stop_at_source_rate** | **float** | Required | The rate withheld at source. |
| **irrecoverable_rate** | **float** | Required | The part of the country rate that cannot be recovered. |
| **relief_at_source_rate** | **float** | Required | The part of the country rate relieved at source. |
| **reclaimable_rate** | **float** | Required | The part of the rate withheld at source that can be reclaimed. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.WithholdingTaxRateSplit import WithholdingTaxRateSplit

instance = WithholdingTaxRateSplit(
    stop_at_source_rate=0.0,  # required — The rate withheld at source.
    irrecoverable_rate=0.0,  # required — The part of the country rate that cannot be recovered.
    relief_at_source_rate=0.0,  # required — The part of the country rate relieved at source.
    reclaimable_rate=0.0  # required — The part of the rate withheld at source that can be reclaimed.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

