# BucketDefinition

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **bucket_id** | **str** | Required | *No description available.* |
| **display_name** | **str** | Required | *No description available.* |
| **filter_expression** | **str** | Required | *No description available.* |
| **bucket_type** | **str** | Required | Available values: Dealing, PnL, Fees, BalanceSheet, Misc. |
| **unitised** | **bool** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BucketDefinition import BucketDefinition

instance = BucketDefinition(
    bucket_id="...",  # required
    display_name="...",  # required
    filter_expression="...",  # required
    bucket_type="...",  # required — Available values: Dealing, PnL, Fees, BalanceSheet, Misc.
    unitised=True  # optional
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

