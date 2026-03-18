# DeleteInstrumentResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **as_at** | **datetime** | Required | The as-at datetime at which the instrument was deleted. |
| **staged_modifications** | [StagedModificationsInfo](StagedModificationsInfo.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.DeleteInstrumentResponse import DeleteInstrumentResponse

instance = DeleteInstrumentResponse(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    as_at=datetime.now(),  # required — The as-at datetime at which the instrument was deleted.
    staged_modifications=StagedModificationsInfo(...),  # optional
    links=[]  # optional
)
```

- [StagedModificationsInfo](StagedModificationsInfo.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

