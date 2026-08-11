# ConvertToViewData

Representation of view data where will template the data into a 'create view' sql
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **query** | **str** | Required | view query |
| **name** | **str** | Required | Name of view |
| **description** | **str** | Optional | Description of view |
| **documentation_link** | **str** | Optional | Documentation link |
| **view_parameters** | [List[ViewParameter]](ViewParameter.md) | Optional | View parameters |
| **other_parameters** | **Dict[str, Optional[str]]** | Optional | Other parameters not explicitly handled by the ConvertToView generation. These will be populated by the \&quot;From SQL\&quot; and should simply be returned by the web GUI should the user edit / update / regenerate |
| **starting_variable_name** | **str** | Optional | Which variable the this start with, null if not started from a full Create View Sql Statement. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.ConvertToViewData import ConvertToViewData

instance = ConvertToViewData(
    query="...",  # required — view query
    name="...",  # required — Name of view
    description="...",  # optional — Description of view
    documentation_link="...",  # optional — Documentation link
    view_parameters=[],  # optional — View parameters
    other_parameters=,  # optional — Other parameters not explicitly handled by the ConvertToView generation. These will be populated by the \&quot;From SQL\&quot; and should simply be returned by the web GUI should the user edit / update / regenerate
    starting_variable_name="..."  # optional — Which variable the this start with, null if not started from a full Create View Sql Statement.
)
```

- [ViewParameter](ViewParameter.md) — used in `view_parameters`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

