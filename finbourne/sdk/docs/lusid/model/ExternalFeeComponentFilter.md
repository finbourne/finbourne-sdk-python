# ExternalFeeComponentFilter

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **filter_id** | **str** | Required | *No description available.* |
| **filter** | **str** | Required | *No description available.* |
| **applies_to** | **str** | Required | Available values: Undefined, PnLBucket, Fees. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ExternalFeeComponentFilter import ExternalFeeComponentFilter

instance = ExternalFeeComponentFilter(
    filter_id="...",  # required
    filter="...",  # required
    applies_to="..."  # required — Available values: Undefined, PnLBucket, Fees.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

