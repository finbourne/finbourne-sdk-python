# BackgroundQueryResponse

Response for Background Query Start requests
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **execution_id** | **str** | Optional | ExecutionId of the started-query |
| **progress** | [../model/Link](Link.md) | Optional | *No description available.* |
| **cancel** | [../model/Link](Link.md) | Optional | *No description available.* |
| **fetch_json** | [../model/Link](Link.md) | Optional | *No description available.* |
| **fetch_json_proper** | [../model/Link](Link.md) | Optional | *No description available.* |
| **fetch_json_proper_with_lineage** | [../model/Link](Link.md) | Optional | *No description available.* |
| **fetch_xml** | [../model/Link](Link.md) | Optional | *No description available.* |
| **fetch_parquet** | [../model/Link](Link.md) | Optional | *No description available.* |
| **fetch_csv** | [../model/Link](Link.md) | Optional | *No description available.* |
| **fetch_pipe** | [../model/Link](Link.md) | Optional | *No description available.* |
| **fetch_excel** | [../model/Link](Link.md) | Optional | *No description available.* |
| **fetch_sqlite** | [../model/Link](Link.md) | Optional | *No description available.* |
| **histogram** | [../model/Link](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.BackgroundQueryResponse import BackgroundQueryResponse

instance = BackgroundQueryResponse(
    execution_id="...",  # optional — ExecutionId of the started-query
    progress=Link(...),  # optional
    cancel=Link(...),  # optional
    fetch_json=Link(...),  # optional
    fetch_json_proper=Link(...),  # optional
    fetch_json_proper_with_lineage=Link(...),  # optional
    fetch_xml=Link(...),  # optional
    fetch_parquet=Link(...),  # optional
    fetch_csv=Link(...),  # optional
    fetch_pipe=Link(...),  # optional
    fetch_excel=Link(...),  # optional
    fetch_sqlite=Link(...),  # optional
    histogram=Link(...)  # optional
)
```

- [Link](Link.md)
- [Link](Link.md)
- [Link](Link.md)
- [Link](Link.md)
- [Link](Link.md)
- [Link](Link.md)
- [Link](Link.md)
- [Link](Link.md)
- [Link](Link.md)
- [Link](Link.md)
- [Link](Link.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

