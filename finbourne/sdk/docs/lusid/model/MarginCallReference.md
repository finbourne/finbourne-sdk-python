# MarginCallReference

A pointer to a margin call in another run.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **run_id** | **str** | Required | The run the referenced call belongs to. |
| **call_id** | **str** | Required | The business key of the referenced call. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.MarginCallReference import MarginCallReference

instance = MarginCallReference(
    run_id="...",  # required — The run the referenced call belongs to.
    call_id="..."  # required — The business key of the referenced call.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

