# SpecifiedTime

A specified time in the day
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **hours** | **int** | Required | Hours |
| **minutes** | **int** | Required | Minutes |
| **type** | **str** | Required | The type of Time of Day |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.SpecifiedTime import SpecifiedTime

instance = SpecifiedTime(
    hours=0,  # required — Hours
    minutes=0,  # required — Minutes
    type="..."  # required — The type of Time of Day
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

