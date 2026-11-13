# TaxReturnWorkflowStep

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **status** | **str** | Optional | The workflow status of the return. Available values: Draft, Prepared, Reviewed, SignedOff, Final. Available values: Draft, Prepared, Reviewed, SignedOff, Final. |
| **as_at** | **datetime** | Optional | The time the workflow step was recorded. |
| **reason** | **str** | Optional | The reason given when the return was advanced or sent back. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TaxReturnWorkflowStep import TaxReturnWorkflowStep

instance = TaxReturnWorkflowStep(
    status="...",  # optional — The workflow status of the return. Available values: Draft, Prepared, Reviewed, SignedOff, Final. Available values: Draft, Prepared, Reviewed, SignedOff, Final.
    as_at=datetime.now(),  # optional — The time the workflow step was recorded.
    reason="..."  # optional — The reason given when the return was advanced or sent back.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

