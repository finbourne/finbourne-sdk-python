# RecExceptionCountByResultType

Exception result counts broken down by result type.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **var_break** | **int** | Required | The number of Break results. |
| **partial_match** | **int** | Required | The number of Partial Match results. |
| **partial_cross** | **int** | Required | The number of Partial Cross results. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecExceptionCountByResultType import RecExceptionCountByResultType

instance = RecExceptionCountByResultType(
    var_break=0,  # required — The number of Break results.
    partial_match=0,  # required — The number of Partial Match results.
    partial_cross=0  # required — The number of Partial Cross results.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

