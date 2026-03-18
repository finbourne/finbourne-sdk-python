# WriterDesign

Representation of a \"designable Query for a writer\" suitable for formatting to SQL or being built from compliant SQL.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **sql** | **str** | Required | Original SQL that started this off |
| **available_to_map_from** | [List[ExpressionWithAlias]](ExpressionWithAlias.md) | Optional | The data able to be mapped from as derived from the Sql |
| **parameter** | [AvailableParameter](AvailableParameter.md) | Optional | *No description available.* |
| **available_parameters** | [List[AvailableParameter]](AvailableParameter.md) | Optional | All the parameter the user may wish to design |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.WriterDesign import WriterDesign

instance = WriterDesign(
    sql="...",  # required — Original SQL that started this off
    available_to_map_from=[],  # optional — The data able to be mapped from as derived from the Sql
    parameter=AvailableParameter(...),  # optional
    available_parameters=[]  # optional — All the parameter the user may wish to design
)
```

- [ExpressionWithAlias](ExpressionWithAlias.md) — used in `available_to_map_from`
- [AvailableParameter](AvailableParameter.md)
- [AvailableParameter](AvailableParameter.md) — used in `available_parameters`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

