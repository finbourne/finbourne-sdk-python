# AvailableParameter

Information about a field that can be designed on (regardless if it currently is) Kind of a \"mini-available catalog entry\"
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **provider_name** | **str** | Required | Name of the Provider with a TableParameter |
| **parameter_name** | **str** | Required | Name of the TableParameter on the Provider |
| **fields** | [List[MappableField]](MappableField.md) | Required | Fields that can be mapped to |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.AvailableParameter import AvailableParameter

instance = AvailableParameter(
    provider_name="...",  # required — Name of the Provider with a TableParameter
    parameter_name="...",  # required — Name of the TableParameter on the Provider
    fields=[]  # required — Fields that can be mapped to
)
```

- [MappableField](MappableField.md) — used in `fields`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

