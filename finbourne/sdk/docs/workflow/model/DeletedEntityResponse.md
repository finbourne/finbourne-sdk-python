# DeletedEntityResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The Uri related to this Entity |
| **effective_from** | **datetime** | Optional | The EffectiveFrom for this response |
| **as_at** | **datetime** | Required | The AsAt for this response |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.DeletedEntityResponse import DeletedEntityResponse

instance = DeletedEntityResponse(
    href="...",  # optional — The Uri related to this Entity
    effective_from=datetime.now(),  # optional — The EffectiveFrom for this response
    as_at=datetime.now(),  # required — The AsAt for this response
    links=[]  # optional
)
```

- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

