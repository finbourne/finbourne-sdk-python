# RecExceptionCountByClosureType

Closed exception result counts broken down by closure type.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **cleared** | **int** | Required | The number of Cleared results. |
| **accepted** | **int** | Required | The number of Accepted results. |
| **force_matched** | **int** | Required | The number of Force Matched results. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecExceptionCountByClosureType import RecExceptionCountByClosureType

instance = RecExceptionCountByClosureType(
    cleared=0,  # required — The number of Cleared results.
    accepted=0,  # required — The number of Accepted results.
    force_matched=0  # required — The number of Force Matched results.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

