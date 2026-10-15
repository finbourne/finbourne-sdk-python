# AllocationGroupClassDefinition

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **share_class_short_code** | **str** | Required | A short code that uniquely identifies the share class within the Fund and is attached to the transaction. |
| **apportionment_factor** | **float** | Optional | Only used for fixed percentage method or be zero, must equal 1 or 0 across all classes in the fund. |
| **share_class_series_code** | **str** | Optional | The series of the share class the member refers to. Not yet supported: an allocation group is apportioned by share class, so a member that names a series is rejected. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationGroupClassDefinition import AllocationGroupClassDefinition

instance = AllocationGroupClassDefinition(
    share_class_short_code="...",  # required — A short code that uniquely identifies the share class within the Fund and is attached to the transaction.
    apportionment_factor=0.0,  # optional — Only used for fixed percentage method or be zero, must equal 1 or 0 across all classes in the fund.
    share_class_series_code="..."  # optional — The series of the share class the member refers to. Not yet supported: an allocation group is apportioned by share class, so a member that names a series is rejected.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

