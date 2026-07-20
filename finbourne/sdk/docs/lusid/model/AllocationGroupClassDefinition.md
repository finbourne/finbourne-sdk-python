# AllocationGroupClassDefinition

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **share_class_short_code** | **str** | Required | A short code that uniquely identifies the share class within the Fund and is attached to the transaction. |
| **apportionment_factor** | **float** | Optional | Only used for fixed percentage method or be zero, must equal 1 or 0 across all classes in the fund. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationGroupClassDefinition import AllocationGroupClassDefinition

instance = AllocationGroupClassDefinition(
    share_class_short_code="...",  # required — A short code that uniquely identifies the share class within the Fund and is attached to the transaction.
    apportionment_factor=0.0  # optional — Only used for fixed percentage method or be zero, must equal 1 or 0 across all classes in the fund.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

