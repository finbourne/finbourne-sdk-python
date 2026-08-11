# Change

The time an entity was modified (amendment and/or historical correction).
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | *No description available.* |
| **entity_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **corrected** | **bool** | Required |  |
| **correction_effective_at** | **datetime** | Optional |  |
| **correction_as_at** | **datetime** | Optional |  |
| **amended** | **bool** | Required |  |
| **amendment_effective_at** | **datetime** | Optional |  |
| **amendment_as_at** | **datetime** | Optional |  |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.Change import Change

instance = Change(
    href="...",  # optional
    entity_id=ResourceId(...),  # required
    corrected=True,  # required — 
    correction_effective_at=datetime.now(),  # optional — 
    correction_as_at=datetime.now(),  # optional — 
    amended=True,  # required — 
    amendment_effective_at=datetime.now(),  # optional — 
    amendment_as_at=datetime.now(),  # optional — 
    links=[]  # optional
)
```

- [ResourceId](ResourceId.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

