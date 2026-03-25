# AllocationGroupClass

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **share_class_short_code** | **str** | Required | A short code that uniquely identifies the share class within the Fund and is attached to the transaction. |
| **share_class_fund_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **apportionment_factor** | **float** | Optional | The weighting factor used for apportionment across this share class. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationGroupClass import AllocationGroupClass

instance = AllocationGroupClass(
    share_class_short_code="...",  # required — A short code that uniquely identifies the share class within the Fund and is attached to the transaction.
    share_class_fund_id=ResourceId(...),  # optional
    apportionment_factor=0.0  # optional — The weighting factor used for apportionment across this share class.
)
```

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

