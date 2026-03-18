# UpdateJobRequest

A request to update a job
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Required | Name of the job |
| **author** | **str** | Optional | Author of the job |
| **description** | **str** | Required | Description of this job |
| **image_name** | **str** | Required | The name of the Docker image that contains this job |
| **image_tag** | **str** | Required | The tag of the Docker image that contains this job |
| **ttl** | **int** | Optional | Time To Live of the job run in seconds Defaults to 5 minutes(300) |
| **min_cpu** | **str** | Optional | Specifies  minimum number of CPUs to be allocated for the job Default to 2 |
| **max_cpu** | **str** | Optional | Specifies  maximum number of CPUs to be allocated for the job |
| **min_memory** | **str** | Optional | Specifies the minimum amount of memory  to be allocated for the job |
| **max_memory** | **str** | Optional | Specifies the maximum amount of memory to be allocated for the job |
| **argument_definitions** | [Dict[str, ArgumentDefinition]](ArgumentDefinition.md) | Required | All arguments for this job to run |
| **command_line_argument_separator** | **str** | Optional | Value to separate command line arguments e.g : If a job has a command line argument named &#39;folder&#39; and the runtime value is &#39;s3://path&#39; then this would be supplied to the command as &#39;folder{separatorValue}s3://path&#39; Default to a space |
| **required_resources** | [RequiredResources](RequiredResources.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.scheduler.models.UpdateJobRequest import UpdateJobRequest

instance = UpdateJobRequest(
    name="...",  # required — Name of the job
    author="...",  # optional — Author of the job
    description="...",  # required — Description of this job
    image_name="...",  # required — The name of the Docker image that contains this job
    image_tag="...",  # required — The tag of the Docker image that contains this job
    ttl=0,  # optional — Time To Live of the job run in seconds Defaults to 5 minutes(300)
    min_cpu="...",  # optional — Specifies  minimum number of CPUs to be allocated for the job Default to 2
    max_cpu="...",  # optional — Specifies  maximum number of CPUs to be allocated for the job
    min_memory="...",  # optional — Specifies the minimum amount of memory  to be allocated for the job
    max_memory="...",  # optional — Specifies the maximum amount of memory to be allocated for the job
    argument_definitions=ArgumentDefinition(...),  # required — All arguments for this job to run
    command_line_argument_separator="...",  # optional — Value to separate command line arguments e.g : If a job has a command line argument named &#39;folder&#39; and the runtime value is &#39;s3://path&#39; then this would be supplied to the command as &#39;folder{separatorValue}s3://path&#39; Default to a space
    required_resources=RequiredResources(...)  # optional
)
```

- [ArgumentDefinition](ArgumentDefinition.md) — used in `argument_definitions`
- [RequiredResources](RequiredResources.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

