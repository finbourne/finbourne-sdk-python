# CutLabelDefinition

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Optional |  |
| **display_name** | **str** | Optional |  |
| **description** | **str** | Optional |  |
| **cut_local_time** | [CutLocalTime](CutLocalTime.md) | Optional | *No description available.* |
| **time_zone** | **str** | Optional |  |
| **href** | **str** | Optional | *No description available.* |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CutLabelDefinition import CutLabelDefinition

instance = CutLabelDefinition(
    code="...",  # optional — 
    display_name="...",  # optional — 
    description="...",  # optional — 
    cut_local_time=CutLocalTime(...),  # optional
    time_zone="...",  # optional — 
    href="...",  # optional
    version=Version(...),  # optional
    links=[]  # optional
)
```

- [CutLocalTime](CutLocalTime.md)
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

