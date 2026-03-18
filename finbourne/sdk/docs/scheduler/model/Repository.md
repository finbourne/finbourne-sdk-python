# Repository

An object representation of a repository
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Optional | The identifier of the repository |
| **creation_time** | **datetime** | Optional | Date of  repository creation |
| **last_update** | **datetime** | Optional | The last update of the repository |
| **description** | **str** | Optional | Description of the repository |
| **pull_count** | **int** | Optional | Number of times images were pulled from this repository |
| **image_count** | **int** | Optional | The number of versions of this image |
| **images** | [Link](Link.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.scheduler.models.Repository import Repository

instance = Repository(
    name="...",  # optional — The identifier of the repository
    creation_time=datetime.now(),  # optional — Date of  repository creation
    last_update=datetime.now(),  # optional — The last update of the repository
    description="...",  # optional — Description of the repository
    pull_count=0,  # optional — Number of times images were pulled from this repository
    image_count=0,  # optional — The number of versions of this image
    images=Link(...),  # optional
    links=[]  # optional
)
```

- [Link](Link.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

