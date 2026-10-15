# ManagementFeeOffset

A fee income the manager has earned elsewhere that offsets the management fee.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **source_ref** | **str** | Required | A reference to the fee income being offset. |
| **amount** | **float** | Required | The amount of fee income received. |
| **offset_percentage** | **float** | Required | The fraction of the fee income that offsets the management fee, between 0 and 1. |
| **deal** | **str** | Optional | For a deal-linked offset, the deal the fee income relates to. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ManagementFeeOffset import ManagementFeeOffset

instance = ManagementFeeOffset(
    source_ref="...",  # required — A reference to the fee income being offset.
    amount=0.0,  # required — The amount of fee income received.
    offset_percentage=0.0,  # required — The fraction of the fee income that offsets the management fee, between 0 and 1.
    deal="..."  # optional — For a deal-linked offset, the deal the fee income relates to.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

