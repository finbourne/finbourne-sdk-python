# Tag

Represents data of an image's tag
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Optional | The name of the tag |
| **pull_time** | **datetime** | Optional | The latest pull time |
| **push_time** | **datetime** | Optional | The date of the tag&#39;s push |
| **signed** | **bool** | Optional | Indicates whether the tag is signed |
| **immutable** | **bool** | Optional | Indicates whether the tag is immutable |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.scheduler.models.Tag import Tag

instance = Tag(
    name="...",  # optional — The name of the tag
    pull_time=datetime.now(),  # optional — The latest pull time
    push_time=datetime.now(),  # optional — The date of the tag&#39;s push
    signed=True,  # optional — Indicates whether the tag is signed
    immutable=True  # optional — Indicates whether the tag is immutable
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

