# ResultField

Defines a Worker Result Field
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Required | Name |
| **type** | **str** | Required | The type of this Parameter |
| **display_name** | **str** | Optional | DisplayName |
| **description** | **str** | Optional | Description |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.ResultField import ResultField

instance = ResultField(
    name="...",  # required — Name
    type="...",  # required — The type of this Parameter
    display_name="...",  # optional — DisplayName
    description="..."  # optional — Description
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

