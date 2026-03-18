# Parameter

Defines a Worker Parameter
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Required | The type of this Parameter |
| **name** | **str** | Required | Name |
| **display_name** | **str** | Optional | DisplayName |
| **description** | **str** | Optional | Description |
| **required** | **bool** | Required | Required or not |
| **default_value** | **str** | Optional | DefaultValue |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.Parameter import Parameter

instance = Parameter(
    type="...",  # required — The type of this Parameter
    name="...",  # required — Name
    display_name="...",  # optional — DisplayName
    description="...",  # optional — Description
    required=True,  # required — Required or not
    default_value="..."  # optional — DefaultValue
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

