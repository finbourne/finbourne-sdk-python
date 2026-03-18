# CutLabelReference

A reference to a Cut Label in LUSID. The time zone of the Cut Label will be used
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Required | Code of the Cut Label |
| **type** | **str** | Required | The type of Time of Day |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.CutLabelReference import CutLabelReference

instance = CutLabelReference(
    code="...",  # required — Code of the Cut Label
    type="..."  # required — The type of Time of Day
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

