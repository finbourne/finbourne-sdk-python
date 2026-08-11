# ViewParameter

Parameters of view
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Required | Name of the provider |
| **data_type** | [DataType](DataType.md) | Required | *No description available.* |
| **value** | **str** | Required | Value of the provider |
| **is_table_data_mandatory** | **bool** | Optional | Should this be selected? False would imply it is only being filtered on. Ignored when Aggregations are present |
| **description** | **str** | Optional | Description of the parameter |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.ViewParameter import ViewParameter

instance = ViewParameter(
    name="...",  # required — Name of the provider
    data_type=DataType(...),  # required
    value="...",  # required — Value of the provider
    is_table_data_mandatory=True,  # optional — Should this be selected? False would imply it is only being filtered on. Ignored when Aggregations are present
    description="..."  # optional — Description of the parameter
)
```

- [DataType](DataType.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

