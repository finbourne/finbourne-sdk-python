# ArgumentDefinition

Job argument definition
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **data_type** | **str** | Required | Data type of the argument |
| **required** | **bool** | Optional | Optionality of the argument |
| **description** | **str** | Required | Argument description |
| **order** | **int** | Required | The order of the argument |
| **constraints** | **str** | Optional | Constrains of the argument value |
| **passed_as** | **str** | Required | Specifies how this argument should be passed in Allowed values are: CommandLine or EnvironmentVariable  Defaults to: CommandLine |
| **default_value** | **str** | Optional | Specify a default value for this argument if no value is provided The value needs to be convertible to the associated data type |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.scheduler.models.ArgumentDefinition import ArgumentDefinition

instance = ArgumentDefinition(
    data_type="...",  # required — Data type of the argument
    required=True,  # optional — Optionality of the argument
    description="...",  # required — Argument description
    order=0,  # required — The order of the argument
    constraints="...",  # optional — Constrains of the argument value
    passed_as="...",  # required — Specifies how this argument should be passed in Allowed values are: CommandLine or EnvironmentVariable  Defaults to: CommandLine
    default_value="..."  # optional — Specify a default value for this argument if no value is provided The value needs to be convertible to the associated data type
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

