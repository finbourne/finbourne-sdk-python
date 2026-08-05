# TransitionRecInstanceRequest

The request to apply a lifecycle transition (re-run, lock or unlock) to a rec instance.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **action** | **str** | Required | The transition to apply. Available values: ReRun, Lock, Unlock. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TransitionRecInstanceRequest import TransitionRecInstanceRequest

instance = TransitionRecInstanceRequest(
    action="..."  # required — The transition to apply. Available values: ReRun, Lock, Unlock.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

