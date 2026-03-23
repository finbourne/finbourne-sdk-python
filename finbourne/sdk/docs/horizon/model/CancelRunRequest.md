# CancelRunRequest

A request to cancel the specified instance execution.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **run_ids** | **List[str]** | Required | The instance run ids to be cancelled. |
| **message** | **str** | Optional | The user provided message as to why the instance executions were cancelled. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.CancelRunRequest import CancelRunRequest

instance = CancelRunRequest(
    run_ids=,  # required — The instance run ids to be cancelled.
    message="..."  # optional — The user provided message as to why the instance executions were cancelled.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

