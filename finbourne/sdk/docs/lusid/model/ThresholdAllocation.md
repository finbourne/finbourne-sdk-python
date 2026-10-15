# ThresholdAllocation

How a threshold is split between the two parties.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **we** | **float** | Required | Our share of the threshold. |
| **they** | **float** | Required | The counterparty&#39;s share of the threshold. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ThresholdAllocation import ThresholdAllocation

instance = ThresholdAllocation(
    we=0.0,  # required — Our share of the threshold.
    they=0.0  # required — The counterparty&#39;s share of the threshold.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

