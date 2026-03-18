# TemplateMetadata

Extra policy template metadata information, used during a generation request
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **template_selection** | [List[TemplateSelection]](TemplateSelection.md) | Optional | List of policy templates used for a generation request |
| **build_as_at** | **datetime** | Optional | Policy template build AsAt time used for a generation request |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.access.models.TemplateMetadata import TemplateMetadata

instance = TemplateMetadata(
    template_selection=[],  # optional — List of policy templates used for a generation request
    build_as_at=datetime.now()  # optional — Policy template build AsAt time used for a generation request
)
```


## Related Models

- [TemplateSelection](TemplateSelection.md) — used in `template_selection`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

