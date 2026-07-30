# RecExecution

The execution outcome for a run.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **outcome** | **str** | Required | The execution outcome. Available values: Succeeded, Failed. |
| **error_detail** | **str** | Optional | Detail of the execution failure. Populated when outcome is Failed. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecExecution import RecExecution

instance = RecExecution(
    outcome="...",  # required — The execution outcome. Available values: Succeeded, Failed.
    error_detail="..."  # optional — Detail of the execution failure. Populated when outcome is Failed.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

