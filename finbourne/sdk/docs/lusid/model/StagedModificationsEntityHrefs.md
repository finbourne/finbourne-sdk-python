# StagedModificationsEntityHrefs

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **when_staged** | **str** | Optional | The specific Uniform Resource Identifier (URI) for the staged modification change at the time when the change was requested. |
| **preview** | **str** | Optional | The specific Uniform Resource Identifier (URI) for the preview of staged modification change once applied. |
| **latest** | **str** | Optional | The specific Uniform Resource Identifier (URI) for the staged modification at latest time. |
| **when_closed** | **str** | Optional | The specific Uniform Resource Identifier (URI) for the staged modification after it has been applied. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.StagedModificationsEntityHrefs import StagedModificationsEntityHrefs

instance = StagedModificationsEntityHrefs(
    when_staged="...",  # optional — The specific Uniform Resource Identifier (URI) for the staged modification change at the time when the change was requested.
    preview="...",  # optional — The specific Uniform Resource Identifier (URI) for the preview of staged modification change once applied.
    latest="...",  # optional — The specific Uniform Resource Identifier (URI) for the staged modification at latest time.
    when_closed="...",  # optional — The specific Uniform Resource Identifier (URI) for the staged modification after it has been applied.
    links=[]  # optional
)
```

- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

