# JobDefinition

Definition of a job
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **job_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **name** | **str** | Optional | Name of the job |
| **author** | **str** | Optional | Author of the job |
| **date_created** | **datetime** | Optional | Date when job was created |
| **description** | **str** | Optional | Description of this job |
| **docker_image** | **str** | Optional | Information about the docker image in the format “image_source/image_name:image_tag” |
| **ttl** | **int** | Optional | Time To Live of the job run in seconds Defaults to 5 minutes(300) |
| **min_cpu** | **str** | Optional | Specifies  minimum number of CPUs to be allocated for the job Default to 2 |
| **max_cpu** | **str** | Optional | Specifies  maximum number of CPUs to be allocated for the job |
| **min_memory** | **str** | Optional | Specifies the minimum amount of memory (in GiB) to be allocated for the job |
| **max_memory** | **str** | Optional | Specifies the maximum amount of memory (in GiB) to be allocated for the job |
| **argument_definitions** | [Dict[str, ArgumentDefinition]](ArgumentDefinition.md) | Optional | All arguments for this job to run |
| **command_line_argument_separator** | **str** | Optional | Value to separate command line arguments e.g : If a job has a command line argument named &#39;folder&#39; and the runtime value is &#39;s3://path&#39; then this would be supplied to the command as &#39;folder{separatorValue}s3://path&#39; Default to a space |
| **required_resources** | [RequiredResources](RequiredResources.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.scheduler.models.JobDefinition import JobDefinition

instance = JobDefinition(
    job_id=ResourceId(...),  # required
    name="...",  # optional — Name of the job
    author="...",  # optional — Author of the job
    date_created=datetime.now(),  # optional — Date when job was created
    description="...",  # optional — Description of this job
    docker_image="...",  # optional — Information about the docker image in the format “image_source/image_name:image_tag”
    ttl=0,  # optional — Time To Live of the job run in seconds Defaults to 5 minutes(300)
    min_cpu="...",  # optional — Specifies  minimum number of CPUs to be allocated for the job Default to 2
    max_cpu="...",  # optional — Specifies  maximum number of CPUs to be allocated for the job
    min_memory="...",  # optional — Specifies the minimum amount of memory (in GiB) to be allocated for the job
    max_memory="...",  # optional — Specifies the maximum amount of memory (in GiB) to be allocated for the job
    argument_definitions=ArgumentDefinition(...),  # optional — All arguments for this job to run
    command_line_argument_separator="...",  # optional — Value to separate command line arguments e.g : If a job has a command line argument named &#39;folder&#39; and the runtime value is &#39;s3://path&#39; then this would be supplied to the command as &#39;folder{separatorValue}s3://path&#39; Default to a space
    required_resources=RequiredResources(...)  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ArgumentDefinition](ArgumentDefinition.md) — used in `argument_definitions`
- [RequiredResources](RequiredResources.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

