# Worker

Information about the Worker
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [../model/ResourceId](ResourceId.md) | Required | *No description available.* |
| **display_name** | **str** | Required | Human readable name |
| **description** | **str** | Optional | Human readable description |
| **worker_configuration** | [../model/WorkerConfigurationResponse](WorkerConfigurationResponse.md) | Required | *No description available.* |
| **version** | [../model/VersionInfo](VersionInfo.md) | Optional | *No description available.* |
| **parameters** | [../model/List[Parameter]](Parameter.md) | Optional | The Parameters this Worker accepts or requires. |
| **result_fields** | [../model/List[ResultField]](ResultField.md) | Optional | The Fields that the Worker results will come back with. |
| **links** | [../model/List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.Worker import Worker

instance = Worker(
    id=ResourceId(...),  # required
    display_name="...",  # required — Human readable name
    description="...",  # optional — Human readable description
    worker_configuration=WorkerConfigurationResponse(...),  # required
    version=VersionInfo(...),  # optional
    parameters=[],  # optional — The Parameters this Worker accepts or requires.
    result_fields=[],  # optional — The Fields that the Worker results will come back with.
    links=[]  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [WorkerConfigurationResponse](WorkerConfigurationResponse.md)
- [VersionInfo](VersionInfo.md)
- [Parameter](Parameter.md) — used in `parameters`
- [ResultField](ResultField.md) — used in `result_fields`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

