# CorporateActionSource

A corporate action source
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **display_name** | **str** | Optional | The name of the corporate action source |
| **description** | **str** | Optional | The description of the corporate action source |
| **instrument_scopes** | **List[str]** | Optional | The list of instrument scopes used as the scope resolution strategy when resolving instruments of upserted corporate actions. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CorporateActionSource import CorporateActionSource

instance = CorporateActionSource(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    id=ResourceId(...),  # optional
    version=Version(...),  # optional
    display_name="...",  # optional — The name of the corporate action source
    description="...",  # optional — The description of the corporate action source
    instrument_scopes=,  # optional — The list of instrument scopes used as the scope resolution strategy when resolving instruments of upserted corporate actions.
    links=[]  # optional
)
```

- [ResourceId](ResourceId.md)
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

