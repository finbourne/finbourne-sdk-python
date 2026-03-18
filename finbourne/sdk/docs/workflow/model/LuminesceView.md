# LuminesceView

Configuration for a Worker that calls a Luminesce view
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Required | The type of worker |
| **name** | **str** | Required | Name of the view in Luminesce |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.LuminesceView import LuminesceView

instance = LuminesceView(
    type="...",  # required — The type of worker
    name="..."  # required — Name of the view in Luminesce
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

